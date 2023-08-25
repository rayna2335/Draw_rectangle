class Rectangle:
    """Represents rectangle in coordinate plane
        Attributes:
            x (int) - x coordinate
            y (int) - y coordinate
            width - width of a rectangle
            height - height of a rectangle"""

    def __init__(self, w, h):
        """Sets rectangle's height and width. x and y set to 0"""
        self.x = 0
        self.y = 0
    
        self.width = w
        self.height = h

    def get_coords(self):
        """Returns the x and y value as a pair"""
        return (self.x, self.y)

    def get_width(self):
        """Returns the rectangle's width"""
        return self.width
        
    def get_height(self):
        """Returns the rectangle's height"""
        return self.height

    def move_up(self):
        """Moves the rectangle up one row"""
        self.y -= 1

    def move_down(self):
        """Moves the rectangle down one row"""
        self.y += 1

    def move_left(self):
        """Moves the rectangle left one column"""
        self.x -= 1

    def move_right(self):
        """Moves the rectangle right one column"""
        self.x += 1
        

