import operaciones_basicas as op


def main():
    suma = op.suma(55, 60)
    print(f'La suma es: {suma}')

    resta = op.resta(200, 50)
    print(f'La resta es: {resta}')

    multiplica = op.multiplicar(4, 30)
    print(f'La multiplicacion es: {multiplica}')

    divide = op.dividir(500, 50)
    print(f'La division es: {divide}')


if __name__ == '__main__':
    main()
