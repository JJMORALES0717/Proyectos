# ====================================================================
 SISTEMA POKÉMON 
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


