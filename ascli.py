from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('-w','--width',type=int,default=80)
parser.add_argument('-h','--height',type=int,default=80)
args = parser.parse_args()

IMG = args.file
output = args.output
widht = args.width
height = args.height

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((widht,height), Image.NEAREST)

    txt = ""

    for i in range(height):
        for j in range(widht):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    #字符画输出到文件
    # if OUTPUT:
    #     with open(OUTPUT,'w') as f:
    #         f.write(txt)
    # else:
    #     with open("output.txt",'w') as f:
    #         f.write(txt)

