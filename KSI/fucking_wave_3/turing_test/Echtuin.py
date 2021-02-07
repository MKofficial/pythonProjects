import math
import time
from functools import reduce
from random import randint
from typing import List, Union

from Pingu import Pingu


class Echtuin(Pingu):
    def __init__(self):
        self._conversationStarted = False
        self._nextGoodbye = 0
        self._greetings = ["Hi", "Hello", "Hi, what's up", "Hey pingu", "It’s been a while", "Kwak", "Servus",
                           "Grüß gott", "fja;sdl", "faksd"]
        self._goodByes = ["Bye", "See you", "Have a nice day", "I'm off"]

    def _isGreetingValid(self, greeting: str) -> bool:
        if greeting.startswith("!"):
            return False
        trimmedGreeting = greeting.strip("!")
        return trimmedGreeting in self._greetings or trimmedGreeting in [x.lower() for x in
                                                                         self._greetings] or trimmedGreeting in [
                   x.upper() for x in self._greetings]

    def startConversation(self, greeting: str) -> str:
        if not self._isGreetingValid(greeting):
            return "..."
        if self._conversationStarted:
            return "What's wrong with you?"
        self._conversationStarted = True
        while True:
            index = randint(0, len(self._greetings) - 1)
            if self._greetings[index] != greeting:
                return self._greetings[index]

    def askQuestion(self, question: str) -> str:
        if not self._conversationStarted:
            return "I won't talk to you until you learn decent manners!!!"
        if question == "How's it going?":
            return "Yeah, fine."
        if question == "What about your family?":
            return "{\"My family\": {\"wives\": {\"count\": 1, \"ages\": [40]},\"sons\": {\"count\": 0, \"ages\": [" \
                   "]},\"daughters\": {\"count\": 2, \"ages\": [10,15]}}} "
        return "Sorry, what did you say?"

    def calculate(self, numbers: List[int]) -> Union[int, str]:
        if not self._conversationStarted:
            return "I won't talk to you until you learn decent manners!!!"
        if len(numbers) < 2 or len(numbers) > 1000:
            return "Go to hell!"
        time.sleep(1 + math.log10(len(numbers)))
        return reduce(lambda x, y: x + y, numbers, 0)

    def endConversation(self) -> str:
        if not self._conversationStarted:
            return "WTF"
        self._conversationStarted = False
        self._nextGoodbye = (self._nextGoodbye + 1) % len(self._goodByes)
        return self._goodByes[self._nextGoodbye]
