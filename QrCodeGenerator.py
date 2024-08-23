# Description: This file is used to generate QR code for the given URL or text.


import pyqrcode
import png

from PIL import Image
big_code = pyqrcode.create('https://ajay-krishna00.github.io/YouTube-Clone/', error='M', version=27, mode='binary')
big_code.png('code.png', scale=3, module_color=[0, 0, 0, 128], background=[255, 255, 253])
img=Image.open('code.png')
img.show()

# url = pyqrcode.create('Hello World!')
# url.svg('uca-url.svg', scale=8)               #generates qrcode in terminal
# url.eps('uca-url.eps', scale=2)
# print(url.terminal(quiet_zone=1))

