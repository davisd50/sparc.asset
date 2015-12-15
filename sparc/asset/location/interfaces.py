from zope.interface import Interface

# LOCATION INFORMATION
class ILocation(Interface):
    """A location"""
    def __eq__(other):
        """True if equal to other"""
    def __ne__(other):
        """True if not equal to other"""
    
class INetworkLocation(ILocation):
    """A network location"""
    def address():
        """String network address"""
    def network():
        """String network"""

class IGeoLocation(ILocation):
    """A geographic location"""
    def latitude():
        """Float latitude of location"""
    def longitude():
        """Float longitude of location"""