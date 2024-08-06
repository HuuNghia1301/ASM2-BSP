if __name__ == '__main__':
    fullName = input('Nhap Vao ho ten :')
    age = int(input('Nhap so tuoi:'))
    print(f'{fullName} {age} tuoi')
    if age > 60:
        print('You are old man')
    elif age >= 30:
        print('you are man')
    elif age >= 20:
        print('you are young man')
    elif age >= 10:
        print('you are teenager')
    else:
        print('you are kid')