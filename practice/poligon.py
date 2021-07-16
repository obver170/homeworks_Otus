from curses.ascii import isalnum
from os import path




def main():
    value = 'wefwefwe3!'
    val = 'f'
    g = 6
    value = g
    g = 7
    print(id(value))
    print(id(g))
    print(id(val))
    print(type(val))
    print(type(value))



if __name__ == '__main__':
    main()
