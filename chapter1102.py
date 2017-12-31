# Create JPEG thumbnails 생성기
# pillow 는 이미지관련 다양한 기능을 제공한다.
# https://pillow.readthedocs.io

from __future__ import print_function
import os, sys
from PIL import Image

size = (128, 128)

# argv 에 파일경로를 제공한다.
for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail.jpg"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for", infile)

# command execute
# $>python chapter1102.py ./file/pencils.jpg
