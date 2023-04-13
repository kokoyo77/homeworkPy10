import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})
data.head()

# Функция для преобразования строки в one-hot вектор
def convert_to_one_hot(row, categories):
    one_hot = [0] * len(categories)
    for i, category in enumerate(categories):
        if row == category:
            one_hot[i] = 1
            break
    return one_hot

# Создание списка уникальных категорий
categories = data['whoAmI'].unique()

# Применение функции конвертации и создание новых столбцов с префиксом 'one_hot_'
for i, category in enumerate(categories):
    data[f"one_hot_{category}"] = data['whoAmI'].apply(lambda row: convert_to_one_hot(row, categories)[i])

data.head()
