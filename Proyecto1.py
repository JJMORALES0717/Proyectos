class DronVigilancia:
    def __init__(self, nombre, modelo):
        """Constructor: Solicita nombre y modelo, fija batería al 100% y estado en Tierra[cite: 12, 13]."""
        self.nombre = nombre
        self.modelo = modelo
        self.bateria = 100
        self.estado_vuelo = "En Tierra"

    def despegar(self):
        """Valida batería mínima de 25% para cambiar estado a En Vuelo[cite: 18, 19]."""
        if self.bateria >= 25:
            self.estado_vuelo = "En Vuelo"
            print(f"\n¡Despegue exitoso! El dron {self.nombre} ahora está en el aire.")
        else:
            print(f"\n[ERROR: Batería insuficiente ({self.bateria}%). Requiere 25%].")

    def patrullar(self):
        """Consume 30% de energía. Si baja de 10%, aterriza automáticamente[cite: 20, 21, 22]."""
        if self.estado_vuelo == "En Vuelo":
            self.bateria -= 30
            if self.bateria < 0: self.bateria = 0
            print(f"\nPatrullaje completado. Consumo: 30%. Batería restante: {self.bateria}%.")
            
            if self.bateria < 10:
                self.estado_vuelo = "En Tierra"
                print("¡ALERTA! Batería en nivel crítico. Aterrizando automáticamente por seguridad.")
        else:
            print("\n[ERROR: El dron no puede patrullar si aún está en tierra].")

    def recargar(self):
        """Restaura batería al 100% solo si está en Tierra[cite: 24]."""
        if self.estado_vuelo == "En Tierra":
            self.bateria = 100
            print(f"\nRecarga finalizada. {self.nombre} está al 100% de energía.")
        else:
            print("\n[ERROR: El dron debe estar en tierra para recargar].")

print(">>> INICIANDO SISTEMA SKYWATCH <<<")
n = input("Ingrese nombre del dron: ")
m = input("Ingrese modelo del dron: ")
dron = DronVigilancia(n, m)

while True:
    print(f"\nESTADO ACTUAL: {dron.nombre} [{dron.modelo}]")
    print(f"Batería: {dron.bateria}% | Estado: {dron.estado_vuelo}")
    print("-" * 30)
    print("1. Despegar | 2. Patrullar | 3. Recargar | 4. Salir")
    opcion = input("Seleccione acción: ")

    if opcion == "1": dron.despegar()
    elif opcion == "2": dron.patrullar()
    elif opcion == "3": dron.recargar()
    elif opcion == "4": break