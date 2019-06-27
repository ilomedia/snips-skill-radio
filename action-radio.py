#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import os
import subprocess

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

    hermes.publish_end_session(intent_message.session_id, "")

    if intent_message.intent.intent_name == 'duch:play':

        subprocess.Popen(['amixer', '-c', '1', 'sset', '"PCM"', '50%'])

        pid = None
        pid = subprocess.Popen(['mplayer', '-quiet', 'http://rai.ice.infomaniak.ch/rai-64.aac?type=.flv']).pid

        fpid = open("/tmp/mplayer-id", "w+")
        fpid.write(str(pid))
        fpid.close()

        print("pid: " + str(pid))

    elif intent_message.intent.intent_name == 'duch:stop':

        fpid = open("/tmp/mplayer-id", "r")
        pid = fpid.read()
        fpid.close()

        os.kill(int(pid), 15)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()

