
# Знакомство с языком Python (семинары)
## Урок 10. Построение графиков

Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

```python
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
```

Для преобрадзования списка в One Hot реализован функция one_hot_enc.
Исходный код программы в файле [src\main.py](src\main.py)


### Пример работы программы

```
В качестве эталонного образца вывод результата get_dummies:

    human  robot
0    True  False
1    True  False
2   False   True
3    True  False
4   False   True
5    True  False
6    True  False
7   False   True
8   False   True
9   False   True
10   True  False
11   True  False
12  False   True
13  False   True
14   True  False
15  False   True
16  False   True
17   True  False
18  False   True
19   True  False

Вывод собственной реализации. Результат функции one_hot_enc:

id    | ('robot', 'human')
0     | [False, True]
1     | [False, True]
2     | [True, False]
3     | [False, True]
4     | [True, False]
5     | [False, True]
6     | [False, True]
7     | [True, False]
8     | [True, False]
9     | [True, False]
10    | [False, True]
11    | [False, True]
12    | [True, False]
13    | [True, False]
14    | [False, True]
15    | [True, False]
16    | [True, False]
17    | [False, True]
18    | [True, False]
19    | [False, True]

```