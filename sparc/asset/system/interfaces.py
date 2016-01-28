from zope import schema
from sparc.entity import IEntity

from sparc.asset import MessageFactory as _

class ISystem(IEntity):
    """A system or application"""
    
    #Implementers **MUST** define a system types vocabulary
    type = schema.Choice(
            title = _(u'Type identification'),
            description = _(u'Identifies the type of system'),
            required = True,
            vocabulary = u'sparc.asset.system.types'
            )
    