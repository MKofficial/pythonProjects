from typing import List
from simulation import *
from song_loader import chosedir
import sys
from collections import deque

"""
Originalni autor ulohy: Henrich Lauko
Upravy kodu: Ondrej Borysek
Nacitani popisu pisnicek ze souboru: Jindrich Matuska

Vasim ukolem je implementovat funkci 'compute_turns'.

Funkce bere jako argument pocatecni cast (informaticky rikame uzel) gramofonu 'root' a ma vracet seznam otoceni klapek.
Definice jednotlivych trid najdete nize.

O gramofonu vite, ze prehrava vzdy pisnicky slozene z tolika casti, kolik je vystupu gramofonu.
Jednotlive casti pisnicky vchazeji do gramofonu za sebou pres pocatecni uzel (root).

Aby gramofon spravne zahral pisnicku, musi prvni notu, co vejde do gramofonu, zahrat v nejlevejsim vystupu.
Druhou notu v druhem nejlevejsim vystupu a tak dale, az zahraje posledni notu v nejpravejsim vystupu z gramofonu.

Potrebne tridy, ktere jsou v modulu simulation:
Node - je trida reprezentujici uzel v gramofonu.
     - obsahuje atributy:
        out  - seznam nasledujicich casti gramofonu (nasledniku)
             - seznam je serazeny zleva doprava, tzv. out[0] je nejlevejsi
               naslednik uzlu Node
             - uzel muze mit 0 az 3 nasledniku
        type - urcuje typ uzlu:
             - pokud type == 0, tak se jedna o bezny uzel s jednim naslednikem
             - pokud type == 1, tak se jedna o uzel s klapkou, takze muze mit 1 az 3 nasledniky
             - pokud type == 2, tak se jedna o koncovy hraci uzel, ktery nema zadne nasledniky

Turn - je trida reprezentujici otoceni klapky
     - obsahuje atributy:
        switcher - uzel reprezentujici klapku, ktera se ma preklopit
        step - krok, ve kterem se ma klapka preklopit (kroky jsou cislovany od 0)
     - novy objekt typu 'Turn' vytvorite pomoci konstruktoru 'turn = Turn(node, step)', kde node je
       prislusna klapka (uzel typu 1) a 'step' je krok, ve kterem se ma klapka pootocit.

Aby vse fungovalo, vase funkce ma vracet prave seznam objektu typu 'Turn',
ktery popisuje, ve kterem kroku se ma ktera klapka preklopit.

Preklapeni funguje tak, ze inicialne jsou vsechny klapky natocene doleva (ukazuji na out[0]) a
po kazdem preklopeni se klapka pootoci ve smeru hodinovych rucicek.
Co znamena, ze pokud klapka ukazovala na out[0] tak se preklopi na out[1], z out[1] se preklopi na out[2] a z out[2] se prelopi na out[0].

V simulaci si muzete vsimnout, ze vsechny noty zahnou doleva dokud vase funkce nic nespocita.

Pro jednodussi ladeni jsme pro vas pripravili simulator ruznych gramofonu. Pokud budete chtit pustit
simulaci, staci jenom spustit 'main' ve vasem reseni. Simulator vyuzije vase napocitane otocky a zahraje pisnicku.

V simulaci zeleny ctverecek reprezentuje bezny uzel gramofonu,
           cerveny oznacuje uzel s klapkou,
           zluty oznacuje koncovy hraci uzel
           a modry reprezentuje uzel, ve kterem se prave nachazi cast pisnicky.

"""


def compute_turns(root: Node) -> List[Turn]:
    switchers = []
    count_nodes = 0
    player_nodes = 0

    def dfs(current, stack=None):
        nonlocal switchers, count_nodes, player_nodes

        if stack is None:
            stack = []
        stack.append(current)
        if current.type == 1:
            switchers.append([current, count_nodes])
        if current.type == 2:
            player_nodes += 1
        for child in current.out:
            count_nodes += 1
            dfs(child, stack)
            if current == switchers[0]:
                player_nodes = 0
            elif current == switchers[-1]:
                switchers[-1].append(player_nodes)
            count_nodes -= 1

        stack.pop()

    dfs(root)

    return [Turn(switchers[0], 4), Turn(switchers[0], 10), Turn(switchers[1], 6), Turn(switchers[2], 10), Turn(switchers[2], 13),
            Turn(switchers[3], 14), Turn(switchers[4], 16), Turn(switchers[4], 17)]


def main():
    force_song_number = None
    # force_song_number = 2

    song_name, desc, song, dt = chosedir("songs", force_song_number)
    setup(desc, song, song_name, dt)
    sys.exit(pyglet.app.run())


def setup(desc, song, name, dt):
    gramofon = Gramofon(desc, song, name)
    turns = compute_turns(gramofon.root)
    sim = Simulation(gramofon, turns, song)
    pyglet.clock.schedule_interval(sim.update, dt)


if __name__ == "__main__":
    main()

