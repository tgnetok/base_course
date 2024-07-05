import numpy as baigashov
import random

flowers = ['Роза', 'Тюльпан', 'Василёк']
colors = ['Красный', 'Жёлтый', 'Зелёный', 'Синий', 'Фиолетовый']
colors_array = baigashov.array (colors)

slovar_eeee = dict(zip(flowers, colors_array))

print (slovar_eeee)