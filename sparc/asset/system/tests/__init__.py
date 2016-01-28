from zope.schema.vocabulary import getVocabularyRegistry
from zope.schema.vocabulary import SimpleVocabulary

def register_system_types_vocab_from_values(values=['test']):
    """Convenience function for vocab registration"""
    vocab_factory = lambda x: SimpleVocabulary.fromValues(values)
    vr = getVocabularyRegistry()
    vr.register(u'sparc.asset.system.types', vocab_factory)