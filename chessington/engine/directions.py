from enum import Enum
class Directions:
    Cardinals = {
        "NORTH": {"row": 1, "col": 0},
        "EAST": {"row": 0, "col": 1},
        "SOUTH": {"row": -1, "col": 0},
        "WEST": {"row": 0, "col": -1}
    }

    KnightDirections = {
        "NORTH_LEFT": {"row": 2, "col": -1},
        "NORTH_RIGHT": {"row": 2, "col": 1},
        "SOUTH_LEFT": {"row": -2, "col": -1},
        "SOUTH_RIGHT": {"row": -2, "col": 1},
        "EAST_LEFT": {"row": 1, "col": 2},
        "EAST_RIGHT": {"row": -1, "col": 2},
        "WEST_LEFT": {"row": -1, "col": -2},
        "WEST_RIGHT": {"row": 1, "col": -2}
    }

    Corners = {
        "NORTH_WEST": {"row": 1, "col": -1},
        "NORTH_EAST": {"row": 1, "col": 1},
        "SOUTH_WEST": {"row": -1, "col": -1},
        "SOUTH_EAST": {"row": -1, "col": 1},
    }

