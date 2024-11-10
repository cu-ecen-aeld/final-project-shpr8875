# Climate Change Monitoring System

## Overview
The **Climate Change Monitoring System** is a project designed to monitor environmental data by utilizing two Raspberry Pi 3B devices. The primary goal of the project is to read data from a BMP280 sensor, which provides temperature and humidity readings, and transmit this data to another Raspberry Pi over MQTT. The second Raspberry Pi receives the data and displays it on UART. This system is built using the Yocto Project, which enables a customized, lightweight build for the Raspberry Pi hardware.

### Project Goals:
- Efficiently monitor environmental conditions (temperature and humidity).
- Communicate sensor data between devices over MQTT.
- Display real-time sensor data on UART on the second Raspberry Pi.
- Use Yocto to create a customized build for the Raspberry Pi 3B platform.

### Block Diagram



## Target Build System
- **Yocto** is the chosen build system to customize and streamline the build for Raspberry Pi 3B.

## Hardware Platform
- **Hardware Platform**: Raspberry Pi 3B
- **Support**: The project will be supported using Yocto, which provides the necessary tools and configurations for the Raspberry Pi 3B.
- **Documentation**: [Yocto Raspberry Pi Support Documentation](https://www.yoctoproject.org/docs/current/yocto-project-qs/yocto-project-qs.html)
- **Hardware Requirements**: Two Raspberry Pi 3B boards. These will either be sourced directly or borrowed from the department.

## Open Source Projects Used
- The project will use the **Mosquitto MQTT broker** for enabling MQTT communication between the Raspberry Pis.
- **BMP280 Sensor Drivers** will be used for reading sensor data.

## Previously Discussed Content
- **MQTT Communication**: Concepts covered in previous lectures.
- **UART Display**: Techniques for serial communication as discussed in lectures.

## New Content
- **Yocto Build System for Raspberry Pi 3B**: This project will explore Yocto’s capabilities for creating a custom Linux distribution for the Raspberry Pi 3B.
- **BMP280 Sensor Integration**: Working with sensors in Yocto, which has not been covered in detail in class.

## Shared Material
- This project does not leverage any components from previous semesters or coursework.

## Source Code Organization
- The **Yocto build environment** will be hosted at [Yocto-Climate-Change-Monitoring-Repo](TBD).
- The **MQTT communication and sensor data processing code** will be hosted in a separate repository at [Climate-Monitoring-App](TBD).
- Additional repositories may be created if more applications are added to the project.

## Group Overview
This project is being completed individually.

## Schedule Page
- A shared schedule and milestones for the project can be found at [Project Schedule](TBD).
