
def manipulate_list(input_list):
    # Проверка на список
    if type(input_list) == list:
        # Найдем произведение элементов с нечетными номерами
        product = 1
        for i in range(len(input_list)):
            if i % 2 != 0:
                product *= input_list[i]
        print("Произведение элементов списка с нечетными номерами:", product)

        # Найдем наибольший элемент и удаление его из списка
        max_value = max(input_list)
        input_list.remove(max_value)
        print("Новый список без наибольшего элемента:", input_list)
    else:
        print("Входной аргумент не является списком.")

# Примеры вызова функции
manipulate_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
manipulate_list([10, 20, 30, 40, 50])
manipulate_list("12345")
