from BTrees.OOBTree import OOBTree
from zope.annotation.interfaces import IAnnotations
from zope.annotation.interfaces import IAttributeAnnotatable
from zope.component import adapts
from zope.component.factory import Factory
from zope.schema import getFields
from zope.schema.fieldproperty import FieldProperty
from zope.interface import implements
from sparc.entity import SparcEntity
from interfaces import INetworkAddressLocations
from interfaces import IIPNetworkAddress
from interfaces import IIPNetwork

class IPNetwork(object):
    implements(IIPNetwork)
    
    def __init__(self, **kwargs):
        if 'network' in kwargs: # allow instantiaion without a network
            self.network = kwargs['network']
    network = FieldProperty(IIPNetwork['network'])
ipNetworkFactory = Factory(IPNetwork)

class IIPNetworkAddress(IPNetwork):
    implements(IIPNetworkAddress)
    
    def __init__(self, **kwargs):
        super(IIPNetworkAddress, self).__init__(**kwargs)
        self.address = kwargs['address']
    address = FieldProperty(IIPNetworkAddress['address'])
ipNetworkAddressFactory = Factory(IIPNetworkAddress)

class NetworkAddressLocationsForAnnotableObjects(object):
    implements(INetworkAddressLocations)
    adapts(IAttributeAnnotatable)
    
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
