def print_pole(pole):  #вывод поля
    used_num = []
    print("---------------------")
    for i in range(4):
        for j in range(4):
            if pole[i][j] == ' ':
                print("| "+ str(pole[i][j])+" ", end = ' ')
            elif int(pole[i][j])<10:
                print("| "+str(pole[i][j])+" ", end = ' ')
            else:
                print("| "+str(pole[i][j])+"", end = ' ')
        print("|")

        print("---------------------")
