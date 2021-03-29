from config.config import Config
from mqtt.mqtt_client import MqttClient
from notifier.email_client import EmailNotifier

if __name__ == '__main__':
    config = Config()
    mqttClient = MqttClient(config)
    emailClient = EmailNotifier(config)
    mqttClient.handle_message(emailClient.send_email)
