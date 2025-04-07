
# second = False
#
# if not second:
#     print ("hello!")
# if 56<481.15:
#     print ("correct!")

# def my_funct():
#     return False
#
# if True:
#     print ("yep")
# else:
#     print ("c\'mon, man")

# my_val = 15
#
# if my_val == 14:
#     print ("yep")
# elif my_val == 15:
#     some = my_val+16
# elif True:
#     pass
# else:
#     print ("c\'mon, man")
#
# print (some)

# x = 1

# while x != 10:
#     print ("hello!")
#     x += 1

# x = 1
#
# while True:
#     print ('hello')
#     x += 1
#     if x == 5:
#         continue

# set1 = {'hgjahsg','1231','ghsd5gds'}
#
# set2 = frozenset(set1)
# print (type(set2 ))

# for integer in range(1,10):
#     print(integer)
#     if integer == 2:
#         break
#     elif integer == 5:
#         continue

# integer = 'Text'
#
# for i in integer:
#     print(i)

# needed_number = input("введіть число")
# print (needed_number)

# def funct_w_args1 (name = "Sergii"):
#     fullname1 = name +" "+ "Mykolayovich"
#     return fullname1
#
# def name_updated (fullname):
#     changed_name = fullname.upper()
#     return changed_name
#
#
# fullname_1 = funct_w_args1()
#
# print(name_updated(funct_w_args1()))

# def funct_w_args1 (**sdasd):
#     for key, value in sdasd.items():
#         print (key*2, value*3)
#
# funct_w_args1(name = 2, surname = "s", age = 435, floasadt_ones = 2.3)

# my_string1 = "my short string"
# print(len(my_string1))
# print(my_string1[14:0:-1])
# print(type(my_string1[14:0:-1]))

my_list = [1, 2.4, 25]

result_for_inline_1 = [i*2 for i in my_list]
print(result_for_inline_1)

result_for_inline_1 = [i*2 for i in my_list]
print(result_for_inline_1)

#
def git_example1 ():
    for i in []:
        return "yay"
print(git_example1())