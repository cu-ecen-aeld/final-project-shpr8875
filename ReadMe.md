# Climate Change Monitoring System

## Project Overview
- https://github.com/cu-ecen-aeld/final-project-shpr8875/wiki

### Project Goals:
- Efficiently monitor environmental conditions (temperature and humidity).
- Communicate sensor data between devices over MQTT.
- Display real-time sensor data on UART on the second Raspberry Pi.
- Use Yocto to create a customized build for the Raspberry Pi 3B platform.

## Source Code Organization
- The **Yocto build environment** will be hosted at [Yocto-Climate-Change-Monitoring-Repo](cu-ecen-aeld/final-project-Induja21).
- The **MQTT communication and sensor data processing code** will be hosted in a separate repository at [Climate-Monitoring-App](https://github.com/cu-ecen-aeld/final-project-shpr8875).

## Group Overview
- This project is being completed with a group of two members:
| Team Member       | Responsibility                                                                                  |
|-------------------|-------------------------------------------------------------------------------------------------|
| Induja Narayanan  | - Add required layers to the Yocto<br> Configuring I2C in Yocto<br> - MQTT server and client communication establishment & script creation<br>- Feasibility of adding RUST |
| Shweta Prasad    | - Initial board bring up by loading yocto on Raspberry Pi 3B <br>- Creation of application script to read the sensor data via I2C<br>- Enabling UART in Yocto<br>- Integration and test|

- Shweta Prasad (shweta.prasad@colorado.edu)
- Induja Narayanan (induja.narayanan@colorado.edu)

## Schedule Page
- A shared schedule and milestones for the project can be found at [[Project Schedule](https://github.com/users/Induja21/projects/1/views/1)].
