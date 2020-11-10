#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from assignment import Pipe
from draw import Segment, log_state, start
from random import randrange, seed


seed(4242)


def hsv_to_rgb(h, s, v):
    h /= 255
    if s == 0.0:
        v *= 255
        return (v, v, v)
    i = int(h*6.)
    f = (h*6.)-i
    p, q, t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))
                                       ), int(255*(v*(1.-s*(1.-f))))
    v *= 255
    i %= 6
    if i == 0:
        return (v, t, p)
    if i == 1:
        return (q, v, p)
    if i == 2:
        return (p, v, t)
    if i == 3:
        return (p, q, v)
    if i == 4:
        return (t, p, v)
    if i == 5:
        return (v, p, q)


a = Pipe(10)
b = Pipe(5)
c = Pipe(4)
d = Pipe(3)
e = Pipe(2)
f = Pipe(1)

a.attach(5, b)
a.attach(2, c)
c.attach(1, d)
b.attach(1, f)
b.attach(2, e)

log_state()

elems = 150
max_size = 5
inputs = [a, b]

for i in range(elems):
    color = hsv_to_rgb(randrange(0, 360), 0.7, 1)
    which = randrange(0, len(inputs))
    length = randrange(1, max_size)
    print("Inserting {0} in pipe {1} with length {2}"
          .format(i, chr(which + ord('A')), length))
    if inputs[which].throw_in(str(i), length, color):
        print("\tSuccess")
        log_state()
    else:
        print("\tFailed")

start()
