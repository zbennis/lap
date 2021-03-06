# source : https://tutorials-raspberrypi.de/datenaustausch-raspberry-pi-mqtt-broker-client/
import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost"
MQTT_TOPIC_TEMP = "temperature"
MQTT_TOPIC_HUM = "humidity"
MQTT_TOPIC_CO2 = "co2"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TOPIC_TEMP)
    client.subscribe(MQTT_TOPIC_HUM)
    client.subscribe(MQTT_TOPIC_CO2)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # more callbacks, etc

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
