import configparser


class Config:
    def __init__(self):
        self._config_file_path = '../resources/cn.ini'
        self._config = self._parse_config_file()

    def get_mqtt_host(self) -> str:
        return self._config['Mqtt']['host']

    def get_mqtt_port(self) -> int:
        return int(self._config['Mqtt']['port'])

    def get_mqtt_topic(self) -> str:
        return self._config['Mqtt']['topic']

    def get_mqtt_read_timeout(self) -> float:
        return float(self._config['Mqtt']['loop-timeout-seconds'])

    def get_smtp_server_host(self) -> str:
        return self._config['Email']['smtp-server-host']

    def get_smtp_port(self) -> str:
        return self._config['Email']['smtp-server-port']

    def get_smtp_password(self) -> str:
        return self._config['Email']['smtp-server-password']

    def get_smtp_sender(self) -> str:
        return self._config['Email']['sender']

    def get_email_recipient_list(self) -> list:
        return self._config['Email']['recipients'].split(",")

    def _parse_config_file(self) -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        config.read(self._config_file_path)
        return config
