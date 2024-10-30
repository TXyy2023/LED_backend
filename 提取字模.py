from PIL import Image, ImageDraw, ImageFont
import numpy as np

def generate_font_bitmap(chars, font_path='苹方黑体-中粗-简.ttf', size=16):
    # 字典存储每个字符的字模
    bitmaps = {}
    
    # 加载字体
    font = ImageFont.truetype(font_path, size)

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
    
    return bitmaps

# 测试输出
chars = "A"  # 多个字符
bitmaps = generate_font_bitmap(chars)
# print(bitmaps)
bit_list_16=[]
for char, bitmap in bitmaps.items():
    print(f"Character: {char}")
    for row in bitmap:
        row_data=''.join(['1' if pixel else '0' for pixel in row])
        # print(row_data)
        bit_list_16.append(row_data)
    #     print(''.join(['1' if pixel else '0' for pixel in row]))
    # print("\n")
print(bit_list_16)
bit_list_8=[]
for i in bit_list_16:
    first_8_bits = i[:8]
    second_8_bits = i[8:]
    bit_list_8.append(first_8_bits)
    bit_list_8.append(second_8_bits)
print(bit_list_8)

