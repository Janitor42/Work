def shoot(q):
    if q=='F':
        print('П ы щ ь ')
        print('нужна перезарядка')
    else:
        print('нужна перезарядка')

def reload():
    q = input('Перезарядка на F'+'\n')
    return q

while True:
    shoot(reload())


