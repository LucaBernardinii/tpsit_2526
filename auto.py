class Veicolo:
    def __init__(self, tipo_motore, posti)
    self.tipo_motore = tipo_motore
    self.posti = posti

    def descrizione(self):
        return f"Veicolo con motore {self.tipo_motore} e {self.posti} posti."

class Auto(Veicolo):
    def __init__(self, tipo_motore, posti, numero_porte)
        super().__init__(tipo_motore, posti)
        self.numero_porte = numero_porte

    def descrizione(self):
        return f"Auto con motore {self.tipo_motore}, {self.posti} posti e {self.numero_porte} porte."