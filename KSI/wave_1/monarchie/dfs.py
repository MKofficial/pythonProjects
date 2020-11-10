class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, children: list):
        self.children.extend(children)


def dfs(start):
    s = [start]
    while len(s) > 0:
        (current, index) = s.pop()
        if index == 0:
            print("Visiting element " + str(current.data))
        if index < len(current.children):
            s.append((current, index + 1))
            s.append((current.children[index], 0))
        else:
            print("Visiting element " + str(current.data) + " has finished")


if __name__ == '__main__':
    king = Node("king")
    oldest_son = Node("oldest son")
    younger_son = Node("younger son")
    son_of_oldest_son = Node("son of oldest son")
    king.add_children([oldest_son, younger_son])
    oldest_son.add_child(son_of_oldest_son)
    dfs(king)