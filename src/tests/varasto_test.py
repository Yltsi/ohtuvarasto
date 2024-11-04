import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_arvot_ali_nollan(self):
        varasto = Varasto(tilavuus=-100, alku_saldo=-1000)
        assert varasto.tilavuus == 0.0
    
    def test_saldo_pienempi_kuin_tilavuus(self):
        varasto = Varasto(tilavuus=10, alku_saldo=100)
        assert varasto.saldo == 10
    
    def test_lisaa_neg(test):
        varasto = Varasto(tilavuus=100, alku_saldo=20)
        varasto.lisaa_varastoon(-10)
        assert varasto.saldo == 20

    def test_lisaa_liikaa(test):
        varasto = Varasto(tilavuus=100, alku_saldo=20)
        varasto.lisaa_varastoon(100)
        assert varasto.saldo == 100

    def test_ota_liikaa(test):
        varasto = Varasto(tilavuus=100, alku_saldo=20)
        varasto.ota_varastosta(100)
        assert varasto.saldo==0.0

    def test_ota_neg(test):
        varasto = Varasto(tilavuus=100, alku_saldo=20)
        varasto.ota_varastosta(-10)
        assert varasto.saldo==0

    def test_varasto_str():
        varasto = Varasto(tilavuus=100, alku_saldo=20)
        odotettu_tulos = "saldo = 20, vielä tilaa 80"
        assert str(varasto) == odotettu_tulos
    
    def test_varasto_str(self):
        varasto = Varasto(tilavuus=100, alku_saldo=20)
        odotettu_tulos = "saldo = 20, vielä tilaa 80"
        assert str(varasto) == odotettu_tulos

