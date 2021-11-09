import math  # buat pembulatan keatas


def Kelvin(val, input):
    if(input == "K"):
        return math.ceil(val + 273.15)  # celcius to kelvin
    elif(input == "C"):
        return math.ceil(val - 273.15)  # kelvin to celcius


def inputToFarenheit(val, input):  # fungsi input ke faren
    if(input == "C"):  # dari c ke farenheit (udh bnr)
        return math.ceil(9/5 * val + 32)
    elif(input == "K"):  # dari K ke faren (udh bnr)
        return math.ceil(9/5 * (val - 273) + 32)


def farenheitToInput(val, input):  # fungsi faren ke input
    if(input == "C"):  # dari farenheit ke C (udh bnr)
        return math.ceil((val - 32) * 5/9)
    elif(input == "K"):  # dari faren ke K (udh bnr)
        return math.ceil((val + 459.67) * 5/9)


# biar gk nulis ulang
c = "C"
k = "K"

print("input angka yang mau dikonversi")
x = int(input())  # input user dikonversi ke int
# output dari masing-masing function
print("hasil konversi")
print("celcius to kelvin")
print(Kelvin(x, k))
print("kelvin to celcius")
print(Kelvin(x, c))
# parameter ke 2 ini buat nentuin dikonversi kemana
print("farenheit to celcius")
print(farenheitToInput(x, c))
print("farenheit to kelvin")
print(farenheitToInput(x, k))
print("celcius to farenheit")
print(inputToFarenheit(x, c))
print("kelvin to farenheit")
print(inputToFarenheit(x, k))
