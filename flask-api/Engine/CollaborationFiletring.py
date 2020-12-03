from .Neo4jConnector import Neo4jConnector

THRESHOLD = 10
WEIGHT_FOR_AVERAGE_PROFESSOR_RATING = 1
WEIGHT_FOR_AVERAGE_COURSE_RATING = 1
WEIGHT_FOR_COURSE_RATING_AND_COMMON_KEYWORD = 1
WEIGHT_FOR_PROFESSOR_RATING_AND_COMMON_KEYWORD = 1

class CollaborationFiltering():

    def __init__(self):
        self.connector = Neo4jConnector()
        self.output_dict = {}
        self.weights = {}

    def recommend(self, student):
        self.output_dict = self.initialize_electives(student)
        self.weights = self.initialize_electives(student)
        field_of_study = self.connector.get_field_of_study_for_student(student)
        for key,value in self.output_dict.items():
            # here will be functions for each subject callculations
            self.recommendation_based_on_average_professor_rating(self.connector.get_course_by_field_of_study(key, field_of_study))
            self.recommendation_based_on_average_course_rating(self.connector.get_course_by_field_of_study(key, field_of_study))
            self.recommendation_based_on_course_rating_and_common_keyword(student, self.connector.get_course_by_field_of_study(key, field_of_study))
            self.recommendation_based_on_professor_rating_and_common_keyword(student, self.connector.get_course_by_field_of_study(key, field_of_study))
            if self.weights[key] != 0:
                self.output_dict[key] = self.output_dict[key] / self.weights[key]
        return self.output_dict

    def initialize_electives(self, student):
        dict_with_electives = {}
        for course in self.connector.get_student_electives_on_next_semester(student):
            dict_with_electives[course.name] = 0
        return dict_with_electives

    def recommendation_based_on_average_professor_rating(self, course):
        professor = self.connector.get_professor_of_particular_course(course)
        avg_professor_rate = self.connector.get_average_student_rate_of_professor(professor, THRESHOLD)
        if avg_professor_rate:
            self.weights[course.name] += WEIGHT_FOR_AVERAGE_PROFESSOR_RATING
            self.output_dict[course.name] += (avg_professor_rate/5) * WEIGHT_FOR_AVERAGE_PROFESSOR_RATING
        else:
            return False

    def recommendation_based_on_average_course_rating(self, course):
        avg_course_rate = self.connector.get_average_student_rate_of_course(course, THRESHOLD)
        if avg_course_rate:
            self.weights[course.name] += WEIGHT_FOR_AVERAGE_COURSE_RATING
            self.output_dict[course.name] += (avg_course_rate/5) * WEIGHT_FOR_AVERAGE_COURSE_RATING
        else:
            return False

    def recommendation_based_on_course_rating_and_common_keyword(self, student, course):
        has_common_keyword, value_course = self.connector.check_if_student_has_common_keyword_if_yes_get_influence_based_on_course(student, course)
        if has_common_keyword:
            self.weights[course.name] += WEIGHT_FOR_COURSE_RATING_AND_COMMON_KEYWORD
            self.output_dict[course.name] += value_course * WEIGHT_FOR_COURSE_RATING_AND_COMMON_KEYWORD
        else:
            return False

    def recommendation_based_on_professor_rating_and_common_keyword(self, student, course):
        professor = self.connector.get_professor_of_particular_course(course)
        has_common_keyword, value_course = self.connector.check_if_student_has_common_keyword_if_yes_get_influence_based_on_professor(student, professor)
        if has_common_keyword:
            self.weights[course.name] += WEIGHT_FOR_PROFESSOR_RATING_AND_COMMON_KEYWORD
            self.output_dict[course.name] += value_course * WEIGHT_FOR_PROFESSOR_RATING_AND_COMMON_KEYWORD
        else:
            return False


    # def recommendation_based_on_professor(self, student, course):
    #     professor = self.connector.get_professor_of_particular_course(course)
    #     professor_rate = self.connector.get_student_rate_of_professor(student, professor)
    #     if professor_rate:
    #         self.weights[course.name] += WEIGHT_FOR_PROFESSOR_RECOMMENDATION
    #         self.output_dict[course.name] += (professor_rate/5) * WEIGHT_FOR_PROFESSOR_RECOMMENDATION
    #     else:
    #         return False
    #
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

