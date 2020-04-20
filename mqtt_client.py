#!/usr/bin/env python3

# Standard Libraries
import argparse

# Third-party Libraries
import paho.mqtt.client as mqtt


class LampController(object):
    def __init__(self):
        self.args = self.parse_args()
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def parse_args(self):
        parser = argparse.ArgumentParser(
            description='Connects Lamp Controller to the MQTT network')
        parser.add_argument('--host', type=str,
                            help='Hostname or IP address of MQTT broker')
        parser.add_argument('--port', '-p', type=int, default=1883,
                            help='Port number of MQTT broker')
        parser.add_argument('--serial', '-s', type=str,
                            help='Serial port to Lamp Controller')
        return parser.parse_args()

    def on_connect(self, client, userdata, flags, rc):
        print('Connected')
        client.subscribe('test/topic')
        client.message_callback_add('')

    def on_message(self, client, userdata, msg):
        print(msg.topic, msg.payload)

    def main(self):
        self.client.connect(self.args.host, self.args.port, 60)

        try:
            self.client.loop_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    lc = LampController()
    lc.main()
