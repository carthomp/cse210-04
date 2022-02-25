import pyray
from Greed.Common.point import Point


class KeyboardService():
    """
    Responsibility: Gather and return user input from the keyboard
    Specifics -
        Get a direction from the currently pressed key
    """

    def __init__(self, cell_size=1):
        """Constructs a new KeyboardService using the specified cell size.

        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1

        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)

        return direction
