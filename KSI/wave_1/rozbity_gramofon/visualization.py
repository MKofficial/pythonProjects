#!/usr/bin/env python3

# Authored by Jakub Stastny, refactored to be general purposed by Ondra Borysek
import math

import pygame as pg
from datetime import datetime
from abc import ABC
# from typing import List
import sys


class DrawableObject(ABC):
    def draw(self, screen):
        pass


class Label(DrawableObject):
    def __init__(self, x, y, text, color=(0, 0, 0), size=16):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.size = size

    def draw(self, screen):
        font = pg.font.Font(pg.font.match_font('Droid Sans Mono'), self.size)
        text_surface = font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        screen.blit(text_surface, text_rect)


class Rectangle(DrawableObject):
    def __init__(self, x, y, color=(0, 0, 0), width=40, height=40, border_width=0):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.border_width = border_width # border width 0 means fill mode

    def draw(self, screen):
        pg.draw.rect(screen,
                     self.color,
                     pg.Rect(self.x, self.y, self.width, self.height),
                     self.border_width)


class Square(Rectangle):
    def __init__(self, x, y, color=(0, 0, 0), size=40, border_width=3):
        super(Square, self).__init__(x, y, color, size, size, border_width)


class Line(DrawableObject):
    def __init__(self, x1, y1, x2, y2, color=(0, 0, 0), width=5):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.width = width

    def draw(self, screen):
        pg.draw.line(screen, self.color, (self.x1, self.y1), (self.x2, self.y2), self.width)


class Arrow(DrawableObject):
    def __init__(self, x1, y1, x2, y2, color=(0, 0, 0), width=5, pointer_size=10):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.width = width
        self.pointer_size = pointer_size

    def draw(self, screen):
        rad = math.pi / 180
        start = (self.x1, self.y1)
        end = (self.x2, self.y2)
        thickness = self.width
        lcolor = self.color
        tricolor = (0, 0, 0)
        trirad = self.pointer_size

        # https://stackoverflow.com/a/56295841
        pg.draw.line(screen, lcolor, start, end, thickness)
        rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi / 2
        pg.draw.polygon(screen, tricolor, ((end[0] + trirad * math.sin(rotation),
                                            end[1] + trirad * math.cos(rotation)),
                                           (end[0] + trirad * math.sin(rotation - 120 * rad),
                                            end[1] + trirad * math.cos(rotation - 120 * rad)),
                                           (end[0] + trirad * math.sin(rotation + 120 * rad),
                                            end[1] + trirad * math.cos(rotation + 120 * rad))))


class Visualization:
    # def __init__(self, states: List[List[DrawableObject]], states_add_music: List[List[str]] = None):
    def __init__(self, states, states_add_music = None):
        self._screen_width = 0
        self._screen_height = 0
        self._cell_size = 0
        self._step = 0
        self._screen = None
        self._autorun = False
        self._speed = 200000

        # self._states: List[List[DrawableObject]] = states
        self._states = states
        # self._states_add_music: List[List[str]] = [[] for _ in range(len(states))]
        self._states_add_music = [[] for _ in range(len(states))]
        if states_add_music:
            self._states_add_music = states_add_music

        self._size_manual_changed = False
        self._window_label = 'KSI Uloha - Rozbity Gramofon'
        self._exit = False

        # self._audio_queue: List[str] = []
        self._audio_queue = []

    def __handle_inputs(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._exit = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    if not self._autorun:
                        self._step = min(
                            self._step + 1, len(self._states) - 1)
                if event.key == pg.K_LEFT:
                    if self._step == 0 or self._autorun:
                        continue
                    self._step -= 1
                if event.key == pg.K_SPACE:
                    self._autorun = not self._autorun
                if event.key == pg.K_PLUS:
                    self._speed *= 0.8
                if event.key == pg.K_MINUS:
                    self._speed /= 0.8
                if event.key == pg.K_s:
                    self._cell_size *= 0.9
                    self._size_manual_changed = True
                if event.key == pg.K_l:
                    self._cell_size /= 0.9
                    self._size_manual_changed = True
            if event.type == pg.VIDEORESIZE:
                self._screen_width = event.w
                self._screen_height = event.h

    def run(self):
        self._pygame_init()
        last_autostep = datetime.now()

        last_drawn_step = -1

        while not self._exit:
            self.__handle_inputs()
            self._play_audio()
            if self._autorun:
                if (datetime.now() - last_autostep).microseconds > self._speed:
                    last_autostep = datetime.now()
                    self._step = min(self._step + 1, len(self._states) - 1)

            if last_drawn_step == self._step:
                continue

            last_drawn_step = self._step
            self._draw()
            pg.display.flip()

    def _draw(self):
        self._screen.fill((255, 255, 255))
        try:
            current_state = self._states[self._step]
            # the following won't work correctly for operation: step back
            new_songs_in_this_step = self._states_add_music[self._step]
            self._audio_queue.extend(new_songs_in_this_step)
        except IndexError:
            print(f"Tried to render step {self._step}, but states only have {len(self._states)} elements.")
            sys.exit(1)
        for single_object in current_state:
            single_object.draw(self._screen)

    def _play_audio(self):
        if len(self._audio_queue) == 0:
            return
        if pg.mixer.music.get_busy():
            return
        next_song = self._audio_queue.pop(0)
        pg.mixer.music.load(next_song)
        pg.mixer.music.play()

    # def add_song(self, path: str):
    def add_song(self, path):
        self._audio_queue.append(path)
        return

    def _pygame_init(self):
        pg.init()

        info_object = pg.display.Info()
        self._screen_width, self._screen_height = (
            info_object.current_w, info_object.current_h)

        self._screen_width = int(0.9 * self._screen_width)
        self._screen_height = int(0.9 * self._screen_height)

        self._cell_size = self._screen_height

        pg.display.set_caption(self._window_label)

        self._screen = pg.display.set_mode(
            (self._screen_width, self._screen_height),  pg.RESIZABLE)


def test_run():
    test1 = Visualization([
        [Square(50, 50)],
        [Square(50, 50), Square(500, 50), Label(40, 50, "test2")],
        [Rectangle(50, 50, color=(0, 255, 0), width=80, height=200, border_width=10)],
        [Label(50, 50, "test3", color=(255, 0, 0), size=50), Line(100, 200, 300, 500)],
        [Arrow(100, 100, 200, 200), Label(500, 50, "test3", color=(255, 0, 0), size=50)]
    ])
    test1.add_song("songs/ACDC-Back-in-black/black3.wav")
    test1.add_song("songs/ACDC-Back-in-black/black5.wav")
    test1.run()


if __name__ == "__main__":
    test_run()