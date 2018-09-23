from PIL import Image

im=Image.open('../wm.png')
im.rotate(45).show()