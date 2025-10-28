from auto.py import Veicolo

class Moto(Veicolo):
    def __init__(self, tipo_motore, posti, tipo_manubrio):
        super().__init__(tipo_motore, posti)
        self.tipo_manubrio = tipo_manubrio

    def descrizione(self):
        return f"Moto con motore {self.tipo_motore}, {self.posti} posti e manubrio di tipo {self.tipo_manubrio}."