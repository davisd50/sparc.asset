from BTrees.OOBTree import OOBTree
from zope.annotation.interfaces import IAnnotations
from zope.annotation.interfaces import IAnnotatable
from zope.component import adapts
from zope.schema import getFields
from zope.interface import implements
from interfaces import IIPNetworkAddress
from interfaces import IIPNetwork

class IPNetworkAddressForAnnotableObjects(object):
    implements(IIPNetworkAddress)
    adapts(IAnnotatable)
    
    def __init__(self, context):
        self.context = context
        self.annotations = IAnnotations(context).\
                                setdefault('IIPNetworkAddress', OOBTree())
        if 'address' not in self.annotations:
            self.annotations['address'] = None
    
    @property
    def address(self):
        return self.annotations['address']
    @address.setter
    def address(self, value):
        getFields(IIPNetworkAddress)['address'].validate(value)
        self.annotations['address'] = value

class IPNetworkForAnnotableObjects(object):
    implements(IIPNetwork)
    adapts(IAnnotatable)
    
    def __init__(self, context):
        self.context = context
        self.annotations = IAnnotations(context).\
                                setdefault('IIPNetwork', OOBTree())
        if 'network' not in self.annotations:
            self.annotations['network'] = None
    
    @property
    def network(self):
        return self.annotations['network']
    @network.setter
    def network(self, value):
        getFields(IIPNetwork)['network'].validate(value)
        self.annotations['network'] = value
