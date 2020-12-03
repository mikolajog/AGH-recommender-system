from neomodel import StructuredNode, StringProperty, UniqueIdProperty, IntegerProperty, RelationshipFrom, Relationship

from .ValuedRelationship import ValuedRelationship


class Keyword(StructuredNode):
    word = StringProperty(required=True)

    course = RelationshipFrom('.Course.Course', 'DESCRIBES', model=ValuedRelationship)

    student = RelationshipFrom('.Student.Student', 'LIKES')
    keyword_related = Relationship('.Keyword.Keyword', 'CONNECTED', model=ValuedRelationship)
