from BTrees.OOBTree import OOBTree
from zope import component
from zope import interface
from zope.annotation.interfaces import IAnnotations
from zope.annotation.interfaces import IAttributeAnnotatable
from zope.component.factory import Factory
from zope.schema import getFields
from zope.schema.fieldproperty import FieldProperty
from .interfaces import INetworkAddressLocations
from .interfaces import IIPNetworkAddress
from .interfaces import IIPNetwork

@interface.implementer(IIPNetwork)
class IPNetwork(object):
    
    def __init__(self, **kwargs):
        if 'network' in kwargs: # allow instantiaion without a network
            self.network = kwargs['network']
    network = FieldProperty(IIPNetwork['network'])
ipNetworkFactory = Factory(IPNetwork)

@interface.implementer(IIPNetworkAddress)
class IIPNetworkAddress(IPNetwork):
    
    def __init__(self, **kwargs):
        super(IIPNetworkAddress, self).__init__(**kwargs)
        self.address = kwargs['address']
    address = FieldProperty(IIPNetworkAddress['address'])
ipNetworkAddressFactory = Factory(IIPNetworkAddress)

@interface.implementer(INetworkAddressLocations)
@component.adapter(IAttributeAnnotatable)
class NetworkAddressLocationsForAnnotableObjects(object):
    
    def __init__(self, context):
        self.context = context
        self.annotations = IAnnotations(context).\
                                setdefault('INetworkAddressLocations', OOBTree())
        if 'locations' not in self.annotations:
            self.annotations['locations'] = set()
    
    @property
    def locations(self):
        return self.annotations['locations']
    @locations.setter
    def locations(self, value):
        getFields(INetworkAddressLocations)['locations'].validate(value)
        self.annotations['locations'] = value
