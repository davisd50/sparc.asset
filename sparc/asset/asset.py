from zope.component.factory import Factory
from zope.interface import implements
from sparc.entity import SparcEntity
from interfaces import IAsset

class SparcAsset(SparcEntity):
    implements(IAsset)
    
    def __init__(self, **kwargs):
        super(SparcAsset, self).__init__(**kwargs)
sparcAssetFactory = Factory(SparcAsset)
