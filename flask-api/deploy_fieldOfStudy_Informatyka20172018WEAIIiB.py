#!/usr/bin/python3.5
import random
import os


# database connector
from Engine.Neo4jConnector import Neo4jConnector
from Engine.models.parse_syllabus_old import parse_syllabus_old

connector = Neo4jConnector()
# connector.drop_db()

# add Field Of Study
field_of_study = connector.add_field_of_study_if_not_exists(name="Informatyka", start_years="2017-2018", faculty="Wydział Elektrotechniki, Automatyki, Informatyki i Inżynierii Biomedycznej")
################### add Professors ####################################
professor1 = connector.add_professor_if_not_exists(name="prof. dr hab. inż. Mitkowski Wojciech")
professor2 = connector.add_professor_if_not_exists(name="dr inż. Cmiel Adam")
professor3 = connector.add_professor_if_not_exists(name="dr hab. Bielecki Andrzej")
professor4 = connector.add_professor_if_not_exists(name="dr hab. Horzyk Adrian")
professor5 = connector.add_professor_if_not_exists(name="Szwed Piotr")
professor6 = connector.add_professor_if_not_exists(name="prof. dr hab. inż. Nalepa Grzegorz J. ")
professor7 = connector.add_professor_if_not_exists(name="prof. dr hab. Kotulski Leszek")
professor8 = connector.add_professor_if_not_exists(name="mgr Śliwa Jacek")
professor9 = connector.add_professor_if_not_exists(name="prof. nadzw. dr hab. inż. Szczerbowska-Boruchowska Magdalena")
professor10 = connector.add_professor_if_not_exists(name="prof. dr hab. inż. Ligęza Antoni")
professor11 = connector.add_professor_if_not_exists(name="Izworski Andrzej")
professor12 = connector.add_professor_if_not_exists(name="Kułakowski Konrad")
professor13 = connector.add_professor_if_not_exists(name="dr hab. inż. Szuba Tadeusz")
professor14 = connector.add_professor_if_not_exists(name="prof. dr hab. Szpyrka Marcin")
professor15 = connector.add_professor_if_not_exists(name="mgr Krukiewicz-Gacek Anna")
professor16 = connector.add_professor_if_not_exists(name="JAMRÓZ DARIUSZ")
professor17 = connector.add_professor_if_not_exists(name="Dudek-Dyduch Ewa")
professor18 = connector.add_professor_if_not_exists(name="Wojnicki Igor")
professor19 = connector.add_professor_if_not_exists(name="Miller Janusz")
professor20 = connector.add_professor_if_not_exists(name="Turek Michał")
professor21 = connector.add_professor_if_not_exists(name="prof. dr hab. inż. Byrski Witold")
professor22 = connector.add_professor_if_not_exists(name="Wąs Jarosław")
professor23 = connector.add_professor_if_not_exists(name="Bubliński Zbigniew")
professor24 = connector.add_professor_if_not_exists(name="Matyasik Piotr ")
professor25 = connector.add_professor_if_not_exists(name="dr Maksymowicz Agata")
professor26 = connector.add_professor_if_not_exists(name="dr Stark Katarzyna")
professor27 = connector.add_professor_if_not_exists(name="dr inż. Wiśniewski Bogusław")
professor28 = connector.add_professor_if_not_exists(name="Klimek Radosław")
professor29 = connector.add_professor_if_not_exists(name="prof. dr hab. inż. Gorgoń Marek")
professor30 = connector.add_professor_if_not_exists(name="dr inż. Adrian Weronika T.")
professor31 = connector.add_professor_if_not_exists(name="dr inż. Kucharska Edyta")
professor32 = connector.add_professor_if_not_exists(name="Kuczek Aleksander")
professor33 = connector.add_professor_if_not_exists(name="Mrówka Rafał")
professor34 = connector.add_professor_if_not_exists(name="dr inż. Gajer Mirosław")
professor35 = connector.add_professor_if_not_exists(name="mgr inż. Fus Andrzej")
professor36 = connector.add_professor_if_not_exists(name="Sędziwy Adam")
professor37 = connector.add_professor_if_not_exists(name="Skrzyński Paweł")
professor38 = connector.add_professor_if_not_exists(name="Szmuc Tomasz")
professor39 = connector.add_professor_if_not_exists(name="Przybyło Jaromir")
professor40 = connector.add_professor_if_not_exists(name="dr inż. Baran Mateusz")
professor41 = connector.add_professor_if_not_exists(name="dr inż. Kraszewska Marta")
professor42 = connector.add_professor_if_not_exists(name="Bobek Szymon")
professor43 = connector.add_professor_if_not_exists(name="dr Pałka Dariusz")
################### add Subjects ####################################

# First Semester
course1 = connector.add_course_if_not_exists(name="Algebra liniowa i geometria analityczna", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-102-s?fields=module-activities"), taught_on_semester=1)
course2 = connector.add_course_if_not_exists(name="Analiza matematyczna", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-103-s?fields=module-activities"), taught_on_semester=1)
course3 = connector.add_course_if_not_exists(name="Matematyka dyskretna", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-104-s?fields=module-activities"), taught_on_semester=1)
course4 = connector.add_course_if_not_exists(name="Wstęp do informatyki", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-105-s?fields=module-activities"), taught_on_semester=1)
course5 = connector.add_course_if_not_exists(name="Języki i metody programowania 1", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-106-s?fields=module-activities"), taught_on_semester=1)
course6 = connector.add_course_if_not_exists(name="Wstęp do systemów uniksowych", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-107-s?fields=module-activities"), taught_on_semester=1)
course7 = connector.add_course_if_not_exists(name="Narzędzia pracy grupowej", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-108-s?fields=module-activities"), taught_on_semester=1)
course8 = connector.add_course_if_not_exists(name="Wychowanie fizyczne 1", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-109-s?fields=module-activities"), taught_on_semester=1)
connector.connect_course_has_field_of_study(course1, field_of_study)
connector.connect_course_has_field_of_study(course2, field_of_study)
connector.connect_course_has_field_of_study(course3, field_of_study)
connector.connect_course_has_field_of_study(course4, field_of_study)
connector.connect_course_has_field_of_study(course5, field_of_study)
connector.connect_course_has_field_of_study(course6, field_of_study)
connector.connect_course_has_field_of_study(course7, field_of_study)
connector.connect_course_has_field_of_study(course8, field_of_study)
connector.connect_professor_teaches_course(professor1, course1)
connector.connect_professor_teaches_course(professor2, course2)
connector.connect_professor_teaches_course(professor3, course3)
connector.connect_professor_teaches_course(professor4, course4)
connector.connect_professor_teaches_course(professor5, course5)
connector.connect_professor_teaches_course(professor6, course6)
connector.connect_professor_teaches_course(professor7, course7)
connector.connect_professor_teaches_course(professor8, course8)
# Second Semester
course9 = connector.add_course_if_not_exists(name="Fizyka 1", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-205-s?fields=module-activities"), taught_on_semester=2)
course10 = connector.add_course_if_not_exists(name="Logika", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-202-s?fields=module-activities"), taught_on_semester=2)
course11 = connector.add_course_if_not_exists(name="Rachunek prawdopodobieństwa i statystyka", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-203-s?fields=module-activities"), taught_on_semester=2)
course12 = connector.add_course_if_not_exists(name="Równania różniczkowe", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-204-s?fields=module-activities"), taught_on_semester=2)
course13 = connector.add_course_if_not_exists(name="Języki i metody programowania 2", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-206-s?fields=module-activities"), taught_on_semester=2)
course14 = connector.add_course_if_not_exists(name="Algorytmy i struktury danych", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-207-s?fields=module-activities"), taught_on_semester=2)
course15 = connector.add_course_if_not_exists(name="Podstawy grafiki komputerowej", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-208-s?fields=module-activities"), taught_on_semester=2)
course16 = connector.add_course_if_not_exists(name="Skład dokumentów w środowisku LaTeX", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-209-s?fields=module-activities"), taught_on_semester=2)
course17 = connector.add_course_if_not_exists(name="Wychowanie fizyczne 2", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-210-s?fields=module-activities"), taught_on_semester=2)
course18 = connector.add_course_if_not_exists(name="Język francuski B-2 – kurs obowiązkowy 135 godzin - semestr 1/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-201-s?fields=module-activities"), taught_on_semester=2, is_elective=True)
course19 = connector.add_course_if_not_exists(name="Język angielski B-2 – kurs obowiązkowy 135 godzin - semestr 1/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-211-s?fields=module-activities"), taught_on_semester=2, is_elective=True)
course20 = connector.add_course_if_not_exists(name="Język hiszpański B-2 – kurs obowiązkowy 135 godzin - semestr 1/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-212-s?fields=module-activities"), taught_on_semester=2, is_elective=True)
course21 = connector.add_course_if_not_exists(name="Język niemiecki B-2 - kurs obowiązkowy 135 godzin - semestr 1/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-213-s?fields=module-activities"), taught_on_semester=2, is_elective=True)
course22 = connector.add_course_if_not_exists(name="Język rosyjski B-2 – kurs obowiązkowy 135 godzin - semestr 1/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-214-s?fields=module-activities"), taught_on_semester=2, is_elective=True)
connector.connect_course_has_field_of_study(course9, field_of_study)
connector.connect_course_has_field_of_study(course10, field_of_study)
connector.connect_course_has_field_of_study(course11, field_of_study)
connector.connect_course_has_field_of_study(course12, field_of_study)
connector.connect_course_has_field_of_study(course13, field_of_study)
connector.connect_course_has_field_of_study(course14, field_of_study)
connector.connect_course_has_field_of_study(course15, field_of_study)
connector.connect_course_has_field_of_study(course16, field_of_study)
connector.connect_course_has_field_of_study(course17, field_of_study)
connector.connect_course_has_field_of_study(course18, field_of_study)
connector.connect_course_has_field_of_study(course19, field_of_study)
connector.connect_course_has_field_of_study(course20, field_of_study)
connector.connect_course_has_field_of_study(course21, field_of_study)
connector.connect_course_has_field_of_study(course22, field_of_study)
connector.connect_professor_teaches_course(professor9, course9)
connector.connect_professor_teaches_course(professor10, course10)
connector.connect_professor_teaches_course(professor11, course11)
connector.connect_professor_teaches_course(professor1, course12)
connector.connect_professor_teaches_course(professor5, course13)
connector.connect_professor_teaches_course(professor12, course14)
connector.connect_professor_teaches_course(professor13, course15)
connector.connect_professor_teaches_course(professor14, course16)
connector.connect_professor_teaches_course(professor8, course17)
connector.connect_professor_teaches_course(professor15, course18)
connector.connect_professor_teaches_course(professor15, course19)
connector.connect_professor_teaches_course(professor15, course20)
connector.connect_professor_teaches_course(professor15, course21)
connector.connect_professor_teaches_course(professor15, course22)
# Third Semester
course23 = connector.add_course_if_not_exists(name="Fizyka 2", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-303-s?fields=module-activities"), taught_on_semester=3)
course24 = connector.add_course_if_not_exists(name="Programowanie w logice", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-301-s?fields=module-activities"), taught_on_semester=3)
course25 = connector.add_course_if_not_exists(name="Programowanie obiektowe", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-305-s?fields=module-activities"), taught_on_semester=3)
course26 = connector.add_course_if_not_exists(name="Architektury komputerów", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-306-s?fields=module-activities"), taught_on_semester=3)
course27 = connector.add_course_if_not_exists(name="Metody numeryczne", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-307-s?fields=module-activities"), taught_on_semester=3)
course28 = connector.add_course_if_not_exists(name="Systemy dynamiczne", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-309-s?fields=module-activities"), taught_on_semester=3)
course29 = connector.add_course_if_not_exists(name="Języki i technologie webowe", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-310-s?fields=module-activities"), taught_on_semester=3)
course30 = connector.add_course_if_not_exists(name="Bazy danych", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-317-s?fields=module-activities"), taught_on_semester=3)
course31 = connector.add_course_if_not_exists(name="Wychowanie fizyczne 3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-316-s?fields=module-activities"), taught_on_semester=3)
course32 = connector.add_course_if_not_exists(name="Język francuski B-2 – kurs obowiązkowy 135 godzin - semestr 2/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-311-s?fields=module-activities"), taught_on_semester=3, is_elective=True)
course33 = connector.add_course_if_not_exists(name="Język angielski B-2 – kurs obowiązkowy 135 godzin - semestr 2/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-312-s?fields=module-activities"), taught_on_semester=3, is_elective=True)
course34 = connector.add_course_if_not_exists(name="Język hiszpański B-2 – kurs obowiązkowy 135 godzin - semestr 2/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-313-s?fields=module-activities"), taught_on_semester=3, is_elective=True)
course35 = connector.add_course_if_not_exists(name="Język niemiecki B-2 - kurs obowiązkowy 135 godzin - semestr 2/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-314-s?fields=module-activities"), taught_on_semester=3, is_elective=True)
course36 = connector.add_course_if_not_exists(name="Język rosyjski B-2 – kurs obowiązkowy 135 godzin - semestr 2/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-315-s?fields=module-activities"), taught_on_semester=3, is_elective=True)
connector.connect_course_has_field_of_study(course23, field_of_study)
connector.connect_course_has_field_of_study(course24, field_of_study)
connector.connect_course_has_field_of_study(course25, field_of_study)
connector.connect_course_has_field_of_study(course26, field_of_study)
connector.connect_course_has_field_of_study(course27, field_of_study)
connector.connect_course_has_field_of_study(course28, field_of_study)
connector.connect_course_has_field_of_study(course29, field_of_study)
connector.connect_course_has_field_of_study(course30, field_of_study)
connector.connect_course_has_field_of_study(course31, field_of_study)
connector.connect_course_has_field_of_study(course32, field_of_study)
connector.connect_course_has_field_of_study(course33, field_of_study)
connector.connect_course_has_field_of_study(course34, field_of_study)
connector.connect_course_has_field_of_study(course35, field_of_study)
connector.connect_course_has_field_of_study(course36, field_of_study)
connector.connect_professor_teaches_course(professor9, course23)
connector.connect_professor_teaches_course(professor10, course24)
connector.connect_professor_teaches_course(professor5, course25)
connector.connect_professor_teaches_course(professor16, course26)
connector.connect_professor_teaches_course(professor17, course27)
connector.connect_professor_teaches_course(professor1, course28)
connector.connect_professor_teaches_course(professor18, course29)
connector.connect_professor_teaches_course(professor14, course30)
connector.connect_professor_teaches_course(professor8, course31)
connector.connect_professor_teaches_course(professor15, course32)
connector.connect_professor_teaches_course(professor15, course33)
connector.connect_professor_teaches_course(professor15, course34)
connector.connect_professor_teaches_course(professor15, course35)
connector.connect_professor_teaches_course(professor15, course36)
# Fourth Semester
course37 = connector.add_course_if_not_exists(name="Analiza numeryczna i symulacja systemów", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-402-s?fields=module-activities"), taught_on_semester=4)
course38 = connector.add_course_if_not_exists(name="Sieci komputerowe", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-405-s?fields=module-activities"), taught_on_semester=4)
course39 = connector.add_course_if_not_exists(name="Podstawy automatyki", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-406-s?fields=module-activities"), taught_on_semester=4)
course40 = connector.add_course_if_not_exists(name="Symulacja dyskretna systemów złożonych", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-407-s?fields=module-activities"), taught_on_semester=4)
course41 = connector.add_course_if_not_exists(name="Programowanie mikrokontrolerów i mikroprocesorów", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-408-s?fields=module-activities"), taught_on_semester=4)
course42 = connector.add_course_if_not_exists(name="Systemy operacyjne", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-409-s?fields=module-activities"), taught_on_semester=4)
course43 = connector.add_course_if_not_exists(name="Programowanie funkcyjne", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-413-s?fields=module-activities"), taught_on_semester=4)
course44 = connector.add_course_if_not_exists(name="Język francuski B-2 – kurs obowiązkowy 135 godzin - semestr 3/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-401-s?fields=module-activities"), taught_on_semester=4, is_elective=True)
course45 = connector.add_course_if_not_exists(name="Język angielski B-2 – kurs obowiązkowy 135 godzin - semestr 3/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-403-s?fields=module-activities"), taught_on_semester=4, is_elective=True)
course46 = connector.add_course_if_not_exists(name="Język hiszpański B-2 – kurs obowiązkowy 135 godzin - semestr 3/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-410-s?fields=module-activities"), taught_on_semester=4, is_elective=True)
course47 = connector.add_course_if_not_exists(name="Język niemiecki B-2 - kurs obowiązkowy 135 godzin - semestr 3/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-411-s?fields=module-activities"), taught_on_semester=4, is_elective=True)
course48 = connector.add_course_if_not_exists(name="Język rosyjski B-2 – kurs obowiązkowy 135 godzin - semestr 3/3", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-412-s?fields=module-activities"), taught_on_semester=4, is_elective=True)
course49 = connector.add_course_if_not_exists(name="Podstawy negocjacji", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-414-s?fields=module-activities"), taught_on_semester=4, is_elective=True)
course50 = connector.add_course_if_not_exists(name="Religie świata: człowiek a sacrum", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-415-s?fields=module-activities"), taught_on_semester=4, is_elective=True)
connector.connect_course_has_field_of_study(course37, field_of_study)
connector.connect_course_has_field_of_study(course38, field_of_study)
connector.connect_course_has_field_of_study(course39, field_of_study)
connector.connect_course_has_field_of_study(course40, field_of_study)
connector.connect_course_has_field_of_study(course41, field_of_study)
connector.connect_course_has_field_of_study(course42, field_of_study)
connector.connect_course_has_field_of_study(course43, field_of_study)
connector.connect_course_has_field_of_study(course44, field_of_study)
connector.connect_course_has_field_of_study(course45, field_of_study)
connector.connect_course_has_field_of_study(course46, field_of_study)
connector.connect_course_has_field_of_study(course47, field_of_study)
connector.connect_course_has_field_of_study(course48, field_of_study)
connector.connect_course_has_field_of_study(course49, field_of_study)
connector.connect_course_has_field_of_study(course50, field_of_study)
connector.connect_professor_teaches_course(professor19, course37)
connector.connect_professor_teaches_course(professor20, course38)
connector.connect_professor_teaches_course(professor21, course39)
connector.connect_professor_teaches_course(professor22, course40)
connector.connect_professor_teaches_course(professor23, course41)
connector.connect_professor_teaches_course(professor7, course42)
connector.connect_professor_teaches_course(professor24, course43)
connector.connect_professor_teaches_course(professor15, course44)
connector.connect_professor_teaches_course(professor15, course45)
connector.connect_professor_teaches_course(professor15, course46)
connector.connect_professor_teaches_course(professor15, course47)
connector.connect_professor_teaches_course(professor15, course48)
connector.connect_professor_teaches_course(professor25, course49)
connector.connect_professor_teaches_course(professor26, course50)
# Fifth Semester
course51 = connector.add_course_if_not_exists(name="Podstawy elektroniki cyfrowej", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-501-s?fields=module-activities"), taught_on_semester=5)
course52 = connector.add_course_if_not_exists(name="Inżynieria oprogramowania", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-503-s?fields=module-activities"), taught_on_semester=5)
course53 = connector.add_course_if_not_exists(name="Programowanie współbieżne i rozproszone", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-504-s?fields=module-activities"), taught_on_semester=5)
course54 = connector.add_course_if_not_exists(name="Przetwarzanie obrazów cyfrowych", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-505-s?fields=module-activities"), taught_on_semester=5)
course55 = connector.add_course_if_not_exists(name="Podstawy sztucznej inteligencji", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-506-s?fields=module-activities"), taught_on_semester=5)
course56 = connector.add_course_if_not_exists(name="Lingwistyka formalna i automaty", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-513-s?fields=module-activities"), taught_on_semester=5)
course57 = connector.add_course_if_not_exists(name="Badania operacyjne i komputerowe wspomaganie decyzji", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-514-s?fields=module-activities"), taught_on_semester=5)
course58 = connector.add_course_if_not_exists(name="Wprowadzenie do systemów ERP", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-502-s?fields=module-activities"), taught_on_semester=5, is_elective=True)
course59 = connector.add_course_if_not_exists(name="Rozwiązania IT w inżynierii produkcji", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-507-s?fields=module-activities"), taught_on_semester=5, is_elective=True)
course60 = connector.add_course_if_not_exists(name="Entrepreneurship And Startups For Technical Students", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-509-s?fields=module-activities"), taught_on_semester=5, is_elective=True)
course61 = connector.add_course_if_not_exists(name="Analiza i modelowanie oprogramowania", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-510-s?fields=module-activities"), taught_on_semester=5, is_elective=True)
course62 = connector.add_course_if_not_exists(name="Design Patterns", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-515-s?fields=module-activities"), taught_on_semester=5, is_elective=True)
connector.connect_course_has_field_of_study(course51, field_of_study)
connector.connect_course_has_field_of_study(course52, field_of_study)
connector.connect_course_has_field_of_study(course53, field_of_study)
connector.connect_course_has_field_of_study(course54, field_of_study)
connector.connect_course_has_field_of_study(course55, field_of_study)
connector.connect_course_has_field_of_study(course56, field_of_study)
connector.connect_course_has_field_of_study(course57, field_of_study)
connector.connect_course_has_field_of_study(course58, field_of_study)
connector.connect_course_has_field_of_study(course59, field_of_study)
connector.connect_course_has_field_of_study(course60, field_of_study)
connector.connect_course_has_field_of_study(course61, field_of_study)
connector.connect_course_has_field_of_study(course62, field_of_study)
connector.connect_professor_teaches_course(professor27, course51)
connector.connect_professor_teaches_course(professor28, course52)
connector.connect_professor_teaches_course(professor24, course53)
connector.connect_professor_teaches_course(professor29, course54)
connector.connect_professor_teaches_course(professor6, course55)
connector.connect_professor_teaches_course(professor28, course56)
connector.connect_professor_teaches_course(professor30, course57)
connector.connect_professor_teaches_course(professor31, course58)
connector.connect_professor_teaches_course(professor32, course59)
connector.connect_professor_teaches_course(professor32, course60)
connector.connect_professor_teaches_course(professor28, course61)
connector.connect_professor_teaches_course(professor33, course62)

# Sixth Semester
course63 = connector.add_course_if_not_exists(name="Praktyki (4 tygodnie po VI semestrze)", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-611-s?fields=module-activities"), taught_on_semester=6)
course64 = connector.add_course_if_not_exists(name="Prawo autorskie i patentowe", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-615-s?fields=module-activities"), taught_on_semester=6)
course65 = connector.add_course_if_not_exists(name="Teoria Obliczeń", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-601-s?fields=module-activities"), taught_on_semester=6)
course66 = connector.add_course_if_not_exists(name="Teoria kompilacji i kompilatory", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-602-s?fields=module-activities"), taught_on_semester=6)
course67 = connector.add_course_if_not_exists(name="Studio projektowe 1", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-610-s?fields=module-activities"), taught_on_semester=6)
course68 = connector.add_course_if_not_exists(name="Wprowadzenie do technologii mobilnych", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-603-s?fields=module-activities"), taught_on_semester=6, is_elective=False)
course69 = connector.add_course_if_not_exists(name="SOA w projektowaniu i implementacji oprogramowania", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-604-s?fields=module-activities"), taught_on_semester=6, is_elective=True)
course70 = connector.add_course_if_not_exists(name="Systemy czasu rzeczywistego", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-606-s?fields=module-activities"), taught_on_semester=6, is_elective=True)
course71 = connector.add_course_if_not_exists(name="Systemy wbudowane", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-607-s?fields=module-activities"), taught_on_semester=6, is_elective=True)
course72 = connector.add_course_if_not_exists(name="Systemy rekonfigurowalne", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-612-s?fields=module-activities"), taught_on_semester=6, is_elective=True)
course73 = connector.add_course_if_not_exists(name="Interfejsy multimodalne", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-613-s?fields=module-activities"), taught_on_semester=6, is_elective=True)
course74 = connector.add_course_if_not_exists(name="Inteligencja obliczeniowa w analizie danych cyfrowych", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-614-s?fields=module-activities"), taught_on_semester=6, is_elective=True)
connector.connect_course_has_field_of_study(course63, field_of_study)
connector.connect_course_has_field_of_study(course64, field_of_study)
connector.connect_course_has_field_of_study(course65, field_of_study)
connector.connect_course_has_field_of_study(course66, field_of_study)
connector.connect_course_has_field_of_study(course67, field_of_study)
connector.connect_course_has_field_of_study(course68, field_of_study)
connector.connect_course_has_field_of_study(course69, field_of_study)
connector.connect_course_has_field_of_study(course70, field_of_study)
connector.connect_course_has_field_of_study(course71, field_of_study)
connector.connect_course_has_field_of_study(course72, field_of_study)
connector.connect_course_has_field_of_study(course73, field_of_study)
connector.connect_course_has_field_of_study(course74, field_of_study)
connector.connect_professor_teaches_course(professor34, course63)
connector.connect_professor_teaches_course(professor35, course64)
connector.connect_professor_teaches_course(professor36, course65)
connector.connect_professor_teaches_course(professor28, course66)
connector.connect_professor_teaches_course(professor28, course67)
connector.connect_professor_teaches_course(professor37, course68)
connector.connect_professor_teaches_course(professor37, course69)
connector.connect_professor_teaches_course(professor38, course70)
connector.connect_professor_teaches_course(professor38, course71)
connector.connect_professor_teaches_course(professor29, course72)
connector.connect_professor_teaches_course(professor39, course73)
connector.connect_professor_teaches_course(professor40, course74)
# Seventh Semester
course75 = connector.add_course_if_not_exists(name="Aspekty prawne i organizacja przedsiębiorstwa", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-714-s?fields=module-activities"), taught_on_semester=7)
course76 = connector.add_course_if_not_exists(name="Pracownia inżynierska dyplomowa", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-702-s?fields=module-activities"), taught_on_semester=7)
course77 = connector.add_course_if_not_exists(name="Praca dyplomowa", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-711-s?fields=module-activities"), taught_on_semester=7)
course78 = connector.add_course_if_not_exists(name="Studio projektowe 2", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-701-s?fields=module-activities"), taught_on_semester=7)
course79 = connector.add_course_if_not_exists(name="Systemy informatyczne ERP", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-703-s?fields=module-activities"), taught_on_semester=7)
course80 = connector.add_course_if_not_exists(name="Systemy i technologie wirtualizacji", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-705-s?fields=module-activities"), taught_on_semester=7, is_elective=True)
course81 = connector.add_course_if_not_exists(name="Hurtownie danych", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-706-s?fields=module-activities"), taught_on_semester=7, is_elective=True)
course82 = connector.add_course_if_not_exists(name="Multimedia i transmisje multimedialne", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-707-s?fields=module-activities"), taught_on_semester=7, is_elective=True)
course83 = connector.add_course_if_not_exists(name="Praca w kole naukowym", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-710-s?fields=module-activities"), taught_on_semester=7, is_elective=True)
course84 = connector.add_course_if_not_exists(name="Prowadzenie badań naukowych", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-712-s?fields=module-activities"), taught_on_semester=7, is_elective=True)
course85 = connector.add_course_if_not_exists(name="Systemy analizy biznesowej", description=parse_syllabus_old("https://syllabuskrk.agh.edu.pl/2017-2018/magnesite/api/faculties/weaiiib/study_plans/stacjonarne-informatyka--6/modules/eit-1-713-s?fields=module-activities"), taught_on_semester=7, is_elective=True)
connector.connect_course_has_field_of_study(course75, field_of_study)
connector.connect_course_has_field_of_study(course76, field_of_study)
connector.connect_course_has_field_of_study(course77, field_of_study)
connector.connect_course_has_field_of_study(course78, field_of_study)
connector.connect_course_has_field_of_study(course79, field_of_study)
connector.connect_course_has_field_of_study(course80, field_of_study)
connector.connect_course_has_field_of_study(course81, field_of_study)
connector.connect_course_has_field_of_study(course82, field_of_study)
connector.connect_course_has_field_of_study(course83, field_of_study)
connector.connect_course_has_field_of_study(course84, field_of_study)
connector.connect_course_has_field_of_study(course85, field_of_study)
connector.connect_professor_teaches_course(professor41, course75)
connector.connect_professor_teaches_course(professor6, course76)
connector.connect_professor_teaches_course(professor14, course77)
connector.connect_professor_teaches_course(professor28, course78)
connector.connect_professor_teaches_course(professor31, course79)
connector.connect_professor_teaches_course(professor42, course80)
connector.connect_professor_teaches_course(professor7, course81)
connector.connect_professor_teaches_course(professor43, course82)
connector.connect_professor_teaches_course(professor12, course83)
connector.connect_professor_teaches_course(professor12, course84)
connector.connect_professor_teaches_course(professor31, course85)

student = connector.add_student_if_not_exists(index_number=200003, name="Tester", email="email", password="pass", api_key="key")
connector.connect_student_evaluates_course(student, course1, random.randint(1,5)) # Algebra liniowa i geometria analityczna
connector.connect_student_evaluates_course(student, course2, random.randint(1,5)) # Analiza matematyczna
connector.connect_student_evaluates_course(student, course3, random.randint(1,5)) # Matematyka dyskretna
connector.connect_student_evaluates_course(student, course4, random.randint(1,5)) # Wstęp do informatyki
connector.connect_student_evaluates_course(student, course5, random.randint(1,5)) # Języki i metody programowania 1
connector.connect_student_evaluates_course(student, course6, random.randint(1,5)) # Wstęp do systemów uniksowych
connector.connect_student_evaluates_course(student, course7, random.randint(1,5)) # Narzędzia pracy grupowej
connector.connect_student_evaluates_course(student, course8, random.randint(1,5)) # Wychowanie fizyczne 1
connector.connect_student_evaluates_course(student, course9, random.randint(1,5)) # Fizyka 1
connector.connect_student_evaluates_course(student, course10, random.randint(1,5)) # Logika
connector.connect_student_evaluates_course(student, course11, random.randint(1,5)) # Rachunek prawdopodobieństwa i statystyka
connector.connect_student_evaluates_course(student, course12, random.randint(1,5)) # Równania różniczkowe
connector.connect_student_evaluates_course(student, course13, random.randint(1,5)) # Języki i metody programowania 2
connector.connect_student_evaluates_course(student, course14, random.randint(1,5)) # Algorytmy i struktury danych
connector.connect_student_evaluates_course(student, course15, random.randint(1,5)) # Podstawy grafiki komputerowej
connector.connect_student_evaluates_course(student, course16, random.randint(1,5)) # Skład dokumentów w środowisku LaTeX
connector.connect_student_evaluates_course(student, course17, random.randint(1,5)) # Wychowanie fizyczne 2
# connector.connect_student_evaluates_course(student, course18, random.randint(1,5)) # Język francuski B-2
connector.connect_student_evaluates_course(student, course19, random.randint(1,5)) # Język angielski B-2
# connector.connect_student_evaluates_course(student, course20, random.randint(1,5)) # Język hiszpański B-2
# connector.connect_student_evaluates_course(student, course21, random.randint(1,5)) # Język niemiecki B-2
# connector.connect_student_evaluates_course(student, course22, random.randint(1,5)) # Język rosyjski B-2
connector.connect_student_evaluates_course(student, course23, random.randint(1,5)) # Fizyka 2
connector.connect_student_evaluates_course(student, course24, random.randint(1,5)) # Programowanie w logice
connector.connect_student_evaluates_course(student, course25, random.randint(1,5)) # Programowanie obiektowe
connector.connect_student_evaluates_course(student, course26, random.randint(1,5)) # Architektury komputerów
connector.connect_student_evaluates_course(student, course27, random.randint(1,5)) # Metody numeryczne
connector.connect_student_evaluates_course(student, course28, random.randint(1,5)) # Systemy dynamiczne
connector.connect_student_evaluates_course(student, course29, random.randint(1,5)) # Języki i technologie webowe
connector.connect_student_evaluates_course(student, course30, random.randint(1,5)) # Bazy danych
connector.connect_student_evaluates_course(student, course31, random.randint(1,5)) # Wychowanie fizyczne 3
# connector.connect_student_evaluates_course(student, course32, random.randint(1,5)) # Język francuski B-2
connector.connect_student_evaluates_course(student, course33, random.randint(1,5)) # Język angielski B-2
# connector.connect_student_evaluates_course(student, course34, random.randint(1,5)) # Język hiszpański B-2
# connector.connect_student_evaluates_course(student, course35, random.randint(1,5)) # Język niemiecki B-2
# connector.connect_student_evaluates_course(student, course36, random.randint(1,5)) # Język rosyjski B-2
connector.connect_student_evaluates_course(student, course37, random.randint(1,5)) # Analiza numeryczna i symulacja systemów
connector.connect_student_evaluates_course(student, course38, random.randint(1,5)) # Sieci komputerowe
connector.connect_student_evaluates_course(student, course39, random.randint(1,5)) # Podstawy automatyki
connector.connect_student_evaluates_course(student, course40, random.randint(1,5)) # Symulacja dyskretna systemów złożonych
connector.connect_student_evaluates_course(student, course41, random.randint(1,5)) # Programowanie mikrokontrolerów i mikroprocesorów
connector.connect_student_evaluates_course(student, course42, random.randint(1,5)) # Systemy operacyjne
connector.connect_student_evaluates_course(student, course43, random.randint(1,5)) # Programowanie funkcyjne
# connector.connect_student_evaluates_course(student, course44, random.randint(1,5)) # Język francuski B-2
connector.connect_student_evaluates_course(student, course45, random.randint(1,5)) # Język angielski B-2
# connector.connect_student_evaluates_course(student, course46, random.randint(1,5)) # Język hiszpański B-2
# connector.connect_student_evaluates_course(student, course47, random.randint(1,5)) # Język niemiecki B-2
# connector.connect_student_evaluates_course(student, course48, random.randint(1,5)) # Język rosyjski B-2
# connector.connect_student_evaluates_course(student, course49, random.randint(1,5)) # Podstawy negocjacji
# connector.connect_student_evaluates_course(student, course50, random.randint(1,5)) # Religie świata: człowiek a sacrum
connector.connect_student_evaluates_course(student, course51, random.randint(1,5)) # Podstawy elektroniki cyfrowej
connector.connect_student_evaluates_course(student, course52, random.randint(1,5)) # Inżynieria oprogramowania
connector.connect_student_evaluates_course(student, course53, random.randint(1,5)) # Programowanie współbieżne i rozproszone
connector.connect_student_evaluates_course(student, course54, random.randint(1,5)) # Przetwarzanie obrazów cyfrowych
connector.connect_student_evaluates_course(student, course55, random.randint(1,5)) # Podstawy sztucznej inteligencji
connector.connect_student_evaluates_course(student, course56, random.randint(1,5)) # Lingwistyka formalna i automaty
connector.connect_student_evaluates_course(student, course57, random.randint(1,5)) # Badania operacyjne i komputerowe wspomaganie decyzji
connector.connect_student_evaluates_course(student, course58, random.randint(1,5)) # Wprowadzenie do systemów ERP
connector.connect_student_evaluates_course(student, course59, random.randint(1,5)) # Rozwiązania IT w inżynierii produkcji
# connector.connect_student_evaluates_course(student, course60, random.randint(1,5)) # Entrepreneurship And Startups For Technical Students
# connector.connect_student_evaluates_course(student, course61, random.randint(1,5)) # Analiza i modelowanie oprogramowania
# connector.connect_student_evaluates_course(student, course62, random.randint(1,5)) # Design Patterns
# connector.connect_student_evaluates_course(student, course63, random.randint(1,5)) # Praktyki (4 tygodnie po VI semestrze)
# connector.connect_student_evaluates_course(student, course64, random.randint(1,5)) # Prawo autorskie i patentowe
# connector.connect_student_evaluates_course(student, course65, random.randint(1,5)) # Teoria Obliczeń
# connector.connect_student_evaluates_course(student, course66, random.randint(1,5)) # Teoria kompilacji i kompilatory
# connector.connect_student_evaluates_course(student, course67, random.randint(1,5)) # Studio projektowe 1
# connector.connect_student_evaluates_course(student, course68, random.randint(1,5)) # Wprowadzenie do technologii mobilnych
# # connector.connect_student_evaluates_course(student, course69, random.randint(1,5)) # SOA w projektowaniu i implementacji oprogramowania
# # connector.connect_student_evaluates_course(student, course70, random.randint(1,5)) # Systemy czasu rzeczywistego
# # connector.connect_student_evaluates_course(student, course71, random.randint(1,5)) # Systemy wbudowane
# # connector.connect_student_evaluates_course(student, course72, random.randint(1,5)) # Systemy rekonfigurowalne
# connector.connect_student_evaluates_course(student, course73, random.randint(1,5)) # Interfejsy multimodalne
# connector.connect_student_evaluates_course(student, course74, random.randint(1,5)) # Inteligencja obliczeniowa w analizie danych cyfrowych
# connector.connect_student_evaluates_course(student, course75, random.randint(1,5)) # Aspekty prawne i organizacja przedsiębiorstwa
# connector.connect_student_evaluates_course(student, course76, random.randint(1,5)) # Pracownia inżynierska dyplomowa
# connector.connect_student_evaluates_course(student, course77, random.randint(1,5)) # Praca dyplomowa
# connector.connect_student_evaluates_course(student, course78, random.randint(1,5)) # Studio projektowe 2
# # connector.connect_student_evaluates_course(student, course79, random.randint(1,5)) # Systemy informatyczne ERP
# connector.connect_student_evaluates_course(student, course80, random.randint(1,5)) # Systemy i technologie wirtualizacji
# connector.connect_student_evaluates_course(student, course81, random.randint(1,5)) # Hurtownie danych
# connector.connect_student_evaluates_course(student, course82, random.randint(1,5)) # Multimedia i transmisje multimedialne
# # connector.connect_student_evaluates_course(student, course83, random.randint(1,5)) # Praca w kole naukowym
# # connector.connect_student_evaluates_course(student, course84, random.randint(1,5)) # Prowadzenie badań naukowych
# # connector.connect_student_evaluates_course(student, course85, random.randint(1,5)) # Systemy analizy biznesowej
connector.connect_student_rates_professor(student, professor1, random.randint(1,5)) # name="prof. dr hab. inż. Mitkowski Wojciech")
connector.connect_student_rates_professor(student, professor2, random.randint(1,5)) # name="dr inż. Cmiel Adam")
connector.connect_student_rates_professor(student, professor3, random.randint(1,5)) # name="dr hab. Bielecki Andrzej")
connector.connect_student_rates_professor(student, professor4, random.randint(1,5)) # name="dr hab. Horzyk Adrian")
connector.connect_student_rates_professor(student, professor5, random.randint(1,5)) # name="Szwed Piotr")
connector.connect_student_rates_professor(student, professor6, random.randint(1,5)) # name="prof. dr hab. inż. Nalepa Grzegorz J. ")
connector.connect_student_rates_professor(student, professor7, random.randint(1,5)) # name="prof. dr hab. Kotulski Leszek")
connector.connect_student_rates_professor(student, professor8, random.randint(1,5)) # name="mgr Śliwa Jacek")
connector.connect_student_rates_professor(student, professor9, random.randint(1,5)) # name="prof. nadzw. dr hab. inż. Szczerbowska-Boruchowska Magdalena")
connector.connect_student_rates_professor(student, professor10, random.randint(1,5)) # name="prof. dr hab. inż. Ligęza Antoni")
connector.connect_student_rates_professor(student, professor11, random.randint(1,5)) # name="Izworski Andrzej")
connector.connect_student_rates_professor(student, professor12, random.randint(1,5)) # name="Kułakowski Konrad")
connector.connect_student_rates_professor(student, professor13, random.randint(1,5)) # name="dr hab. inż. Szuba Tadeusz")
connector.connect_student_rates_professor(student, professor14, random.randint(1,5)) # name="prof. dr hab. Szpyrka Marcin")
connector.connect_student_rates_professor(student, professor15, random.randint(1,5)) # name="mgr Krukiewicz-Gacek Anna")
connector.connect_student_rates_professor(student, professor16, random.randint(1,5)) # name="JAMRÓZ DARIUSZ")
connector.connect_student_rates_professor(student, professor17, random.randint(1,5)) # name="Dudek-Dyduch Ewa")
connector.connect_student_rates_professor(student, professor18, random.randint(1,5)) # name="Wojnicki Igor")
connector.connect_student_rates_professor(student, professor19, random.randint(1,5)) # name="Miller Janusz")
connector.connect_student_rates_professor(student, professor20, random.randint(1,5)) # name="Turek Michał")
connector.connect_student_rates_professor(student, professor21, random.randint(1,5)) # name="prof. dr hab. inż. Byrski Witold")
connector.connect_student_rates_professor(student, professor22, random.randint(1,5)) # name="Wąs Jarosław")
connector.connect_student_rates_professor(student, professor23, random.randint(1,5)) # name="Bubliński Zbigniew")
connector.connect_student_rates_professor(student, professor24, random.randint(1,5)) # name="Matyasik Piotr ")
connector.connect_student_rates_professor(student, professor25, random.randint(1,5)) # name="dr Maksymowicz Agata")
connector.connect_student_rates_professor(student, professor26, random.randint(1,5)) # name="dr Stark Katarzyna")
connector.connect_student_rates_professor(student, professor27, random.randint(1,5)) # name="dr inż. Wiśniewski Bogusław")
connector.connect_student_rates_professor(student, professor28, random.randint(1,5)) # name="Klimek Radosław")
connector.connect_student_rates_professor(student, professor29, random.randint(1,5)) # name="prof. dr hab. inż. Gorgoń Marek")
connector.connect_student_rates_professor(student, professor30, random.randint(1,5)) # name="dr inż. Adrian Weronika T.")
connector.connect_student_rates_professor(student, professor31, random.randint(1,5)) # name="dr inż. Kucharska Edyta")
connector.connect_student_rates_professor(student, professor32, random.randint(1,5)) # name="Kuczek Aleksander")
connector.connect_student_rates_professor(student, professor33, random.randint(1,5)) # name="Mrówka Rafał")
connector.connect_student_rates_professor(student, professor34, random.randint(1,5)) # name="dr inż. Gajer Mirosław")
connector.connect_student_rates_professor(student, professor35, random.randint(1,5)) # name="mgr inż. Fus Andrzej")
connector.connect_student_rates_professor(student, professor36, random.randint(1,5)) # name="Sędziwy Adam")
connector.connect_student_rates_professor(student, professor37, random.randint(1,5)) # name="Skrzyński Paweł")
connector.connect_student_rates_professor(student, professor38, random.randint(1,5)) # name="Szmuc Tomasz")
connector.connect_student_rates_professor(student, professor39, random.randint(1,5)) # name="Przybyło Jaromir")
connector.connect_student_rates_professor(student, professor40, random.randint(1,5)) # name="dr inż. Baran Mateusz")
connector.connect_student_rates_professor(student, professor41, random.randint(1,5)) # name="dr inż. Kraszewska Marta")
connector.connect_student_rates_professor(student, professor42, random.randint(1,5)) # name="Bobek Szymon")
connector.connect_student_rates_professor(student, professor43, random.randint(1,5)) # name="dr Pałka Dariusz")

