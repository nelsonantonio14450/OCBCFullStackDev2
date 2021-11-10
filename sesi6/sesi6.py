# def my_generator():
#     print("Inside my generator")
#     yield 'a'
#     yield 'b'
#     yield 'c'


# for char in my_generator():
#     print(char)


# def counter_generator(low, high):
#     while low <= high:
#         yield low  # return tapi gk lgsg terminate
#         low += 1


# for i in counter_generator(5, 10):
#     print(i, end=' ')

# x = counter_generator(5, 10)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# def say_hello(name):
#     return f"Hello {name}"


# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"


# def wether(name):
#     return f"Test, {name}"


# def greet_bob(greeter_func, name):
#     return greeter_func(name)


# print(greet_bob(wether, "bobz"))

# def parent(): #gbs manggil fungsi didalam fungsi, mesti jadii class baru bs
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")

#     def second_child():
#         print("Printing from the second_child() function")

#     second_child()
#     first_child()

# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"

#     def second_child():
#         return "Call me Liam"

#     if num == 1:
#         return first_child
#     else:
#         return second_child


# p = parent(1)
# print(p())


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper


# @my_decorator
# def say_whee():
#     print("Whee!")


# # say_whee = my_decorator(say_whee) #kalo udh ada @ diatas say_whee, udh gk perlu pke ini lagi
# print(say_whee())


class Asd():
    name = "timmy"


class Bsd():
    name = "bsd"


class Asd(Bsd):
    pass


# A()
bsd = Asd()
print(bsd.name)

Bsd = True
print(Bsd)
