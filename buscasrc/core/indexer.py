# coding: utf-8

from buscasrc.core.analyzer import Analyzer


class Indexer:
    """
    Entity that is responsable for index terms in the inverted index
    """
    def __init__(self, database, analyzer):
        self.database = database
        self.analyzer = analyzer


    def index_document(self, document):
        tokens_list = self.analyzer.prepare_text(document["text"])

        self.database.index(tokens_list, document)


    def index_documents(self, documents):
        for document in documents:
            self.index_document(document)
