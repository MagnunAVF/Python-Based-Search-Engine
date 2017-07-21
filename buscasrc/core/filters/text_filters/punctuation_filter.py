import re


class PunctuationFilter:
    """
        Filter that receive a text and returns a text without punctuation
    """
    def __init__(self, text):
        self.text = text

    def filter_text(self):
        result = self.text
        return re.sub("[?!.,#;:]", "", result)
