# 例子二进制字符串
binary_str = '10000000'

# 1. 将二进制字符串转换为整数
decimal_value = int(binary_str, 2)

# 2. 使用 hex() 将整数转换为16进制字符串
hex_value = hex(decimal_value)  # [2:] 去掉 '0x' 前缀

print(hex_value)