class SignalDetection:
    def __init__(self, hits, false_alarms, misses, correct_rejections):
        self.hits = hits
        self.false_alarms = false_alarms
        self.misses = misses
        self.correct_rejections = correct_rejections

    def hit_rate(self):
        if (self.hits + self.misses) == 0:
            return 0
        return self.hits / (self.hits + self.misses)

    def false_alarm_rate(self):
        if (self.false_alarms + self.correct_rejections) == 0:
            return 0
        return self.false_alarms / (self.false_alarms + self.correct_rejections)
