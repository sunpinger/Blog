# base = input("请输入要转换的字符串：")
# by = bytes(base, 'GBK')  # 先将输入的字符串转化成字节码
# hexstring = by.hex()  # 得到16进制字符串，不带0x
# print(hexstring)
# a = int(hexstring,16)
# print(a)
# # 输出如下：
# # 请输入要转换的字符串：大多数
# # e5a4a7e5a49ae695b0
# # 02795d1fb4ac3b246a01ab46c634475c
import binascii

hex_str = '02795d1fb4ac3b246a01ab46c634475c' # thank you very much!
hexs = hex_str.encode('utf-8')
hexs = '02795d1fb4ac3b246a01ab46c634475c'
str_bin = binascii.unhexlify(hexs)
strs = str_bin.decode('UTF-8')
print(strs)
