from zope.component import getSiteManager
from zope.interface import alsoProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


#def register_system_types_vocab_from_values(values=['test']):
#    """Convenience function for vocab registration"""
#    vocab_factory = lambda : SimpleVocabulary.fromValues(values)
#    alsoProvides(vocab_factory, IVocabularyFactory)
#    sm = getSiteManager()
#    sm.registerUtility(vocab_factory, IVocabularyFactory, u'sparc.asset.system.types')

def testingSystemAssetTypeVocabulary(context):
    """A vocab factory used for testing purposes"""
    return SimpleVocabulary.fromValues(['test_type_1', 'test_type_2', 'test_type_3'])
alsoProvides(testingSystemAssetTypeVocabulary, IVocabularyFactory)