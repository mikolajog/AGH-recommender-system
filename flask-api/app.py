import binascii
import hashlib
import os
import ast
import re
import sys
import uuid
from dotenv import load_dotenv, find_dotenv
from functools import wraps

from flask import Flask, g, request, send_from_directory, abort, request_started
from flask_cors import CORS
from flask_restful import Resource, reqparse
from flask_restful_swagger_2 import Api, swagger, Schema
from flask_json import FlaskJSON, json_response

from neo4j import GraphDatabase, basic_auth

from .Engine.RecommendationEngine import RecommendationEngine
from .Engine.Neo4jConnector import Neo4jConnector

load_dotenv(find_dotenv())

app = Flask(__name__)
CORS(app)
FlaskJSON(app)
api = Api(app, title='AGH Recommender System', api_version='0.0.1')
# comment


@api.representation('application/json')
def output_json(data, code, headers=None):
    return json_response(data_=data, headers_=headers, status_=code)


# def env(key, default=None, required=True):
#     """
#     Retrieves environment variables and returns Python natives. The (optional)
#     default will be returned if the environment variable does not exist.
#     """
#     try:
#         value = os.environ[key]
#         return ast.literal_eval(value)
#     except (SyntaxError, ValueError):
#         return value
#     except KeyError:
#         if default or not required:
#             return default
#         raise RuntimeError("Missing required environment variable '%s'" % key)

#
# DATABASE_USERNAME = env('MOVIE_DATABASE_USERNAME')
# DATABASE_PASSWORD = env('MOVIE_DATABASE_PASSWORD')
# DATABASE_URL = env('MOVIE_DATABASE_URL')
#
# driver = GraphDatabase.driver(DATABASE_URL, auth=basic_auth(DATABASE_USERNAME, str(DATABASE_PASSWORD)))
#
# app.config['SECRET_KEY'] = env('SECRET_KEY')

# Adding paths to api


def serialize_user(user):
    return {
        'index_number': user.index_number,
        'name': user.name,
        'email': user.email,
        'avatar': {
            'full_size': 'https://www.gravatar.com/avatar/{}?d=retro'.format(hash_avatar(user.name))
        }
    }

def hash_password(username, password):
    if sys.version[0] == 2:
        s = '{}:{}'.format(username, password)
    else:
        s = '{}:{}'.format(username, password).encode('utf-8')
    return hashlib.sha256(s).hexdigest()


def hash_avatar(username):
    if sys.version[0] == 2:
        s = username
    else:
        s = username.encode('utf-8')
    return hashlib.md5(s).hexdigest()

def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return {'message': 'no authorization provided'}, 401
        return f(*args, **kwargs)
    return wrapped

class UserModel(Schema):
    type = 'object'
    properties = {
        'index_number': {
            'type': 'string',
        },
        'name': {
            'type': 'string',
        },
        'email': {
            'type': 'string',
        },
    }


class Register(Resource):
    @swagger.doc({
        'tags': ['users'],
        'summary': 'Register a new user',
        'description': 'Register a new user',
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'index_number': {
                            'type': 'string',
                        },
                        'name': {
                            'type': 'string',
                        },
                        'email': {
                            'type': 'string',
                        },
                        'password': {
                            'type': 'string',
                        }
                    }
                }
            },
        ],
        'responses': {
            '201': {
                'description': 'Your new user',
                'schema': UserModel,
            },
            '400': {
                'description': 'Error message(s)',
            },
        }
    })
    def post(self):
        data = request.get_json()
        index_number = data.get('index_number')
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not index_number:
            return {'index_number': 'This field is required.'}, 400
        if not name:
            return {'name': 'This field is required.'}, 400
        if not email:
            return {'email': 'This field is required.'}, 400
        if not password:
            return {'password': 'This field is required.'}, 400

        connector = Neo4jConnector()
        result = connector.get_student(index_number)
        print(result)
        if result is not None:
            return {'index_number': 'index number already in use'}, 400

        user = connector.add_student_if_not_exists(index_number, name, email, hash_password(name, password),binascii.hexlify(os.urandom(20)).decode())
        return serialize_user(user), 201


class Login(Resource):
    @swagger.doc({
        'tags': ['users'],
        'summary': 'Login a user',
        'description': 'Login a user',
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'index_number': {
                            'type': 'string',
                        },
                        'password': {
                            'type': 'string',
                        }
                    }
                }
            },
        ],
        'responses': {
            '200': {
                'description': 'succesful login'
            },
            '400': {
                'description': 'invalid credentials'
            }
        }
    })
    def post(self):
        data = request.get_json()
        index_number = data.get('index_number')
        password = data.get('password')
        if not index_number:
            return {'index_number': 'This field is required.'}, 400
        if not password:
            return {'password': 'This field is required.'}, 400

        connector = Neo4jConnector()
        user = connector.get_student(index_number)
        if user is None:
            return {'username': 'username does not exist'}, 400

        expected_password = hash_password(user.name, password)
        if user.password != expected_password:
            return {'password': 'wrong password'}, 400
        return {
            'token': user.api_key
        }

class ApiDocs(Resource):
    def get(self, path=None):
        if not path:
            path = 'index.html'
        return send_from_directory('swaggerui', path)

class KeywordModelResponse(Schema):
    type = 'object'
    properties = {
        'word': {
            'type': 'string',
        }
    }

class AddKeywordModelPost(Schema):
    type = 'object'
    properties = {
        'word': {
            'type': 'string',
        },
        'token': {
            'type': 'string',
        }
    }

def serialize_keyword(word):
    return {
        'word': word
    }

class AddKeywords(Resource):
    @swagger.doc({
        'tags': ['keyword'],
        'summary': 'Add keyword',
        'description': 'Add keywords for particular user',
        'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': AddKeywordModelPost
        }
        ],
        'responses': {
            '200': {
                'description': 'the keyword',
                'schema': KeywordModelResponse,
            },
            '400': {
                'description': 'user does not exist',
            },
            '401': {
                'description': 'user already has this keyword',
            },
        }
    })
    def post(self):
        data = request.get_json()
        word = data.get('word')
        token = data.get('token')
        connector = Neo4jConnector()
        user = connector.get_student_by_token(token)
        if user is None:
            return {'token': 'user does not exist'}, 400
        word = connector.add_keyword_if_not_exists(word)
        all_student_keywords = connector.get_all_keywords_student_likes(user)
        if word in all_student_keywords:
            return {'word': 'user already has this keyword'}, 401
        connector.connect_student_likes_keyword(keyword=word, student=user)
        all_student_keywords = connector.get_all_keywords_student_likes(user)
        return [serialize_keyword(word.word) for word in all_student_keywords], 200


class GetKeywords(Resource):
    @swagger.doc({
        'tags': ['keyword'],
        'summary': 'Get keywords',
        'description': 'Get keywords of particular user',
        'parameters': [
        {
            'name': 'token',
            'description': 'token',
            'in': 'path',
            'type': 'string',
        }],
        'responses': {
            '200': {
                'description': 'A list of keywords',
                    'schema': {
                        'type': 'array',
                        'items': KeywordModelResponse,
                    }
            },
            '400': {
                'description': 'user does not exist',
            },
        }
    })
    def get(self, token):
        connector = Neo4jConnector()
        user = connector.get_student_by_token(token)
        if user is None:
            return {'token': 'user does not exist'}, 400
        all_student_keywords = connector.get_all_keywords_student_likes(user)
        return [serialize_keyword(word.word) for word in all_student_keywords], 200

class DeleteKeywords(Resource):
    @swagger.doc({
        'tags': ['keyword'],
        'summary': 'Delete keyword',
        'description': 'Delete keywords for particular user',
        'parameters': [
            {
                'name': 'token',
                'description': 'token',
                'in': 'path',
                'type': 'string',
            },
            {
                'name': 'word',
                'description': 'word',
                'in': 'path',
                'type': 'string',
            }
        ],
        'responses': {
            '200': {
                'description': 'A list of keywords',
                    'schema': {
                        'type': 'array',
                        'items': KeywordModelResponse,
                    }
            },
            '400': {
                'description': 'user does not exist',
            },
            '401': {
                'description': 'user does not have this keyword',
            },
        }
    })
    def delete(self, token, word):
        connector = Neo4jConnector()
        user = connector.get_student_by_token(token)
        print(word, token)
        if user is None:
            return {'token': 'user does not exist'}, 400
        all_student_keywords = connector.get_all_keywords_student_likes(user)
        for k in all_student_keywords:
            print(k.word, word)
            if k.word==word:
                word = connector.get_keyword(word)
                connector.disconnect_student_likes_keyword(keyword=word, student=user)
                all_student_keywords = connector.get_all_keywords_student_likes(user)
                return [serialize_keyword(word.word) for word in all_student_keywords], 200
        return {'word': 'user does not have this keyword'}, 401

class FacultyModelResponse(Schema):
    type = 'object'
    properties = {
        'faculty': {
            'type': 'string',
        }
    }
def serialize_faculty(faculty):
    return {
        'faculty': faculty
    }

class GetFaculty(Resource):
    @swagger.doc({
        'tags': ['fieldofstudy'],
        'summary': 'Get possible faculties',
        'description': 'Get possible faculties',
        'responses': {
            '200': {
                'description': 'A list of faculties',
                'schema': {
                    'type': 'array',
                    'items': FacultyModelResponse,
                }
            },
    }})
    def get(self):
        connector = Neo4jConnector()
        faculties = connector.get_all_possible_faculties()
        return [serialize_faculty(faculty) for faculty in faculties], 200


class FieldofstudyModelResponse(Schema):
    type = 'object'
    properties = {
        'fieldofstudy': {
            'type': 'string',
        }
    }
def serialize_fieldofstudy(field):
    return {
        'fieldofstudy': field
    }

class GetFieldofStudyNames(Resource):
    @swagger.doc({
        'tags': ['fieldofstudy'],
        'summary': 'Get possible field of study names for particular faculty',
        'description': 'Get possible field of study names for particular faculty',
        'parameters': [
            {
                'name': 'faculty',
                'description': 'faculty',
                'in': 'path',
                'type': 'string',
            }
        ],
        'responses': {
            '200': {
                'description': 'A list of field of studies names',
                'schema': {
                    'type': 'array',
                    'items': FieldofstudyModelResponse,
                }
            },
            '401': {
                'description': 'no such faculty',
            },
        }})
    def get(self, faculty):
        connector = Neo4jConnector()
        fields = connector.get_all_possible_fieldofstudiesnames(faculty)
        return [serialize_fieldofstudy(field) for field in fields], 200

class StartYearsModelResponse(Schema):
    type = 'object'
    properties = {
        'years': {
            'type': 'string',
        }
    }
def serialize_startyears(years):
    return {
        'years': years
    }


class GetStartYears(Resource):
    @swagger.doc({
        'tags': ['fieldofstudy'],
        'summary': 'Get possible start years for particular field of study',
        'description': 'Get possible start years for particular field of study',
        'parameters': [
            {
                'name': 'faculty',
                'description': 'faculty',
                'in': 'path',
                'type': 'string',
            },
            {
                'name': 'fieldofstudyname',
                'description': 'fieldofstudyname',
                'in': 'path',
                'type': 'string',
            },

        ],
        'responses': {
            '200': {
                'description': 'A list of start years',
                'schema': {
                    'type': 'array',
                    'items': StartYearsModelResponse,
                }
            },
            '401': {
                'description': 'no such faculty',
            },
            '402': {
                'description': 'no such field of study',
            },
        }})
    def get(self, faculty, fieldofstudyname):
        connector = Neo4jConnector()
        years = connector.get_all_start_years_for_particular_fieldofstudy(faculty, fieldofstudyname)
        return [serialize_startyears(year) for year in years], 200

class FieldOfStudyModelPost(Schema):
    type = 'object'
    properties = {
        'token': {
            'type': 'string',
        },
        'fieldofstudy': {
            'type': 'object',
            'schema':{
                'faculty': {
                    'type':'string'
                },
                'fieldofstudyname':{
                    'type': 'string'
                },
                'on_semester':{
                    'type': 'string'
                },
                'startyears': {
                    'type': 'string'
                }
            }
        }
    }

class FullFieldofstudyModelResponse(Schema):
    type = 'object'
    properties = {
            'schema':{
                'faculty': {
                    'type':'string'
                },
                'fieldofstudyname':{
                    'type': 'string'
                },
                'on_semester':{
                    'type': 'string'
                },
                'start_years': {
                    'type': 'string'
                }
            }
        }

def serialize_full_fields_of_study(faculty, name, years, semester):
    return {
            'faculty': faculty,
            'fieldofstudyname':name,
            'on_semester': semester,
            'start_years': years
            }


class ConnectFieldOfStudy(Resource):
    @swagger.doc({
        'tags': ['fieldofstudy'],
        'summary': 'Add field of study for particular user',
        'description': 'Add field of study for particular user',
        'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': FieldOfStudyModelPost
        }
        ],
        'responses': {
            '200': {
                'description': 'A list of fields of study for particular user',
                'schema': {
                    'type': 'array',
                    'items': FullFieldofstudyModelResponse,
                }
            },
            '401': {
                'description': 'no such user',
            },
            '402': {
                'description': 'no such field of study',
            },
        }})
    def post(self):
        data = request.get_json()
        fos = data.get('fieldofstudy')
        token = data.get('token')
        print(token, fos.get('on_semester'))
        connector = Neo4jConnector()
        user = connector.get_student_by_token(token)
        if user is None:
            return {'token': 'user does not exist'}, 400
        print(fos.get('fieldofstudyname'), fos.get('startyears'), fos.get('faculty'))
        fieldofstudy = connector.get_field_of_study(fos.get('fieldofstudyname'), fos.get('startyears'), fos.get('faculty'))
        if fieldofstudy is None:
            return {'fieldofstudy': 'no such field of study'}, 401
        result2 = connector.get_all_fields_of_study_for_student(user)
        if result2 is None:
            result = connector.connect_student_studies_field_of_study(user, fieldofstudy, fos.get('on_semester'))
        elif fieldofstudy in result2:
            return [serialize_full_fields_of_study(field.faculty, field.name, field.start_years, connector.get_student_on_semester_for_fieldofstudy(user, field)) for field in result2], 200
        result2 = connector.get_all_fields_of_study_for_student(user)
        if result2 is None:
            return [],200
        return [serialize_full_fields_of_study(field.faculty, field.name, field.start_years, connector.get_student_on_semester_for_fieldofstudy(user, field)) for field in result2], 200

class DisconnectFieldOfStudy(Resource):
    @swagger.doc({
        'tags': ['fieldofstudy'],
        'summary': 'Disconnect field of study for particular user',
        'description': 'Disconnect field of study for particular user',
        'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': FieldOfStudyModelPost
        }
        ],
        'responses': {
            '200': {
                'description': 'A list of fields of study for particular user',
                'schema': {
                    'type': 'array',
                    'items': FullFieldofstudyModelResponse,
                }
            },
            '401': {
                'description': 'no such user',
            },
            '402': {
                'description': 'no such field of study',
            },
        }})
    def post(self):
        data = request.get_json()
        print(data)
        fos = data.get('fieldofstudy')
        token = data.get('token')
        print(token, fos.get('on_semester'))
        connector = Neo4jConnector()
        user = connector.get_student_by_token(token)
        if user is None:
            return {'token': 'user does not exist'}, 400
        print(fos.get('fieldofstudy'), fos.get('startyears'), fos.get('faculty'))
        fieldofstudy = connector.get_field_of_study(fos.get('fieldofstudyname'), fos.get('startyears'), fos.get('faculty'))
        if fieldofstudy is None:
            return {'fieldofstudy': 'no such field of study'}, 401
        result = connector.disconnect_student_studies_field_of_study(user, fieldofstudy)
        result2 = connector.get_all_fields_of_study_for_student(user)
        if result2 is None:
            return [],200
        return [serialize_full_fields_of_study(field.faculty, field.name, field.start_years, connector.get_student_on_semester_for_fieldofstudy(user, field)) for field in result2], 200

class GetMyFieldofStudyNames(Resource):
    @swagger.doc({
        'tags': ['fieldofstudy'],
        'summary': 'Get studied fields of study for particular user',
        'description': 'Get studied fields of study for particular user',
        'parameters': [
        {
            'name': 'token',
            'description': 'token',
            'in': 'path',
            'type': 'string',
        }
    ],
        'responses': {
            '200': {
                'description': 'A list of fields of study for particular user',
                'schema': {
                    'type': 'array',
                    'items': FullFieldofstudyModelResponse,
                }
            },
            '401': {
                'description': 'no such user',
            },
            '402': {
                'description': 'no such field of study',
            },
        }})
    def get(self, token):
        connector = Neo4jConnector()
        user = connector.get_student_by_token(token)
        if user is None:
            return {'token': 'user does not exist'}, 400
        result2 = connector.get_all_fields_of_study_for_student(user)
        if result2 is None:
            return [], 200
        return [serialize_full_fields_of_study(field.faculty, field.name, field.start_years, connector.get_student_on_semester_for_fieldofstudy(user, field)) for
                field in result2], 200


def serialize_full_user(user):
    return {
        'index_number': user.index_number,
        'name': user.name,
        'email': user.email,
    }


class GetUserMe(Resource):
    @swagger.doc({
        'tags': ['users'],
        'summary': 'Get your user',
        'description': 'Get your user',
        'parameters': [
        {
            'name': 'token',
            'description': 'token',
            'in': 'path',
            'type': 'string',
        }],
        'responses': {
            '200': {
                'description': 'the user',
                'schema': UserModel,
            },
            '401': {
                'description': 'invalid / missing authentication',
            },
        }
    })

    def get(self, token):
        connector = Neo4jConnector()
        user = connector.get_student_by_token(token)
        if user is None:
            return {'token': 'user does not exist'}, 400

        return serialize_full_user(user)

class CourseResponse(Schema):
    type = 'object'
    properties = {
            'schema':{
                'name': {
                    'type':'string'
                },
                'rating':{
                    'type': 'string'
                },
            }
        }

def serialize_course(name, rating):
    return {
            'name': name,
            'rating': rating,
            }

class CoursesModelPost(Schema):
    type = 'object'
    properties = {
        'compulsory': {
            'type': 'array',
            'items': CourseResponse
        },
        'elective': {
            'type': 'array',
            'items': CourseResponse
        },
    }

class GetMyCourses(Resource):
    @swagger.doc({
        'tags': ['courses'],
        'summary': 'Get your courses',
        'description': 'Get your courses',
        'parameters': [
        {
            'name': 'token',
            'description': 'token',
            'in': 'path',
            'type': 'string',
        },
            {
                'name': 'faculty',
                'description': 'faculty',
                'in': 'path',
                'type': 'string',
            },
            {
                'name': 'fieldofstudy',
                'description': 'fieldofstudy',
                'in': 'path',
                'type': 'string',
            },
            {
                'name': 'startyears',
                'description': 'startyears',
                'in': 'path',
                'type': 'string',
            }
        ],
        'responses': {
            '200': {
                'description': 'array of courses and ratings',
                'schema': {
                    'type': 'object',
                    'items': CoursesModelPost,
                }
            },
            '400': {
                'description': 'no such user',
            },
            '401': {
                'description': 'field of study does not exist',
            },
        }
    })

    def get(self, token, faculty, fieldofstudy, startyears):
        fieldofstudyname = fieldofstudy
        connector = Neo4jConnector()
        user = connector.get_student_by_token(token)
        if user is None:
            return {'token': 'user does not exist'}, 400
        fieldofstudy = connector.get_field_of_study(fieldofstudyname, startyears, faculty)
        if fieldofstudy is None:
            return {'fieldofstudy': 'no such field of study'}, 401
        courses = connector.get_all_courses_on_given_fieldofstudy(user, faculty,fieldofstudyname, startyears)
        compulsory = []
        electives = []
        for course in courses:
            if connector.is_course_elective(course, faculty, startyears, fieldofstudyname):
                electives.append(serialize_course(course.name, connector.get_student_rating_course(user, course, faculty, startyears, fieldofstudyname)))
            else:
                compulsory.append(serialize_course(course.name, connector.get_student_rating_course(user, course, faculty, startyears, fieldofstudyname)))
        return {'compulsory': compulsory, 'elective': electives},200

class UpdateMyCourses(Resource):
    @swagger.doc({
        'tags': ['courses'],
        'summary': 'Update your courses',
        'description': 'Update your courses',
        'parameters': [
        {
            'name': 'body',
                'in': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'compulsory': {
                            'type': 'array',
                            'items': CourseResponse
                            },
                        'elective': {
                            'type': 'array',
                            'items': CourseResponse
                        },
                        'faculty': {
                            'type': 'string'
                        },
                        'fieldofstudy': {
                            'type': 'string'
                        },
                        'onsemester': {
                            'type': 'string'
                        },
                        'token': {
                            'type': 'string'
                        },
                        'startyears':{
                            'type': 'string'
                        }
                    }
                }
        }],
        'responses': {
            '200': {
                'description': 'array of courses and ratings',
                'schema': {
                    'type': 'object',
                    'items': CoursesModelPost,
                }
            },
            '400': {
                'description': 'no such user',
            },
            '401': {
                'description': 'field of study does not exist',
            },
        }
    })

    def post(self):
        data = request.get_json()
        compulsory = data.get('compulsory')
        connector = Neo4jConnector()
        token = data.get('token')
        fieldofstudyname = data.get('fieldofstudy')
        onsemester = data.get('onsemester')
        faculty = data.get('faculty')
        startyears = data.get('startyears')
        elective = data.get('elective')
        user = connector.get_student_by_token(token)

        if user is None:
            return {'token': 'user does not exist'}, 400
        for course in compulsory:
            print(course.get('name'))
            fos = connector.get_field_of_study(fieldofstudyname, startyears, faculty)
            print(fos)
            c = connector.get_course_by_field_of_study(course.get('name'), fos)
            rating = connector.get_student_rating_course(user, c, faculty, startyears, fieldofstudyname)
            if int(rating)==0:
                connector.connect_student_evaluates_course(user, c, course.get('rating'))
        for course in elective:
            fos = connector.get_field_of_study(fieldofstudyname, startyears, faculty)
            c = connector.get_course_by_field_of_study(course.get('name'), fos)
            rating = connector.get_student_rating_course(user, c, faculty, startyears, fieldofstudyname)
            if int(rating)==0:
                connector.connect_student_evaluates_course(user, c, course.get('rating'))
        courses = connector.get_all_courses_on_given_fieldofstudy(user, faculty, fieldofstudyname, startyears)
        compulsory = []
        electives = []
        for course in courses:
            if connector.is_course_elective(course, faculty, startyears, fieldofstudyname):
                electives.append(serialize_course(course.name,
                                                  connector.get_student_rating_course(user, course, faculty, startyears,
                                                                                      fieldofstudyname)))
            else:
                compulsory.append(serialize_course(course.name,
                                                   connector.get_student_rating_course(user, course, faculty,
                                                                                       startyears, fieldofstudyname)))
        return {'compulsory': compulsory, 'elective': electives}, 200



api.add_resource(ApiDocs, '/docs', '/docs/<path:path>')
api.add_resource(Register, '/api/v0/register')
api.add_resource(Login,'/api/v0/login')
api.add_resource(GetUserMe, '/api/v0/user/get/me/<string:token>')

api.add_resource(AddKeywords, '/api/v0/keywords/add')
api.add_resource(GetKeywords, '/api/v0/keywords/get/me/<string:token>')
api.add_resource(DeleteKeywords, '/api/v0/keywords/delete/<string:token>/<string:word>')

api.add_resource(GetFieldofStudyNames, '/api/v0/fieldofstudy/get/<string:faculty>/fieldofstudynames')
api.add_resource(GetFaculty, '/api/v0/fieldofstudy/get/faculty')
api.add_resource(GetStartYears, '/api/v0/fieldofstudy/get/startyears/<string:faculty>/<string:fieldofstudyname>')

api.add_resource(ConnectFieldOfStudy, '/api/v0/fieldofstudy/connect/me')
api.add_resource(DisconnectFieldOfStudy, '/api/v0/fieldofstudy/disconnect/me')

api.add_resource(GetMyFieldofStudyNames, '/api/v0/fieldofstudy/get/me/<string:token>')

api.add_resource(GetMyCourses, '/api/v0/courses/get/me/<string:token>/<string:faculty>/<string:fieldofstudy>/<string:startyears>')
api.add_resource(UpdateMyCourses, '/api/v0/courses/updateratings/me')

# def get_db():
#     if not hasattr(g, 'neo4j_db'):
#         g.neo4j_db = driver.session()
#     return g.neo4j_db
#
#
# @app.teardown_appcontext
# def close_db(error):
#     if hasattr(g, 'neo4j_db'):
#         g.neo4j_db.close()
#
#
# def set_user(sender, **extra):
#     auth_header = request.headers.get('Authorization')
#     if not auth_header:
#         g.user = {'id': None}
#         return
#     match = re.match(r'^Token (\S+)', auth_header)
#     if not match:
#         abort(401, 'invalid authorization format. Follow `Token <token>`')
#         return
#     token = match.group(1)
#
#     def get_user_by_token(tx, token):
#         return tx.run(
#             '''
#             MATCH (user:User {api_key: $api_key}) RETURN user
#             ''', {'api_key': token}
#         ).single()
#
#     db = get_db()
#     result = db.read_transaction(get_user_by_token, token)
#     try:
#         g.user = result['user']
#     except (KeyError, TypeError):
#         abort(401, 'invalid authorization key')
#     return
# request_started.connect(set_user, app)
#
#
# def login_required(f):
#     @wraps(f)
#     def wrapped(*args, **kwargs):
#         auth_header = request.headers.get('Authorization')
#         if not auth_header:
#             return {'message': 'no authorization provided'}, 401
#         return f(*args, **kwargs)
#     return wrapped
#
#
#
# def serialize_genre(genre):
#     return {
#         'id': genre['id'],
#         'name': genre['name'],
#     }
#
#
# def serialize_movie(movie, my_rating=None):
#     return {
#         'id': movie['tmdbId'],
#         'title': movie['title'],
#         'summary': movie['plot'],
#         'released': movie['released'],
#         'duration': movie['runtime'],
#         'rated': movie['imdbRating'],
#         'tagline': movie['plot'],
#         'poster_image': movie['poster'],
#         'my_rating': my_rating,
#     }
#
#
# def serialize_person(person):
#     return {
#         'id': person['tmdbId'],
#         'name': person['name'],
#         'poster_image': person['poster'],
#     }
#
#
# def serialize_user(user):
#     return {
#         'id': user['id'],
#         'username': user['username'],
#         'avatar': {
#             'full_size': 'https://www.gravatar.com/avatar/{}?d=retro'.format(hash_avatar(user['username']))
#         }
#     }
#
#
# def hash_password(username, password):
#     if sys.version[0] == 2:
#         s = '{}:{}'.format(username, password)
#     else:
#         s = '{}:{}'.format(username, password).encode('utf-8')
#     return hashlib.sha256(s).hexdigest()
#
#
# def hash_avatar(username):
#     if sys.version[0] == 2:
#         s = username
#     else:
#         s = username.encode('utf-8')
#     return hashlib.md5(s).hexdigest()
#
#
#
# class GenreModel(Schema):
#     type = 'object'
#     properties = {
#         'id': {
#             'type': 'integer',
#         },
#         'name': {
#             'type': 'string',
#         }
#     }
#
#
# class MovieModel(Schema):
#     type = 'object'
#     properties = {
#         'id': {
#             'type': 'string',
#         },
#         'title': {
#             'type': 'string',
#         },
#         'summary': {
#             'type': 'string',
#         },
#         'released': {
#             'type': 'string',
#         },
#         'duration': {
#             'type': 'integer',
#         },
#         'rated': {
#             'type': 'string',
#         },
#         'tagline': {
#             'type': 'string',
#         },
#         'poster_image': {
#             'type': 'string',
#         },
#         'my_rating': {
#             'type': 'integer',
#         }
#     }
#
#
# class PersonModel(Schema):
#     type = 'object'
#     properties = {
#         'id': {
#             'type': 'integer',
#         },
#         'name': {
#             'type': 'string',
#         },
#         'poster_image': {
#             'type': 'string',
#         }
#     }
#
#
# class UserModel(Schema):
#     type = 'object'
#     properties = {
#         'id': {
#             'type': 'string',
#         },
#         'username': {
#             'type': 'string',
#         },
#         'avatar': {
#             'type': 'object',
#         }
#     }
#
#
#
# class GenreList(Resource):
#     @swagger.doc({
#         'tags': ['genres'],
#         'summary': 'Find all genres',
#         'description': 'Returns all genres',
#         'responses': {
#             '200': {
#                 'description': 'A list of genres',
#                 'schema': GenreModel,
#             }
#         }
#     })
#     def get(self):
#         def get_genres(tx):
#             return list(tx.run('MATCH (genre:Genre) SET genre.id=id(genre) RETURN genre'))
#         db = get_db()
#         result = db.write_transaction(get_genres)
#         return [serialize_genre(record['genre']) for record in result]
#
#
# class Movie(Resource):
#     @swagger.doc({
#         'tags': ['movies'],
#         'summary': 'Find movie by ID',
#         'description': 'Returns a movie',
#         'parameters': [
#             {
#                 'name': 'Authorization',
#                 'in': 'header',
#                 'type': 'string',
#                 'default': 'Token <token goes here>',
#                 'required': False
#             },
#             {
#                 'name': 'id',
#                 'description': 'movie tmdbId, a string',
#                 'in': 'path',
#                 'type': 'string',
#                 'required': True,
#             }
#         ],
#         'responses': {
#             '200': {
#                 'description': 'A movie',
#                 'schema': MovieModel,
#             },
#             '404': {
#                 'description': 'movie not found'
#             },
#         }
#     })
#     def get(self,id):
#         def get_movie(tx, user_id, id):
#             return list(tx.run(
#                 '''
#                 MATCH (movie:Movie {tmdbId: $id})
#                 OPTIONAL MATCH (movie)<-[my_rated:RATED]-(me:User {id: $user_id})
#                 OPTIONAL MATCH (movie)<-[r:ACTED_IN]-(a:Person)
#                 OPTIONAL MATCH (related:Movie)<--(a:Person) WHERE related <> movie
#                 OPTIONAL MATCH (movie)-[:IN_GENRE]->(genre:Genre)
#                 OPTIONAL MATCH (movie)<-[:DIRECTED]-(d:Person)
#                 OPTIONAL MATCH (movie)<-[:PRODUCED]-(p:Person)
#                 OPTIONAL MATCH (movie)<-[:WRITER_OF]-(w:Person)
#                 WITH DISTINCT movie,
#                 my_rated,
#                 genre, d, p, w, a, r, related, count(related) AS countRelated
#                 ORDER BY countRelated DESC
#                 RETURN DISTINCT movie,
#                 my_rated.rating AS my_rating,
#                 collect(DISTINCT d) AS directors,
#                 collect(DISTINCT p) AS producers,
#                 collect(DISTINCT w) AS writers,
#                 collect(DISTINCT{ name:a.name, id:a.tmdbId, poster_image:a.poster, role:r.role}) AS actors,
#                 collect(DISTINCT related) AS related,
#                 collect(DISTINCT genre) AS genres
#                 ''', {'user_id': user_id , 'id': id}
#             ))
#         db = get_db()
#
#         result = db.read_transaction(get_movie, g.user['id'], id)
#         for record in result:
#             return {
#                 'id': record['movie']['tmdbId'],
#                 'title': record['movie']['title'],
#                 'summary': record['movie']['plot'],
#                 'released': record['movie']['released'],
#                 'duration': record['movie']['runtime'],
#                 'rated': record['movie']['rated'],
#                 'tagline': record['movie']['plot'],
#                 'poster_image': record['movie']['poster'],
#                 'my_rating': record['my_rating'],
#                 'genres': [serialize_genre(genre) for genre in record['genres']],
#                 'directors': [serialize_person(director)for director in record['directors']],
#                 'producers': [serialize_person(producer) for producer in record['producers']],
#                 'writers': [serialize_person(writer) for writer in record['writers']],
#                 'actors': [
#                     {
#                         'id': actor['id'],
#                         'name': actor['name'],
#                         'role': actor['role'],
#                         'poster_image': actor['poster_image'],
#                     } for actor in record['actors']
#                 ],
#                 'related': [serialize_movie(related) for related in record['related']],
#             }
#         return {'message': 'movie not found'}, 404
#
#
# class MovieList(Resource):
#     @swagger.doc({
#         'tags': ['movies'],
#         'summary': 'Find all movies',
#         'description': 'Returns a list of movies',
#         'responses': {
#             '200': {
#                 'description': 'A list of movies',
#                 'schema': {
#                     'type': 'array',
#                     'items': MovieModel,
#                 }
#             }
#         }
#     })
#     def get(self):
#         def get_movies(tx):
#             return list(tx.run(
#                 '''
#                 MATCH (movie:Movie) RETURN movie
#                 '''
#             ))
#         db = get_db()
#         result = db.read_transaction(get_movies)
#         return [serialize_movie(record['movie']) for record in result]
#
#
# class MovieListByGenre(Resource):
#     @swagger.doc({
#         'tags': ['movies'],
#         'summary': 'Find movie by genre id',
#         'description': 'Returns a list of movies by genre',
#         'parameters': [
#             {
#                 'name': 'genre_id',
#                 'description': 'The name of the genre.',
#                 'in': 'path',
#                 'type': 'string',
#                 'required': 'true'
#             }
#         ],
#         'responses': {
#             '200': {
#                 'description': 'A list of movies with the specified genre',
#                 'schema': {
#                     'type': 'array',
#                     'items': MovieModel,
#                 }
#             }
#         }
#     })
#     def get(self, genre_id):
#         def get_movies_by_genre(tx, genre_id):
#             return list(tx.run(
#                 '''
#                 MATCH (movie:Movie)-[:IN_GENRE]->(genre:Genre)
#                 WHERE toLower(genre.name) = toLower($genre_id)
#                     // while transitioning to the sandbox data
#                     OR id(genre) = toInteger($genre_id)
#                 RETURN movie
#                 ''', {'genre_id': genre_id}
#             ))
#         db = get_db()
#         result = db.read_transaction(get_movies_by_genre, genre_id)
#         return [serialize_movie(record['movie']) for record in result]
#
# # Not sure this is useful anymore
# class MovieListByDateRange(Resource):
#     @swagger.doc({
#         'tags': ['movies'],
#         'summary': 'Find movie by year range',
#         'description': 'Returns a list of movies released between a range of years',
#         'parameters': [
#             {
#                 'name': 'start',
#                 'description': 'start year',
#                 'in': 'path',
#                 'type': 'integer',
#                 'required': 'true'
#             },
#             {
#                 'name': 'end',
#                 'description': 'end year',
#                 'in': 'path',
#                 'type': 'integer',
#                 'required': 'true'
#             }
#         ],
#         'responses': {
#             '200': {
#                 'description': 'A list of movies released between the specified years',
#                 'schema': {
#                     'type': 'array',
#                     'items': MovieModel,
#                 }
#             }
#         }
#     })
#     def get(self, start, end):
#         try:
#             params = {'start': start, 'end': end}
#         except ValueError:
#             return {'description': 'invalid year format'}, 400
#
#         def get_movies_list_by_date_range(tx, params):
#             return list(tx.run(
#                 '''
#                 MATCH (movie:Movie)
#                 WHERE movie.year > $start AND movie.year < $end
#                 RETURN movie
#                 ''', params
#             ))
#
#         db = get_db()
#         result = db.read_transaction(get_movies_list_by_date_range, params)
#         return [serialize_movie(record['movie']) for record in result]
#
#
# class MovieListByPersonActedIn(Resource):
#     @swagger.doc({
#         'tags': ['movies'],
#         'summary': 'Find movies by actor',
#         'description': 'Returns a list of movies that a person has acted in.',
#         'parameters': [
#             {
#                 'name': 'person_id',
#                 'description': 'person id',
#                 'in': 'path',
#                 'type': 'string',
#                 'required': 'true'
#             },
#         ],
#         'responses': {
#             '200': {
#                 'description': 'A list of movies the specified person has acted in',
#                 'schema': {
#                     'type': 'array',
#                     'items': MovieModel,
#                 }
#             }
#         }
#     })
#     def get(self, person_id):
#         def get_movies_by_acted_in(tx, person_id):
#             return list(tx.run(
#                 '''
#                 MATCH (actor:Actor {tmdbId: $person_id})-[:ACTED_IN]->(movie:Movie)
#                 RETURN DISTINCT movie
#                 ''', {'person_id': person_id}
#             ))
#         db = get_db()
#         result = db.read_transaction(get_movies_by_acted_in, person_id)
#         return [serialize_movie(record['movie']) for record in result]
#
#
# class MovieListByWrittenBy(Resource):
#     @swagger.doc({
#         'tags': ['movies'],
#         'summary': 'Find movies by writer',
#         'description': 'Returns a list of movies writen by a person',
#         'parameters': [
#             {
#                 'name': 'person_id',
#                 'description': 'person id',
#                 'in': 'path',
#                 'type': 'string',
#                 'required': 'true'
#             },
#         ],
#         'responses': {
#             '200': {
#                 'description': 'A list of movies the specified person has written',
#                 'schema': {
#                     'type': 'array',
#                     'items': MovieModel,
#                 }
#             }
#         }
#     })
#     def get(self, person_id):
#         def get_movies_list_written_by(tx, person_id):
#             return list(tx.run(
#                 '''
#                 MATCH (actor:Writer {tmdbId: $person_id})-[:WRITER_OF]->(movie:Movie)
#                 RETURN DISTINCT movie
#                 ''', {'person_id': person_id}
#             ))
#         db = get_db()
#         result = db.read_transaction(get_movies_list_written_by, person_id)
#         return [serialize_movie(record['movie']) for record in result]
#
#
# class MovieListByDirectedBy(Resource):
#     @swagger.doc({
#         'tags': ['movies'],
#         'summary': 'Find movies by director',
#         'description': 'Returns a list of movies directed by a person',
#         'parameters': [
#             {
#                 'name': 'person_id',
#                 'description': 'person id',
#                 'in': 'path',
#                 'type': 'string',
#                 'required': 'true'
#             },
#         ],
#         'responses': {
#             '200': {
#                 'description': 'A list of movies the specified person has directed',
#                 'schema': {
#                     'type': 'array',
#                     'items': MovieModel,
#                 }
#             }
#         }
#     })
#     def get(self, person_id):
#         def get_mmovies_list_directed_by(tx, person_id):
#             return list(tx.run(
#                 '''
#                 MATCH (actor:Director {tmdbId: $person_id})-[:DIRECTED]->(movie:Movie)
#                 RETURN DISTINCT movie
#                 ''', {'person_id': person_id}
#             ))
#         db = get_db()
#         result = db.read_transaction(get_mmovies_list_directed_by, person_id)
#         return [serialize_movie(record['movie']) for record in result]
#
#
# class MovieListRatedByMe(Resource):
#     @swagger.doc({
#         'tags': ['movies'],
#         'summary': 'A list of movies the authorized user has rated.',
#         'description': 'A list of movies the authorized user has rated.',
#         'parameters': [
#             {
#                 'name': 'Authorization',
#                 'in': 'header',
#                 'type': 'string',
#                 'default': 'Token <token goes here>',
#                 'required': True
#             },
#         ],
#         'responses': {
#             '200': {
#                 'description': 'A list of movies the authorized user has rated',
#                 'schema': {
#                     'type': 'array',
#                     'items': MovieModel,
#                 }
#             }
#         }
#     })
#     @login_required
#     def get(self):
#         def get_movies_rated_by_me(tx, user_id):
#             return list(tx.run(
#                 '''
#                 MATCH (:User {id: $user_id})-[rated:RATED]->(movie:Movie)
#                 RETURN DISTINCT movie, rated.rating as my_rating
#                 ''', {'user_id': user_id}
#             ))
#         db = get_db()
#         result = db.read_transaction(get_movies_rated_by_me, g.user['id'])
#         return [serialize_movie(record['movie'], record['my_rating']) for record in result]
#
#
# class MovieListRecommended(Resource):
#     @swagger.doc({
#         'tags': ['movies'],
#         'summary': 'A list of recommended movies for the authorized user.',
#         'description': 'A list of recommended movies for the authorized user.',
#         'parameters': [
#             {
#                 'name': 'Authorization',
#                 'in': 'header',
#                 'type': 'string',
#                 'default': 'Token <token goes here>',
#                 'required': True
#             },
#         ],
#         'responses': {
#             '200': {
#                 'description': 'A list of recommended movies for the authorized user',
#                 'schema': {
#                     'type': 'array',
#                     'items': MovieModel,
#                 }
#             }
#         }
#     })
#     @login_required
#     def get(self):
#         def get_movies_list_recommended(tx, user_id):
#             return list(tx.run(
#                 '''
#                 MATCH (me:User {id: $user_id})-[my:RATED]->(m:Movie)
#                 MATCH (other:User)-[their:RATED]->(m)
#                 WHERE me <> other
#                 AND abs(my.rating - their.rating) < 2
#                 WITH other,m
#                 MATCH (other)-[otherRating:RATED]->(movie:Movie)
#                 WHERE movie <> m
#                 WITH avg(otherRating.rating) AS avgRating, movie
#                 RETURN movie
#                 ORDER BY avgRating desc
#                 LIMIT 25
#                 ''', {'user_id': user_id}
#             ))
#         db = get_db()
#         result = db.read_transaction(get_movies_list_recommended, g.user['id'])
#         return [serialize_movie(record['movie']) for record in result]
#
# class Person(Resource):
#     @swagger.doc({
#         'tags': ['people'],
#         'summary': 'Find person by id',
#         'description': 'Returns a person',
#         'parameters': [
#             {
#                 'name': 'id',
#                 'description': 'person id',
#                 'in': 'path',
#                 'type': 'integer',
#                 'required': True
#             }
#         ],
#         'responses': {
#             '200': {
#                 'description': 'A person',
#                 'schema': PersonModel,
#             },
#             '404': {
#                 'description': 'person not found'
#             },
#         }
#     })
#     def get(self, id):
#         def get_person_by_id(tx, user_id):
#             return list(tx.run(
#                 '''
#                 MATCH (person:Person {tmdbId: $id})
#                 OPTIONAL MATCH (person)-[:DIRECTED]->(d:Movie)
#                 OPTIONAL MATCH (person)<-[:PRODUCED]->(p:Movie)
#                 OPTIONAL MATCH (person)<-[:WRITER_OF]->(w:Movie)
#                 OPTIONAL MATCH (person)<-[r:ACTED_IN]->(a:Movie)
#                 OPTIONAL MATCH (person)-->(movies)<-[relatedRole:ACTED_IN]-(relatedPerson)
#                 RETURN DISTINCT person,
#                 collect(DISTINCT { name:d.title, id:d.tmdbId, poster_image:d.poster}) AS directed,
#                 collect(DISTINCT { name:p.title, id:p.tmdbId, poster_image:p.poster}) AS produced,
#                 collect(DISTINCT { name:w.title, id:w.tmdbId, poster_image:w.poster}) AS wrote,
#                 collect(DISTINCT{ name:a.title, id:a.tmdbId, poster_image:a.poster, role:r.role}) AS actedIn,
#                 collect(DISTINCT{ name:relatedPerson.name, id:relatedPerson.tmdbId, poster_image:relatedPerson.poster, role:relatedRole.role}) AS related
#                 ''', {'id': user_id}
#             ))
#         db = get_db()
#         results = db.read_transaction(get_person_by_id, id)
#         for record in results:
#             return {
#                 'id': record['person']['id'],
#                 'name': record['person']['name'],
#                 'poster_image': record['person']['poster'],
#                 'directed': [
#                     {
#                         'id': movie['id'],
#                         'name': movie['name'],
#                         'poster_image': movie['poster_image'],
#                     } for movie in record['directed']
#                 ],
#                 'produced': [
#                     {
#                         'id': movie['id'],
#                         'name': movie['name'],
#                         'poster_image': movie['poster_image'],
#                     } for movie in record['produced']
#                 ],
#                 'wrote': [
#                     {
#                         'id': movie['id'],
#                         'name': movie['name'],
#                         'poster_image': movie['poster_image'],
#                     } for movie in record['wrote']
#                 ],
#                 'actedIn': [
#                     {
#                         'id': movie['id'],
#                         'name': movie['name'],
#                         'poster_image': movie['poster_image'],
#                         'role': movie['role'],
#                     } for movie in record['actedIn']
#                 ],
#                 'related': [
#                     {
#                         'id': person['id'],
#                         'name': person['name'],
#                         'poster_image': person['poster_image'],
#                         'role': person['role'],
#                     } for person in record['related']
#                 ],
#             }
#         return {'message': 'person not found'}, 404
#
#
# class PersonList(Resource):
#     @swagger.doc({
#         'tags': ['people'],
#         'summary': 'Find all people',
#         'description': 'Returns a list of people',
#         'responses': {
#             '200': {
#                 'description': 'A list of people',
#                 'schema': {
#                     'type': 'array',
#                     'items': PersonModel,
#                 }
#             }
#         }
#     })
#     def get(self):
#         def get_persons_list(tx):
#             return list(tx.run(
#                 '''
#                 MATCH (person:Person) RETURN person
#                 '''
#             ))
#         db = get_db()
#         results = db.read_transaction(get_persons_list)
#         return [serialize_person(record['person']) for record in results]
#
#
# class PersonBacon(Resource):
#     @swagger.doc({
#         'tags': ['people'],
#         'summary': 'Find all Bacon paths',
#         'description': 'Returns all bacon paths from person 1 to person 2',
#         'parameters': [
#             {
#                 'name': 'name1',
#                 'description': 'Name of the origin user',
#                 'in': 'query',
#                 'type': 'string',
#                 'required': True,
#             },
#             {
#                 'name': 'name2',
#                 'description': 'Name of the target user',
#                 'in': 'query',
#                 'type': 'string',
#                 'required': True,
#             }
#         ],
#         'responses': {
#             '200': {
#                 'description': 'A list of people',
#                 'schema': {
#                     'type': 'array',
#                     'items': PersonModel,
#                 }
#             }
#         }
#     })
#     def get(self):
#         name1 = request.args['name1']
#         name2 = request.args['name2']
#         def get_bacon(tx, name1, name2):
#             return list(tx.run(
#                 '''
#                 MATCH p = shortestPath( (p1:Person {name: $name1})-[:ACTED_IN*]-(target:Person {name: $name2}) )
#                 WITH [n IN nodes(p) WHERE n:Person | n] as bacon
#                 UNWIND(bacon) AS person
#                 RETURN DISTINCT person
#                 ''', {'name1': name1, 'name2': name2}
#             ))
#         db = get_db()
#         results = db.read_transaction(get_bacon, name1, name2)
#         return [serialize_person(record['person']) for record in results]
#
#
#
#
# class RateMovie(Resource):
#     @swagger.doc({
#         'tags': ['movies'],
#         'summary': 'Rate a movie from',
#         'description': 'Rate a movie from 0-5 inclusive',
#         'parameters': [
#             {
#                 'name': 'Authorization',
#                 'in': 'header',
#                 'type': 'string',
#                 'required': True,
#                 'default': 'Token <token goes here>',
#             },
#             {
#                 'name': 'id',
#                 'description': 'movie tmdbId',
#                 'in': 'path',
#                 'type': 'string',
#             },
#             {
#                 'name': 'body',
#                 'in': 'body',
#                 'schema': {
#                     'type': 'object',
#                     'properties': {
#                         'rating': {
#                             'type': 'integer',
#                         },
#                     }
#                 }
#             },
#         ],
#         'responses': {
#             '200': {
#                 'description': 'movie rating saved'
#             },
#             '401': {
#                 'description': 'invalid / missing authentication'
#             }
#         }
#     })
#     @login_required
#     def post(self, id):
#         parser = reqparse.RequestParser()
#         parser.add_argument('rating', choices=list(range(0, 6)), type=int, required=True, help='A rating from 0 - 5 inclusive (integers)')
#         args = parser.parse_args()
#         rating = args['rating']
#
#         def rate_movie(tx, user_id, movie_id, rating):
#             return tx.run(
#                 '''
#                 MATCH (u:User {id: $user_id}),(m:Movie {tmdbId: $movie_id})
#                 MERGE (u)-[r:RATED]->(m)
#                 SET r.rating = $rating
#                 RETURN m
#                 ''', {'user_id': user_id, 'movie_id': movie_id, 'rating': rating}
#             )
#
#         db = get_db()
#         results = db.write_transaction(rate_movie, g.user['id'], id, rating)
#         return {}
#
#     @swagger.doc({
#         'tags': ['movies'],
#         'summary': 'Delete your rating for a movie',
#         'description': 'Delete your rating for a movie',
#         'parameters': [
#             {
#                 'name': 'Authorization',
#                 'in': 'header',
#                 'type': 'string',
#                 'required': True,
#                 'default': 'Token <token goes here>',
#             },
#             {
#                 'name': 'id',
#                 'description': 'movie tmdbId',
#                 'in': 'path',
#                 'type': 'string',
#             },
#         ],
#         'responses': {
#             '204': {
#                 'description': 'movie rating deleted'
#             },
#             '401': {
#                 'description': 'invalid / missing authentication'
#             }
#         }
#     })
#     @login_required
#     def delete(self, id):
#         def delete_rating(tx, user_id, movie_id):
#             return tx.run(
#                 '''
#                 MATCH (u:User {id: $user_id})-[r:RATED]->(m:Movie {tmdbId: $movie_id}) DELETE r
#                 ''', {'movie_id': movie_id, 'user_id': user_id}
#             )
#         db = get_db()
#         db.write_transaction(delete_rating, g.user['id'], id)
#         return {}, 204
#
#
# api.add_resource(ApiDocs, '/docs', '/docs/<path:path>')
# # api.add_resource(GenreList, '/api/v0/genres')
# # api.add_resource(Movie, '/api/v0/movies/<string:id>')
# # api.add_resource(RateMovie, '/api/v0/movies/<string:id>/rate')
# # api.add_resource(MovieList, '/api/v0/movies')
# # api.add_resource(MovieListByGenre, '/api/v0/movies/genre/<string:genre_id>/')
# # api.add_resource(MovieListByDateRange, '/api/v0/movies/daterange/<int:start>/<int:end>')
# # api.add_resource(MovieListByPersonActedIn, '/api/v0/movies/acted_in_by/<string:person_id>')
# # api.add_resource(MovieListByWrittenBy, '/api/v0/movies/written_by/<string:person_id>')
# # api.add_resource(MovieListByDirectedBy, '/api/v0/movies/directed_by/<string:person_id>')
# # api.add_resource(MovieListRatedByMe, '/api/v0/movies/rated')
# # api.add_resource(MovieListRecommended, '/api/v0/movies/recommended')
# # api.add_resource(Person, '/api/v0/people/<string:id>')
# # api.add_resource(PersonList, '/api/v0/people')
# # api.add_resource(PersonBacon, '/api/v0/people/bacon')
# api.add_resource(Register, '/api/v0/register')
# api.add_resource(Login, '/api/v0/login')
# api.add_resource(UserMe, '/api/v0/users/me')
