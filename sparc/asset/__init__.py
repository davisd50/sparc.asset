# I18N messaging
from sparc.i18n import SparcMessageFactory
MessageFactory = SparcMessageFactory('sparc.asset')

# Configuration (this package only)
from importlib import import_module
from sparc.configuration.zcml import Configure as SparcConfigure
def Configure():
    SparcConfigure([import_module(__name__)])

from interfaces import IAsset
from interfaces import ILocatableAsset
