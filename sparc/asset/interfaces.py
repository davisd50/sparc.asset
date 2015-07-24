__docformat__ = 'restructuredtext'
from zope.interface import Interface
from zope.schema import List, TextLine, ASCII

class ICommandLaunch(Interface):
    """Manages executables launch strings
    
    This interface is used to help developers launch known programs that 
    reside in unknown, or changing locations (e.g. the 'ping' program
    lives in /usr/bin on Linux, but in /usr/sbin on Solaris).  This 
    interface allows for easy separation of the launch string vs. the
    command file system location.
    """
    
    executable = ASCII(
        title = u"Executable",
        description = u"Name of the executable",
        required = True
        )
    arguments = List(
        title = u"Executable launch argument list",
        description = u"Python list of ordered command line arguments to pass into the launch string",
        required = False,
        value_type=ASCII(title=u"Argument")
        )
    location = ASCII(
        title = u"Executable location",
        description = u"Path of the executable parent directory",
        required = False
        )
    
    def __call__(executable, arguments=list(), location=''):
        """Populate object attributes.
        
        This will reset the object attributes.  Attributes will be set based on
        the arguments delivered.  Default values will be set for attributes not
        delivered in a argument.
        """
    
    def getDefaultExecutableLocation():
        """Identify the environment's default directory path of object executable.

        This will search the current OS environment PATH directories for
        :attr:executable.
        
        Returns:
            The parent directory path of the environment's default search
            location for self.executable.  Return value will be one of the
            directories listed in the environment's PATH variable.
        
        Raises:
            LookupError: if unable to find the specified executable in
            any of the directories specified in PATH.
        """
    
    def getExecutablePath():
        """Find and return the currently configure directory path of the executable.
        
        Raises:
            LookupError: object path has not been explicitly set, and command
                can not be found in the current system PATH.
        
        Returns:
            If executable path has been explicitly set, then this will return
            a concatenated string of the location and executable name.
        
            If explicit path has not been set, this will return the absolute path
            based on a system PATH search.
        """
    
    def getExecutableLocation():
        """Find and return the directory location of the currently configured
        executable.
        
        Raises:
            LookupError: object path has not been explicitly set, and command
                can not be found in the current system PATH.
        
        Returns:
            String of explicitly set path, or if the path has not been 
            explicitly set, returns the default system PATH location of the
            command.
        """
    
    def getLaunchList():
        """Return a CommandLaunch object's launch string as a list.
        
        Returns:
            A list of strings that can be passed to the subprocess.call() 
            method as the args command for that method.
        """

    def validate():
        """Verify that the executable object exists and can be executed.
        
        On Windows, this will only check for file existence.  Note: this will
        not validate the arguments.
            
        Returns:
            True if the executable has been validated
        """



