from neomodel import StructuredNode, StringProperty, UniqueIdProperty, IntegerProperty, RelationshipFrom, Relationship

from .ValuedRelationship import ValuedRelationship
from .YearRelationship import YearRelationship


class FieldOfStudy(StructuredNode):
    name = StringProperty(required=True)
    start_years = StringProperty(required=True)
    faculty = StringProperty(required=True)


    student = RelationshipFrom('.Student.Student', 'STUDIES', model=YearRelationship)
    courses = RelationshipFrom('.Course.Course', 'HAS')
