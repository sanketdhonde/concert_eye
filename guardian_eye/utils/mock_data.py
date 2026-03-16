import random
import time

def generate_alerts(num_alerts):
    alerts = []
    for _ in range(num_alerts):
        alert = {
            'id': random.randint(1000, 9999),
            'type': random.choice(['INFO', 'WARNING', 'ERROR']),
            'message': f'Test alert message {random.randint(1, 100)}',
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()),
        }
        alerts.append(alert)
    return alerts

if __name__ == '__main__':
    num_alerts_to_generate = 10
    test_alerts = generate_alerts(num_alerts_to_generate)
    print(test_alerts)