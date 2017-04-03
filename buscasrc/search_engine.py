from buscasrc.core.database import Database
from buscasrc.core.indexer import Indexer
from buscasrc.core.searcher import Searcher
from buscasrc.core.analyzer import Analyzer


class SearchEngine:
    def __init__(self):
        self.database = Database()
        self.indexer = Indexer(self.database, Analyzer())
        self.searcher = Searcher(self.database, Analyzer())

    def index(self, document):
        self.indexer.index_document(document)

    def search(self, text):
        return self.searcher.search_documents(text)
