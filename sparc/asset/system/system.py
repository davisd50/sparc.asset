from zope import interface
from persistent import Persistent
from zope.component.factory import Factory
from zope.schema.fieldproperty import FieldProperty
from sparc.entity import SparcEntity
from .interfaces import ISystem

@interface.implementer(ISystem)
class SparcSystem(SparcEntity):
    
    def __init__(self, **kwargs):
        super(SparcSystem, self).__init__(**kwargs)
        self.type = kwargs['type']
    
    type = FieldProperty(ISystem['type'])
sparcSystemFactory = Factory(SparcSystem)


@interface.implementer(ISystem)
class PersistentSparcSystem(SparcSystem, Persistent):
    """A Sparc entity that can be persisted in a ZODB"""
persistentSparcSystemFactory = Factory(PersistentSparcSystem)