grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades[0] = sum(grades[0]) / len(grades[0])
grades[1] = sum(grades[1]) / len(grades[1])
grades[2] = sum(grades[2]) / len(grades[2])
grades[3] = sum(grades[3]) / len(grades[3])
grades[4] = sum(grades[4]) / len(grades[4])
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}#set - множество
new_students = list(sorted(students))#множество преобразовали в список, где элементы отсортированы по алфавиту
new_dict = dict(zip(new_students, grades))#собираем два списка в словарь с помощью функций dict и zip (zip собирает элементы по парам)
print(new_dict)
