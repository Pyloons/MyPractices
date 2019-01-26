from PIL import Image
import math, os, string, hashlib, time


class VectorCompare:
    def magnitude(self, concordance):
        total = 0
        for word, count in concordance.iteritems():
            total += count ** 2
        return math.sqrt(total)

    def relation(self, concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.iteritems():
            if concordance2.has_key(word):
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


class CrackCaptcha(object):
    def __init__(self, fp):
        self.im = Image.open(fp)
        self.im.convert("P")
        self.im2 = Image.new("P", self.im.size, 255)
        self.v = VectorCompare()

    def cut_single_number(self):
        inletter = False
        foundletter = False
        start = 0
        end = 0

        letters = []

        '''
        y is width, x is height.
        these code find every number where start and end.
        '''
        for y in range(self.im2.size[0]):
            for x in range(self.im2.size[1]):
                pix = self.im2.getpixel((y,x))
                if pix !=255:
                    inletter = True
            if foundletter == False and inletter == True:
                foundletter = True
                start = y

            if foundletter == True and inletter == False:
                foundletter = False
                end = y
                letters.append((start, end))
            inletter = False
        return letters

    def convert_two_color(self, pixes=[] fp=None):
        for x in range(self.im.size[1]):
            for y in range(self.im.size[0]):
                pix = self.im.getpixel((y, x))
                if pix in pixes:
                    self.im2.putpixel((y,x),0)
        if fp != None:
            self.im2.save(fp + ".gif")
        self.im2.show()

    def find_most_color(self):
        '''
        find feature color in human eye
        '''
        his = self.im.histogram()
        values = {}

        for i in range(256):
            values[i] = his[i]

        for j,k in sorted(values.items(), key=lambda x:x[1], reverse=True)[:10]:
            print j,k

    def buildvector(self, im):
        d1 = {}
        count = 0
        for i in im.getdata():
            d1[count] = i
            count += 1
        return d1

    def train(self):
        iconset = [i for i in (string.digits + string.ascii_lowercase)]
        imageset = []
        for letter in iconset:
            for img in os.listdir('./iconset/%s/'%(letter)):
                temp = []
                if img != "Thumbs.db" and img != ".DS_Store":
                    t_img = Image.open("./iconset/%s/%s"%(letter,img))
                    temp.append(self.buildvector(t_img))
                imageset.append({letter:temp})
        return imageset

    def cut_captcha(self, letters, imageset, build_pic=False):
        count = 0
        for letter in letters:
            m = hashlib.md5()
            im3 = self.im2.crop((letter[0], 0, letter[1], self.im2.size[1]))
            if build_pic:
                m.update("%s%s"%(time.time(),count))
                im3.save("./%s.gif"%(m.hexdigest()))

            guess = []

            for image in imageset:
                for x,y in image.iteritems():
                    if len(y) != 0:
                        guess.append((self.v.relation(y[0], self.buildvector(im3)),x))
            guess.sort(reverse=True)
            print "",guess[0]

            count += 1


    def run(self, make_img=False):
        self.convert_two_color([220, 227])
        letters = self.cut_single_number()
        imageset = self.train()
        self.cut_captcha(letters,imageset,make_img)


if __name__ == '__main__':
    cc = CrackCaptcha("captcha.gif")
    cc.run()

