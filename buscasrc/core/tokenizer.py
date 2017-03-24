"""
    Entity that receive a text and create and return a list of tokens
"""
class Tokenizer:
    def __init__(self, text):
        self.text = text


    def generate_tokens(self):
        return self.text.split(' ')
