# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# # использование get_dummies()
# one_hot_encoded = pd.get_dummies(data, columns=['whoAmI'])
# one_hot_encoded.head()


categories = list(set(data['whoAmI']))
one_hot_encoded = []

for item in data['whoAmI']:
    one_hot_row = [0] * len(categories)
    one_hot_row[categories.index(item)] = 1
    one_hot_encoded.append(one_hot_row)

print(pd.DataFrame(one_hot_encoded, columns=categories))

