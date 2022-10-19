from pygame import Color
from pygame.math import Vector2

# window
TITLE = "Norder"
WIDTH = 500
HEIGHT = 500
FPS = 60
BG_COLOR = (119, 158, 203)

# particle constants
P_RECT_SIZE = Vector2(100, 100)
P_HALF_RECT_SIZE = 0.5 * P_RECT_SIZE
P_COUNT_X = int(WIDTH / P_RECT_SIZE.x)
P_COUNT_Y = int(HEIGHT / P_RECT_SIZE.y)

P_SELECTED_COLOR = (0, 0, 0)
P_SELECTED_RADIUS = 8

P_RADIUS = 20
P_INIT_VALUE_LOW = 0
P_ABS_HIGH_VALUE = 150

P_CON_MIN_RADIUS = P_RADIUS + 2
P_CON_MAX_RADIUS = P_RADIUS + 100
P_CON_WIDTH = 2


# particle functions
def getParticleConnectionRadius(dValue):
    return max(P_CON_MIN_RADIUS, min(P_CON_MAX_RADIUS, P_RADIUS + (0.03 * abs(dValue))))


def getParticleIndex(x, y):
    return int(x / P_RECT_SIZE.x) * P_COUNT_X + int(y / P_RECT_SIZE.y)


def getParticleColor(value):
    hue = int(value) % 360
    color = Color(100, 100, 100)
    color.hsva = (hue, 100, 100, 100)
    return color
