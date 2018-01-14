# MQTT Client 
# Continualy monitor two different MQTT topics for data
# Check if the received data matches the predefined 'commands'

import paho.mqtt.client as mqtt

#The callback for when the client receives a COMM
def on_connect
