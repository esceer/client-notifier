class MqttClient:
    from config.config import Config

    def __init__(self, config: Config):
        import paho.mqtt.client as mqtt
        self._client = mqtt.Client("client-notifier")
        self._client.connect(config.get_mqtt_host(), config.get_mqtt_port())
        self._client.subscribe(config.get_mqtt_topic())
        self._client.loop_forever(config.get_mqtt_read_timeout())

    def handle_message(self, handler_fn):
        self._client.on_message = handler_fn
