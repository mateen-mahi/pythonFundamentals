# input1,input2,input3 = input("write Your three numbers").split(',')
# final_input = int(input1) + int(input2) + int(input3)
# print("Your result is " + str(final_input))
# x = input('Enter Your Value here: ')
# x=int(x)
# if x < 14:
#     print("underage")
# else:
#     print("ok you Can Play")

# name = 'Mateen'
# age=22
# if name[0]=='M' or name[0]=='S' and age>=22:
#     print('you can Watch Movie')
# else:
#     print('you can not watch this video ')



# numbers = input('Choose a number: ')
# total = 0
# i = 0
# while i <len(numbers):
#     total += int(numbers[i])
#     i += 1
# print(total)


# numbers = input('Plz Write your Name: ')
# total = 0
# i = 0
# while i <len(numbers):
#     print(f"{numbers[i]} : {numbers.count(numbers[i])}")
#     i += 1



# import random

# random_num = random.randint(1, 100)
# game_over = False
# guesses = 1
# user_guess = int(input("Enter a number between 1 to 100: "))

# while not game_over:
#     if user_guess == random_num:
#         print(f"You win in {guesses} tries!")
#         print(f"The random number was {random_num}.")
#         game_over = True 
#     elif user_guess < random_num:
#         print("Too low!")
#         guesses += 1
#         user_guess = int(input("Guess again: "))
#     else:
#         print("Too high!")
#         guesses += 1
#         user_guess = int(input("Guess again: "))


# def hello_func(num1,num2):
#     print(num1+num2)


# hello_func(20,30)



# Delete and Add In List 
# Insert extend append
# del pop remove

# name=input("Write Your Name: ")
# age=input("Write Your Age: ")
# input_val=input("Write Your Values: ").split(',')
# User={}
# User['name']=name
# User['age']=age
# User['fav songs']= input_val

# for Use,val in User.items():
#     print(f"{Use}:{val}")



# list_m = list(range(1,11))
# even = []
# odd = []
# for i in list_m:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)


# we can create this in a short way odd|Even
# odd = [number for number in range(1,11) if number%2 != 0]
# even = [number for number in range(1,11) if number%2 == 0]
# print(odd)
# print(even)
# Togather

# list_b = [2,4,6,8,33,5,6,7]
# odd_even = [number if number % 2 == 0 else -number for number in list_b]

# print(odd_even)


# Nested List with comprehensive 
# nested_comprehensive = [[i for i in range(1,4)] for j in range(1,4)]
# print(nested_comprehensive)


#Dictionary Comprehensive

# user = 'Mateen'
# Dict = {char : user.count(char) for char in user}
# print(Dict)

# dictionary = {num :('odd' if num%2 != 0 else 'even') for num in range(1,11)}
# print(dictionary)



#Set Comprehensive
# users = ['Mateen', "Usman" , "khan"]
# first_word = {user[0] for user in users}
# print(first_word)


# *args

# def arg_func(num,*args):
#     total =1 
#     for arg in args:
#            total *= arg
#     return num + total
# print(arg_func(3,1,3,5))          

# def arg_func(num,*args):
#     if args:
#         return[i**num for i in args]
#     else:
#         return "You should Pass The Value"
# print(arg_func(3, *[2,3]))


# def func(li, **kwargs):
#     if kwargs.get('reverse_string'):
#          return [name[::-1].title() for name in li]
#     else:
#          return [name.title() for name in li]

# names = ["mateen", 'harshit', 'ajay']
# print(func(names))





#lambda Expression
# func =  lambda s : True if len(s) > 5 else False 
# print(func([1,2,3,4,5,]))
#Short Way To do this
# func =  lambda s : len(s) > 5
# print(func([1,2,3,4,5,6]))



# enamurate Function 
# names = ['Mateen','Mahi','Usman','Khan']
# for post,name in enumerate(names):
#     print(f"{post} is position of {name}")


#Map Function
# numbers = [1,2,3,4]
# squares = list(map(lambda a:a**2, numbers))
# print(squares)
# 2nd way to do this
# list_squ = [a**2 for a in numbers]
# print(list_squ)
#Same thing With Normal way
# def squares(a):
#     return a**2
# new_list = []
# for a in numbers:
#     new_list.append(squares(a)) 
# print(new_list)



#filter Method
# number = [1,2,3,4,5,6,7,8,9,10]
# even = list(filter(lambda a:a%2==0 , number))
# print(even)
#same with List Comprehension 
# li = [a for a in number if a%2==0]
# print(li)

# names =['mateen','Harshit','mohit']
# user_identity = ["user1","user2",]
# # user_identity = ["","user1",]

# output = zip(names,user_identity)
# print(list(output))

# reverse_zip = [('mateen', 'user1'), ('Harshit', 'user2')]
# for unzip in reverse_zip:
#     print(list(unzip))

# Here are some examples of iterables in Python:

# Lists
# Tuples
# Strings
# Sets
# Generators
# Here are some examples of iterators in Python:

# Iterators created by the iter() function
# Generator objects
# Iterators are often used in Python for efficiency reasons. When you iterate over an iterable object, Python creates an iterator object behind the scenes. The iterator object then keeps track of the current position in the iterable object and returns the next item in the iterable object each time the next() method is called. This allows Python to avoid repeatedly iterating over the entire iterable object each time the for loop is executed. 




# all and any function 
# even = [2,4,6,8,10]
# odd = [1,3,8,5,7,9]
# result_1 = any([i % 2 == 0 for i in odd])
# result_2 = all([i % 2 == 0 for i in even])
# print(result_1)
# print(result_2)
# def func(*args):
#     if all([(type(arg)==int or type(arg)==float or type(arg)==args) for arg in args]):
#         total=0
#         for num in args:
#             total +=num
#         return total 
#     else:
#         return 'Plz enter correct values'
# print(func(1,2,3))


# def func (a,b):
#     '''this is our doc string'''
#     return a+b 

# print(func.__doc__)

# def func(a):
#     return a**2
# l = [1,2,3,4,5,6]
# #print(list(map(func,l)))
# def func_inside(infunc , l):
#    return (infunc(i) for i in l)
       
# print(list(func_inside(func, l)))



#Decorator is a function that enhance the functionality of other function
# from functools import wraps
# import time
# def decorator_function(any_func):
#     @wraps(any_func)
#     def inner_func(*args,**kwargs):
#         print(f'this is {any_func.__name__} function')
#         print(f"{any_func.__doc__}")
#         t1 = time.time()
#         return_value =  any_func(*args,**kwargs)
#         t2 = time.time()
#         runtime = t2 - t1
#         print(f"Runing time is {runtime}")
#         return return_value
#     return inner_func

# @decorator_function
# def func1(a,b):
#     '''This is doc string of func1 that add two values'''
#     return a+b


# print(func1(7,5))





#Generator 
# def even_gen(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             yield i


# for num in even_gen(10):
#     print(num)

    #List Comprehension and Generator Comprehension Both are 99% Same The 
    #difference is we use parentheses in Generator instead of Square Brackets 



#Object Oriented Programming 


# class Laptop:
#     count = 0
#     discount = 50
#     def __init__(self,model_name,price,processer):
#         print("Init Method has called")
#         Laptop.count +=1
#         #instance variable
#         self.model = model_name
#         self.price = price
#         self.processer = processer

#     @classmethod 
#     def count_instances(cls):
#        return f"you have called Init mothod {cls.count} times od {cls.__name__} class "


#     def apply_discount(self):
#             off_price = (self.discount/100)*self.price
#             return  self.price - off_price

# p1 = Laptop('Dell' , 44000 ,"intel")
# print(p1.apply_discount())
# print(Laptop.count_instances())
# print(p1.__dict__)


# def division(a,b):
#     try:
#             return a/b
#     except ZeroDivisionError:
#         print("plz don't divide with zero")
#     except:
#         print("unexpected Error")
#     finally:
#         print("finally block")

# print(division(4,2))


# import pdb
# pdb.set_trace()
# # To check our line we can write l and to exicute our line we can use command "n" to stop "c"

# #Text Files
# f = open('file.txt')
# print(f" Cursor position {f.tell()}")
# # we use  f.seek(0) to change cursor's position 
# print(f.read())
# print(f" Cursor position {f.tell()}")
# #print(f.readline(),end='') for reading a line  
#f.readlines() to get a list with all line's String
# #we should write f.close() at the end where we want to finish our reading
#print(f.name)
#print(f.closed)

#Context Manager
# with open("file.txt") as f:
#     data = f.read()
#     print(data)

    # to write we use W r+ a
# W will delete previous data 
# a will not delete previous data
# with open("file.txt" , "w") as f:
#     f.write('hello') #we can write \n in last to append many times


# with open('index.html','r') as webpage:
#     with open('output.txt','a') as wf:
#         for line in webpage.readlines():
#             if '<a href=' in line:
#                 pos = line.find('<a href=')
#                 first_quotation = line.find('\"',pos)
#                 second_quotation = line.find('\"',first_quotation+1)
#                 url = line[first_quotation+1:second_quotation]
#                 wf.write(url + '\n')

# #To read CSV Files
# from csv import reader
# with open('file.csv','r') as f:
#     csv_filereader = reader(f)
#     #to skip first line we can use next(csv_reader)
#     for row in csv_filereader:
#         print(row)
# to read csv with dict
# from csv import DictReader
# with open('file.csv','r') as f:
#     csv_dictreader = DictReader(f ,delimiter=',')
#     for line in csv_dictreader:
#         print(line['name'])#or whatever we want to access  


# to write in csv file
# from csv import writer
# with open('file.csv','w',newline='') as f:
#     csv_writer = writer(f)
#     # csv_writer.writerow(['name','country'])
#     # csv_writer.writerow(['Mateen','Pakistan'])
#     # csv_writer.writerow(['Leila','Tanzania'])
#     csv_writer.writerows([['name','country'],['Leila','Tanzania'],['Mateen','Pakistan'],])


#to write csv with dictwriter
# from csv import DictWriter
# with open('dict.csv','w',newline='') as f:
#     csv_writer = DictWriter(f,fieldnames=['FirstName','LastName','age'])
#     csv_writer.writeheader()        
#     # csv_writer.writerow(
#     #     {
#     #      'FirstName':'Mateen',
#     #      'LastName':'Mahi',
#     #      'age':22   
#     #     }
#     # )
#     # csv_writer.writerow(
#     #     {
#     #      'FirstName':'jennifer',
#     #      'LastName':'lopez',
#     #      'age':52   
#     #     }
#     # )
#     csv_writer.writerows([
#                 {
#          'FirstName':'jennifer',
#          'LastName':'lopez',
#          'age':52   
#         },
#                 {
#          'FirstName':'Mateen',
#          'LastName':'Mahi',
#          'age':22   
#         },
#                 {
#          'FirstName':'Ariana',
#          'LastName':'Grande',
#          'age':25   
#         }
        
#     ])



#both reading and writing in csv files
# from csv import DictReader,DictWriter
# with open('dict.csv','r') as rf:
#     with open('newfile.csv','w' , newline='') as wf:
#         csv_writer = DictWriter(wf,fieldnames=['first_name','last_name','age'])
#         csv_writer.writeheader()
#         for line in DictReader(rf):
#             f_name,l_name,age = line['FirstName'],line['LastName'],line['age']
#             csv_writer.writerow({
#                 'first_name':f_name.upper(),
#                 'last_name':l_name.upper(),
#                 'age':age.upper(),
#             })



import os

# os.getcwd()
# os.chdir(r'F:\stuff')
# print(os.getcwd())
# os.mkdir('movies')
# print(os.path.exists('movies'))
# if os.path.exists('movies'):
#     print('already exists')
# else:
#     os.mkdir('movies')

# open('file.txt','a').close()
# os.mkdir(r'F:\stuff\movies')

# for item in os.listdir(r'F:\stuff'):
#     path = os.path.join(r'F:\stuff',item)
#     print(path)



#we need to install pillow library (pip install pillow) and than import 
# from PIL import Image,ImageEnhance,ImageFilter
# import os
# # img1 = Image.open('dog1.jpg')
# # img1.save('dog1.pdf')
# # img1.show()
# # MAX_SIZE(250,250)
# # img1.thumbinal(MAX_SIZE)
# # img1.save('small_dog1.jpg')
# # for item in os.listdir:
# #     if item.endswith('.jpg'):
# #         img1 = Image.open(item)
# #         filename,extension = os.path.splitext(item)
# #         img1.save(f"{filename}.png")

# # img2 = Image.open('img2.jpg')
# # enhancer = ImageEnhance.Sharpness(img2)
# # enhancer.enhance(2).save('edited_img.jpg')
# # 0 is blurry
# # 1 is Original 
# # 2 increase Sharpness


# # --------Color-------------
# #  img2 = Image.open('img2.jpg')
# # enhancer = ImageEnhance.Color(img2)
# # enhancer.enhance(2).save('edited_img.jpg')
# # colors also have values like sharpness
# # 0 is black&white
# # 1 is original 
# # 2 adds extra colors


# # --------Brightness-------------
# #  img2 = Image.open('img2.jpg')
# # enhancer = ImageEnhance.Brightness(img2)
# # enhancer.enhance(2).save('edited_img.jpg')
# # Brightness also have values like others
# # 0 is black and 1 is original and 3++ extra brightness


# # --------Contrast-------------
# #  img2 = Image.open('img2.jpg')
# # enhancer = ImageEnhance.Contrast(img2)
# # enhancer.enhance(2).save('edited_img.jpg')
# # Contrast also have values like others
# # 0 is black and 1 is original and 3++ extra


# # -------Blur---------
# # img3 = Image.open('img3.jpg')
# # img3.filter(ImageFilter,GaussianBlur(radius=4).save('edited.jpg'))

# import os
# import shutil
# extensions_dict = {
#     'Video_files': ('.mp4','.MP4','.mkv','.MKV','.flv','.mpeg'),
#     'Audio_files':('.mp3','.m4a','.wav','.flac'),
#     'document_files':('.pdf','.doc','.txt'),
#     'pictures_extension':('.png','.jpg'),}
# folderpath= input("plz enter your folder path:  ")

# def find_files(folder_path,file_extension):
#     return [file for file in os.listdir(folder_path) 
#             for extension in file_extension if file.endswith(extension)]
#     # files = []
#     # for file in os.listdir(folder_path):
#     #     for extension in file_extension:
#     #         if file.endswith(extension):
#     #             files.append(file)
#     # return files 

# for keys,values in  extensions_dict.items():
#     folder_names = keys.split('_')[0] + 'Folder'
#     folder_path = os.path.join(folderpath,folder_names)
#     os.mkdir(folder_path)
#     for item in  find_files(folderpath,values):
#         item_path = os.path.join(folderpath,item)
#         item_new_path = os.path.join(folder_path,item)
#         shutil.move(item_path,item_new_path)




