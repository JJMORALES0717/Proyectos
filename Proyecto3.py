# ====================================================================
# PROYECTO 3: SISTEMA POKÉMON (VERSIÓN FINAL PROFESIONAL)
# ====================================================================

try:
    from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
except ImportError:
    print("\n[!] ERROR: No se encontró 'pokedex.py' en esta carpeta.")
    print("Asegúrese de que el archivo del profesor esté junto a este script.")
    exit()

class Pokemon:
    """Clase base con la estructura principal de POO."""
    def __init__(self, nombre, tipo, hp_max, ep_max):
        self.nombre = nombre
        self.tipo = tipo
        self.hp = self.hp_max = hp_max
        self.ep = self.ep_max = ep_max

    def mostrar_interfaz(self):
        """Dibuja una interfaz visual en la consola."""

        bloques = int((self.ep / self.ep_max) * 10)
        barra = "▰" * bloques + "▱" * (10 - bloques)
        
        print(f"\n{'━'*40}")
        print(f"  POKÉMON: {self.nombre.upper()}")
        print(f"  TIPO:    {self.tipo}")
        print(f"  SALUD:   {self.hp}/{self.hp_max} HP")
        print(f"  ENERGÍA: {barra} ({self.ep} EP)")
        print(f"{'━'*40}")

    def descansar(self):
        self.ep = self.ep_max
        print(f"\n✨ {self.nombre} ha descansado y recuperado su energía.")

# --- Aplicación de Herencia para ataques específicos ---

class PokemonFuego(Pokemon):
    def atacar(self):
        if self.ep >= 20:
            self.ep -= 20
            print(f" ¡{self.nombre} usó LLAMARADA!")
        else: print(" Energía insuficiente para este ataque.")

class PokemonAgua(Pokemon):
    def atacar(self):
        if self.ep >= 25:
            self.ep -= 25
            print(f"¡{self.nombre} usó HIDROBOMBA!")
        else: print("Energía insuficiente para este ataque.")

class PokemonPlanta(Pokemon):
    def atacar(self):
        if self.ep >= 15:
            self.ep -= 15
            print(f"¡{self.nombre} usó RAYO SOLAR!")
        else: print("Energía insuficiente para este ataque.")

class PokemonElectrico(Pokemon):
    def atacar(self):
        if self.ep >= 20:
            self.ep -= 20
            print(f"¡{self.nombre} usó IMPACTRUENO!")
        else: print("Energía insuficiente para este ataque.")

# --- Lógica de Ejecución ---

def principal():
    print("\n" + "═"*40)
    print("      CENTRO DE ENTRENAMIENTO POKÉMON")
    print("═"*40)

    # Mostrar catálogo del archivo externo
    mostrar_catalogo_disponible()
    
    seleccion = input("\n❯ Ingrese el ID del Pokémon para comenzar: ")

    if seleccion in CATALOGO_POKEMON:
        datos = CATALOGO_POKEMON[seleccion]
     
        clases = {
            "Fuego": PokemonFuego, 
            "Agua": PokemonAgua, 
            "Planta": PokemonPlanta, 
            "Electrico": PokemonElectrico
        }
        
        tipo_pokemon = datos['tipo']
        clase_base = clases.get(tipo_pokemon, Pokemon)
        
        mi_poke = clase_base(
            datos['nombre'], 
            tipo_pokemon, 
            datos['hp_maximo'], 
            datos['energia_maxima']
        )

        print(f"\n{mi_poke.nombre} está listo para el entrenamiento.")

        while True:
            mi_poke.mostrar_interfaz()
            print(" [1] Atacar  [2] Descansar  [3] Salir")
            opcion = input(" Seleccione una acción: ")

            if opcion == "1":
                mi_poke.atacar()
            elif opcion == "2":
                mi_poke.descansar()
            elif opcion == "3":
                print("\nCerrando sistema... ¡Buen viaje, Entrenador!\n")
                break
            else:
                print("\nOpción inválida, intente de nuevo.")
    else:
        print("\nEl ID ingresado no existe en el catálogo.")

if __name__ == "__main__":
    principal()