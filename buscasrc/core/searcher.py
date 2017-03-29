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
        inverted_index = database.inverted_index

        searched_tokens = analyzer.prepare_text(text)

        


    def order_results(self, result_docs):
        raise NotImplementedError

    def score_doc(self, doc):
        raise NotImplementedError
