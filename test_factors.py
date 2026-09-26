import unittest

from factors import S1_FACTORS, adjusted_days


class TestFactors(unittest.TestCase):
    def test_all_factors_between_0_and_1(self):
        for name, value in S1_FACTORS.items():
            self.assertTrue(0 < value <= 1, name)

    def test_trader_sme_adjustment(self):
        self.assertEqual(adjusted_days(30.0, "Trader (SME)"), 7.5)

    def test_unknown_company_type(self):
        with self.assertRaises(ValueError):
            adjusted_days(10.0, "Retailer")


if __name__ == "__main__":
    unittest.main()
