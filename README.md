# Home Assistant Local Development Environment

This project sets up a local development environment for Home Assistant, allowing integration with various devices and services. It uses Docker Compose to orchestrate multiple containers, providing a comprehensive setup for testing and development.

## Components

- **Home Assistant**: The core home automation platform.
- **Mosquitto**: An MQTT broker for device communication.
- **Ecowitt2MQTT**: A bridge for Ecowitt-compatible weather stations.
- **InfluxDB**: Time series database for storing sensor data.
- **Grafana**: Data visualization and monitoring tool.
- **Weather Emulator**: A custom service that generates mock weather data.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone this repository:
```bash
git clone https://github.com/adomenech73/home-assistant-ldenv
cd home-assistant-ldenv
```
2. Build and start the services:
```bash
docker-compose up -d
```

## Accessing Services

- Home Assistant: http://localhost:8123
- Grafana: http://localhost:3000
- InfluxDB: http://localhost:8086

## Configuration

- Home Assistant configuration files are located in `./ha/config/`.
- Mosquitto configuration is in `./mqtt/config/mosquitto.conf`.
- InfluxDB data is stored in `./influxdb/`.
- Grafana data is stored in `./grafana/`.

## Weather Emulator

The Weather Emulator service generates mock weather data and publishes it to MQTT. You can configure its behavior using environment variables in the `docker-compose.yml` file.

## Customization

- Modify the `docker-compose.yml` file to add or remove services as needed.
- Adjust volume mappings to persist data or configurations.
- Add additional devices or integrations by extending the Home Assistant configuration.

## Troubleshooting

- Check container logs: `docker-compose logs [service_name]`
- Ensure all required ports are available on your host machine.
- Verify network connectivity between containers.

## Contributing

Contributions to improve this setup are welcome. Please submit pull requests or open issues for any enhancements or bug fixes.

## License

[MIT License](LICENSE)
