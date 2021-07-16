# #program 1
# from collections import Counter

# sandwiches= ['veg','veg','non-veg','veg','mutton','mutton']
# count= Counter(sandwitches)
# print(count)

# #output Counter({'veg':3,'non-veg':1,'mutton':2}) , it will give a dict as output 



# #program 2
# from collections import   Counter
# print(Counter(a=5,b=9,c=8))
# print({'hi':8,'bye':90})


# program 3
# from collections import namedtuple
# sandwich = namedtuple('sandwich','name , price')
# first_sandwitch=sandwich('veg-sanwich','$34')
# print(first_sandwitch)
# print(first_sandwitch.name)
# print(first_sandwitch.price)

# second_sandwich = sandwich._make(['cheese','$33'])
# print(second_sandwich)
# print(second_sandwich.name)
# print(second_sandwich.price)


#program 4
from collections import defaultdict
sandwich = defaultdict(str) #if the element is not fount what default value it return i, in case of this is str. we can pass int instead of str
sandwich[0]='veg'
sandwich[1]='non-veg'
sandwich[2]='mutton'
print(sandwich[0])
print(sandwich[7]) #in default dict this line will not give any error , but in case of normal dict it definately throws error




#program 6
#used to combine two or more dictionary
#it brings in a single dictionary
from collections import ChainMap

sandwich_menu={'veg':'$4','non-veg':'$45','mutton':'$99'}
secret_menu={'pizza':'$40','burger':'$5'}
menu =ChainMap(sandwich_menu,secret_menu)
print(menu)
print(menu["veg"])
print(list(menu.keys()))
print(list(menu.values()))
