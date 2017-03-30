# coding: utf-8

import os


class Database:
    """
        Entity that is responsable for store the app data
    """
    def __init__(self):
        self.documents = {}
        self.inverted_index = {}


    def index(self, terms, document):
        self._store_document(document)
        self._index_terms(document['id'], terms)


    def _store_document(self, document):
        self.documents[document['id']] = document


    def _index_terms(self, tokens_list, document):
        for token in tokens_list:
            key_name = token[0]
            position_array = token[1]

            doc_id = document['id']

            # search if exists:
            if key_name in self.inverted_index.keys():
                self.inverted_index[key_name][doc_id] = position_array
            #create if not exists:
            else:
                self.inverted_index[key_name] = { doc_id : position_array }
