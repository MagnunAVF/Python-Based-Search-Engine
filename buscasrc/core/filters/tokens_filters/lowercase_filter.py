class LowercaseFilter:
    """
        Filter that receive a token list and returns a tokens list with lowercase words
    """
    def __init__(self, tokens_list):
        self.tokens_list = tokens_list


    def filter_tokens(self):
        return [token.lower() for token in self.tokens_list]
