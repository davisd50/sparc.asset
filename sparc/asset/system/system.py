from persistent import Persistent
from zope.interface import implements
from zope.component.factory import Factory
from zope.schema.fieldproperty import FieldProperty
from sparc.entity import SparcEntity
from interfaces import ISystem


class SparcSystem(SparcEntity):
    implements(ISystem)
    
    def __init__(self, **kwargs):
        super(SparcSystem, self).__init__(**kwargs)
        self.type = kwargs['type']
    
    type = FieldProperty(ISystem['type'])
sparcSystemFactory = Factory(SparcSystem)


class PersistentSparcSystem(SparcSystem, Persistent):
    """A Sparc entity that can be persisted in a ZODB"""
    implements(ISystem)
persistentSparcSystemFactory = Factory(PersistentSparcSystem)