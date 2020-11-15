# POC - MQTT PUB/SUB - Java Client
## HOW TO
### PYTHON
python3 and pip3 are needed
#### START MOSQUITTO SERVER
To start the mosquitto mqtt broker, one has to run the command `sh ./start_mosquitto_broker.sh`
!!! Before running this command, you have to first install mosquitto `sudo apt-get install -y mosquitto mosquitto-clients` 
#### START PUBLISHER
`sh ./start_publisher.sh`
#### START SUBSCRIBER

#### START Java paho client subscriber
`cd ./mqtt-consumer`
`mvn clean compile`
`mvn spring-boot:run`
Once the spring boot app is started, the subsriber client starts listening to topics!