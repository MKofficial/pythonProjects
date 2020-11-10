#!/usr/bin/env python3
# -*- coding: utf-8 -*-

segments = []
states = []


class Segment:
    def __init__(self):
        global segments
        segments.append(self)
        self._color = (255, 255, 255)
        self._content = None
        self._neighbours = []

    def set_content(self, content):
        self._content = content

    def set_color(self, color):
        self._color = (255, 255, 255) if color is None else color

    def get_color(self):
        return self._color

    def add_neighbour(self, other):
        self._neighbours.append(other)


def _calculate_deep(root, state, deep=0):
    if len(state) == 0:
        return 0
    a, b, c = state[root]
    state[root] = (a, b, c, deep)
    for n in c:
        _calculate_deep(n, state, deep+1)


def _format_state():
    global segments
    state = []
    ids = {}
    nextId = 0
    for seg in segments:
        ids[seg] = nextId
        nextId += 1
    for seg in segments:
        state.append((seg._content, seg._color, [
                     ids[x] for x in seg._neighbours]))
    _calculate_deep(0, state)
    return state


def log_state():
    global states
    states.append(_format_state())


def start():
    global states
    from visualization import Visualization
    Visualization(states).run()
