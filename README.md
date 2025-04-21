# Temperature and Humidity Monitoring System

This project implements a temperature and humidity monitoring system using a DHT sensor and Pycom microcontroller. The system reads environmental data and sends it to ThingSpeak for visualization and analysis.

## Components

- Pycom microcontroller
- DHT sensor (DHT11/DHT21/DHT22)
- WiFi connection
- ThingSpeak API

## Features

- Real-time temperature and humidity monitoring
- Automatic data logging to ThingSpeak
- LED status indication
- Configurable data collection interval (default: 30 minutes)

## Project Structure

- `main.py`: Main application code that handles sensor reading and data transmission
- `dth.py`: DHT sensor driver implementation
- `connection.py`: WiFi connection management (referenced but not shown in repository)

## Setup

1. Connect the DHT sensor to pin P3 of your Pycom device
2. Configure your WiFi credentials in the `connection.py` file
3. Update the ThingSpeak API key in `main.py` with your channel's API key
4. Upload the code to your Pycom device

## Configuration

- The data collection interval can be modified by changing the `time.sleep()` value in `main.py`
- The sensor type can be configured in the DTH class initialization (0 for DHT11, 1 for DHT21/DHT22)

## Usage

1. Power on the device
2. The system will automatically:
   - Connect to WiFi
   - Read temperature and humidity data
   - Send data to ThingSpeak
   - Display a green LED when data is being collected
   - Wait for the configured interval before the next reading

## Dependencies

- Pycom firmware
- Network module
- Machine module
- Socket module
- SSL module
- Time module

## Troubleshooting

- If the LED doesn't turn green, check the sensor connection
- If data isn't being sent to ThingSpeak, verify:
  - WiFi connection
  - API key configuration
  - Internet connectivity

## License

This project is open source and available under the MIT License. 