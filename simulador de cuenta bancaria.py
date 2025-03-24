class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, saldo = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}\nSaldo de la cuenta {self.numero_cuenta}: ${self.saldo}'

    def depositar(self, monto_deposito):
        self.saldo += monto_deposito
        print("Depósito aceptado")

    def retirar(self, monto_retiro):
        if self.saldo >= monto_retiro:
            self.saldo -= monto_retiro
            print('Retiro realizado')
        else:
            print('Fondos insuficientes')


def crear_cliente():
    nombre_cliente = input("Ingresa tu nombre: ")
    apellido_cliente = input("Tu apellido: ")
    numero_cuenta = input("Ingresa tu número de cuenta: ")
    cliente1 = Cliente(nombre_cliente, apellido_cliente, numero_cuenta)

    return cliente1


def iniciar():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print("Elige: Depositar (D), Retirar (R), o Salir (S)")
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_ret)

        print(mi_cliente)

    print("Gracias por usar el Banco Python")


iniciar()
