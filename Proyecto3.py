# ====================================================================
# PROYECTO 3: SISTEMA POKÉMON 
# ====================================================================

import random  
try:
    from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
except ImportError:
    print("\n[!] ERROR CRÍTICO: No se encontró el archivo 'pokedex.py'.")
    print("Asegúrese de que el archivo del profesor esté en la misma carpeta.")
    exit()


class Pokemon:
    """Clase base que define la estructura principal y el encapsulamiento."""

    def __init__(self, nombre, tipo, hp_max, ep_max):

        self.nombre = nombre
        self.tipo = tipo

        self.__hp_max = hp_max
        self.__ep_max = ep_max

        self.hp = hp_max
        self.ep = ep_max


    @property
    def hp(self):
        """Getter para la vida actual."""
        return self.__hp

    @hp.setter
    def hp(self, valor):
        """Setter para la vida con lógica de validación (CRITERIO 7)."""
        if valor < 0:

            self.__hp = 0
        elif valor > self.__hp_max:
            self.__hp = self.__hp_max
        else:
            self.__hp = valor

    @property
    def ep(self):
        """Getter para la energía actual."""
        return self.__ep

    @ep.setter
    def ep(self, valor):
        """Setter para la energía."""
        if valor < 0:
            self.__ep = 0
        elif valor > self.__ep_max:
            self.__ep = self.__ep_max
        else:
            self.__ep = valor

    @property
    def hp_max(self): return self.__hp_max

    @property
    def ep_max(self): return self.__ep_max


    def esta_con_vida(self):
        """Retorna True si el Pokémon tiene HP mayor a 0."""
        return self.hp > 0

    def mostrar_interfaz(self, es_rival=False):
        """Dibuja la interfaz visual de salud y energía en consola."""
        ancho = 40
        tag = "[RIVAL]" if es_rival else "[TU POKÉMON]"
        
        def generar_barra(actual, maximo, color_bloque="▰"):
            if maximo == 0: return "▱" * 10
            bloques = int((actual / maximo) * 10)
            return color_bloque * bloques + "▱" * (10 - bloques)

        barra_hp = generar_barra(self.hp, self.hp_max)
        barra_ep = generar_barra(self.ep, self.ep_max)
        
        print(f"\n{'━'*ancho}")
        print(f"  {tag} {self.nombre.upper()}")
        print(f"  TIPO:    {self.tipo}")
        print(f"  SALUD:   {barra_hp} ({self.hp}/{self.hp_max} HP)")
        print(f"  ENERGÍA: {barra_ep} ({self.ep}/{self.ep_max} EP)")
        print(f"{'━'*ancho}")

    def descansar(self):
        """Recupera toda la energía del Pokémon."""
        self.ep = self.ep_max
        print(f"\n {self.nombre} ha descansado y recuperado su energía.")

    def atacar(self, rival):
        """Método base para atacar (debe ser sobrescrito)."""

        print(f"{self.nombre} realiza un ataque básico (sin efecto).")


class PokemonFuego(Pokemon):
    """Subclase para Pokémon tipo Fuego."""

    def atacar(self, rival):
        costo = 20
        danio_base = 30
        
        if self.ep >= costo:
            self.ep -= costo
            
            # Lógica de ventaja elemental
            modificador = 1.0
            mensaje_ventaja = ""
            if rival.tipo == "Planta":
                modificador = 2.0
                mensaje_ventaja = " ¡Es súper eficaz!"
            elif rival.tipo in ["Agua", "Fuego"]:
                modificador = 0.5
                mensaje_ventaja = " No es muy eficaz..."

            danio_final = int(danio_base * modificador)
            rival.hp -= danio_final 
            
            print(f"\n¡{self.nombre} usó LLAMARADA contra {rival.nombre}!{mensaje_ventaja}")
            print(f" -> Causó {danio_final} puntos de daño.")
        else:
            print(f"\n{self.nombre} no tiene suficiente energía para atacar.")

class PokemonAgua(Pokemon):
    """Subclase para Pokémon tipo Agua."""
    def atacar(self, rival):
        costo = 25
        danio_base = 35
        
        if self.ep >= costo:
            self.ep -= costo
            modificador = 1.0
            mensaje_ventaja = ""
            if rival.tipo == "Fuego":
                modificador = 2.0
                mensaje_ventaja = " ¡Es súper eficaz!"
            elif rival.tipo in ["Agua", "Planta"]:
                modificador = 0.5
                mensaje_ventaja = " No es muy eficaz..."

            danio_final = int(danio_base * modificador)
            rival.hp -= danio_final
            
            print(f"\n¡{self.nombre} usó HIDROBOMBA contra {rival.nombre}!{mensaje_ventaja}")
            print(f" -> Causó {danio_final} puntos de daño.")
        else:
            print(f"\n{self.nombre} no tiene suficiente energía para atacar.")

class PokemonPlanta(Pokemon):
    """Subclase para Pokémon tipo Planta."""
    def atacar(self, rival):
        costo = 15
        danio_base = 25
        
        if self.ep >= costo:
            self.ep -= costo
            modificador = 1.0
            mensaje_ventaja = ""
            if rival.tipo == "Agua":
                modificador = 2.0
                mensaje_ventaja = " ¡Es súper eficaz!"
            elif rival.tipo in ["Planta", "Fuego"]:
                modificador = 0.5
                mensaje_ventaja = " No es muy eficaz..."

            danio_final = int(danio_base * modificador)
            rival.hp -= danio_final
            
            print(f"\n ¡{self.nombre} usó RAYO SOLAR contra {rival.nombre}!{mensaje_ventaja}")
            print(f" -> Causó {danio_final} puntos de daño.")
        else:
            print(f"\n {self.nombre} no tiene suficiente energía para atacar.")

class PokemonElectrico(Pokemon):
    """Subclase para Pokémon tipo Eléctrico."""
    def atacar(self, rival):
        costo = 20
        danio_base = 30
        
        if self.ep >= costo:
            self.ep -= costo
            modificador = 1.0
            mensaje_ventaja = ""
 
            if rival.tipo == "Agua":
                modificador = 2.0
                mensaje_ventaja = " ¡Es súper eficaz!"
            elif rival.tipo == "Planta":

                modificador = 0.8 
                mensaje_ventaja = " No es muy eficaz..."

            danio_final = int(danio_base * modificador)
            rival.hp -= danio_final
            
            print(f"\n¡{self.nombre} usó IMPACTRUENO contra {rival.nombre}!{mensaje_ventaja}")
            print(f" -> Causó {danio_final} puntos de daño.")
        else:
            print(f"\n {self.nombre} no tiene suficiente energía para atacar.")


def obtener_instancia_pokemon(id_pokedex):
    """
    CRITERIO 2 (Instanciación Dinámica):
    Extrae la info en crudo del catálogo y usa condicionales/diccionarios
    para llamar al constructor de la clase hija correspondiente.
    """
    if id_pokedex in CATALOGO_POKEMON:
        datos = CATALOGO_POKEMON[id_pokedex]
        
        mapa_clases = {
            "Fuego": PokemonFuego, 
            "Agua": PokemonAgua, 
            "Planta": PokemonPlanta, 
            "Electrico": PokemonElectrico
        }
        
        tipo_str = datos['tipo']

        clase_a_instanciar = mapa_clases.get(tipo_str, Pokemon)
        
        return clase_a_instanciar(
            datos['nombre'], 
            tipo_str, 
            datos['hp_maximo'], 
            datos['energia_maxima']
        )
    return None

def turno_rival(rival, jugador):
    """
    CRITERIO 8 (Modo Simulación PvE):
    La computadora toma decisiones autónomas usando la librería random.
    """
    print(f"\n--- Turno de {rival.nombre} (Rival) ---")

    accion = random.random()
    
    if accion < 0.8 and rival.ep >= 15:
        rival.atacar(jugador)
    else:
        rival.descansar()

def principal():
    print("\n" + "═"*40)
    print("      CENTRO DE COMBATE POKÉMON (PvE)")
    print("═"*40)

    mostrar_catalogo_disponible()

    mi_poke = None
    while mi_poke is None:
        seleccion = input("\n❯ Ingrese el ID de SU Pokémon para combatir: ")

        mi_poke = obtener_instancia_pokemon(seleccion)
        if mi_poke is None:
            print("\n[!] ID inválido o no encontrado en el catálogo. Intente de nuevo.")

    print("\n... Generando oponente aleatorio ...")

    ids_disponibles = list(CATALOGO_POKEMON.keys())
    id_rival = random.choice(ids_disponibles)
    poke_rival = obtener_instancia_pokemon(id_rival)

    print(f"\n¡Un {poke_rival.nombre} salvaje (Tipo: {poke_rival.tipo}) ha aparecido!")
    print(f"¡{mi_poke.nombre} está listo para el combate!")

    while mi_poke.esta_con_vida() and poke_rival.esta_con_vida():

        poke_rival.mostrar_interfaz(es_rival=True)
        mi_poke.mostrar_interfaz(es_rival=False)
        
        print("\n--- TU TURNO ---")
        print(" [1] Atacar   [2] Descansar   [3] Huir del Combate")

        try:
            opcion = input(" Seleccione una acción (1-3): ")
            
            if opcion == "1":
                mi_poke.atacar(poke_rival)

                if not poke_rival.esta_con_vida():
                    break

                turno_rival(poke_rival, mi_poke)
                
            elif opcion == "2":
                mi_poke.descansar()

                turno_rival(poke_rival, mi_poke)
                
            elif opcion == "3":
                print("\ Has huido del combate... ¡Cobarde!")
                break
                
            else:
                print("\n[!] Opción inválida, por favor elija 1, 2 o 3.")
                
        except Exception as e:

            print(f"\n[!] Ocurrió un error inesperado: {e}. Intente de nuevo.")

    # --- Resultados del Combate ---
    print("\n" + "═"*40)
    print("         FIN DEL COMBATE")
    print("═"*40)
    
    if not mi_poke.esta_con_vida():
        print(f"\n{mi_poke.nombre} se ha debilitado. ¡Has perdido!")
    elif not poke_rival.esta_con_vida():
        print(f"\n¡{poke_rival.nombre} se ha debilitado! ¡ERES EL GANADOR!")

if __name__ == "__main__":
    principal()
