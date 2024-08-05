grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades[0] = sum([5, 3, 3, 5, 4]) / len(''.join(map(str, [5, 3, 3, 5, 4])))#в каждом списке сложили элементы, разделили на количество элементов в списке, преобразованном в строку
grades[1] = sum([2, 2, 2, 3]) / len(''.join(map(str, [2, 2, 2, 3])))
grades[2] = sum([4, 5, 5, 2]) / len(''.join(map(str, [4, 5, 5, 2])))
grades[3] = sum([4, 4, 3]) / len(''.join(map(str, [4, 4, 3])))
grades[4] = sum([5, 5, 5, 4, 5]) / len(''.join(map(str, [5, 5, 5, 4, 5])))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}#set - множество
new_students = list(sorted(students))#множество преобразовали в список, где элементы отсортированы по алфавиту
new_dict = dict(zip(new_students, grades))#собираем два списка в словарь с помощью функций dict и zip (zip собирает элементы по парам)
print(new_dict)
