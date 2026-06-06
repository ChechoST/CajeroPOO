class Cajero:
    def __init__(self, titular, saldo_inicial): 
        self.titular = titular 
        self.saldo = saldo_inicial

    def consultar_saldo(self): 
        print(f"\nSaldo disponible: ${self.saldo:,.0f}") 
    def depositar(self): 
        monto = float(input("Ingrese el monto a depositar: ")) 
        if monto > 0: 
            self.saldo += monto 
            print("Depósito realizado correctamente.") 
        else: 
            print("Monto inválido.") 
    def retirar(self):
        monto = float(input("Ingrese el monto a retirar: ")) 
        if monto <= 0:
            print("Monto inválido.")

        elif monto > self.saldo:
            print("Fondos insuficientes.")
        
        else:
            self.saldo -= monto 
            print("Retiro realizado correctamente.")
    def menu(self):
        while True:

            print("\n--- CAJERO AUTOMATICO---")
            print("1. Consultar saldo")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.consultar_saldo()
            elif opcion == "2":
                self.depositar()
            elif opcion == "3":
                self.retirar()
            elif opcion == "4":
                print("Gracias por usar el cajero.")
                break
            else:
                print("Opción inválida.")
            
    #Crear objeto
cliente =Cajero("Juan Pérez", 1000)
    #ejecutar programa
cliente.menu()