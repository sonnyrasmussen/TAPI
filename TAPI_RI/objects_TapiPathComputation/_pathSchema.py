from teLink import TeLink
from routingConstraint import RoutingConstraint
from nameAndValue import NameAndValue
from extensionsSpec import ExtensionsSpec
from resource import Resource
from objects_common.keyedArrayType import KeyedArrayType

class _pathSchema(Resource):

    def __init__(self, json_struct=None):
        self._telink=KeyedArrayType(TeLink, 'localId')
        self.uuid=""
        self.resourceSpecification=""
        self._routingConstraint=RoutingConstraint() #import
        self.label=KeyedArrayType(NameAndValue, 'valueName')
        self._extensions=KeyedArrayType(ExtensionsSpec, 'extensionsSpecification')
        self.name=KeyedArrayType(NameAndValue, 'valueName')
        super(_pathSchema, self).__init__(json_struct)

