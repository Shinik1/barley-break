import random
import numpy as np
from fill_pole import fill_pole
from print_pole import print_pole

def mexanika(pole, win_pole): # Механика игры
    while pole != win_pole: # Пока поле не совпадает с выйгрышным
        for i in range(4):
            for j in range(4):
                if pole[i][j] == ' ': # Находим координаты пустой клетки
                  swap_0_x = i
                  swap_0_y = j

        swap_1 = input('Введите клетку, которую хотите переместить ')
        while swap_1 not in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']: # Проверка на корректность ввода
            swap_1 = input('Эта клетка не доступна, выберите другую ')
        swap_1 = int(swap_1)
        
        ok = True
        while ok == True:
            for i in range(4):
                for j in range(4):
                    if pole[i][j] == swap_1: # Находим координаты выбранной клетки
                        swap_1_x = i  
                        swap_1_y = j 
                        if ((swap_1_x == swap_0_x - 1) and (swap_1_y == swap_0_y)) or ((swap_1_x == swap_0_x + 1) and (swap_1_y == swap_0_y)) or ((swap_1_x == swap_0_x) and (swap_1_y == swap_0_y - 1)) or ((swap_1_x == swap_0_x) and (swap_1_y == swap_0_y + 1)):
                            ok = False 
                        else: 
                            swap_1 = input('Введите другую клетку, которую хотите переместить ')
                            while swap_1 not in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']:
                                swap_1 = input('Эта клетка не доступна, выберите другуюх ')
                            swap_1 = int(swap_1)
        a = swap_1 
        pole[swap_1_x][swap_1_y] = ' ' # Замена клеток
        pole[swap_0_x][swap_0_y] = a  # Замена клеток
        print_pole(pole)
