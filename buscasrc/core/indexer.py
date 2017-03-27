# coding: utf-8

from buscasrc.core.filters.text_filters.punctuation_filter import PunctuationFilter
from buscasrc.core.filters.tokens_filters.lowercase_filter import LowercaseFilter
from buscasrc.core.filters.tokens_filters.stop_words_filter import StopWordsFilter
from buscasrc.core.tokenizer import Tokenizer

"""
    Entity that is responsable for index terms in the inverted index
"""
class Indexer:
    def __init__(self, database):
        self.database = database


    """
    Receives a tokens_list with the format:
    for each token: token, document id, positions in document,
    Ex.: ("conan",  document_id, [1, 5]), ... ]
    """
    def index_document(self, tokens_list):
        inverted_index = self.database.inverted_index

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
            self.index_document(self.prepare_document(document))


    def prepare_document(self, document):
        tokens_list = []
        doc_id = document["id"]

        #before text filters
        punctuation_filter = PunctuationFilter(document["text"])
        doc_text = punctuation_filter.filter_text()

        #tokenizer
        tokenizer = Tokenizer(doc_text)
        doc_tokens = tokenizer.generate_tokens()

        #after tokens filter
        lowercase_filter = LowercaseFilter(doc_tokens)
        doc_tokens = lowercase_filter.filter_tokens()

        stop_words_filter = StopWordsFilter(doc_tokens)
        doc_tokens = stop_words_filter.filter_tokens()

        #TODO: implement this filter
        #remove dumb words
        dumb_words = ['', ' ', '-']
        for token in doc_tokens:
            if token in dumb_words:
                doc_tokens.remove(token)

        tokens_added = []
        #create structured list
        for token in doc_tokens:
            if token not in tokens_added:
                tokens_added.append(token)
                tokens_list.append( (token, doc_id, self.get_token_positions(token, doc_tokens)) )

        return tokens_list


    def get_token_positions(self, token, token_list):
        positions = []
        for id_token, value in enumerate(token_list):
            if value == token:
                positions.append(id_token)
        return positions
