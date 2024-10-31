binary_str = '00001111'
# 将二进制转换为整数，然后转换为十六进制字符串并去除'0x'前缀
hex_str = hex(int(binary_str, 2))[2:].zfill(2)
print(hex_str)