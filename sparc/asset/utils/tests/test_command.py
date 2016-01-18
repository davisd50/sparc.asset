"""Test
"""
import unittest
from doctest import DocFileSuite

import sparc.asset.utils

def test_suite():
    return unittest.TestSuite((
        DocFileSuite('command.txt',
                     package=sparc.asset.utils),))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')

#from sparc.asset import CommandLaunch


class testCommand(unittest.TestCase):
    """A test class for the command module.
    
    Usage (from command shell): 
        # python test_command.py
    """
    #_root = '/' if os.path.join == '/' else 'C:\\'
    
    #def test_suite(self):
    #    # This will test the doctest(s) contained in command.py
    #    return unittest.TestSuite((DocTestSuite('sparc.asset.CommandLaunch'),))


    '''def testWindowsPath(self):
        # Create a new command object and seed it 
        myWindowsCommand = command('ps',args=['-e','-f'])
        
        # Set the path (denoted as a raw string, otherwise the \b (backspace) becomes \x08)
        myWindowsCommand.setExecutablePath(r'C:\Program Files\cygwin\cdrive\bin')
        myWindowsCommandList = myWindowsCommand.getLaunchList()
        self.assertEqual(myWindowsCommandList[0],r'C:\Program Files\cygwin\cdrive\bin\ps','This test fails: '+myWindowsCommandList[0])

        # Break the path down to its parts
        myExecutableList = myWindowsCommandList[0].split('\\')
        self.assertEqual(myExecutableList[0],'C:','Fails on '+myExecutableList[0])
        self.assertEqual(myExecutableList[1],'Program Files','Fails on '+myExecutableList[1])
        self.assertEqual(myExecutableList[2],'cygwin','Fails on '+myExecutableList[2])
        self.assertEqual(myExecutableList[3],'cdrive','Fails on '+myExecutableList[3])
        self.assertEqual(myExecutableList[4],'bin','Fails on '+myExecutableList[4])'''

