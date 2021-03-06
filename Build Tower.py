def tower_builder(n_floors):
    tower = []
    i = 1
    while i <= n_floors and n_floors > 0:
            space = ' ' * (n_floors - i)
            tower.append(space + '*' * (i*2 - 1) + space)
            i += 1
    return tower

print(tower_builder(5))
