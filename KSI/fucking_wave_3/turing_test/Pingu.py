import random
from abc import ABC, abstractmethod
from typing import List


class Pingu(ABC):

    @abstractmethod
    def startConversation(self, greetings: str) -> str:
        pass

    @abstractmethod
    def askQuestion(self, question: str) -> str:
        pass

    @abstractmethod
    def calculate(self, numbers: List[int]) -> int:
        pass

    @abstractmethod
    def endConversation(self) -> str:
        pass
