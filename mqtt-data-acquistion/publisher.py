#* ---------------------------------------------------------------------------------
# * @Author: Induja Narayanan <Induja.Narayanan@in.bosch.com>
# * ECEN 5713, Publisher.py
# * Fall 2024, Prof. Dan Walkes
# * University of Colorado at Boulder
# * ------------------------------------------------------------------------------------
# * This file implements publisher functionality of MQTT. 
# * --------------------------------------------------------------------------------------*/

import time
import paho.mqtt.client as mqtt
import bmp180sensor

# Broker details
hostname = "10.0.0.167"  # Broker address (use "localhost" for local broker or IP of remote broker)
broker_port = 1883      # MQTT port
topic = "Sensor data publisher"  # Topic to publish messages to

# Create MQTT client
client = mqtt.Client()

# Define the callback for successful connection
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code: " + str(rc))

# Set up callback for successful connection
client.on_connect = on_connect

# Connect to the broker
client.connect(hostname, broker_port, 60)

# Start the loop to process network traffic, handle callbacks, etc.
client.loop_start()

# Publish messages to the topic
try:
    while True:
        # Simulate sensor data (replace with actual sensor reading)
        #sensor_data = "Temperature: 25.5C, Humidity: 60%"  # Example sensor data


	# Get sensor data from the BMP180 sensor
        temp, pressure, altitude = bmp180sensor.readBmp180()

        # Display the sensor data into a string
        sensor_data = f"Temperature: {temp:.1f}C, Pressure: {pressure//1000}kPa, Altitude: {altitude:.2f}m"

        # Publish the message to the topic
        client.publish(topic, sensor_data)
        #print("Message published: " + sensor_data)
        
        print(f"Message published: {sensor_data}")
 
        # Wait for 5 seconds before sending the next message
        time.sleep(5)

except KeyboardInterrupt:
    print("Exiting program")

# Stop the loop when exiting
client.loop_stop()

