from random import shuffle
from time import time, sleep
from string import ascii_lowercase


class GuessTime:
    """
    Timing estimate
    """

    def __init__(self, delta):
        """
        :param delta: Number of seconds which user will try to guess
        :type delta: float
        """
        self.delta = delta

    def invoke(self):
        """
        Method prints out a time and a user tries to press enter key in that exact time

        :return: Negative difference between user guess and time provided by an examiner
        """
        print("In " + str(self.delta) + " seconds press ENTER")
        start = time()
        input()
        end = time()

        return -abs(self.delta - (end - start))


class OpenAnswer:
    """
    Arbitrarily long text response
    """

    def __init__(self, question, answer):
        """
        :param question: Question provided by an examiner
        :type question: str
        :param answer: Correct answer an examiner is expecting
        :type answer: str
        """
        self.question = question
        self.answer = answer

    def invoke(self):
        """
        Method prints out a question and user will try to answer it

        :return: 1 if a user is correct, 0 if not
        """
        print(self.question)
        response = input("Answer: ")
        return 1 if self.answer in response else 0


class Reaction:
    """
    Flash copying
    """

    def __init__(self, delta, answer):
        """
        :param delta: Number of seconds for how long the answer will be displayed
        :type delta: float
        :param answer: String which user has to rewrite
        :type answer: str
        """
        self.delta = delta
        self.answer = answer

    def invoke(self):
        """
        Method wait for delta seconds pass then display text which user has to rewrite

        :return: Negative number of seconds that indicates how long it took the user to copy the text
        """
        print("Rewrite this text as fast as possible:")
        sleep(self.delta)
        print(self.answer)
        start = time()
        while True:
            guess = input()
            if guess == self.answer:
                end = time()
                break

        return start - end


class MultipleChoice:
    """
    Zero to everything correct
    """

    def __init__(self, question, correct_answer, wrong_answer):
        """
        :param question: Question provided by an examiner
        :type question: str
        :param correct_answer: Correct answers for the question
        :type correct_answer: list
        :param wrong_answer: Wrong answers for the question
        :type wrong_answer: list
        """
        self.question = question
        self.all_answers = [[ascii_lowercase[i], sorted(correct_answer + wrong_answer)[i]]
                            for i in range(len(correct_answer + wrong_answer))]
        self.correct_letters = "".join([i[0] for i in self.all_answers if i[1] in correct_answer])

    def invoke(self):
        print(self.question)
        for i in self.all_answers:
            print("{}) {}".format(i[0], i[1]))
        my_ans = input()
        length = 0
        for i in my_ans:
            if i in self.correct_letters:
                length += 1
            else:
                length -= 1
        return length


if __name__ == '__main__':
    MultipleChoice("Kolik kreditů je minimálně potřeba k dokončení 1. semestru na FI MUNI?",
                ["20", "27"], ["30", "15", "18", "25"]).invoke()