# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для 
# всех значений предикат. Предикату можно заменить на понятие "бит". Должна получиться 
# таблица истинности.

def logical_statement():
    print("*"*60)
    print("X", "Y", "Z", "result", sep=(" "*15))
    print("*"*60)
    for X in range(2):
        for Y in range(2):
            for Z in range(2):
                result = not (X or Y or Z) == (not (X) and not (Y) and not (Z))
                print(
                    f'{X}      |        {Y}       |       {Z}        |       {result}')


logical_statement()
