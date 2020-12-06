from neomodel import config, db, clear_neo4j_database

from .models import ValuedRelationship
from .models.Course import Course
from .models.FieldOfStudy import FieldOfStudy
from .models.Keyword import Keyword
from .models.Professor import Professor
from .models.Student import Student


# import spacy


class Neo4jConnector():
    def __init__(self):
        config.DATABASE_URL = 'bolt://neo4j:Password123@localhost:7687'

    def drop_db(self):
        clear_neo4j_database(db)

    def add_student_if_not_exists(self, index_number, name, is_on_semester):
        if self.get_student(index_number) is None:
            return Student(index_number=index_number, name=name, is_on_semester=is_on_semester).save()
        else:
            return self.get_student(index_number)

    def add_student_if_not_exists(self, index_number, name, email, password, api_key):
        if self.get_student(index_number) is None:
            return Student(index_number=index_number, name=name, email=email, password=password, api_key=api_key).save()
        else:
            return self.get_student(index_number)

    def add_field_of_study_if_not_exists(self, name, start_years, faculty):
        if self.get_field_of_study(name, start_years, faculty) is None:
            return FieldOfStudy(name=name, start_years=start_years, faculty=faculty).save()
        else:
            return self.get_field_of_study(name, start_years, faculty)

    def add_professor_if_not_exists(self, name):
        if self.get_professor(name) is None:
            return Professor(name=name).save()
        else:
            return self.get_professor(name)

    def add_course_if_not_exists(self, name, description, taught_on_semester, is_elective=False):
        if self.get_course(name, taught_on_semester, is_elective) is None:
            return Course(name=name, description=description, taught_on_semester=taught_on_semester,
                          is_elective=is_elective).save()
        else:
            return self.get_course(name, taught_on_semester, is_elective)

    def add_keyword_if_not_exists(self, word):
        if self.get_keyword(word) is None:
            return Keyword(word=word).save()
        else:
            return self.get_keyword(word)

    def get_student(self, index_number):
        results, meta = db.cypher_query(
            'MATCH (student:Student) WHERE student.index_number=' + str(index_number) + ' RETURN student')
        student = [Student.inflate(row[0]) for row in results]
        return (student or [None])[0]

    def get_student_by_token(self, token):
        results, meta = db.cypher_query(
            'MATCH (student:Student) WHERE student.api_key=\"' + token + '\" RETURN student')
        student = [Student.inflate(row[0]) for row in results]
        return (student or [None])[0]

    def get_field_of_study(self, name, start_years, faculty):
        results, meta = db.cypher_query(
            'MATCH (fieldOfStudy:FieldOfStudy) WHERE (fieldOfStudy.name=\"' + name + '\"AND fieldOfStudy.start_years=\"' + str(
                start_years) + '\" AND fieldOfStudy.faculty=\"' + faculty + '\") RETURN fieldOfStudy')
        fieldOfStudy = [FieldOfStudy.inflate(row[0]) for row in results]
        return (fieldOfStudy or [None])[0]

    def get_professor(self, name):
        results, meta = db.cypher_query(
            'MATCH (professor:Professor) WHERE professor.name=\"' + name + '\" RETURN professor')
        professor = [Professor.inflate(row[0]) for row in results]
        return (professor or [None])[0]

    def get_course(self, name, taught_on_semester, is_elective):
        # taught_on_semester, is_elective=is_elective
        results, meta = db.cypher_query(
            'MATCH (course:Course) WHERE (course.name=\"' + name + '\" AND course.taught_on_semester=' + str(
                taught_on_semester) + ' AND course.is_elective=' + str(is_elective) + ') RETURN course')
        course = [Course.inflate(row[0]) for row in results]
        return (course or [None])[0]

    def get_course_by_field_of_study(self, name, field_of_study):
        # taught_on_semester, is_elective=is_elective
        results, meta = db.cypher_query(
            'MATCH (c:Course)-[r:HAS]->(f:FieldOfStudy) WHERE (c.name=\"' + name + '\" AND f.name=\"' + field_of_study.name + '\" AND f.start_years=\"' + field_of_study.start_years + '\" and f.faculty=\"' + field_of_study.faculty + '\") RETURN c')
        course = [Course.inflate(row[0]) for row in results]
        return (course or [None])[0]

    def get_keyword(self, word):
        results, meta = db.cypher_query(
            'MATCH (keyword:Keyword) WHERE keyword.word=\"' + word + '\" RETURN keyword')
        keyword = [Keyword.inflate(row[0]) for row in results]
        return (keyword or [None])[0]

    def connect_course_has_field_of_study(self, course, field_of_study):
        field_of_study.courses.connect(course)

    def connect_professor_teaches_course(self, professor, course):
        professor.course_taught.connect(course)

    def connect_keyword_describes_course_with_rating(self, keyword, course, rating):
        course.keyword.connect(keyword, {'rating': rating})

    def connect_student_studies_field_of_study(self, student, field_of_study, semester):
        student.field_of_study.connect(field_of_study, {'on_semester': semester})

    def connect_student_likes_keyword(self, student, keyword):
        student.keywords.connect(keyword)

    def connect_student_evaluates_course(self, student, course, rating):
        student.course_marks.connect(course, {'rating': rating})

    def connect_keyword_connected_keyword(self, keyword1, keyword2, rating):
        keyword1.keyword_related.connect(keyword2, {'rating': rating})

    def connect_student_rates_professor(self, student, professor, rating):
        student.professor.connect(professor, {'rating': rating})

    def disconnect_student_likes_keyword(self, student, keyword):
        student.keywords.disconnect(keyword)

    def disconnect_student_studies_field_of_study(self, student, field_of_study):
        student.field_of_study.disconnect(field_of_study)

    def disconnect_student_rates_professor(self, student, professor, rating):
        student.professor.disconnect(professor)

    def disconnect_student_evaluates_course(self, student, course, rating):
        student.course_marks.disconnect(course)

    def get_all_courses(self):
        results, meta = db.cypher_query(
            'MATCH (course:Course) RETURN course')
        courses = [Course.inflate(row[0]) for row in results]
        return courses

    def get_past_professors(self, student):
        field_of_study = self.get_field_of_study_for_student(student)
        results, meta = db.cypher_query(
            'MATCH (p:Professor)-[r:TEACHES]->(c:Course)-[r2:HAS]->(f:FieldOfStudy) WHERE (f.name=\"' + field_of_study.name + '\" AND f.start_years=\"' + field_of_study.start_years + '\" AND f.faculty=\"' + field_of_study.faculty + '\" )  RETURN DISTINCT p')
        professors = [Professor.inflate(row[0]) for row in results]
        return professors

    def get_past_courses_without_electives(self, student):
        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r1:STUDIES]->(f:FieldOfStudy)<-[r2:HAS]-(c:Course) WHERE (c.taught_on_semester<=s.is_on_semester AND s.index_number=' + str(
                student.index_number) + ' AND c.is_elective==False ) RETURN c')
        courses = [Course.inflate(row[0]) for row in results]
        return courses

    def get_past_courses_only_electives(self, student):
        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r1:STUDIES]->(f:FieldOfStudy)<-[r2:HAS]-(c:Course) WHERE (c.taught_on_semester<=s.is_on_semester AND s.index_number=' + str(
                student.index_number) + ' AND c.is_elective==True ) RETURN c')
        courses = [Course.inflate(row[0]) for row in results]
        return courses

    def get_all_courses_on_given_fieldofstudy(self, user, faculty, fieldofstudy, startyears):
        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r:STUDIES]->(f:FieldOfStudy) WHERE (f.faculty=\"' + faculty + '\" AND f.start_years=\"' + startyears + '\" AND f.name=\"' + fieldofstudy + '\") RETURN r.on_semester')
        semester = [row[0] for row in results]
        print("Hej        ", semester)
        results, meta = db.cypher_query(
            'MATCH (c:Course)-[r:HAS]->(f:FieldOfStudy) WHERE (f.faculty=\"' + faculty + '\" AND f.start_years=\"' + startyears + '\" AND f.name=\"' + fieldofstudy + '\" AND c.taught_on_semester<=' + str(
                semester[0]) + ') RETURN c')
        courses = [Course.inflate(row[0]) for row in results]
        return courses

    def get_all_professors_on_given_fieldofstudy(self, user, faculty, fieldofstudy, startyears):
        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r:STUDIES]->(f:FieldOfStudy) WHERE (f.faculty=\"' + faculty + '\" AND f.start_years=\"' + startyears + '\" AND f.name=\"' + fieldofstudy + '\") RETURN r.on_semester')
        semester = [row[0] for row in results]
        print("Hej        ", semester)
        results, meta = db.cypher_query(
            'MATCH (p:Professor)-[r1:TEACHES]->(c:Course)-[r:HAS]->(f:FieldOfStudy) WHERE (f.faculty=\"' + faculty + '\" AND f.start_years=\"' + startyears + '\" AND f.name=\"' + fieldofstudy + '\" AND c.taught_on_semester<=' + str(
                semester[0]) + ') RETURN p')
        professors = [Professor.inflate(row[0]) for row in results]
        return professors

    def get_student_rating_course(self, student, course, faculty, startyears, fieldofstudy):
        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r:EVALUATES]->(c:Course)-[r1:HAS]->(f:FieldOfStudy) WHERE(s.index_number=' + str(student.index_number) + ' AND c.name=\"' + course.name + '\" AND f.faculty=\"' + faculty + '\" AND f.start_years=\"' + startyears + '\" AND f.name=\"' + fieldofstudy + '\") RETURN r.rating')
        rating = [row[0] for row in results]
        if len(rating) == 0:
            return 0
        else:
            return rating[0]

    def get_student_rating_professor(self, student, professor):
        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r:RATES]->(p:Professor) WHERE(s.index_number=' + str(student.index_number) + ' AND p.name=\"' + professor.name + '\") RETURN r.rating')
        rating = [row[0] for row in results]
        if len(rating) == 0:
            return 0
        else:
            return rating[0]

    def is_course_elective(self, course, faculty, startyears, fieldofstudy):
        results, meta = db.cypher_query(
            'MATCH (c:Course)-[r1:HAS]->(f:FieldOfStudy) WHERE( c.name=\"' + course.name + '\" AND f.faculty=\"' + faculty + '\" AND f.start_years=\"' + startyears + '\" AND f.name=\"' + fieldofstudy + '\") RETURN c.is_elective')
        elective = [row[0] for row in results]
        if bool(elective[0]):
            return True
        else:
            return False

    def get_field_of_study_for_student(self, student):
        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r:STUDIES]->(f:FieldOfStudy) WHERE s.name=\"' + student.name + '\" RETURN f')
        field_of_study = [FieldOfStudy.inflate(row[0]) for row in results]
        return field_of_study[0]

    def get_all_fields_of_study_for_student(self, student):
        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r:STUDIES]->(f:FieldOfStudy) WHERE s.index_number=' + str(
                student.index_number) + ' RETURN f')
        field_of_study = [FieldOfStudy.inflate(row[0]) for row in results]
        if len(field_of_study) == 0:
            return None
        else:
            return field_of_study

    def get_student_on_semester_for_fieldofstudy(self, student, fieldofstudy):
        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r:STUDIES]->(f:FieldOfStudy) WHERE (s.index_number=' + str(
                student.index_number) + ' and f.name=\"' + fieldofstudy.name + '\" and f.faculty=\"' + fieldofstudy.faculty + '\" and f.start_years=\"' + fieldofstudy.start_years + '\") RETURN r.on_semester')
        semester = [row[0] for row in results]
        return (semester or [None])[0]

    def get_student_electives_on_next_semester(self, student):
        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r:STUDIES]->(f:FieldOfStudy)<-[r2:HAS]-(c:Course) WHERE (s.name=\"' + student.name + '\" and c.is_elective and s.is_on_semester + 1 = c.taught_on_semester) RETURN c')
        courses = [Course.inflate(row[0]) for row in results]
        return courses

    def get_professor_of_particular_course(self, course):
        results, meta = db.cypher_query(
            'MATCH (p:Professor)-[r:TEACHES]->(c:Course) WHERE c.name=\"' + course.name + '\" RETURN p')
        professor = [Professor.inflate(row[0]) for row in results]
        return professor[0]

    def get_student_rate_of_professor(self, student, professor):
        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r:RATES]->(p:Professor) WHERE (s.name=\"' + student.name + '\" AND p.name=\"' + professor.name + '\") RETURN r.rating')
        value = [row[0] for row in results]
        if len(value) == 0:
            return False

        return value[0]

    def get_all_keywords_student_likes(self, student):
        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r:LIKES]->(k:Keyword) WHERE s.name=\"' + student.name + '\" RETURN k')
        keywords = [Keyword.inflate(row[0]) for row in results]
        return keywords

    def get_all_keywords_describing_course(self, course):
        results, meta = db.cypher_query(
            'MATCH (k:Keyword)-[r:DESCRIBES]->(c:Course) WHERE c.name=\"' + course.name + '\" RETURN k')
        keywords = [Keyword.inflate(row[0]) for row in results]
        return keywords

    def get_top_n_keywords_describing_course(self, course, n):
        results, meta = db.cypher_query(
            'MATCH (k:Keyword)-[r:DESCRIBES]->(c:Course) WHERE c.name=\"' + course.name + '\" RETURN k ORDER BY r.rating DESC LIMIT ' + str(
                n))
        keywords = [Keyword.inflate(row[0]) for row in results]
        return keywords

    def get_all_possible_faculties(self):
        results, meta = db.cypher_query(
            'MATCH (n:FieldOfStudy) RETURN DISTINCT n.faculty')
        faculties = [row[0] for row in results]
        return faculties

    def get_all_possible_fieldofstudiesnames(self, faculty):
        results, meta = db.cypher_query(
            'MATCH (n:FieldOfStudy) WHERE n.faculty=\"' + faculty + '\" RETURN DISTINCT n.name')
        fields = [row[0] for row in results]
        return fields

    def get_all_possible_start_years(self, faculty, name):
        results, meta = db.cypher_query(
            'MATCH (n:FieldOfStudy) WHERE n.faculty=\"' + faculty + '\" RETURN DISTINCT n.name')
        fields = [row[0] for row in results]
        return fields

    def get_all_start_years_for_particular_fieldofstudy(self, faculty, name):
        results, meta = db.cypher_query(
            'MATCH (n:FieldOfStudy) WHERE n.faculty=\"' + faculty + '\" AND n.name=\"' + name + '\" RETURN DISTINCT n.start_years')
        start_years = [row[0] for row in results]
        return start_years

    def get_rating_keyword_describes_course(self, keyword_course, course):
        results, meta = db.cypher_query(
            'MATCH (k:Keyword)-[r:DESCRIBES]->(c:Course) WHERE (k.word=\"' + keyword_course.word + '\" AND c.name=\"' + course.name + '\") RETURN DISTINCT r.rating')
        value = [row[0] for row in results]
        if len(value) == 0:
            return False
        return value[0]

    def get_rating_of_two_keywords_if_exists(self, keyword1, keyword2):
        results, meta = db.cypher_query(
            'MATCH (k1:Keyword)-[r:DESCRIBES]->(k2:Keyword) WHERE (k1.word=\"' + keyword1.word + '\" AND k2.word=\"' + keyword2.word + '\") RETURN r.rating')
        value = [row[0] for row in results]
        if len(value) == 0:
            return False
        return value[0]

    # def count_rating_and_connect_two_keywords(self, keyword1, keyword2):
    #     nlp = spacy.load('pl_core_news_md')
    #     words = keyword1.word + " " +keyword2.word
    #     print(words)
    #     tokens = nlp(words)
    #     token1, token2 = tokens[0], tokens[1]
    #     self.connect_keyword_connected_keyword(keyword1, keyword2, token1.similarity(token2))

    def get_average_student_rate_of_professor(self, professor, threshold):
        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r:RATES]->(n:Professor) WHERE n.name=\"' + professor.name + '\" RETURN count(r)')
        value = [row[0] for row in results]
        if value[0] < threshold:
            return False

        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r:RATES]->(n:Professor) WHERE n.name=\"' + professor.name + '\" RETURN avg(r.rating)')
        value = [row[0] for row in results]

        return value[0]

    def get_average_student_rate_of_course(self, course, threshold):
        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r:EVALUATES]->(c:Course) WHERE c.name=\"' + course.name + '\" RETURN count(r)')
        value = [row[0] for row in results]
        if value[0] < threshold:
            return False

        results, meta = db.cypher_query(
            'MATCH (s:Student)-[r:EVALUATES]->(c:Course) WHERE c.name=\"' + course.name + '\" RETURN avg(r.rating)')
        value = [row[0] for row in results]

        return value[0]

    def check_if_student_has_common_keyword_if_yes_get_influence_based_on_course(self, student, course):
        student_keywords = self.get_all_keywords_student_likes(student)
        list_of_student_ratings_of_course = []

        for keyword in student_keywords:
            results, meta = db.cypher_query(
                'MATCH (k:Keyword)<-[r2:LIKES]-(s:Student)-[r1:EVALUATES]->(c:Course) WHERE (k.word=\"' + keyword.word + '\" AND c.name=\"' + course.name + '\") RETURN r1.rating')
            list_of_student_ratings_of_course.extend([float(row[0]) for row in results])

        if len(list_of_student_ratings_of_course) > 0:
            has_common_keyword = True
            value_course = 0

            results, meta = db.cypher_query(
                'MATCH (s:Student)-[r1:EVALUATES]->(c:Course) WHERE (c.name=\"' + course.name + '\") RETURN avg(r1.rating)')
            average_rating_of_course = [float(row[0]) for row in results]
            average_rating_of_course = average_rating_of_course[0]

            for rating in list_of_student_ratings_of_course:
                if rating >= average_rating_of_course:
                    value_course += 1

            value_course = value_course / len(list_of_student_ratings_of_course)
        else:
            has_common_keyword = False
            value_course = 0

        return has_common_keyword, value_course

    def check_if_student_has_common_keyword_if_yes_get_influence_based_on_professor(self, student, professor):
        student_keywords = self.get_all_keywords_student_likes(student)
        list_of_student_ratings_of_professor = []

        for keyword in student_keywords:
            results, meta = db.cypher_query(
                'MATCH (k:Keyword)<-[r2:LIKES]-(s:Student)-[r1:RATES]->(p:Professor) WHERE (k.word=\"' + keyword.word + '\" AND p.name=\"' + professor.name + '\") RETURN r1.rating')
            list_of_student_ratings_of_professor.extend([float(row[0]) for row in results])

        if len(list_of_student_ratings_of_professor) > 0:
            has_common_keyword = True
            value_course = 0

            results, meta = db.cypher_query(
                'MATCH (s:Student)-[r1:RATES]->(p:Professor) WHERE (p.name=\"' + professor.name + '\") RETURN avg(r1.rating)')
            average_rating_of_professor = [float(row[0]) for row in results]
            average_rating_of_professor = average_rating_of_professor[0]

            for rating in list_of_student_ratings_of_professor:
                if rating >= average_rating_of_professor:
                    value_course += 1

            value_course = value_course / len(list_of_student_ratings_of_professor)
        else:
            has_common_keyword = False
            value_course = 0

        return has_common_keyword, value_course
