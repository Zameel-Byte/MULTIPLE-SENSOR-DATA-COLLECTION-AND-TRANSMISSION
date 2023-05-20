# Sensor Data Collection and Transmission

This project collects data from various sensors and transmits it to the ThingSpeak platform using the Bolt IoT device. The collected data includes temperature, moisture, and light sensor readings. The project aims to provide real-time environmental data for analysis, monitoring, and visualization.

## Features

- Collects sensor data from temperature, moisture, and light sensors.
- Converts raw sensor data into real-world values.
- Transmits data to the ThingSpeak platform for storage and analysis.
- Easy setup and integration with the Bolt IoT device.
- Customizable code for adding more sensors or modifying functionality.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies (Bolt Python library).
3. Connect the Bolt IoT device to your hardware setup (temperature, moisture, and light sensors).
4. Configure the Bolt IoT device by providing your API key and device ID.
5. Run the main Python script to start collecting and transmitting sensor data.

```bash
python main.py
```
Make sure to update the configuration variables (API_KEY, DEVICE_ID, THINGSPEAK_API_KEY, etc.) in the main.py script according to your setup and ThingSpeak account.

## Dependencies
Bolt Python library (Install using pip install boltiot)

## Circuit Diagram 
<img src="https://github.com/Zameel-Byte/MULTIPLE-SENSOR-DATA-COLLECTION-AND-TRANSMISSION/blob/main/Bolt%20IoT%20multiplexed_bb.jpg"

## ThingSpeak Graphs
<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/2155566/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Bolt+IoT+Multiplexed+Temperature&type=column"></iframe>

<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/2155566/charts/2?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Bolt+IoT+Multiplexed+Moisture+%25&type=spline"></iframe>

<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/2155566/charts/3?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Bolt+IoT+Multiplexed+Sun+Light&type=spline"></iframe>

## Contributing
Contributions to this project are welcome. You can contribute by adding new features, fixing bugs, or improving the documentation. Please follow the standard GitHub workflow for contributing to this project.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Bolt IoT](https://www.boltiot.com/) for providing the IoT platform and hardware.
- [ThingSpeak](https://thingspeak.com/) for the data storage and visualization platform.
- Python community for the rich ecosystem of libraries and tools used in this project.
