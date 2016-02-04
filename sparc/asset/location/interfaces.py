import ipaddress
from zope.interface import Interface
from zope.interface import Attribute
from zope import schema


# SCHEMA CONSTRAINTS
def _is_valid_ipnetwork(object):
    if isinstance(object, ipaddress.IPv4Network): return True
    if isinstance(object, ipaddress.IPv6Network): return True
    return False

def _is_valid_ipaddress(object):
    if isinstance(object, ipaddress.IPv4Address): return True
    if isinstance(object, ipaddress.IPv6Address): return True
    return False

# LOCATION INFORMATION
class ILocation(Interface):
    """A location"""
    def __eq__(other):
        """True if equal to other"""
    def __ne__(other):
        """True if not equal to other"""

class ILocations(Interface):
    """A set of locations"""
    locations = Attribute('A set of ILocation objects')

class INetworkAddressLocations(ILocations):
    """A set IIPNetworkAddress objects"""
    locations = schema.Set(
            title = u'IP Addresses',
            description = u'a set of INetworkAddress objects',
            value_type = schema.Field(
                    constraint = lambda v: INetworkAddress.providedBy(v)
                    )
            )

# NETWORK INFORMATION
class INetwork(ILocation):
    """A network that contains addresses"""
    network = Attribute('Network location identifier')

class INetworkAddress(INetwork):
    """A network address location"""
    address = Attribute('Network address location identifier')

# IP NETWORK INFORMATION
class IIPNetwork(INetwork):
    """Network location identified via Python ipaddress.ip_network"""
    network = schema.Field(
            title = u'IIPNetwork',
            description = u'An IP network identifier from ipaddress package',
            constraint = _is_valid_ipnetwork
            )

class IIPNetworkAddress(INetworkAddress, IIPNetwork):
    """Network address locaton identified via Python ipaddress.ip_address"""
    address = schema.Field(
            title = u'IIPNetworkAddress',
            description = u'An IPv4Address/IPv6Address address from ipaddress package',
            constraint = _is_valid_ipaddress
            )

# GEOLOCATION INFORMATION
class IGeoLocation(ILocation):
    """A geographic location"""
    def latitude():
        """Float latitude of location"""
    def longitude():
        """Float longitude of location"""