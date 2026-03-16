class AISituationalSynthesis:
    def __init__(self):
        self.alerts = []

    def add_alert(self, alert):
        """Add a new alert to the system."""
        self.alerts.append(alert)

    def generate_summary(self):
        """Generate a summary from the collected alerts."""
        if not self.alerts:
            return "No alerts to summarize."
        summary = "Aggregate Alerts Summary:\n"
        for alert in self.alerts:
            summary += f"- {alert}\n"
        return summary.strip()  

# Example usage:
# synthesizer = AISituationalSynthesis()
# synthesizer.add_alert('Alert 1: Fire detected at location A.')
# synthesizer.add_alert('Alert 2: Flood warning issued.')
# print(synthesizer.generate_summary())