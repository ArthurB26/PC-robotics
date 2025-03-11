"""
    JackBord_Mqtt_Receiver.py

    11 March 2025 > This is for use with the JackBord BASIC, PRO or Virtual.

        It connects to the JackBord MQTT Server using your JackBords profile credentials
        and listens to the PID/# mqtt topic for data from your JackBord.

        Where PID is the JackBords dashboard profile ID.
        Mqtt messages sent to and from the JackBord are visable in the terminal.

    NOTE: You need to get the unique credentials for your JackBord as stated 
            in the repository readme.
"""
from datetime import datetime, timedelta
import paho.mqtt.client as mqtt
import uuid
import ssl
import time
import re


# MQTT broker configuration >>>>>>>>>
dest_broker = "wsa.jackbord.org"
dest_port = 443  # Secure WSS port

"""
MQTT Credentials from the Dashboard. >>>>>>>>>
    eg  from the JB BASIC Helper page URL:
        https://jb.works/basic?pid=Your pid&qtid=your id&pw=your pw&
"""
jb_pid = "your pid"
jb_username = "your id"
jb_password = "your pw"

# My Virtual JackBord
jb_pid = "10GT"
jb_username = "113568327219567611054"
jb_password = "176642e451"

"""
    JackBord MQTT Topics 
        We will subscribe to these topics.
"""
# JackBord Command Topic > Send commands to this topic.
jb_cmd_topic = jb_pid + "/cmd"

# jprint Topic > Has print output from the command line.
jprint_topic = jb_pid + "/jprint"

# data Topic > Has the state of the pins.
data_topic = jb_pid + "/data"

# po Topic > Shows the output of your program in the Print Tab.
po_topic = jb_pid + "/po"



# List to store new messages >>>>>>>>>>>>
message_queue = []

# Message to send when our program stops.
exitprog_message = "exitprog"

"""
    Setup the MQTT Server Connection
"""
# Define the callback function for connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker, on standby")

        # Subscribe the JackBord Topics >>>>>>>>
        client.subscribe(jb_cmd_topic)
        client.subscribe(jprint_topic)
        client.subscribe(data_topic)
        client.subscribe(po_topic)


        print(f"Subscribed to topics.")

        # Send a hi command to the JB when we connect
        send_jb_command("hi")

	    # Get the status
        send_jb_command("vs")

    else:
        print(f"Connection failed with code {rc}")


"""
    Get New MQTT Messages >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        This function is called when a new mqtt message is received.
        To keep things fast it will add the new message to a
        message que list variable called message_queue and exit.
        We will deal with the new messages later.
"""
def on_message(client, userdata, msg):

    # Declare as global variable
    global message_counter

    # Decode the message payload >>>>>>>>>>>>>>>>
    message = msg.payload.decode('utf-8')

    # Display the new message from the JackBord >>>>>>>>>>>>>>>>
    print(f"NEW>{message_counter}> Topic [{msg.topic}]\nMessage [{message}]")

    # Append the new message to the message queue >>>>>>>>>>>>>>>>
    message_queue.append(message)

    # Inc the message_counter
    message_counter += 1

# Define the callback function for disconnection
def on_disconnect(client, userdata, rc):
    print("Disconnected from broker")



# Send a New Command to the cmd topic >>>>>>>
def send_jb_command( command ):
    
    print(f"Send comamnd [{command}]")

    # Publish the command to the /cmd topic >>>>>>>>>>
    client.publish(jb_cmd_topic, command)



# Connect to the MQTT Server >>>>>>>>>>>> 
# Create an MQTT client instance
client_id = str(uuid.uuid4())
client = mqtt.Client(client_id=client_id, transport='websockets', protocol=mqtt.MQTTv311)

# Set username and password
client.username_pw_set(jb_username, jb_password)

# Assign the on_connect and on_disconnect callback functions
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# Configure SSL/TLS
ssl_context = ssl.create_default_context()
client.tls_set_context(ssl_context)

# Connect to the broker using WSS
client.ws_set_options(path="/mqtt")

# if the server uses a self-signed certificate, use this line carefully
client.tls_insecure_set(True)

# Start the MQTT client loop
client.connect(dest_broker, dest_port)
client.loop_start()

# Message Counter > Tracks the number of messges we received.
message_counter = 0

# Wait for New MQTT Messages in a loop >>>>>>>>>>
try:
    while True:

        # Process new MQTT messages on the message_queue
        while message_queue:

            # Get the first message in the queue
            new_message = message_queue.pop(0)
            # print(f"Process message: [{new_message}]")

            # Add any additional processing logic here >>>>>

        # Do other stuff in the main prog loop.
        print(f'Message count [{message_counter}]')

        # Delay so we dont load the system too much.
        time.sleep(1)


# Exit the program Loop. >>>>>>>>>>>>>
except KeyboardInterrupt:
    print("Exiting program. Good bye.")


# Send a final command to the JB before we disconnect.
send_jb_command(exitprog_message)


# Stop the MQTT client loop and disconnect
client.loop_stop()
client.disconnect()
