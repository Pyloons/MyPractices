'''
This script can convert a picture to character picture.

Usage:
python3 ascii.py filename [-o|--output] [--width] [--height]
'''
from PIL import Image
import argparse


class ImgToChar():
    '''
    Usage:
    1.New a object
    2.Call draw() method
    '''
    def __init__(self):
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument('file')
        self.parser.add_argument('-o', '--output')
        self.parser.add_argument('--width', type=int, default=50)
        self.parser.add_argument('--height', type=int, default=50)

        self.args = self.parser.parse_args()

        self.IMG = self.args.file
        self.WIDTH = self.args.width
        self.HEIGHT = self.args.height
        self.OUTPUT = self.args.output

    def __get_char(self, r, g, b, alpha=256):
        ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjf"+\
                "t/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

        if alpha == 0:
            return ' '

        length = len(ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        unit = (256.0 + 1) / length
        return ascii_char[int(gray/unit)]

    def draw(self):
        im = Image.open(self.IMG)
        im = im.resize((self.WIDTH, self.HEIGHT), Image.NEAREST)

        txt = ''

        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                txt += self.__get_char(*im.getpixel((j, i)))
            txt += '\n'
        print(txt)
        self.__output_to_file(txt)

    def __output_to_file(self, txt):
        if self.OUTPUT:
            with open(self.OUTPUT, 'w') as f:
                f.write(txt)
        else:
            with open('output.txt', 'w') as f:
                f.write(txt)


if __name__ == '__main__':
    to_char = ImgToChar()
    to_char.draw()
