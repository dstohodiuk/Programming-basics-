year = 2024
word = 'Study'
it = 'Programming'
logical_type = True
key = {'min': 12, 'max': 6}

first_list = [year, word, it, logical_type, key]
print(first_list)

type_list = [type(year), type(word), type(it), type(logical_type), type(key)]
print(type_list)

if type_list != str:
    print('Найчастіший тип: ', type(word))

elif type_list != int:
    print('Найчастіший тип: ', type(year))

else:
    type_list != str
    print("Exit")
