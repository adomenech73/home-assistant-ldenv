import paho.mqtt.client as mqtt
import signal
import time
import random
import json
import os
from datetime import datetime

# MQTT Configuration
MQTT_BROKER = os.getenv("MQTT_BROKER", "mosquitto")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "weather/sainlogic")

# Weather data ranges (adjust as needed)
TEMP_RANGE = (float(os.getenv("TEMP_MIN", -10)), float(os.getenv("TEMP_MAX", 40)))
HUMIDITY_RANGE = (
    float(os.getenv("HUMIDITY_MIN", 20)),
    float(os.getenv("HUMIDITY_MAX", 90)),
)
PRESSURE_RANGE = (
    float(os.getenv("PRESSURE_MIN", 950)),
    float(os.getenv("PRESSURE_MAX", 1050)),
)
WIND_SPEED_RANGE = (
    float(os.getenv("WIND_SPEED_MIN", 0)),
    float(os.getenv("WIND_SPEED_MAX", 100)),
)
WIND_DIR_RANGE = (
    float(os.getenv("WIND_DIR_MIN", 0)),
    float(os.getenv("WIND_DIR_MAX", 359)),
)
RAIN_RANGE = (float(os.getenv("RAIN_MIN", 0)), float(os.getenv("RAIN_MAX", 50)))

# Update frequency in seconds
UPDATE_FREQUENCY = int(os.getenv("UPDATE_FREQUENCY", 60))


def graceful_shutdown(signum, frame):
    print("Received shutdown signal. Stopping the weather data generator.")
    client.loop_stop()
    client.disconnect()
    exit(0)


def generate_weather_data():
    return {
        "temperature": round(random.uniform(*TEMP_RANGE), 1),
        "humidity": round(random.uniform(*HUMIDITY_RANGE), 1),
        "pressure": round(random.uniform(*PRESSURE_RANGE), 1),
        "wind_speed": round(random.uniform(*WIND_SPEED_RANGE), 1),
        "wind_direction": round(random.uniform(*WIND_DIR_RANGE), 0),
        "rainfall": round(random.uniform(*RAIN_RANGE), 1),
        "timestamp": datetime.now().isoformat(),
    }


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


client = mqtt.Client()
client.on_connect = on_connect

client.connect(MQTT_BROKER, MQTT_PORT, 60)

client.loop_start()

signal.signal(signal.SIGTERM, graceful_shutdown)
signal.signal(signal.SIGINT, graceful_shutdown)

try:
    while True:
        weather_data = generate_weather_data()
        client.publish(MQTT_TOPIC, json.dumps(weather_data))
        print(f"Published: {weather_data}")
        time.sleep(UPDATE_FREQUENCY)

except Exception as e:
    print(f"An error occurred: {e}")
    client.loop_stop()
    client.disconnect()
    exit(1)
