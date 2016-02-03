import unittest
from doctest import DocTestSuite
from doctest import DocFileSuite

import sparc.asset

def test_suite():
    return unittest.TestSuite((
        DocFileSuite('asset.txt',
                     package=sparc.asset),))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')