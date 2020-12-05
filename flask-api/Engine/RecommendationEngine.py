import os
from collections import Counter

from stempel import StempelStemmer

from .CollaborationFiletring import CollaborationFiltering
from .ContentBasedFiltering import ContentBasedFiletring
from .Neo4jConnector import Neo4jConnector

from sklearn.feature_extraction.text import TfidfVectorizer

class RecommendationEngine():
    def __init__(self):
        self.connector = Neo4jConnector()

    def load_db_scripts(self):
        os.system(os.getcwd()+'/Engine/db_scripts/deploy_fieldOfStudy_Informatyka20172018WEAIIiB.py')
        os.system(os.getcwd()+'/Engine/db_scripts/deploy_fieldOfStudy_Informatyka20162017WEAIIiB.py')
        os.system(os.getcwd()+'/Engine/db_scripts/deploy_fieldOfStudy_Informatyka20152016WEAIIiB.py')
        self.get_and_connect_keywords_to_courses()

    def load_students(self):
        os.system('./db_scripts/deploy_students.py')

    def get_and_connect_keywords_to_courses(self):
        courses = self.connector.get_all_courses()

        for course in courses:
            print(course.description)
            # for key,value in self.get_dict_with_stemmed_keywords(course.description).items():
            for key, value in self.get_ifidf_for_words(course.description).items():
                keyword = self.connector.get_keyword(key)
                if not keyword:
                    keyword = self.connector.add_keyword_if_not_exists(word=key)
                self.connector.connect_keyword_describes_course_with_rating(keyword, course, value)


    def get_ifidf_for_words(self, text):

        tfidf = TfidfVectorizer()
        tfidf.fit([text])
        feature_names = tfidf.get_feature_names()

        tfidf_matrix = tfidf.transform([text]).todense()
        feature_index = tfidf_matrix[0, :].nonzero()[1]
        tfidf_scores = zip([feature_names[i] for i in feature_index], [tfidf_matrix[0, x] for x in feature_index])
        return dict(tfidf_scores)

    def get_stemmed_word(self, word):
        stemmer = StempelStemmer.polimorf()
        return stemmer.stem(word)

    def get_dict_with_stemmed_keywords(self, course_description):
        dict_with_keywords = self.get_ifidf_for_words(course_description)
        dict_with_stemmed_keywords = {}
        for key, value in dict(Counter(dict_with_keywords).most_common(5)).items():
            stemmed_key = self.get_stemmed_word(key)
            if stemmed_key in dict_with_stemmed_keywords:
                dict_with_stemmed_keywords[stemmed_key] = dict_with_stemmed_keywords[stemmed_key] + value
            else:
                dict_with_stemmed_keywords[stemmed_key] = value

        return dict_with_stemmed_keywords

    def get_recommendation(self, mode, student):
        if mode == "individual":
            return ContentBasedFiletring().recommend(student)
        elif mode == "team":
            return CollaborationFiltering().recommend(student)
        elif mode == "hybrid":
            content_based = ContentBasedFiletring().recommend(student)
            collaboration = CollaborationFiltering().recommend(student)
            return self.get_hybrid_recommendation(content_based, collaboration)
        else:
            return "Error"

    def get_hybrid_recommendation(self, content_based, collaboration):
        output_dict = {}
        for key,value in content_based.items():
            output_dict[key] = (content_based[key] + collaboration[key])/2
        return output_dict












