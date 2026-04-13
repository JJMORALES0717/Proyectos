class PlantaEspacial:
    def __init__(self, nombre, especie):
        """Constructor: Recibe nombre y especie; fija hidratación, salud y estado[cite: 63, 64]."""
        self.nombre = nombre
        self.especie = especie
        self.hidratacion = 100
        self.salud = 100
        self.estado = "Saludable"

    def regar(self):
        """Suma 15 de hidratación sin exceder 100. No funciona si está marchita[cite: 68, 72]."""
        if self.estado == "Marchita":
            print(f"\n[ERROR: No se puede regar. {self.nombre} está marchita].")
            return
        
        self.hidratacion += 15
        if self.hidratacion > 100: self.hidratacion = 100
        print(f"\nSuministrando agua... Hidratación actual: {self.hidratacion}%.")

    def pasar_dia(self):
        """Reduce hidratación en 20. Si es < 30, resta 40 de salud[cite: 69, 70]."""
        if self.estado == "Marchita": return
        
        self.hidratacion -= 20
        if self.hidratacion < 0: self.hidratacion = 0
        print(f"\nHa pasado un día en Marte. La hidratación bajó a {self.hidratacion}%.")

        if self.hidratacion < 30:
            self.salud -= 40
            print(f"¡ALERTA! Hidratación crítica. La salud de {self.nombre} ha sufrido daños.")
        
        if self.salud <= 0:
            self.salud = 0
            self.estado = "Marchita"
            print(f"Trágico: {self.nombre} se ha marchitado.")

    def reporte(self):
        """Informa el estado detallado tras cada acción[cite: 75]."""
        print(f"\nREPORTE DE BIO-MONITOR: {self.nombre}")
        print(f"Estado: {self.estado} | Hidratación: {self.hidratacion}% | Salud: {self.salud}%")

print(">>> INICIANDO SISTEMA DE BIO-INGENIERÍA ARES-1 <<<")
n_p = input("Nombre de la planta: ")
e_p = input("Especie de la planta: ")
mi_planta = PlantaEspacial(n_p, e_p)

while True:
    mi_planta.reporte()
    print("-" * 30)
    print("1. Regar | 2. Dejar pasar día | 3. Salir")
    op = input("Seleccione acción: ")

    if op == "1": mi_planta.regar()
    elif op == "2": mi_planta.pasar_dia()
    elif op == "3": break