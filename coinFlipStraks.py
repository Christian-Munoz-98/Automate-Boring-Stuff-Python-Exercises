import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    list_of_flips = []

    for i in range(100):
        coin_flip = random.randint(0, 1)
        list_of_flips.append(coin_flip)

    str_list = "".join([str(_) for _ in list_of_flips])

    # Code that checks if there is a streak of 6 heads or tails in a row.
    if ('111111' in str_list) or ('000000' in str_list):
        numberOfStreaks += 1

print(f'La probabilidad de acertar 6 caras o cruces seguidas en 12 lanzamientos de moneda es del {numberOfStreaks//100}%')