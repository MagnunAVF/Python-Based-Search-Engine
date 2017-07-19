import unittest

from buscasrc.core.tokenizer import Tokenizer


class TestTokenizer(unittest.TestCase):
    def test_generate_tokens(self):
        input_text = "Why would you schedule a vote on a bill that" \
            " is at 17% approval?"

        tokenizer = Tokenizer(input_text)

        self.assertEquals(tokenizer.generate_tokens(),  [
            "Why", "would", "you", "schedule", "a", "vote", "on", "a", "bill",
            "that", "is", "at", "17%", "approval?"])
