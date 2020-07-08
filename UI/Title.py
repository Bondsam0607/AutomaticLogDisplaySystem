from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PIL import Image, ImageDraw, ImageFont
import CONF

class title(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        #self.resize(300,400)
        self.layout=QVBoxLayout()
        self.pic = QLabel()
        ttfont = ImageFont.truetype('/System/Library/Fonts/STHeiti Light.ttc',22)
        im = Image.new("RGBA",(300,30))
        draw = ImageDraw.Draw(im)
        draw.text((0,5),CONF.title, fill=(0,0,0),font=ttfont)
        im.save('title.png', 'png')
        self.pic.setPixmap(QPixmap(r"title.png"))
        self.layout.addWidget(self.pic)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = title()
    demo.show()
    sys.exit(app.exec_())