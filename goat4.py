__author__ = 'giovanni'

to_do = ['make bed', 'make breakfast', 'make lunch']


print (len(to_do))

to_do.append('drive car') # this function is to add new item in the list

print (len(to_do)) # this will give length of the list

print (to_do[3])

del to_do[0] # this is to delete the item in the list

print (to_do)

print
print

new_list = [] #this is iteration within list using for loop
for x in to_do:
    new_list.append(x*3)

print (new_list)