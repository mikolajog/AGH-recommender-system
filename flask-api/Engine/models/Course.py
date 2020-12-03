from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config, UniqueIdProperty, \
    IntegerProperty, BooleanProperty

from .ValuedRelationship import ValuedRelationship


class Course(StructuredNode):
    name = StringProperty(required=True)
    description = StringProperty(required=True)
    taught_on_semester = IntegerProperty(required=True)
    is_elective = BooleanProperty(default=False)

    student_mark = RelationshipTo('.Student.Student', 'EVALUATES', model=ValuedRelationship)
    professor = RelationshipFrom('.Professor.Professor', 'TEACHES')
    keyword = RelationshipFrom('.Keyword.Keyword', 'DESCRIBES', model=ValuedRelationship)
    field_of_study = RelationshipTo('.FieldOfStudy.FieldOfStudy', 'HAS')
