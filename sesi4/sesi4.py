# file = open('Hack8_Sample_Text.txt')

# file.close()

# try:
#     f = open("Hack8_Sample_Text.txt", encoding='utf-8')

# finally:
#     f.close()

# try:
#     with open("Hack8_Sample_Text.txt", 'w', encoding='utf-8') as f:
#         f.write("my first file\n")
#         f.write("This file\n\n")
#         f.write("contains three lines\n")
#         f.write("asdasdasde\n")
#         f.write("assssssle\n\n")
#         f.write("aaaaaaaaaaaas\n")
# finally:
#     f.close()

# f = open("Hack8_Sample_Text.txt", 'a', encoding='utf=8') #append/tambahkan
# f.write("lalalalalalala")

try:
    f = open("Hack8_Saample_Text.txt", 'r', encoding='utf=8')
    # data = f.read(4)
    # print(data)
    # print(f.tell())
    # print(f.read(8))
    # f.seek(0)
    # print(f.read(8))
    # for line in f:
    #     print(line, end=' ')
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())

except:
    print('no file')

finally:
    f.close()
