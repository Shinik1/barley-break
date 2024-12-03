from fill_pole import fill_pole
from game_mechanics import mexanika
from print_pole import print_pole

def main():
    win_pole = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,' ']] #победное поле
    pole = [[],[],[],[]] #поле (двумерный массив)
    pole = fill_pole(pole)
    print_pole(pole)
    mexanika(pole, win_pole)
