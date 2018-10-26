strana = int(input('Zadej delku strany: '))

for radek in range(strana):
    if radek == 0 or radek == (strana - 1):
        print('x '*strana)
    else:
        print('x', int(1.99*(strana-2))*' ','x')
