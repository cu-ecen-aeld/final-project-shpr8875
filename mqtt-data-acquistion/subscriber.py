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
import lcd_display

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

   # Decode the message payload (assumed to be the sensor data string)
    sensor_data = msg.payload.decode()
    
    print(f"Message received: {sensor_data}")

    # Split the message into individual parts: Temperature, Pressure, Altitude
    parts = sensor_data.split(", ")

    # Extract temperature, pressure, and altitude data from the parts
    temp_str = parts[0] 
    pressure_str = parts[1]  
    altitude_str = parts[2]  

    # Formatting the first and second lines for the LCD
    line1 = f"T:{temp_str.split(':')[1]} P:{pressure_str.split(':')[1]}"
    line2 = f"Alt:{altitude_str.split(':')[1]}"

    # Displaying the data on the LCD
    lcd_display.display_string(line1, line=1)  # Display temperature and pressure on the first line
    lcd_display.display_string(line2, line=2)  # Display altitude on the second line


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

