# MQTT Publish Demo
# Publish two messages to two different topics

import paho.mqtt.publish as publish

publish.single("Home/Temperature/Family_room", "70", hostname = "test.morquitto.org)
publish.single("Home/Temperature/Living_room", "72", hostname = "test.mosquitto.org")
print("Done")
