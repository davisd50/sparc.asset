from zope.component import getGlobalSiteManager
from zope.interface import alsoProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

def register_system_types_vocab_from_values(values=['test']):
    """Convenience function for vocab registration"""
    vocab_factory = lambda x: SimpleVocabulary.fromValues(values)
    alsoProvides(vocab_factory, IVocabularyFactory)
    gsm = getGlobalSiteManager()
    gsm.registerUtility(vocab_factory, IVocabularyFactory, u'sparc.asset.system.types')