def geometric_progression(start, step):
    current = start
    while True:
        yield current
        current *= step

progression_1 = geometric_progression(-4, -10)
for _ in range(4):
    print(next(progression_1))

print('-' * 50)

progression_2 = geometric_progression(1, 5)
for _ in range(4):
    print(next(progression_2))
