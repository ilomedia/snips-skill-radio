#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import subprocess
import playsound

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"


class SnipsConfigParser(configparser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.read_file(f)
            return conf_parser.to_dict()
    except (IOError, configparser.Error) as e:
        return dict()


def subscribe_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)

    if intentMessage.asr_confidence < float(conf['global']['confidence_threshold']):
        hermes.publish_end_session(intentMessage.session_id)
    else:
        action_wrapper(hermes, intentMessage, conf)


def action_wrapper(hermes, intentMessage, conf):

    hermes.publish_end_session(intentMessage.session_id, "")

    playsound.playsound('http://direct.franceinter.fr/live/franceinter-midfi.mp3', False)

    # subprocess.Popen(['amixer', '-c', '1', 'sset', '"PCM"', '50%'])
    #
    # pid = None
    # pid = subprocess.Popen(['mplayer', '-quiet', 'http://rai.ice.infomaniak.ch/rai-64.aac?type=.flv']).pid
    #
    # fpid = open("/tmp/mplayer-id", "w+")
    # fpid.write(str(pid))
    # fpid.close()
    #
    # print("pid: " + str(pid))


if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("duch:play", subscribe_intent_callback).start()

