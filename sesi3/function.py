# def printme(nama, age=18):
#     print('nama: ', nama)
#     print('age: ', age)
#     return


# printme("adasdadasda", 30)
# printme(age=30, nama="adasdadasda")
# printme("asdasd")


# def buy(customer_name, *items):  # bintang bwt kalo gk tau brp byk datanya
#     print(customer_name)
#     print(items)


# buy('asdasdasd', 'choco', 'greentea', 'kuussss')


# def my_func(p, l):
#     print(p*l)


# def printme(str_input):
#     print(str_input)


# my_func(5, 4)
# printme("testtt")


# def changeme(mylist):
#     mylist = mylist+[1, 2, 3, 4]
#     print(mylist)
#     return mylist


# mylist = [10, 20, 30]
# print(mylist)
# mylist = changeme(mylist)
# print(mylist)

# printme(True)


# def calculate_rect(length, width):
#     print('Area: ', length*width)


# calculate_rect(100, 10)


# def printinfo(args, *vartuple):  # *args (tuple)
#     print(args)
#     print(type(vartuple))
#     for var in vartuple:
#         print(var)


# def printinfodict(args, **vartuple):  # **kwargs (dict)
#     print(args)
#     print(type(vartuple))
#     for key, value in vartuple.items():  # loop key dan valuenya, keluar pair of key and value
#         print(key, " ", value)

#     for key in vartuple.keys():  # loop key
#         print(key)

#     for value in vartuple.values():  # loop valuenya
#         print(value)


# printinfo(70, 60, 50, "asd")

# printinfodict(70, test=60, test1=50, test3="asd")

# def calcu_rect_area(length, width): return length * width

# print(calcu_rect_area(10, 20))

from pkg.book import printin as p
import pkg.book as book
book.printin()
p()
