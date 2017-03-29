# coding: utf-8

from buscasrc.core.filters.text_filters.punctuation_filter import PunctuationFilter
from buscasrc.core.filters.tokens_filters.lowercase_filter import LowercaseFilter
from buscasrc.core.filters.tokens_filters.stop_words_filter import StopWordsFilter
from buscasrc.core.tokenizer import Tokenizer


class Analyzer:
    """
        Entity that is responsable for prepare the document to index or to search
    """
    def __init__(self):
        self.document = {}


    def prepare_document(self, document):
        doc_tokens = self.prepare_text(document["text"])

        tokens_list = self.generate_structure(doc_tokens, document["id"])

        return tokens_list

    def prepare_text(self, text):
        result_text = self.execute_before_filters(text)

        tokenizer = Tokenizer(result_text)
        result_tokens = tokenizer.generate_tokens()

        result_tokens = self.execute_after_filters(result_tokens)

        return result_tokens


    def execute_before_filters(self, text):
        punctuation_filter = PunctuationFilter(text)
        result_text = punctuation_filter.filter_text()

        return result_text


    def execute_after_filters(self, tokens_list):
        lowercase_filter = LowercaseFilter(tokens_list)
        result_tokens = lowercase_filter.filter_tokens()

        stop_words_filter = StopWordsFilter(result_tokens)
        result_tokens = stop_words_filter.filter_tokens()

        #TODO: implement this filter
        #remove dumb words
        dumb_words = ['', ' ', '-']
        for token in result_tokens:
            if token in dumb_words:
                result_tokens.remove(token)

        return result_tokens


    def generate_structure(self, tokens_list, document_id):
        result_tokens_list = []
        tokens_added = []

        for token in tokens_list:
            if token not in tokens_added:
                tokens_added.append(token)
                result_tokens_list.append( (token, document_id, self.get_token_positions(token, tokens_list)) )

        return result_tokens_list


    def get_token_positions(self, token, token_list):
        positions = []
        for id_token, value in enumerate(token_list):
            if value == token:
                positions.append(id_token)

        return positions
