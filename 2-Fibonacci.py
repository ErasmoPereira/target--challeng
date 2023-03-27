print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
print('~'*30)
n = int (input('Digite um numero: '))
print('~'*30)
t1 = 0
t2 = 1

print(f'{t1} -> {t2}', end='')

pertence = False

while True :
    t3 = t1 +t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3

    if not pertence and n == t3:
        pertence = True
        break
    elif t3>n:
        break

if pertence :
    print('\nEste valor pertênce a sequência.')
else:
    print('\nEste valor não pertênce a sequência.')
print("Fim")

