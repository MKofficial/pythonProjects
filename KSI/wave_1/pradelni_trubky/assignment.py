#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from draw import Segment


class Pipe:
    def __init__(self, n):
        """
        Constructor
        :param n: Length of pipe
        :type n: int
        """
        self.length = n
        self.boxes = [Segment() for i in range(self.length)]
        if len(self.boxes) > 1:
            for i in range(self.length):
                if i == 0:
                    # self.boxes[0].next = self.boxes[1]
                    self.boxes[0].add_neighbour(self.boxes[1])
                elif i == self.length - 1:
                    # self.boxes[-1].next = None
                    pass
                else:
                    # self.boxes[i].next = self.boxes[i + 1]
                    self.boxes[i].add_neighbour(self.boxes[i + 1])
        else:
            # self.boxes[0].next = None
            pass

    def get_length(self):
        """
        Getter
        :return: Length of pipe
        """
        return self.length

    def attach(self, n, other_pipe):
        """
        Method attaching one pipe to another
        :param n: Index of box in bottom pipe on which other_pipe will be connected
        :param other_pipe: A Pipe which will be connected
        :type n: int
        :type other_pipe: Pipe
        :return: None
        """
        # other_pipe.boxes[-1].next = self.boxes[n - 1]
        other_pipe.boxes[-1].add_neighbour(self.boxes[n - 1])

    def throw_in(self, name, length, color=None):
        """
        Method throwing clothes to Pipe
        :param name: Name of clothes
        :param length: Length of clothes
        :param color: Color of clothes
        :type name: str
        :type length: int
        :type color: str
        :return: None
        """


    def fall_out(self):
        """
        Method checking if some clothes fall out of Pipes
        :return: If it is true, return clothes, else return None
        """
