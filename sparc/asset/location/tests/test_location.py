import unittest
from doctest import DocTestSuite
from doctest import DocFileSuite

import sparc.asset.location

def test_suite():
    return unittest.TestSuite((
        DocFileSuite('location.txt',
                     package=sparc.asset.location),))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')