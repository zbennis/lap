package de.neustasdwest.h4w.mqtt.subscriber.mqttconsumer;

import java.time.LocalDateTime;

import javax.annotation.PostConstruct;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MqttConsumerApplication implements MqttCallback {
	private static final String MQTT_SERVER = "tcp://127.0.0.1:1883";
	private static final String MQTT_TOPIC_TEMP_ENV = "ENV_TEMP";
	private static final String MQTT_TOPIC_TEMP_SENS = "SENSOR_TEMP";
	private static final String MQTT_TOPIC_PRESSURE = "PRESSURE";
	private static final String MQTT_TOPIC_HUM = "HUM";
	private static final String MQTT_TOPIC_CO2 = "CO2";


	public static void main(String[] args) {
		SpringApplication.run(MqttConsumerApplication.class, args);
	}

	@PostConstruct
	public void process() {
		try (MqttClient coronaLapClient = new MqttClient(MQTT_SERVER, "corona-lap")) {
			coronaLapClient.connect();
			coronaLapClient.subscribe(MQTT_TOPIC_TEMP_SENS, (topic,msg) -> {
				System.out.println("Received sensor temperature -> "+msg+ " at -> "+LocalDateTime.now());
			});
			coronaLapClient.subscribe(MQTT_TOPIC_TEMP_ENV, (topic,msg) -> {
				System.out.println("Received env temperature -> "+msg+ " at -> "+LocalDateTime.now());
			});
			coronaLapClient.subscribe(MQTT_TOPIC_PRESSURE, (topic,msg) -> {
				System.out.println("Received pressure -> "+msg+ " at -> "+LocalDateTime.now());
			});
			coronaLapClient.subscribe(MQTT_TOPIC_HUM, (topic,msg) -> {
				System.out.println("Received humiditiy -> "+msg+ " at -> "+LocalDateTime.now());
			});
			coronaLapClient.subscribe(MQTT_TOPIC_CO2, (topic,msg) -> {
				System.out.println("Received co2 -> "+msg+ " at -> "+LocalDateTime.now());
			});
		} catch (MqttException e) {
			System.err.println(e.getMessage());
		} 
	}

	@Override
	public void connectionLost(Throwable cause) {
		System.out.println("The connection was lost the cause is -> "+cause);
	}

	@Override
	public void messageArrived(String topic, MqttMessage message) throws Exception {
		System.out.println(topic + " :: " + message.getPayload());

	}

	@Override
	public void deliveryComplete(IMqttDeliveryToken token) {
		System.out.println("Delivery complete of -> "+token.toString());
	}
}
