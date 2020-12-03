#!/usr/bin/python3.5
from Engine.Neo4jConnector import Neo4jConnector
import random
# database connector
connector = Neo4jConnector()

field_of_study = connector.get_field_of_study(name="Informatyka", start_years="2016-2017", faculty="Wydział Elektrotechniki, Automatyki, Informatyki i Inżynierii Biomedycznej")
#
# students_list = []
# list_courses_elective = connector.get_past_courses_only_electives(student1)
#
# student1 = connector.add_student_if_not_exists(index_number=100001, name="Jan1 Kowalski", is_on_semester=7)
# students_list.append(student1)
# list_courses_elective = connector.get_past_courses_only_electives(student1)
# for course in list_courses_elective:
#     if course.name
# student2 = connector.add_student_if_not_exists(index_number=100002, name="Jan2 Kowalski", is_on_semester=7)
# students_list.append(student2)
# student3 = connector.add_student_if_not_exists(index_number=100003, name="Jan3 Kowalski", is_on_semester=7)
# students_list.append(student3)
# student4 = connector.add_student_if_not_exists(index_number=100004, name="Jan4 Kowalski", is_on_semester=7)
# students_list.append(student4)
# student5 = connector.add_student_if_not_exists(index_number=100005, name="Jan5 Kowalski", is_on_semester=7)
# students_list.append(student5)
# student6 = connector.add_student_if_not_exists(index_number=100006, name="Jan6 Kowalski", is_on_semester=7)
# students_list.append(student6)
# student7 = connector.add_student_if_not_exists(index_number=100007, name="Jan7 Kowalski", is_on_semester=7)
# students_list.append(student7)
# student8 = connector.add_student_if_not_exists(index_number=100008, name="Jan8 Kowalski", is_on_semester=7)
# students_list.append(student8)
# student9 = connector.add_student_if_not_exists(index_number=100009, name="Jan9 Kowalski", is_on_semester=7)
# students_list.append(student9)
# student10 = connector.add_student_if_not_exists(index_number=100010, name="Jan10 Kowalski", is_on_semester=7)
# students_list.append(student10)
#
#
#
# def randomize_all_ratings(students, field_of_study):
#     for student1 in students:
#         if student1:
#             connector.connect_student_studies_field_of_study(student1, field_of_study)
#             for professor in connector.get_past_professors(student1):
#                 connector.connect_student_rates_professor(student1, professor, random.randint(1, 5))
#
#             for course in connector.get_past_courses_without_electives(student1):
#                 connector.connect_student_evaluates_course(student1, course, random.randint(1, 5))
#
# randomize_all_ratings(students_list, field_of_study)



