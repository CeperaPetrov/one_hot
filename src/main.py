import pandas as pd
import random

def one_hot_enc(lst):
    '''Конвертер списка в one hot вид'''
    categories = tuple(set(lst))
    def encode(item):
        return [i == item for i in categories]
    return {categories : list(map(encode, lst))}


def print_one_hot(one_hot):
    '''Печать one hot'''
    for header,data in one_hot.items():
        print(f"id    | {header}")
        for i in range(len(data)):
            print(f"{str(i).ljust(5)} | {data[i]}")

def main():
    lst = ['robot'] * 10
    lst += ['human'] * 10
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI':lst})
    print("В качестве эталонного образца вывод результата get_dummies: \n")
    print(pd.get_dummies(data['whoAmI']))
    print("\nВывод собственной реализации. Результат функции one_hot_enc: \n")
    one_hot = one_hot_enc(lst)
    print_one_hot(one_hot)
    

if __name__ == '__main__':
    main()