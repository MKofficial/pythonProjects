import unittest
from typing import List

from Echtuin import Echtuin
from Pingu import Pingu


class TuringTest(unittest.TestCase):
    correct_greetings = ["hi", "hello", "hi, what's up", "hey pingu", "it's been a while", "kwak", "servus",
                         "grüß gott"]

    def __init__(self, *args, **kwargs):
        self.sut: Pingu = Echtuin()
        # self.sut: Ping = Falschuin()
        super().__init__(*args, **kwargs)

    # Implement your other tests here
    def testGreetingCorrect(self):
        # conversation is not already started
        self.assertFalse(self.sut._conversationStarted)

        # greeting is in greetings
        valid_greetings = self.greetingIsValid(True)
        pass
        # answer is in greetings

        # answer is not same as greeting

    def testGreetingFalse(self):
        self.sut.startConversation("Hi")
        # conversation is already started
        self.assertTrue(self.sut._conversationStarted)
        self.assertEqual(self.sut.startConversation("Hi"), "What's wrong with you?")

        # greeting is not in greetings
        invalid_greetings = self.greetingIsValid(False)
        pass
        # answer is not in greetings (ROBOT option)

        # answer is same as greetings (ROBOT option)

    def greetingIsValid(self, param: bool) -> List[int]:
        if param:
            return [i.lower().removesuffix("!") for i in self.sut._greetings if i.lower().removesuffix("!")
                    in self.correct_greetings]
        else:
            return [i.lower().removesuffix("!") for i in self.sut._greetings if i.lower().removesuffix("!")
                    not in self.correct_greetings]


if __name__ == '__main__':
    unittest.main()
