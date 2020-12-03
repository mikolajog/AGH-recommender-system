from neomodel import StructuredNode, StringProperty, UniqueIdProperty, IntegerProperty, RelationshipTo, StructuredRel, \
    FloatProperty


class ValuedRelationship(StructuredRel):
    rating = FloatProperty()
