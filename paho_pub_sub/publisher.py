#source: https: //tutorials-raspberrypi.de/datenaustausch-raspberry-pi-mqtt-broker-client/
import paho.mqtt.publish as publish
import time
import random

MQTT_SERVER = "localhost"
MQTT_TOPIC_TEMP_ENV = "h4o/la1/environment/temperature" # env temp
MQTT_TOPIC_TEMP_SENS = "h4o/la1/sensor/temperature" # sensor temp
MQTT_TOPIC_PRESSURE = "h4o/la1/pressure" # luftdurck
MQTT_TOPIC_HUM = "h4o/la1/humidity" # relative luftfeuchtigkeit
MQTT_TOPIC_CO2 = "h4o/la1/co2" # co2

while True:
        temp_sens = random.randint(-50, 50)
        temp_env = random.randint(-15, 50)
        pressure = random.randint(1, 999999)
        hum = random.randint(0, 999999)
        co2 = random.randint(-100, 99999)
        print('Publishing sensor temperature value', temp_sens, sep = " : ")
        print('Publishing env temperature value', temp_env, sep = " : ")
        print('Publishing pressure value', pressure, sep = " : ")
        print('Publishing humidity value', hum, sep = " : ")
        print('Publishing co2 value', co2, sep = " : ")
        publish.single(MQTT_TOPIC_TEMP_SENS,temp_sens, 2, hostname = MQTT_SERVER)
        publish.single(MQTT_TOPIC_TEMP_ENV, temp_env, 2, hostname = MQTT_SERVER)
        publish.single(MQTT_TOPIC_PRESSURE,pressure, 2, hostname = MQTT_SERVER)
        publish.single(MQTT_TOPIC_HUM,hum, 2, hostname = MQTT_SERVER)
        publish.single(MQTT_TOPIC_CO2, co2, 2, hostname = MQTT_SERVER)
        time.sleep(3)