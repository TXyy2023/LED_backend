binary_string = "0110000001100000"

# 将二进制转换为十六进制
hex_value = hex(int(binary_string, 2))[2:]



print(hex_value.upper())  # 输出大写格式