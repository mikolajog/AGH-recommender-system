from neomodel import StructuredNode, StringProperty, UniqueIdProperty, IntegerProperty, RelationshipTo, StructuredRel, \
    FloatProperty


class YearRelationship(StructuredRel):
    on_semester = IntegerProperty()
