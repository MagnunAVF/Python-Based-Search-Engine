# coding: utf-8

from buscasrc.core.analyzer import Analyzer


class Searcher:
    """
    Entity that is responsable for search terms stored in the inverted index
    """
    def __init__(self, database, analyzer):
        self.database = database
        self.analyzer = analyzer

    def search_documents(self, text):
        search_tokens = self.analyzer.prepare_text(text)

        result_docs = self.database.search(search_tokens)

        return self.database.return_documents(result_docs)

    def order_results(self, result_docs):
        raise NotImplementedError

    def score_doc(self, doc):
        raise NotImplementedError
