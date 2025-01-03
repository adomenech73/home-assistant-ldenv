# Weather Emulator

## Description
This Python script generates mock weather data and publishes it to an MQTT broker. It's designed to simulate a weather station, providing random but realistic weather data at regular intervals.

## Features
- Generates mock data for temperature, humidity, pressure, wind speed, wind direction, and rainfall
- Publishes data to an MQTT broker
- Configurable data ranges and update frequency
- Designed to work within a Docker environment

## Requirements
- Python 3.9+
- paho-mqtt 1.6.1

## Installation
This project uses uv for dependency management. To set up the project:

1. Ensure you have Python 3.9+ and uv installed.
2. Clone this repository.
3. Navigate to the project directory.
4. Run `uv pip install .` to install dependencies.

## Usage
To run the script:
```bash
python weather_emulator.py
```
The script will connect to the MQTT broker specified in the configuration and start publishing weather data.

## Configuration
You can modify the following variables in the script to adjust the behavior:

- `MQTT_BROKER`: The address of your MQTT broker (default: "mosquitto")
- `MQTT_PORT`: The port of your MQTT broker (default: 1883)
- `MQTT_TOPIC`: The MQTT topic to publish weather data (default: "weather/sainlogic")
- Weather data ranges (e.g., `TEMP_RANGE`, `HUMIDITY_RANGE`, etc.)
- Update frequency (default: 60 seconds)

## Docker Usage
This script is designed to be run in a Docker container. A Dockerfile is provided in the repository. To build and run the Docker container:

1. Build the image: `docker build -t weather-emulator .`
2. Run the container: `docker run --network host weather-emulator`

## Contributing
Contributions to improve the script or extend its functionality are welcome. Please feel free to submit pull requests or open issues for any bugs or feature requests.