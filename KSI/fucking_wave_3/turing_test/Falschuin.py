from functools import reduce
from random import randint
from typing import List, Union

from Pingu import Pingu


class Falschuin(Pingu):
    def __init__(self):
        self._conversationStarted = False
        self._nextGoodbye = 0
        self._greetings = ["Hi", "Hello", "Hi, what's up", "Hey pingu", "It’s been a while", "Kwak", "Servus",
                           "Grüß gott", "fasl", "fa; "]
        self._goodByes = ["Bye", "See you", "Have a nice day", "I'm off"]

    def startConversation(self, greeting: str) -> str:
        if self._conversationStarted:
            return "What's wrong with you?"
        self._conversationStarted = True
        while True:
            index = randint(0, len(self._greetings) - 1)
            if self._greetings[index] != greeting:
                return self._greetings[index]

    def askQuestion(self, question: str) -> str:
        if question == "How's it going?":
            return "Yeah, fine."
        if question == "What about your family?":
            return "{\"My family\": {\"wives\": {\"count\": 1, \"ages\": [40]},\"daughters\": {\"count\": 2, " \
                   "\"ages\": [10,15]}}} "
        return "Sorry, what did you say?"

    def calculate(self, numbers: List[int]) -> Union[int, str]:
        if len(numbers) < 2 or len(numbers) > 1000:
            return "Go to hell!"
        return reduce(lambda x, y: x + y, numbers, 0)

    def endConversation(self) -> str:
        self._conversationStarted = False
        self._nextGoodbye = (self._nextGoodbye) % len(self._goodByes)
        return self._goodByes[self._nextGoodbye]
