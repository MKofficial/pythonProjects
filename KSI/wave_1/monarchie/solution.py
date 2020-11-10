from Pinguin import Gender, Pingu
import sys

sys.setrecursionlimit(sys.maxsize)
TARGET_PENGUIN = "Karlík Veliký"


def killPenguins(penguin: Pingu):
    """
    Method killing king and its relatives
    :param penguin: Penguin king
    :type: penguin: Pingu
    :return: None
    """

    # if penguin name is equal to TARGET_PENGUIN then the program will stop
    if penguin.getName() != TARGET_PENGUIN:
        penguin.kill()  # kill penguin

        # get only men children
        penguin.children = [child for child in penguin.getChildren() if child.getGender() == Gender.MALE]

        # if the length of children is 0 then the penguin does not have any other descendant and we have to go back
        if len(penguin.children) == 0:
            # the parent of that penguin (who does not have any descendants)
            new_penguin = penguin.previous
            # if the parent does not have any descendants too then the program will go back to his parent and so on
            while len(new_penguin.children) == 0:
                new_penguin = new_penguin.previous

            # recursive call !!!
            killPenguins(new_penguin.children.pop())

        penguin.children.sort(key=lambda element: element.getAge())  # sort penguin.children by their age

        if penguin.children:
            # for every descendant set attr previous to point to their parent
            for child in penguin.children:
                child.previous = penguin

            # recursive call !!!
            killPenguins(penguin.children.pop())

