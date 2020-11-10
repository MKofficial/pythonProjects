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
        self.length = n  # get a length of pipe
        self.segments = [Segment() for i in range(n)]  # store all segments in one pipe

        # check if segments in pipe can have neighbours
        if len(self.segments) > 1:
            # for each segments set its neighbours
            for i in range(len(self.segments)):
                # set neighbour for the first segment
                if i == 0:
                    self.segments[0].add_neighbour(self.segments[1])
                    self.segments[0].next = self.segments[1]
                # set neighbour for the last segment
                elif i == len(self.segments) - 1:
                    self.segments[-1].add_neighbour(self.segments[-2])
                    self.segments[-1].next = None
                else:
                    self.segments[i].add_neighbour(self.segments[i - 1])
                    self.segments[i].add_neighbour(self.segments[i + 1])
                    self.segments[i].next = self.segments[i + 1]
        else:
            self.segments[0].next = None

    def get_length(self):
        """
        Getter
        :return: Length of pipe
        """
        return self.pipe_length

    def attach(self, n, other_pipe):
        """
        Method attaching one pipe to another
        :param n: Index of box in bottom pipe on which other_pipe will be connected
        :param other_pipe: A Pipe which will be connected
        :type n: int
        :type other_pipe: Pipe
        :return: None
        """
        other_pipe.segments[-1].next = self.segments[n - 1]
        other_pipe.segments[-1].add_neighbour(self.segments[n - 1])
        self.segments[n - 1].add_neighbour(other_pipe.segments[-1])

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
