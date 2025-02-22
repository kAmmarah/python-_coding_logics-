# # # def box(){
# # #     return a=b
# # # }

# # def box(a, b=3):
# #     return a+b
# # sum =  box(2)
# # print(sum)


# # def func(a,b):   variable function (ab) this is default 
# #     a+b

# # c=func(2,3)
# # print(c)

# # #string methods
# # customize function & built-in function and method is also function(dot notaion)
# # method is a built-in function 

# name = "pakistan"

# # print(type(name))

# # # name. see the function all
# # print (name.capitalize())
# # print(name.count('a,t'))


# new_str ="my name is sami. my nationaly is pakistani"
# # print(new_str.count('my'))

# # # print(new_str.__len__()) this is the 2 way we are using "lenth"
# # print(len(new_str))
# # print(new_str.find('my'))
# # print(new_str.index('my'))
# # print(new_str.replace("pakistani", "american").upper())

# my_list = ["Ameen", "Sohaib", "najma", "Ammara" ]

# #append
# my_list.append('ameen alam')
# print(my_list)

# #insert
# my_list.insert(1,'sir zia')
# print(my_list)

# #reversed
# my_list.reverse()
# print(my_list)

# #pop
# print(my_list)
# print(my_list.pop(2))

# print(my_list)


# #sort
# my_list.sort(reverse=True)
# print(my_list)

# #extend 
# new_faculty = ['Abdullah', 'Ghous']
# print("old list",my_list)
# my_list.extend(new_faculty)

# print("updated",new_faculty)

#Dictionary

my_dict = {
"name":"John",
"age" : 25,
"city" : "karachi"
}

# Dictionary methods

#get()
#key(
#value()
#itom()
#update()
#clear()
#pop()

#keys : 
print(my_dict.keys())

#value
print(my_dict.values())

#item
print(my_dict.items())

#get
print(my_dict.get("name"))

#upadte
new_dict = {"city" : "Ialsmabad"}
new_dict2 = {"country" : "Pakstan"}
my_dict.update(new_dict)
my_dict.update(new_dict2)
print(my_dict)


#pop
print(my_dict.pop('city'))
print(my_dict)

#clear
print(my_dict.clear())
print(my_dict)

#empty
