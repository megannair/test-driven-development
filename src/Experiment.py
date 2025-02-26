import matplotlib.pyplot as plt

class Experiment:
    def __init__(self):
        self.conditions = []

    def add_condition(self, sdt_obj, label=None):
        self.conditions.append((sdt_obj, label))

    def sorted_roc_points(self):
        if not self.conditions:
            raise ValueError("No conditions have been added.")

        fa_rates = [sdt.false_alarm_rate() for sdt, _ in self.conditions]
        hit_rates = [sdt.hit_rate() for sdt, _ in self.conditions]

        sorted_indices = sorted(range(len(fa_rates)), key=lambda i: fa_rates[i])
        return ([fa_rates[i] for i in sorted_indices], [hit_rates[i] for i in sorted_indices])

    def compute_auc(self):
        fa_rates, hit_rates = self.sorted_roc_points()
        
        if len(fa_rates) < 2:
            raise ValueError("Not enough conditions to compute AUC.")

        auc = 0.0
        for i in range(1, len(fa_rates)):
            width = fa_rates[i] - fa_rates[i - 1]
            height = (hit_rates[i] + hit_rates[i - 1]) / 2
            auc += width * height

        return auc

    def plot_roc_curve(self, show_plot=True):
        fa_rates, hit_rates = self.sorted_roc_points()
        plt.plot(fa_rates, hit_rates, marker='o', linestyle='-')
        plt.xlabel("False Alarm Rate")
        plt.ylabel("Hit Rate")
        plt.title("ROC Curve")
        plt.show() if show_plot else None

