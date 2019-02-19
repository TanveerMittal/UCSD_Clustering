from math import sqrt


def distance(pos1, pos2):
    """Return the Euclidean distance between pos1 and pos2, which are pairs."""
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
