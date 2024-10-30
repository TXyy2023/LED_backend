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
chars = "刘永洋"  # 多个字符
bitmaps = generate_font_bitmap(chars)
for char, bitmap in bitmaps.items():
    print(f"Character: {char}")
    for row in bitmap:
        print(''.join(['1' if pixel else '0' for pixel in row]))
    print("\n")