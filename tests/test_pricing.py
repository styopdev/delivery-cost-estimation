import unittest

from app.pricing import estimate_delivery_fee


class EstimateDeliveryFeeTests(unittest.TestCase):
    def test_estimates_heavy_deliveries_from_route_and_weight(self):
        self.assertEqual(estimate_delivery_fee(65, 50), 9400)
        self.assertEqual(estimate_delivery_fee(65, 400), 26900)

    def test_applies_minimum_fee(self):
        self.assertEqual(estimate_delivery_fee(0, 1), 700)

    def test_rejects_non_positive_weight(self):
        with self.assertRaises(ValueError):
            estimate_delivery_fee(65, 0)


if __name__ == "__main__":
    unittest.main()
