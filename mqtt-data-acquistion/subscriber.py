#* ---------------------------------------------------------------------------------
# * @Author: Induja Narayanan <Induja.Narayanan@in.bosch.com>
# * ECEN 5713, Publisher.py
# * Fall 2024, Prof. Dan Walkes
# * University of Colorado at Boulder
# * ------------------------------------------------------------------------------------
# * This file implements subscriber functionality of MQTT.
# * --------------------------------------------------------------------------------------*/

import time
import paho.mqtt.client as mqtt

# Broker details
hostname = "localhost"  # Broker address
broker_port = 1883      # MQTT port
topic = "Sensor data publisher"  # Topic to subscribe to

# Create MQTT client
client = mqtt.Client()

# Define the callback for successful connection
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code: " + str(rc))
    client.subscribe(topic)  # Subscribe to the topic

# Define the callback for incoming messages
def on_message(client, userdata, msg):
    print("Message received: " + msg.payload.decode())  # Print received message

# Set up callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(hostname, broker_port, 60)

# Start the loop to process network traffic, handle callbacks, etc.
client.loop_start()

# Keep the program running
try:
    while True:
        time.sleep(1)  # Keep the program running to maintain the connection
except KeyboardInterrupt:
    print("Exiting program")

# Stop the loop if interrupted
client.loop_stop()

