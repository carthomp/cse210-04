class Color():
    """
    Responsibility: Hold RGBA values and return them when needed
    Specifics -
        Store RBGA values as attributes in init method
        Return all 4 as a tuple in separate method
    """
    def __init__(self, red, green, blue, alpha = 255):
        """Constructs a new Color using the specified red, green, blue and alpha values. The alpha 
        value is the color's opacity.
        
        Args:
            red (int): A red value.
            green (int): A green value.
            blue (int): A blue value.
            alpha (int): An alpha or opacity.
        """
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha

    def to_tuple(self):
        """Gets the color as a tuple of four values (red, green, blue, alpha).

        Returns:
            Tuple(int, int, int, int): The color as a tuple.
        """
        return (self._red, self._green, self._blue, self._alpha)