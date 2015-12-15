from zope.location import ILocation

class ICommandLaunch(ILocation):
    """Create Python subprocess.call() arguments with potentially unknown executable location
    
    Also provides ILocation where __parent__ is the directory the executable
    is location and __name__ is the executable.
    """
    
    def __iter__():
        """iterator of args that can be delivered to subprocess.call()"""
    
    def validate():
        """True if executable can be located (Windows) and can be executed (Unix)"""
