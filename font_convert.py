from PIL import Image, ImageDraw, ImageFont
import numpy as np

def generate_font_bitmap(chars, font_path='proggy_square/ProggySquare.ttf', size=16):
    # 字典存储每个字符的字模
    bitmaps = {}
    # 加载字体
    font = ImageFont.truetype(font_path, size*2)
    for char in chars:
        # 创建空白图片
        img = Image.new('1', (size, size), color=0)
        draw = ImageDraw.Draw(img)
        
        # 获取字符大小，并在中心绘制字符
        bbox = draw.textbbox((0, 0), char, font=font)
        width, height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        position = ((size - width) // 2, (size - height) // 2)
        draw.text(position, char, font=font, fill=1)
        
        # 转换为二进制数组并存储
        bitmap = np.array(img)
        bitmaps[char] = bitmap
    # print(bitmap)
    bit_list_16=[]
    for char, bitmap in bitmaps.items():
        print(f"Character: {char}")
        for row in bitmap:
            row_data=''.join(['1' if pixel else '0' for pixel in row])
            # print(row_data)
            bit_list_16.append(row_data)
            print(''.join(['1' if pixel else '0' for pixel in row]))
        # print("\n")
   
    bit_list_16 = [''.join(row) for row in zip(*bit_list_16)]
    print(bit_list_16)
    # bit_list_8=[]
    # for i in bit_list_16:
    #     first_8_bits = i[:8]
    #     second_8_bits = i[8:]
    #     fir_hex=hex(int(first_8_bits, 2))[2:].zfill(2)
    #     sec_hex=hex(int(second_8_bits, 2))[2:].zfill(2)
    #     bit_list_8.append(fir_hex)
    #     bit_list_8.append(sec_hex)
    bit_list_hex=[]
    for i in bit_list_16:
        # row_data=hex(int(i, 2))[2:].zfill(4)
        row_data = hex(int(i, 2))[2:]
        print(row_data)
        bit_list_hex.append(row_data)
    return row_data
    # return bit_list_8

def image_to_bitmap(img_path, size=(16, 16)):
    # 打开图片并转换为灰度模式
    img = Image.open(img_path).convert('L')
    # 调整图片大小
    img = img.resize(size)
    # 将图片转换为二值化（黑白）模式
    threshold = 128
    img = img.point(lambda x: 0 if x > threshold else 1, mode='1')
    # 转换为 numpy 数组
    bitmap = np.array(img)
    
    # 打印字模
    bit_list_16 = []
    for row in bitmap:
        row_data = ''.join(['1' if pixel else '0' for pixel in row])
        bit_list_16.append(row_data)
        print(row_data)
    bit_list_16 = [''.join(row) for row in zip(*bit_list_16)]
    # 将16位二进制转为8位的两个十六进制数
    bit_list_8 = []
    for row in bit_list_16:
        first_8_bits = row[:8]
        second_8_bits = row[8:]
        fir_hex = hex(int(first_8_bits, 2))[2:].zfill(2)
        sec_hex = hex(int(second_8_bits, 2))[2:].zfill(2)
        bit_list_8.append(fir_hex)
        bit_list_8.append(sec_hex)

    return bit_list_8
if __name__ == '__main__':
    # 测试输出
    chars = "A"  # 多个字符
    bit_list_8 = generate_font_bitmap(chars)
    print(bit_list_8)

    # img_path = '01.png'  # 替换为实际图片路径
    # bit_list_8 = image_to_bitmap(img_path)
    # print("Bitmap 字模数据：")
    # print(bit_list_8)

