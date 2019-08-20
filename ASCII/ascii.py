from PIL import Image
import argparse



def get_char(r, g, b, alpha = 256):

    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QL\
                    CJUYXzcvunxrjft/\|()1{}\
                    []?-_+~<>i!lI;:,\"^`'. ")
    # 判断alpha值
    if alpha == 0:
        return ' '

    length = len(ascii_char)
    # 将RGB值转为灰度值gray， 灰度值范围为0-255
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)
    # 进行处理使得灰度值能够映射到指定的字符上
    unit = (256.0 + 1) / length
    # 返回灰度值对应的字符
    return ascii_char[int(gray / unit)]

def main():
    # 首先，构建命令行输入参数处理ArgumentParser实例
    parser = argparse.ArgumentParser()

    # 定义输入文件、输出文件、输出字符画的宽和高
    parser.add_argument('file')  #输入文件
    parser.add_argument('-o', '--output')  #输出文件
    parser.add_argument('--width', type=int, default=80)  #输出字符画宽
    parser.add_argument('--height', type=int, default=80)  #输出字符画高

    # 解析并获取参数
    args = parser.parse_args()
    # 输入的图片文件路径
    IMG = args.file
    # 输出字符画的宽度
    WIDTH = args.width
    # 输出字符画的高度
    HEIGHT = args.height
    # 输出字符画的路径
    OUTPUT = args.output

    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    
    print(txt)

    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)

if __name__ == '__main__':
    main()