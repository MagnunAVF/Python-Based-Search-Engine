import re

"""
    Filter that receive a text and returns a text without punctuation
"""
class PunctuationFilter:
    def __init__(self, text):
        self.text = text


    def filter_text(self):
        result = self.text
        return re.sub("[?!.,#;:]", "", result)
