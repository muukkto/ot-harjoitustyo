import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaatteessa_on_aluksi_oikeat_tilastot(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)



    def test_edulliset_kateisosto_riittaa_rahat_kassa_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_edulliset_kateisosto_riittaa_rahat_vaihtoraha_oikein(self):

        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_edulliset_kateisosto_riittaa_rahat_myyty_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.edulliset, 1)


    
    def test_edulliset_kateisosto_ei_riita_rahat_kassa_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_edulliset_kateisosto_ei_riita_rahat_vaihtoraha_oikein(self):

        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_edulliset_kateisosto_ei_riita_rahat_myyty_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 0)




    def test_maukkaat_kateisosto_riittaa_rahat_kassa_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)

    def test_maukkaat_kateisosto_riittaa_rahat_vaihtoraha_oikein(self):

        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_maukkaat_kateisosto_riittaa_rahat_myyty_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    
    def test_maukkaat_kateisosto_ei_riita_rahat_kassa_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_maukkaat_kateisosto_ei_riita_rahat_vaihtoraha_oikein(self):

        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_maukkaat_kateisosto_ei_riita_rahat_myyty_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.maukkaat, 0)



    def test_edulliset_korttiosto_saldo_riittaa_rahat_veloitetaan(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)
    
    def test_edulliset_korttiosto_saldo_riittaa_palautetaan_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_edulliset_korttiosto_saldo_riittaa_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edulliset_korttiosto_saldo_riittaa_kassapaate_saldo_ei_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)



    def test_edulliset_korttiosto_saldo_ei_riita_rahoja_ei_veloiteta(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo_euroina(), 2)
    
    def test_edulliset_korttiosto_saldo_ei_riita_palautetaan_false(self):
        maksukortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)

    def test_edulliset_korttiosto_saldo_ei_riita_maara_ei_kasva(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 0)



    def test_maukkaat_korttiosto_saldo_riittaa_rahat_veloitetaan(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)
    
    def test_maukkaat_korttiosto_saldo_riittaa_palautetaan_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_maukkaat_korttiosto_saldo_riittaa_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukkaat_korttiosto_saldo_riittaa_kassapaate_saldo_ei_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)



    def test_maukkaat_korttiosto_saldo_ei_riita_rahoja_ei_veloiteta(self):
        maksukortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo_euroina(), 3)
    
    def test_maukkaat_korttiosto_saldo_ei_riita_palautetaan_false(self):
        maksukortti = Maksukortti(300)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)

    def test_edulliset_korttiosto_saldo_ei_riita_maara_ei_kasva(self):
        maksukortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_kortille_ladataan_saldoa_kortin_saldo_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)

        self.assertEqual(self.maksukortti.saldo_euroina(), 12)

    def test_kortille_ladataan_saldoa_kassan_saldo_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002)

    def test_kortille_ei_voi_ladata_negatiivista(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
