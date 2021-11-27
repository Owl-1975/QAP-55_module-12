per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print('')

money = int(input("Сумма вклада:"))
print('')

print('Deposit:')
for key, value in per_cent.items():
    print(key, int(value * money / 100))

print('')
max_val = max(per_cent.values())
print("Максимальная сумма, которую вы можете забрать - ", (int(max_val * money / 100)))

