#!/usr/bin/env python3

import pygame as pg
from datetime import datetime
import os


class Visualization:
    def __init__(self, states):
        self._screen_width = 0
        self._screen_height = 0
        self._cell_size = 0
        self._finish = None
        self._step = 0
        self._screen = None
        self._autorun = False
        self._speed = 200000
        self._states = states
        self._size_manual_changed = False

    def run(self):
        self._pygame_init()
        exit = False
        last_autostep = datetime.now()
        while not exit:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit = True
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

            if self._autorun:
                if (datetime.now() - last_autostep).microseconds > self._speed:
                    last_autostep = datetime.now()
                    self._step = min(self._step + 1, len(self._states) - 1)
            self._draw()
            pg.display.flip()

    def _get_levels_count(self):
        res = -1
        for seg in self._states[self._step]:
            level = seg[3]
            res = max(level, res)
        return res

    def _draw_text(self, text, size, position, color):
        font = pg.font.Font(pg.font.match_font('Droid Sans Mono'), size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (position[0], position[1] - 20)
        self._screen.blit(text_surface, text_rect)

    def _drawTree(self, y_pos, root=0, left=0, right=1, parent_x=-1, parent_y=-1):
        if not self._size_manual_changed and y_pos - self._cell_size // 2 < 20:
            self._cell_size *= 0.9
            return
        if len(self._states[self._step]) == 0:
            return
        content, color, neighbours, lvl = self._states[self._step][root]
        x_pos = int(self._screen_width * ((right + left) / 2)) - \
            self._cell_size // 2
        pg.draw.rect(self._screen, (0, 0, 0), pg.Rect(
            x_pos, y_pos, self._cell_size, self._cell_size), 3)
        pg.draw.rect(self._screen, color, pg.Rect(
            x_pos, y_pos, self._cell_size, self._cell_size))
        self._draw_text(content, 16, (x_pos + self._cell_size //
                                      2, y_pos + self._cell_size // 2), (0, 0, 0))
        if parent_x != -1 and parent_y != -1:
            pg.draw.line(self._screen, (0, 0, 0), (x_pos + self._cell_size // 2, y_pos +
                                                   self._cell_size), (parent_x + self._cell_size // 2, parent_y))
        for i in range(len(neighbours)):
            step = (right - left) / len(neighbours)
            newLeft = left + i * step
            newRight = left + (i + 1) * step
            newYPos = y_pos - \
                self._cell_size if len(
                    neighbours) == 1 else y_pos - int(2.5 * self._cell_size)
            self._drawTree(
                newYPos, neighbours[i], newLeft, newRight, x_pos, y_pos)

    def _draw(self):
        self._screen.fill((255, 255, 255))
        maxDeep = self._get_levels_count()
        self._drawTree(self._screen_height - 2 * self._cell_size)

    def _pygame_init(self):
        pg.init()
        infoObject = pg.display.Info()
        self._screen_width, self._screen_height = (
            infoObject.current_w, infoObject.current_h)
        self._screen_height = int(0.9 * self._screen_height)
        self._cell_size = self._screen_height
        pg.display.set_caption("KSI pipes")
        self._screen = pg.display.set_mode(
            (self._screen_width, self._screen_height),  pg.RESIZABLE)
