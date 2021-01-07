from .Neo4jConnector import Neo4jConnector




connector = Neo4jConnector()
# connector.add_field_of_study_if_not_exists(name="Informatyka", start_years="2017-2018", faculty="Wydział Elektrotechniki, Automatyki, Informatyki i Inżynierii Biomedycznej")
# connector.add_field_of_study_if_not_exists(name="Zarządzanie", start_years="2017-2018", faculty="Wydział Zarządzania")
# connector.add_field_of_study_if_not_exists(name="Matematyka Stosowana", start_years="2017-2018", faculty="Wydział Matematyki Stosowanej")
# connector.add_field_of_study_if_not_exists(name="Informatyka", start_years="2018-2019", faculty="Wydział Elektrotechniki, Automatyki, Informatyki i Inżynierii Biomedycznej")
# connector.add_field_of_study_if_not_exists(name="Zarządzanie", start_years="2018-2019", faculty="Wydział Zarządzania")
# connector.add_field_of_study_if_not_exists(name="Matematyka Stosowana", start_years="2018-2019", faculty="Wydział Matematyki Stosowanej")
connector.drop_db()
# engine = RecommendationEngine().load_db_scripts()
# engine = RecommendationEngine().load_students()

# engine = RecommendationEngine()

# student = engine.connector.get_student("100020")
# keyword = connector.add_keyword_if_not_exists("slowo")
# connector.connect_student_likes_keyword(student, keyword)
# keyword = connector.add_keyword_if_not_exists("slowoa")
# connector.connect_student_likes_keyword(student, keyword)
#
# student = engine.connector.get_student("200003")
# keyword = connector.add_keyword_if_not_exists("obliczeniowa")
# connector.connect_student_likes_keyword(student, keyword)
# keyword = connector.add_keyword_if_not_exists("cyfrowych")
# connector.connect_student_likes_keyword(student, keyword)
#
#
# # keyword = connector.add_keyword_if_not_exists("algebra")
# # connector.connect_student_likes_keyword(student, keyword)
# # keyword = connector.add_keyword_if_not_exists("dane")
# # connector.connect_student_likes_keyword(student, keyword)
# # keyword = connector.add_keyword_if_not_exists("python")
# # connector.connect_student_likes_keyword(student, keyword)
# field_of_study = connector.get_field_of_study(name="Informatyka", start_years="2017-2018", faculty="Wydział Elektrotechniki, Automatyki, Informatyki i Inżynierii Biomedycznej")
# connector.connect_student_studies_field_of_study(student, field_of_study)
# print(engine.get_recommendation("team", student))

