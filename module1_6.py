my_dict = {'Nastya': 2004, 'Egor': 2005, 'Misha': 2000}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Nastya'])
print('Not existing value: ', my_dict.get('Vasya'))
my_dict.update({'Vasya': 2002, 'Lena': 1998})
a = my_dict. pop('Egor')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)
my_set = {'Vasya', 'Misha', 'Vasya', 6, 9, 11, 9, True, False, True}
print('Set: ', my_set)
my_set.update({8, 'Nick'})
my_set.remove(11)
print('Modified set: ', my_set)