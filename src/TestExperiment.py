import unittest
from Experiment import Experiment
from SignalDetection import SignalDetection

class TestExperiment(unittest.TestCase):

    def test_add_condition(self):
        exp = Experiment()
        sdt = SignalDetection(30, 10, 20, 40)
        exp.add_condition(sdt, "Test Condition")
        self.assertEqual(len(exp.conditions), 1)

    def test_sorted_roc_points(self):
        exp = Experiment()
        exp.add_condition(SignalDetection(40, 10, 20, 30), "A")
        exp.add_condition(SignalDetection(30, 15, 25, 30), "B")
        fa_rates, hit_rates = exp.sorted_roc_points()
        self.assertEqual(sorted(fa_rates), fa_rates)

    def test_compute_auc(self):
        exp = Experiment()
        exp.add_condition(SignalDetection(50, 10, 10, 30), "A")
        exp.add_condition(SignalDetection(30, 5, 20, 45), "B")
        auc = exp.compute_auc()
        self.assertTrue(0 <= auc <= 1)

    def test_empty_experiment_error(self):
        exp = Experiment()
        with self.assertRaises(ValueError):
            exp.sorted_roc_points()
        with self.assertRaises(ValueError):
            exp.compute_auc()

if __name__ == '__main__':
    unittest.main()
