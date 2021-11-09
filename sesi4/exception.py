# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

import sys
# print(sys.platform)
# # kali kondisi terpenuhi gk akan jalan


def os_inter():
    assert ('win32' in sys.platform), "This code runs on win32 only."
    assert ('windows' in sys.platform), "This code runs on Windows only."
    assert ('linux' in sys.platform), "This code runs on Linux only."
    print("do somtin")


# try:
#     os_inter()
#     print('msk ke blog')
# except:
#     print('msk except')
#     pass

# try:
#     os_inter()
# except AssertionError as err:
#     print(err)
#     print('aint excecuted')

# def check_coins(coins):
#     assert(coins > 10), "coinz ferr don"


# coins = 8
# try:
#     check_coins(coins)
# except:
#     raise Exception('some coinz ferr agen')

# try:
#     with open('asd.txt') as file:
#         read_data = file.read()
# except FileNotFoundError as error:
#     print(error)
#     print('Could not open file.log')
# else:
#     print('Executing the else clause.')

try:
    os_inter()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')
