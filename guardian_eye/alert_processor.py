import json
import logging

class AlertProcessor:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.alerts = []

    def add_alert(self, alert):
        if isinstance(alert, dict):
            self.alerts.append(alert)
            logging.info(f"Alert added: {json.dumps(alert)}")
        else:
            logging.error("Invalid alert format. Must be a dictionary.")

    def process_alerts(self):
        for alert in self.alerts:
            self.handle_alert(alert)
        self.alerts.clear()  # Clear alerts after processing

    def handle_alert(self, alert):
        logging.info(f"Processing alert: {json.dumps(alert)}")
        # Implement specific alert handling logic here

    def get_alerts(self):
        return self.alerts

# Example usage
if __name__ == '__main__':
    processor = AlertProcessor()
    processor.add_alert({"type": "temperature", "value": 37.5})
    processor.process_alerts()