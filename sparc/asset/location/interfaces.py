from zope.interface import Interface
from zope.interface import Attribute

# LOCATION INFORMATION
class ILocation(Interface):
    """A location"""
    def __eq__(other):
        """True if equal to other"""
    def __ne__(other):
        """True if not equal to other"""

# NETWORK INFORMATION
class INetwork(ILocation):
    """A network that contains addresses"""
    network = Attribute('Network location identifier')

class IIPNetwork(INetwork):
    """Network location identified via Python ipaddress.ip_network"""

class INetworkAddress(ILocation):
    """A network address location"""
    address = Attribute('Network address location identifier')

class IIPNetworkAddress(INetworkAddress):
    """Network address locaton identified via Python ipaddress.ip_address"""

# GEOLOCATION INFORMATION
class IGeoLocation(ILocation):
    """A geographic location"""
    def latitude():
        """Float latitude of location"""
    def longitude():
        """Float longitude of location"""