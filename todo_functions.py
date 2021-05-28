def cap(case=""):
    print('\nTODO: ' + case)
    print('-----------------------------------------------')
    """
    Печать общей шапки. По умочанию, поле после TODO пустое.
    При необходимости заполняем аргумент функции требуемым текстом.
    
    """


def print_requested(base):
    for index, value in enumerate(base, 1):
        print(("{}: {}".format(index, value)).replace("\n", ""))
    """
    Построчная нумерация, начиная с 1, и печать запрошенного списка - base.
    
    """


def print_changes(base, i, mark):
    for index, value in enumerate(base, 1):
        if index != i:
            print(("{}: {}".format(index, value)).replace("\n", ""))
        else:
            print(("{}: {}".format(i, value)).replace("\n", "") + mark)
    """
    Построчная нумерация, начиная с 1, и печать измененного списка - base.
    Строка с индексом i принимает изменения и получает соответствующую случаю отметку mark.
    
    """
