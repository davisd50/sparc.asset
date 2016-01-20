from sparc.entity import IEntity

class IAsset(IEntity):
    """An asset, device, or host"""

class ILocatableAsset(IAsset):
    """An asset located on one or more networks"""
    def network_address_locations():
        """
        Returns Set of sparc.asset.location.INetworkAddress objects 
        associated with asset
        """
    def network_locations():
        """
        Returns Set of sparc.asset.location.INetworkAddress objects 
        associated with asset
        """
    def geo_location():
        """Returns a sparc.asset.location.IGeoLocation of asset if available"""