from persistent import Persistent
from zope.component.factory import Factory
from zope import interface
from sparc.entity import SparcEntity
from .interfaces import IAsset

@interface.implementer(IAsset)
class SparcAsset(SparcEntity):
    
    def __init__(self, **kwargs):
        super(SparcAsset, self).__init__(**kwargs)
sparcAssetFactory = Factory(SparcAsset)


@interface.implementer(IAsset)
class PersistentSparcAsset(SparcAsset, Persistent):
    """A Sparc Asset that can be persisted in a ZODB"""
persistentSparcAssetFactory = Factory(PersistentSparcAsset)