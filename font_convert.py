from PIL import Image, ImageDraw, ImageFont
import numpy as np

def generate_font_bitmap(chars, font_path='proggy_square/ProggySquare.ttf', size=16):
    bit_list_hex=[]
    for char in chars:
        # 字典存储每个字符的字模
        bitmaps = {}
        # 加载字体
        font = ImageFont.truetype(font_path, size*2)
        
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
        print(bit_list_16) 
        bit_list_16 = [''.join(row) for row in zip(*bit_list_16)]
        # print(bit_list_16)
        # bit_list_8=[]
        # for i in bit_list_16:
        #     first_8_bits = i[:8]
        #     second_8_bits = i[8:]
        #     fir_hex=hex(int(first_8_bits, 2))[2:].zfill(2)
        #     sec_hex=hex(int(second_8_bits, 2))[2:].zfill(2)
        #     bit_list_8.append(fir_hex)
        #     bit_list_8.append(sec_hex)
        
        for i in bit_list_16:
            # row_data=hex(int(i, 2))[2:].zfill(4)
            row_data = hex(int(i, 2))[2:]
            print(row_data)
            bit_list_hex.append(row_data)
    return bit_list_hex
    # return bit_list_8

def image_to_bitmap(img):
    bit_list_hex=[]
    # width, height = img.size
    # 打开图片并转换为灰度模式
    img = img.convert('L')
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
        # print(row_data)
    bit_list_16 = [''.join(row) for row in zip(*bit_list_16)]
    for i in bit_list_16:
        # row_data=hex(int(i, 2))[2:].zfill(4)
        row_data = hex(int(i, 2))[2:]
        # print(row_data)
        bit_list_hex.append(row_data)
    return bit_list_hex
def split_image(img_path):
    bit_list_16=[]
    # 打开图片
    img = Image.open(img_path)
    width, height = img.size
    
    # 检查尺寸是否满足高度为16，宽度为16的倍数
    if height != 16 or width % 16 != 0:
        raise ValueError("图片高度必须为16，宽度必须为16的倍数")
    
    # 计算小图片的数量
    num_splits = width // 16

    # 分割并保存每个16x16的子图片
    for i in range(num_splits):
        # 计算每个子图片的区域 (left, upper, right, lower)
        box = (i * 16, 0, (i + 1) * 16, 16)
        img_chunk = img.crop(box)

        out=image_to_bitmap(img_chunk)
        for out_1 in out:
            bit_list_16.append(out_1)
        # 保存为 PNG 文件，每个文件命名为 "output_<index>.png"
        # img_chunk.save(f"output_{i}.png", "PNG")
    return bit_list_16
if __name__ == '__main__':
    # # 测试输出
    # chars = ""  # 多个字符

    # bit_list_8 = generate_font_bitmap(chars)
    # print(bit_list_8)

    # img_path = '01.png'  # 替换为实际图片路径
    # bit_list_8 = image_to_bitmap(img_path)
    
    bit_list_16=split_image('temp.png')
    print(bit_list_16)


