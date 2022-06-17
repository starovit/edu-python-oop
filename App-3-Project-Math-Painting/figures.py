class Rectangle:
    """
    Rectangle with specified patameters for drawing
    """

    def __init__(self, upleft, RGB, height, width):
        """
        Args:
            upleft (list): list of two integers [x, y]
            RGB (list): list of three integers [R, G, B]
            height (int): 
            width (int): 
        """        

        self.upleft = upleft
        self.RGB = RGB
        self.height = height
        self.width = width

    def draw(self, canvas):        
        canvas.image[self.upleft[0]:self.upleft[0]+self.height,
                    self.upleft[1]:self.upleft[1]+self.width] = self.RGB

class Square():
    """
    Square with specified patameters for drawing
    """

    def __init__(self, upleft, RGB, side):
        """
        Args:
            upleft (list): list of two integers [x, y]
            RGB (list): list of three integers [R, G, B]
            side (int):
        """

        self.upleft = upleft
        self.RGB = RGB
        self.side = side
    
    def draw(self, canvas):
        canvas.image[self.upleft[0]:self.upleft[0]+self.side,
                    self.upleft[1]:self.upleft[1]+self.side] = self.RGB