#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes
import subprocess

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

    subprocess.Popen(['amixer', '-c', '1', 'sset', '"PCM"', '50%'])

#    c = radiopy.Player('PCM')
#    c.play("Radio Algérie Internationale")

    pid = None
    pid = subprocess.Popen(['mplayer', '-quiet', 'http://rai.ice.infomaniak.ch/rai-64.aac?type=.flv']).pid

    fpid = open("/tmp/mplayer-id", "w")
    fpid.write(pid)
    fpid.close()

    print("pid: " + str(pid))


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
