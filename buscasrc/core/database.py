# coding: utf-8

import os


class Database:
    """
    Entity that is responsable for store the app data
    """
    def __init__(self):
        self.documents = {}
        self.inverted_index = {}

    def search(self, tokens_list):
        result_docs = {}
        index_result = self._search_tokens(tokens_list)

        for token in index_result.keys():
            for doc in index_result[token]:
                # search if exists:
                if doc in result_docs.keys():
                    result_docs[doc][token] = index_result[token][doc]
                #create if not exists:
                else:
                    result_docs[doc] = {token : index_result[token][doc]}

        return result_docs


    def return_documents(self, docs_with_positions):
        docs = []

        for doc in docs_with_positions:
            docs.append(self.documents[doc])

        return docs

    def _search_tokens(self, tokens_list):
        result_docs_ids = {}

        for term in tokens_list:
            if term[0] in self.inverted_index.keys():
                result_docs_ids[term[0]] = self.inverted_index[term[0]]

        return result_docs_ids

    def index(self, terms, document):
        self._store_document(document)
        self._index_terms(terms, document)

    def _store_document(self, document):
        self.documents[document['id']] = document['text']

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
