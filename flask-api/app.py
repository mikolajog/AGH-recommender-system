import binascii
import hashlib
import os
import sys
from dotenv import load_dotenv, find_dotenv
from functools import wraps

from flask import Flask, request, send_from_directory
from flask_cors import CORS
from flask_restful import Resource
from flask_restful_swagger_2 import Api, swagger, Schema
from flask_json import FlaskJSON, json_response

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
        recom = RecommendationEngine().get_and_connect_keywords_to_courses()
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
        if result2 is None or int(connector.get_student_on_semester_for_fieldofstudy(user, fieldofstudy))!=int(fos.get('on_semester')):
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
            else:
                connector.disconnect_student_evaluates_course(user, c, rating)
                connector.connect_student_evaluates_course(user, c, course.get('rating'))
        for course in elective:
            fos = connector.get_field_of_study(fieldofstudyname, startyears, faculty)
            c = connector.get_course_by_field_of_study(course.get('name'), fos)
            rating = connector.get_student_rating_course(user, c, faculty, startyears, fieldofstudyname)
            if int(rating)==0:
                connector.connect_student_evaluates_course(user, c, course.get('rating'))
            else:
                connector.disconnect_student_evaluates_course(user, c, rating)
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



#############################

class ProfessorResponse(Schema):
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

def serialize_professor(name, rating):
    return {
            'name': name,
            'rating': rating,
            }

class ProfessorModelPost(Schema):
    type = 'object'
    properties = {
        'professors': {
            'type': 'array',
            'items': ProfessorResponse
        }
    }

class GetMyProfessors(Resource):
    @swagger.doc({
        'tags': ['professors'],
        'summary': 'Get your professors',
        'description': 'Get your professors',
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
                'description': 'array of professors and ratings',
                'schema': {
                    'type': 'object',
                    'items': ProfessorModelPost,
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
        professors = connector.get_all_professors_on_given_fieldofstudy(user, faculty,fieldofstudyname, startyears)
        prof = []
        prof_names = []
        for professor in professors:
            if professor.name not in prof_names:
                prof.append(serialize_professor(professor.name, connector.get_student_rating_professor(user, professor)))
                prof_names.append(professor.name)
        return {'professors': prof},200

class UpdateMyProfessors(Resource):
    @swagger.doc({
        'tags': ['professors'],
        'summary': 'Update your professors',
        'description': 'Update your professors',
        'parameters': [
        {
            'name': 'body',
                'in': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'professors': {
                            'type': 'array',
                            'items': ProfessorResponse
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
                    'items': ProfessorModelPost,
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
        professors = data.get('professors')
        connector = Neo4jConnector()
        token = data.get('token')
        fieldofstudyname = data.get('fieldofstudy')
        onsemester = data.get('onsemester')
        faculty = data.get('faculty')
        startyears = data.get('startyears')
        user = connector.get_student_by_token(token)

        if user is None:
            return {'token': 'user does not exist'}, 400
        for professor in professors:
            prof = connector.get_professor(professor.get('name'))
            rating = professor.get('rating')
            if(rating)==0:
                connector.connect_student_rates_professor(user,prof, rating)
            else:
                connector.disconnect_student_rates_professor(user, prof, connector.get_student_rating_professor(user, prof))
                connector.connect_student_rates_professor(user, prof, rating)

        professors = connector.get_all_professors_on_given_fieldofstudy(user, faculty, fieldofstudyname, startyears)
        prof = []
        prof_names = []
        for professor in professors:
            if professor.name not in prof_names:
                prof.append(
                    serialize_professor(professor.name, connector.get_student_rating_professor(user, professor)))
                prof_names.append(professor.name)
        return {'professors': prof}, 200



class GetMyRecommendation(Resource):
    @swagger.doc({
        'tags': ['recommendation'],
        'summary': 'Get your recommendation',
        'description': 'Get your recommendations',
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
            },
            {
                'name': 'onsemester',
                'description': 'onsemester',
                'in': 'path',
                'type': 'string',
            },
            {
                'name': 'mode',
                'description': 'mode',
                'in': 'path',
                'type': 'string',
            }
        ],
        'responses': {
            '200': {
                'description': 'array of professors and ratings',
                'schema': {
                    'type': 'array',
                    'items': CourseResponse,
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

    def get(self, token, faculty, fieldofstudy, startyears, onsemester, mode):
        fieldofstudyname = fieldofstudy
        connector = Neo4jConnector()
        user = connector.get_student_by_token(token)
        if user is None:
            return {'token': 'user does not exist'}, 400
        fieldofstudy = connector.get_field_of_study(fieldofstudyname, startyears, faculty)
        if fieldofstudy is None:
            return {'fieldofstudy': 'no such field of study'}, 401
        engine = RecommendationEngine()
        dict_with_courses = engine.get_recommendation(mode, user, faculty, fieldofstudyname, startyears, onsemester)

        sorted_tuples = sorted(dict_with_courses.items(), key=lambda item: item[1], reverse=True)
        print(sorted_tuples)
        dict_with_courses = {k: v for k, v in sorted_tuples}

        return [serialize_course(key, int(value*100)) for key, value in dict_with_courses.items()],200




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

api.add_resource(GetMyProfessors, '/api/v0/professors/get/me/<string:token>/<string:faculty>/<string:fieldofstudy>/<string:startyears>')
api.add_resource(UpdateMyProfessors, '/api/v0/professors/updateratings/me')

api.add_resource(GetMyRecommendation, '/api/v0/recommendation/get/me/<string:token>/<string:faculty>/<string:fieldofstudy>/<string:startyears>/<string:onsemester>/<string:mode>')
