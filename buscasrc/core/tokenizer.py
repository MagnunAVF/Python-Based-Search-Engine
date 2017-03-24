class Tokenizer:
    def __init__(self, text):
        self.text = text

    def generate_tokens(self):
        return self.text.split(' ')
