#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes
import radiopy

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

    c = radiopy.Player('PCM')
    c.stop()


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
