def manipulate_list(input_list):
    # Проверка на список
    if isinstance(input_list, list):
        # Найдем произведение элементов с нечетными индексами
        product = 1
        for i in range(len(input_list)):
            if i % 2 != 0:
                product *= input_list[i]
        print("Произведение элементов списка с нечетными номерами:", product)

        # Найдем наибольший элемент списка и удаление его
        max_value = max(input_list)
        input_list.remove(max_value)
        print("Новый список без наибольшего элемента:", input_list)
    else:
        print("Входной аргумент не является списком.")

# Примеры вызова функции
list1 = [1, 2, 3, 4, 5]
manipulate_list(list1)

list2 = [10, 8, 6, 12, 2]
manipulate_list(list2)

string = "abcde"
manipulate_list(string)

number = 12345
manipulate_list(number)

