while True:
    file_path = "products.txt"
    with open(file_path, mode="r", encoding="utf8") as file:
        products = file.read().split('\n')
    print("Меню\n1) Переглянути запис\n2) Додати запис\n3) Видалити запис\n0) Вихід")
    diya = int(input("Ведіть дію: "))
    if diya == 0:
        break
    elif diya == 1:
        print("Список продуктів: ")
        for product in products:
            print(f' - {product}')
    elif diya == 2:
        with open(file_path, mode="w", encoding="utf8") as file:
            haha = input("Ведіть список: ")
            products.append(haha)
            file.write("\n".join(products))
    elif diya == 3:
        with open(file_path, mode="w", encoding="utf8") as file:
            print("Список продуктів: ")
            for product in products:
                print(f' - {product}')
            ha = input("Ведіть строку, яку треба видалити: ")
            products.remove(ha)
            file.write("\n".join(products))
    else:
        "Неправильно"




