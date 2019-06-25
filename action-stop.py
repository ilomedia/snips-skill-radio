#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes
import os

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

    fpid = open("/tmp/mplayer-id", "r")
    pid = fpid.read()
    fpid.close()

    os.kill(int(pid), 15)

with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
