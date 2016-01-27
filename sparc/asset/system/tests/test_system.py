import unittest
from doctest import DocTestSuite
from doctest import DocFileSuite

import sparc.asset.system

def test_suite():
    return unittest.TestSuite((
        DocFileSuite('system.txt',
                     package=sparc.asset.system),))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')