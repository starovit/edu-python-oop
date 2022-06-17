import numpy as np
from PIL import Image

class Canvas:
    """
    Creates a canvas for drawing figures
    """
    def __init__(self, height=1000, width=1000, background='white'):
        """
        Args:
            height (int, optional): Defaults to 1000.
            width (int, optional): Defaults to 1000.
            background (str, optional): 'white' or 'black'. Defaults to 'white'.
        """    

        self.height = height
        self.width = width

        matrix = np.zeros([height, width, 3], dtype=np.uint8)
        if background == 'white':
            matrix[:] = [255, 255, 255]
            self.image = matrix
        else:
            matrix[:] = [0, 0, 0]
            self.image = matrix

    def generate(self, filename):
        
        img = Image.fromarray(self.image, 'RGB')
        img.save(f'{filename}.png')

