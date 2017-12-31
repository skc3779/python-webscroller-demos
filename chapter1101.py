from __future__ import print_function
from PIL import Image, ImageFilter

# 필로 라이브러리 테스트
# http://pillow.readthedocs.org

im = Image.open("./files/pencils.jpg")

print(im.format, im.size, im.mode)

blurryKitten = im.filter(ImageFilter.GaussianBlur)
blurryKitten.save("./files/pencils_blurred.jpg")
# blurryKitten.show()