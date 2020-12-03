from neomodel import StructuredNode, StringProperty, UniqueIdProperty, IntegerProperty, RelationshipTo

from .YearRelationship import YearRelationship
from .ValuedRelationship import ValuedRelationship


class Student(StructuredNode):
    index_number = IntegerProperty(required=True)
    name = StringProperty(required=True)
    email = StringProperty(required=False)
    password = StringProperty(required=False)
    api_key = StringProperty(required=False)


    professor = RelationshipTo('.Professor.Professor', 'RATES', model=ValuedRelationship)
    course_marks = RelationshipTo('.Course.Course', 'EVALUATES', model=ValuedRelationship)
    keywords = RelationshipTo('.Keyword.Keyword', 'LIKES')
    field_of_study = RelationshipTo('.FieldOfStudy.FieldOfStudy', 'STUDIES', model=YearRelationship)
