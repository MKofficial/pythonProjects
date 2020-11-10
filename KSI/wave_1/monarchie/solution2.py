from Pinguin import Gender, Pingu

TARGET_PENGUIN = "Karlík Veliký"
stack = []


def killPenguins(penguin: Pingu):
    """
    Method killing king and its relatives
    :param penguin: Penguin king
    :type: penguin: Pingu
    :return: None
    """
    penguin.previous = None
    if not penguin.children:
        penguin.kill()

    penguin.children = [child for child in penguin.getChildren() if child.getGender() == Gender.MALE]

    if penguin.children:
        # if the descendant has some offsprings
        pass
