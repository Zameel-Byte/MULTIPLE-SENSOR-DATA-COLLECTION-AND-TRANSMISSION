from boltiot import Bolt
import time
import requests
import json

# Bolt Cloud API Configuration
api_key = "YOUR_API_KEY"
device_id = "YOUR_DEVICE_ID"
bolt = Bolt(api_key, device_id)

# ThingSpeak Configuration
THINGSPEAK_API_KEY = "YOUR_THINGSPEAK_WRITE_API_KEY"
THINGSPEAK_URL = f"https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}"

# Analog Pin
analog_pin = "A0"

# Multiplexing Digital Pins
pins = {
    "Temp": "0",
    "Mos": "1",
    "Lig": "2"
}

def select_sensor_type(sensor_type):
    """
    Selects a specific sensor by setting the corresponding digital pin to HIGH.
    Args:
        sensor_type (str): The type of sensor to select.
    """
    response = bolt.digitalWrite(pins[sensor_type], 'HIGH')
    print(f"{sensor_type} is selected and the response is {response}")
    time.sleep(60)

def deselect_sensors(sensor_type):
    """
    Deselects a specific sensor by setting the corresponding digital pin to LOW.
    Args:
        sensor_type (str): The type of sensor to deselect.
    """
    response = bolt.digitalWrite(pins[sensor_type], 'LOW')
    print(f"{sensor_type} is deselected and the response is {response}")
    time.sleep(60)

def get_sensor_data(pin, sensor_type):
    """
    Reads sensor data from the specified pin.
    Args:
        pin (str): The pin to read the sensor data from.
        sensor_type (str): The type of sensor being read.
    Returns:
        int: The sensor value.
    """
    select_sensor_type(sensor_type)
    response = bolt.analogRead(pin)
    print(f"Reading {sensor_type} data and response is {response}")
    deselect_sensors(sensor_type)
    data = json.loads(response)
    sensor_value = int(data["value"])
    return sensor_value

def send_to_thingspeak(data):
    """
    Sends sensor data to ThingSpeak.
    Args:
        data (dict): The sensor data to send.
    """
    payload = {
        "api_key": THINGSPEAK_API_KEY,
        "field1": data["temperature"],
        "field2": data["moisture"],
        "field3": data["light"]
    }
    requests.get(THINGSPEAK_URL, params=payload)
    print("Data sent to ThingSpeak")

def collect_and_transmit_data():
    """
    Collects sensor data and transmits it to ThingSpeak.
    """
    print("Collecting Sensors Data")
    temperature = get_sensor_data(analog_pin, "Temp")
    moisture = get_sensor_data(analog_pin, "Mos")
    light = get_sensor_data(analog_pin, "Lig")

    # Converting RAW data
    temp_val = temperature / 10
    moisture_percentage = 100 - (moisture / 1023.0) * 100

    # Prepare data in the desired format
    sensor_data = {
        "temperature": temp_val,
        "moisture": moisture_percentage,
        "light": light
    }

    # Send data to ThingSpeak
    send_to_thingspeak(sensor_data)

# Main program loop
while True:
    try:
        collect_and_transmit_data()
    except KeyboardInterrupt:
        print("Program terminated by user.")
        break
    except Exception as e:
        print("An error occurred:", str(e))
