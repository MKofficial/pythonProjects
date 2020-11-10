import time
# from typing import Tuple, List

import pyglet
from pyglet import shapes
import queue as Queue
import string
import visualization

# Having global variables is a dirty, dirty hack. But for the sake of backwards compatibility... Let's pretend we don't see it.
# gl_states: List[List[visualization.DrawableObject]] = []
gl_states = []
# gl_states_add_music: List[List[str]] = []
gl_states_add_music = []
disable_pyglet_sounds = True

def enum(**enums):
    return type('Enum', (), enums)


class Node:
    def __init__(self):
        self.next = None
        self.type = 0
        self.note = None
        self.tmpnote = None
        self.out = []

    def move(self):
        if self.next is not None:
            self.next.tmpnote = self.note
            self.note = None

    def check(self):
        self.note = self.tmpnote
        self.tmpnote = None


class Switcher(Node, object):
    def __init__(self):
        super(Switcher, self).__init__()
        self.dir = 0
        self.type = 1

    def addBranch(self, node):
        self.out.append(node)

    def switch(self):
        self.dir = (self.dir + 1) % len(self.out)

    def move(self):
        tmp = self.out[self.dir]
        if tmp is not None:
            tmp.tmpnote = self.note
            self.note = None


class PlayerNode(Node, object):
    # def __init__(self, player, source, player_id_int: int, source_path: str):
    def __init__(self, player, source, player_id_int, source_path):
        super(PlayerNode, self).__init__()
        self.player = player
        self.source = source
        self.source_path = source_path
        self.type = 2
        self.player_id = str(player_id_int)  # string.ascii_uppercase[player_id_int - 1]

    def move(self):
        if self.note is not None:
            self.note = None
            self.player.queue(self.source)
            if not self.player.playing:
                if not disable_pyglet_sounds:
                    self.player.play()
            gl_states_add_music[-1].append(self.source_path)


Dir = enum(left=0, up=1, right=2)


class Rectangle(object):
    def __init__(self, stem, parent, d):
        self.stem = stem
        self.parent = parent
        self.x = 0
        self.y = 0
        self.d = d
        self.size = 20

    # def get_color(self) -> Tuple[int, int, int]:
    def get_color(self):
        final_color = (0, 255, 0)
        if isinstance(self.stem, PlayerNode):
            final_color = (255, 255, 0)
        if isinstance(self.stem, Switcher):
            final_color = (255, 0, 0)
        if self.stem.note is not None:
            final_color = (0, 0, 255)
        return final_color

    def recalculate_pos(self):
        parent = self.parent
        if parent == None:
            return
        if parent.d == Dir.up:
            if self.d == Dir.up:
                self.x = parent.x
                self.y = parent.y + 21
            elif self.d == Dir.left:
                self.x = parent.x - 21
                self.y = parent.y
            else:
                self.x = parent.x + 21
                self.y = parent.y
        elif parent.d == Dir.left:
            if parent.parent.d == Dir.left:
                self.x = parent.x
                self.y = parent.y + 21
                self.d = Dir.up
            else:
                self.x = parent.x - 21
                self.y = parent.y
                self.d = Dir.left
        else:
            if parent.parent.d == Dir.right:
                self.x = parent.x
                self.y = parent.y + 21
                self.d = Dir.up
            else:
                self.x = parent.x + 21
                self.y = parent.y
                self.d = Dir.right

    def draw_rectangle(self):
        square = shapes.Rectangle(self.x, self.y, self.size, self.size,
                                  color=self.get_color())
        square.draw()
        gl_states[-1].append(visualization.Rectangle(self.x, self.y, color=self.get_color(), width=self.size, height=self.size))

    def draw_text(self):
        label_color = (0, 0, 0, 255)
        draw_label = False

        if self.stem.note is not None:
            draw_label = True
            # label_text = self.stem.note[-1]
            label_text = str(self.stem.note[1])

        if isinstance(self.stem, PlayerNode):
            draw_label = True
            label_text = str(self.stem.player_id)
            label_color = (0, 0, 0, 255)

        if draw_label:
            label = pyglet.text.Label(label_text,
                                      font_name='Times New Roman',
                                      font_size=20,
                                      x=self.x + self.size // 2, y=self.y + self.size // 2,
                                      color=label_color,
                                      anchor_x='center', anchor_y='center')
            label.draw()
            gl_states[-1].append(visualization.Label(self.x + self.size // 2,
                                                     self.y, #+ self.size // 2,
                                                     label_text,
                                                     color=label_color[:3],
                                                     size=int(self.size*1.5))
                                 )


class Simulation(pyglet.window.Window, object):
    def __init__(self, gramofon, turns, notes):
        super(Simulation,self).__init__(fullscreen=False, caption='Simulation')
        self.gramofon = gramofon
        self.notes = notes
        self.notes_count = len(self.notes)
        self.turns = turns
        self.set_size(800,600)
        #for turn in self.turns:
        #    print(turn.switcher),
        #    print(turn.step)
        self.steps = -1

    def draw_gramofon(self):
        gl_states.append([])
        gl_states_add_music.append([])

        rec = Rectangle(self.gramofon.root, None, Dir.up)
        rec.x = int(round(self.width / 2))
        rec.y = 10
        q = Queue.Queue()
        q.put(rec)
        while not q.empty():
            rec = q.get()
            rec.recalculate_pos()

            rec.draw_rectangle()
            rec.draw_text()

            pa = rec
            if rec.stem.next is not None:
                rec = Rectangle(rec.stem.next, pa, Dir.up)
                q.put(rec)
            elif isinstance(rec.stem, Switcher):
                for i in range(len(pa.stem.out)):
                    if i == 0:
                        rec = Rectangle(pa.stem.out[i], pa, Dir.left)
                    elif i == 1:
                        rec = Rectangle(pa.stem.out[i], pa, Dir.up)
                    elif i == 2:
                        rec = Rectangle(pa.stem.out[i], pa, Dir.right)
                    q.put(rec)

    def update(self, dt):
        # if self.gramofon.player.playing:
        #     time.sleep(0.1)
        self.clear()  # this doesn't work correctly
        # redraw_box = shapes.Rectangle(0, 0, 800, 600, color=(0,0,0))
        # redraw_box.draw()
        if self.turns is not None:
            for turn in self.turns:
                if turn.step == self.steps:
                    if isinstance(turn.switcher, Switcher):
                        turn.switcher.switch()
                    else:
                        print("Trying to switch a Node that is not a Switcher.")
        self.gramofon.step()
        if len(self.notes) != 0:
            note = self.notes.pop()
            self.gramofon.root.note = (note, self.notes_count - len(self.notes))
        self.draw_gramofon()
        self.steps += 1


class Gramofon:
    def __init__(self, desc, sources, path_to_song=""):
        self.player = pyglet.media.Player()
        #self.player.play()
        self.notes = []
        self.notes_paths = []
        for s in sources:
            self.notes.append( pyglet.media.load(path_to_song + "/" + s + '.wav', streaming=False) )           # Adding sounds to notes
            self.notes_paths.append(path_to_song + "/" + s + '.wav')
        self.notes_count = len(self.notes)
        self.switchers = []
        self.stems = []
        self.root = self.built(desc)

    def built(self, desc):
        if desc is None:
            return None

        if len(desc) == 0:
            note = self.notes.pop()
            note_source = self.notes_paths.pop()
            stem = PlayerNode(self.player, note, self.notes_count-len(self.notes), note_source)
            self.stems.append(stem)
            return stem

        first = None
        last = None
        stem = None

        if isinstance(desc[0], (int)):
            for _ in range(desc[0]):
                stem = Node()
                self.stems.append(stem)
                if last is not None:
                    last.out.append(stem)
                    last.next = stem
                else:
                    first = stem
                last = stem

        if len(desc) == 2 and len(desc[1]) == 0:
            stem = self.built(desc[1])
        else:
            stem = Switcher()
            self.stems.append(stem)
            self.switchers.append(stem)
            for branch in range(1, len(desc)):
                stem.addBranch(self.built(desc[branch]))
        if last is not None:
            last.out.append(stem)
            last.next = stem
        else:
            first = stem

        return first

    def step(self):
        for stem in self.stems:
            stem.move()
        for stem in self.stems:
            stem.check()


class Turn:
    def __init__(self, switcher, step):
        self.switcher = switcher
        self.step = step