from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipTo, RelationshipFrom


class Professor(StructuredNode):
    name = StringProperty(required=True)

    course_taught = RelationshipTo('.Course.Course', 'TEACHES')

    student = RelationshipFrom('.Student.Student', 'RATES')
