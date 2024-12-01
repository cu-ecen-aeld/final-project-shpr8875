import time
import bmp180sensor

while True:
    # Retrieve temperature, pressure, and altitude
    temp, pressure, altitude = bmp180sensor.readBmp180()

    # Print the results
    print("Temperature is:", temp, "°C")  # Temperature in degrees Celsius
    print("Pressure is:", pressure, "Pa")  # Pressure in Pascal
    print("Altitude is:", altitude, "m")  # Altitude in meters
    print("\n")
    time.sleep(2)  # Pause for 2 seconds