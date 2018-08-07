from wand.image import Image

class Resizer(object):


    def print_size(self, source):
        with Image(filename=source) as img:
            print(img.size)