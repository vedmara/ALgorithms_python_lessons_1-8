for y in range(2, 9):
    count = 0
    for i in range(2, 99):
        if i % y == 0:
            count += 1
    print("Количество чисел кратных", y, "=", count)
