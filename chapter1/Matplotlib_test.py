from PIL import Image
from matplotlib.pylab import *

class Matplotlib_test():
    def __init__(self):
        self.img_test = '../img/1.jpg'

    def pot_line(self):
        im = array(Image.open(self.img_test))
        imshow(im)
        x = [100, 100, 400, 400]
        y = [200, 500, 200, 500]
        plot(x, y, 'b*')
        plot(x[:2], y[:2])
        title('ren a wei')
        show()


if __name__ == '__main__':
    test = Matplotlib_test()
    test.pot_line()
