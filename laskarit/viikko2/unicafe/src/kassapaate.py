class Kassapaate:
    def __init__(self):
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0

    def kateis_maksu(self, hinta, maksu, laskuri):
        if maksu >= hinta:
            self.kassassa_rahaa = self.kassassa_rahaa + hinta
            setattr(self, laskuri, getattr(self, laskuri) + 1)
            return maksu - hinta
        else:
            return maksu

    def kortti_maksu(self, hinta, kortti, laskuri):
        if kortti.saldo >= hinta:
            kortti.ota_rahaa(hinta)
            setattr(self, laskuri, getattr(self, laskuri) + 1)
            return True
        else:
            return False

    def syo_edullisesti_kateisella(self, maksu):
        return self.kateis_maksu(240, maksu, "edulliset")

    def syo_maukkaasti_kateisella(self, maksu):
        return self.kateis_maksu(400, maksu, "maukkaat")

    def syo_edullisesti_kortilla(self, kortti):
        return self.kortti_maksu(240, kortti, "edulliset")

    def syo_maukkaasti_kortilla(self, kortti):
        return self.kortti_maksu(400, kortti, "maukkaat")

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
        else:
            return

    def kassassa_rahaa_euroina(self):
        return self.kassassa_rahaa / 100
