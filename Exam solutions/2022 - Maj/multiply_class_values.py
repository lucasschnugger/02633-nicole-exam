import numpy as np
def multiply_class_values(text):
    list = text.split(', ')
    numbers = []  # tom liste
    for txt in list:
        lst = txt.split(': ')
        name = lst[0]
        value = int(lst[1])  # laver tekst-værdien om til en heltals-værdi
        if name.__contains__('a'):  # hvis name indeholde a
            numbers.append(value)  # gemmer value i numbers listen
    product = np.product(numbers)
    return product

#Løsning CodeJudge
text = "jaw-less fish: 7, cartilaginous fish: 13, bony fish: 3, amphibians: 2, reptiles: 17, birds: 5, mammals: 19"
print(multiply_class_values(text))

def multiply_class_values(class_string):
    class_string = class_string.lower()
    classes_with_values = class_string.split(',')

    product = 1
    a_found = False
    for class_v in classes_with_values:
        class_value_array = class_v.split(':')
        if 'a' in class_value_array[0]:
            a_found = True
            product = product * int(class_value_array[1])

    if a_found:
        return product
    return 0
