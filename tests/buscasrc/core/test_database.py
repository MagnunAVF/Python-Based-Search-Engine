import unittest

from buscasrc.core.database import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = Database()
        self.documentFixture = {
            "id": "doc001",
            "text": "Hello! Conan! Have you read Conan HQ? "
        }
        self.documentsFixture = {
            'doc001': "The fox run.",
            'doc002': "The fox is red."
        }

        self.inverted_indexFixture = {
            'fox': {'doc001': [0], 'doc002': [0]},
            'red': {'doc002': [1]},
            'run': {'doc001': [1]},
        }

    def test_search(self):
        self.database.inverted_index = self.inverted_indexFixture
        self.database.documents = self.documentsFixture

        documents = self.database.search([('fox', [3])])
        self.assertEquals(documents, {'doc001': {'fox': [0]}, 'doc002': {'fox': [0]}})

    def test_return_documents(self):
        self.database.documents = {
            'doc001': "The fox run.",
            'doc002': "The fox is red.",
            'doc003': "The horse is white"
        }

        result_docs = self.database.return_documents({'doc001': {'fox': [0]}, 'doc002': {'fox': [0]}})

        self.assertEquals(result_docs, ["The fox run.", "The fox is red."])


    def test_search_tokens(self):
        self.database.inverted_index = self.inverted_indexFixture
        self.database.documents = self.documentsFixture

        documents = self.database._search_tokens([('fox', [3])])

        self.assertEquals(documents, {'fox': {'doc001': [0], 'doc002': [0]}})

    #TODO: Change tests to check function call
    def test_index(self):
        tokens_list = [('hello', [0]), ('conan', [1,3]), ('read', [2]), ('hq', [4])]

        self.database._store_document(self.documentFixture)
        self.database._index_terms(tokens_list, self.documentFixture)

        self.assertEquals(self.database.documents['doc001'], self.documentFixture['text'])
        self.assertEquals(self.database.inverted_index, {'hello': {'doc001': [0]}, 'conan': {'doc001': [1,3]}, 'read': {'doc001': [2]}, 'hq': {'doc001': [4]}})

    def test_store_document(self):
        self.database._store_document(self.documentFixture)

        self.assertEquals(self.database.documents['doc001'], self.documentFixture['text'])


    def test_index_terms(self):
        tokens_list = [('hello', [0]), ('conan', [1,3]), ('read', [2]), ('hq', [4])]

        self.database._index_terms(tokens_list, self.documentFixture)

        self.assertEquals(self.database.inverted_index, {'hello': {'doc001': [0]}, 'conan': {'doc001': [1,3]}, 'read': {'doc001': [2]}, 'hq': {'doc001': [4]}})
