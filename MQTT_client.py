# MQTT Client 
# Continualy monitor two different MQTT topics for data
# Check if the received data matches the predefined 'commands'

import paho.mqtt.client as mqtt

#The callback for when the client receives a COMM
def on_connect(client, userdata, flags, rc):
  print("Connected with result code" +str(rc))
  
  #Subscribing in on_connect() if we lose the connection and
  #reconnect then subscriptions will be renewed
  client.subscribe("")
  client.subscribe("")
  
#The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
  print(
