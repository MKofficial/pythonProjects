#!/usr/bin/python3.7
# -*- coding: utf8 -*-

from sys import argv
from Pinguin import Pingu, Gender
from solution import killPenguins
import json

killedPigus = []
kingsOrder = [""]


def killPinguin(pinguin: Pingu):
    global killedPigus
    print("Pinguin: {} [age: {}, Gender: {}] has been killed".format(
        pinguin.getName(), pinguin.getAge(), Gender.to_string(pinguin.getGender())))
    killedPigus.append(pinguin.getName())


def loadInput(fileName: str) -> Pingu:
    global kingsOrder
    data = None
    with open(fileName, encoding="utf-8") as json_file:
        data = json.load(json_file)
    if "expectedKingsOrder" in data:
        kingsOrder = data["expectedKingsOrder"]
    pingus = dict([(x["name"], (Pingu(x["name"], Gender.parse(x["gender"]), x["age"],
                                      [], killPinguin), x["parents"])) for x in data["pinguins"]])
    for act, parents in pingus.values():
        for parent in parents:
            pingus[parent][0]._children.append(act)
    return pingus[data["king"]][0]


if __name__ == "__main__":
    fileName = argv[1] if len(argv) > 1 else ""
    if fileName == "":
        print("Enter path to input file: ", end="")
        fileName = input()
    king = loadInput(fileName)
    if king is not None:
        killPenguins(king)
        if len(argv) <= 2 or argv[2].lower() != "no-vis":
            from visualization import Visualization
            Visualization(killedPigus, king, kingsOrder).run()
