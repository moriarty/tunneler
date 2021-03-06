'''
Copyright 2011 Allan Lavell 
This file is part of Tunneler2.

   Tunneler2 is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   Tunneler2 is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with Tunneler2.  If not, see <http://www.gnu.org/licenses/>.
'''

from pygame.locals import *

NUM_UNITS = 11
PIXELS_PER_UNIT = 29
FPS = 30
TICK_LIMIT = 50

VP_WIDTH = NUM_UNITS * PIXELS_PER_UNIT
VP_HEIGHT = NUM_UNITS * PIXELS_PER_UNIT
SCREEN_WIDTH = VP_WIDTH
HUD_HEIGHT = 80
SCREEN_HEIGHT = VP_HEIGHT + HUD_HEIGHT

LEFT_KEY = K_LEFT
RIGHT_KEY = K_RIGHT
UP_KEY = K_UP
DOWN_KEY = K_DOWN
SHOOT_KEY = K_SPACE

FONT_SIZE = 40
TITLE_FONT_SIZE = 23
