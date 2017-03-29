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
        """
            Receives a tokens_list with the format:
            for each token: token, document id, positions in document,
            Ex.: ("conan",  document_id, [1, 5]), ... ]
        """
        inverted_index = self.database.inverted_index

        tokens_list = self.analyzer.prepare_document(document)

        for token in tokens_list:
            key_name = token[0]
            doc_id = token[1]
            position_array = token[2]

            # search if exists:
            if key_name in inverted_index.keys():
                inverted_index[key_name][doc_id] = position_array
            #create if not exists:
            else:
                inverted_index[key_name] = { doc_id : position_array }

        print(inverted_index)


    def index_documents(self, documents):
        for document in documents:
            self.index_document(document)
