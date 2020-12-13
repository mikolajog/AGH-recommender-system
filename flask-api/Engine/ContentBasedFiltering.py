import sys
import spacy

from .Neo4jConnector import Neo4jConnector


WEIGHT_FOR_PROFESSOR_RECOMMENDATION = 1
WEIGHT_FOR_KEYWORD_RECOMMENDATION = 1
WEIGHT_FOR_KEYWORD_COURSE_NAME = 100
NUMBER_OF_KEYWORDS = 5

class ContentBasedFiletring():
    def __init__(self):
        self.connector = Neo4jConnector()
        self.output_dict = {}
        self.weights = {}

    def recommend(self, student,faculty,fieldofstudyname, startyears, onsemester):
        self.output_dict = self.initialize_electives(student,faculty,fieldofstudyname, startyears)
        self.weights = self.initialize_electives(student,faculty,fieldofstudyname, startyears)
        field_of_study = self.connector.get_field_of_study(faculty=faculty, name=fieldofstudyname, start_years=startyears)
        for key,value in self.output_dict.items():
            # here will be functions for each subject callculations
            self.recommendation_based_on_professor(student, self.connector.get_course_by_field_of_study(key, field_of_study))
            self.recommendation_based_on_student_keywords(student, self.connector.get_course_by_field_of_study(key, field_of_study))
            self.recommendation_based_on_student_keywords_and_course_names(student, self.connector.get_course_by_field_of_study(key, field_of_study))
            if self.weights[key] != 0:
                self.output_dict[key] = self.output_dict[key] / self.weights[key]
        return self.output_dict

    def initialize_electives(self, student,faculty,fieldofstudyname, startyears):
        dict_with_electives = {}
        for course in self.connector.get_student_electives_on_next_semester(student,faculty,fieldofstudyname, startyears):
            dict_with_electives[course.name] = 0
        print(dict_with_electives)
        return dict_with_electives

    def recommendation_based_on_professor(self, student, course):
        professor = self.connector.get_professor_of_particular_course(course)
        professor_rate = self.connector.get_student_rate_of_professor(student, professor)
        if professor_rate:
            self.weights[course.name] += WEIGHT_FOR_PROFESSOR_RECOMMENDATION
            self.output_dict[course.name] += (professor_rate/5) * WEIGHT_FOR_PROFESSOR_RECOMMENDATION
        else:
            return False

    def recommendation_based_on_student_keywords(self, student, course):
        course_description = course.description
        keywords_student = self.connector.get_all_keywords_student_likes(student)
        if len(keywords_student)==0:
            return
        student_sentence = ""
        for keyword in keywords_student:
            student_sentence += keyword.word
            student_sentence += " "

        nlp = spacy.load('pl_core_news_md')
        course_description = nlp(course.description)
        student_sentence = nlp(student_sentence)

        value_of_similarity = student_sentence.similarity(course_description)

        self.weights[course.name] += WEIGHT_FOR_KEYWORD_RECOMMENDATION
        self.output_dict[course.name] += value_of_similarity * WEIGHT_FOR_KEYWORD_RECOMMENDATION

    def recommendation_based_on_student_keywords_and_course_names(self, student, course):
        keywords_student = self.connector.get_all_keywords_student_likes(student)
        for keywords_student in keywords_student:
            if keywords_student.word.lower() in course.name.lower():
                self.weights[course.name] += WEIGHT_FOR_KEYWORD_COURSE_NAME
                self.output_dict[course.name] += WEIGHT_FOR_KEYWORD_COURSE_NAME

    # def recommendation_based_on_student_keywords(self, student, course):
    #     keywords_student = self.connector.get_all_keywords_student_likes(student)
    #     keywords_course = self.connector.get_top_n_keywords_describing_course(course, NUMBER_OF_KEYWORDS)
    #     ratings = 0.0
    #     for keyword_student in keywords_student:
    #         sum_of_ratings_keyword_with_course = 0.0
    #         sum_of_ratings_multiplied = 0.0
    #         for keyword_course in keywords_course:
    #             if keyword_student.word == keyword_course.word:
    #                 self.weights[course.name] += WEIGHT_FOR_KEYWORD_RECOMMENDATION
    #                 self.output_dict[course.name] += 1.0
    #                 return
    #             rating_keyword_with_course = self.connector.get_rating_keyword_describes_course(keyword_course, course)
    #             rating_between_keywords = self.connector.get_rating_of_two_keywords_if_exists(keyword_course, keyword_student)
    #             print(rating_between_keywords)
    #             if not rating_between_keywords:
    #                 self.connector.count_rating_and_connect_two_keywords(keyword_course, keyword_student)
    #                 rating_between_keywords = self.connector.get_rating_of_two_keywords_if_exists(keyword_course, keyword_student)
    #             sum_of_ratings_multiplied += (rating_keyword_with_course * rating_between_keywords)
    #             sum_of_ratings_keyword_with_course += rating_keyword_with_course
    #         if sum_of_ratings_multiplied != 0.0:
    #             ratings += (sum_of_ratings_multiplied / sum_of_ratings_keyword_with_course)
    #         else:
    #             ratings += 0.0
    #     self.weights[course.name] += WEIGHT_FOR_KEYWORD_RECOMMENDATION
    #     self.output_dict[course.name] += ratings * WEIGHT_FOR_KEYWORD_RECOMMENDATION

