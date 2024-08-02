mutable_list = [1, 2, 'top']
mutable_list[2] = 3
print('Mutable list: ', mutable_list)
tuple_ = 1, 2, 'top'
immutable_var = tuple_
print('Immutable tuple: ', immutable_var)
immutable_var[0] = 2
print(immutable_var)