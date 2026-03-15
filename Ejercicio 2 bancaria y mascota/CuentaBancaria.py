class CuentaBancaria:

    def __init__(self, titular, numeroCuenta, saldo):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo

    # 2. Método para depositar 
    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print(f"Has depositado: ${cantidad}")

    # 3. Método para retirar
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
            return cantidad
        else:
            return "Saldo insuficiente :("

    # 4. Método para consultar saldo
    def consultarSaldo(self):
        return self.saldo

    def mostrarInformacion(self):
        return f"{self.titular} tienes ${self.saldo}"

# --- USO DEL CÓDIGO ---
cuenta1 = CuentaBancaria("Maximus Lopez", "8963454", 1500)

print(cuenta1.mostrarInformacion()) 

cuenta1.depositar(500.0)
print(cuenta1.mostrarInformacion())

cuenta1.retirar(250)
cuenta1.depositar(200)

print(cuenta1.mostrarInformacion())