# MQTT connection to the Jackbord
The jackbord can be accesed via MQTT. You can do most things such as sending/receiving commands and running programs.

## Finding the MQTT details for the Jackbord
To start using MQTT, you must first find the MQTT details of your Jackbord. Go to the connect page where you connect the Jackbord to serial. In the URL bar, look for a long digit string (about 21 digits next to each other). This is your Jackbord's username for MQTT. Next, find the 10-character string after the username in the URL. This is the Jackbord's MQTT password. Lastly, find your Jackbord's topic, which can be found by entering "hi" into the Jackbord dashboard. The Jackbord will return "Hello from 10xx", with "xx" being two capital letters. You are now ready to move on to setting up the editor for running the program.

## Setting up MQTT for GitHub Codespaces
Once you have set up a GitHub Codespace, go to the terminal and enter:

    pip install paho-mqtt paho-mqtt-client uuid ssl
This will install all of the required modules for the Python script.

Using the Jackbord's MQTT details from earlier,  replace the YOUR_USERNAME, YOUR_PASSWORD and 10xx/cmd with the information you have found. You can also replace the MQTT programs as well if you would like to.