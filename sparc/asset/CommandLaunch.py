__docformat__ = 'restructuredtext'
import logging
import os
import sys

from zope.interface import implements, implementedBy
from zope.schema.fieldproperty import FieldProperty
from zope.component.interfaces import IFactory
from zope.component.factory import Factory

from sparc.asset.interfaces import ICommandLaunch
import sparc.log
logger = logging.getLogger(__name__)

class CommandLaunch(object):
    """Utility used to manage executable launch strings.
    
    Attributes:
        - executable (str): the short name of a *command* (e.g. 'ps')
        - location (str): the directory where the executable is located 
          (e.g. '/usr/bin') - note that the executable is not included
        - _list (list): a list of arguments to the CommandLaunch (e.g. ['-e','-f'])
        - logger: a logging object, used for message logging
    
    Usage:
        Create a new object based on the ping command

        >>> _root = 'C:\\\\' if os.path.sep == '\\\\' else '/'
        >>> myCommandLaunch = CommandLaunch('ping',arguments=['-n', '1', 'localhost'])
        
        Find the current system's default ping executable path
        
        >>> defaultPath = myCommandLaunch.getDefaultExecutableLocation()
        
        Get a launch list that can be delivered to subprocess.call().
        This list does not yet have a defined path for 'ping', so
        subprocess would use the current system's PATH statement.
        
        >>> # myCommandLaunch.getLaunchList()
    """
    implements(ICommandLaunch)
    
    executable = FieldProperty(ICommandLaunch['executable'])
    arguments = FieldProperty(ICommandLaunch['arguments'])
    location = FieldProperty(ICommandLaunch['location'])
    
    def __call__(self, executable, arguments=list(), location=''):
        """Populate object attributes.
        """
        self.executable = executable
        self.arguments = arguments
        self.location = location
        return self

    def getDefaultExecutableLocation(self):
        """Identify the environment's default directory path of object executable.
        """
        for p in os.getenv('PATH').split(os.path.pathsep):
            if os.path.exists(os.path.join(p,self.executable)):
                return p
            if sys.platform.startswith('win') and not self.executable.endswith('.exe') :
                if os.path.exists(os.path.join(p,self.executable + '.exe')):
                    return p
        raise LookupError("No %s in system PATH %s" % (self.executable,os.getenv('PATH')))
    
    def getExecutablePath(self):
        """Find and return the currently configure directory path of the executable.
        """
        return os.path.join(self.location,self.executable) if self.location else os.path.join(self.getDefaultExecutableLocation(),self.executable)
    
    def getExecutableLocation(self):
        """Find and return the directory location of the currently configured executable.
        """
        return self.getDefaultExecutableLocation() if not self.location else self.location
    
    def getLaunchList(self):
        """Return a CommandLaunch object's launch string as a list.
        """
        _call = [self.executable]
        if self.location:
            _call = [os.path.join(self.location,self.executable)]
        return _call + self.arguments

    def validate(self):
        """Verify that the executable object exists and can be executed.
        """
        if not os.path.isfile(self.getExecutablePath()):
            self.logger.info("not a valid file: %s", self.getExecutablePath())
            return False
        if not sys.platform.startswith('win'):
            if not os.access(self.getExecutablePath(), os.F_OK):
                self.logger.info("file not executable: %s", self.getExecutablePath())
                return False
        return True
    
    def _test(self):
        """Docstring method used to test class
        
        Tests:
            >>> import os
            >>> from zope.interface import classImplements
            >>> from zope.interface.verify import verifyClass, verifyObject
            >>> from interfaces import ICommandLaunch
            >>> classImplements(CommandLaunch, ICommandLaunch)
            >>> verifyClass(ICommandLaunch, CommandLaunch)
            True
            >>> _root = 'C:\\\\' if os.path.sep == '\\\\' else '/'
            >>> dummy123 = CommandLaunch('dummy123')
            >>> verifyObject(ICommandLaunch, dummy123)
            True
            >>> try:
            ...     dummy123.getDefaultExecutableLocation()
            ...     assert True == False, "expected bad executable to throw LookupError"
            ... except LookupError:
            ...     pass
            >>> ping = CommandLaunch('ping', arguments=['localhost'])
            >>> _default = ping.getDefaultExecutableLocation()
            >>> if sys.platform.startswith('win'):
            ...     assert _default == _root + os.path.sep.join(['Windows','system32']), "expected ping.exe to be in system32 folder"
            ...     ping.location = _default
            ...     assert ping.getLaunchList() == ['C:\\Windows\\system32\\ping', 'localhost'], "got: " +  str(ping.getLaunchList())
            ... elif sys.platform.startswith('lin'):
            ...     assert '/bin/' in _default, "expected ping to be in a bin location"
            ...     ping.setExecutableLocation(_default)
            ...     assert ping.getLaunchList() == "['/usr/bin/ping', 'localhost']", "expected valid launch list"  # this will fail on some Unix because ping is in sbin
        """
        pass

"""
CommandLaunchFactory = Factory(
    CommandLaunch,
    title=u"Create a CommandLaunch",
    description=u"This factory creates CommandLaunch objects"
    )

"""
class CommandLaunchFactory:
    implements(IFactory)
    
    title = u"Create a CommandLaunch"
    description = u"This factory creates CommandLaunch objects"
    
    def __call__(self, executable='', arguments=list(), location=''):
        _command = CommandLaunch()
        _command.executable = executable
        _command.arguments = arguments
        _command.location = location
        return _command
    
    def getInterfaces(self):
        return implementedBy(CommandLaunch)

#CommandLaunchFactory = CommandLaunchFactory()

if __name__ == "__main__":
    import doctest
    doctest.testmod()