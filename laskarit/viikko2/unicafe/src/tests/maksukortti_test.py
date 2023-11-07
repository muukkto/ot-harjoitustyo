import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldon_merkkijonoesitys_toimii(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_rahan_lisaaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 15)

    def test_rahan_ottaminen_pienentaa_saldoa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5)

    def test_rahan_ottaminen_ei_vaikuta_saldon_jos_ei_rahaa(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_rahan_ottaminen_palauttaa_true_jos_tarpeeksi_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
    
    def test_rahan_ottaminen_palauttaa_false_jos_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)
    
