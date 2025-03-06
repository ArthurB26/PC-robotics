import paho.mqtt.client as mqtt
import uuid
import ssl
import time

# MQTT broker configuration
dest_broker = "wsa.jackbord.org" # Server where mqtt is handled
dest_port = 443  # WSS port, do not touch
dest_username = "YOUR_USERNAME" # 21-digit code found on the connection page in google
dest_password = "YOUR_PASSWORD" # 10-character string found on the connection page after the username
dest_topic = "10xx/cmd" # Replace "xx" with the two characters from your Jackbord name

# MQTT Programs (Optional)
boot = "hi" # This will be run once the Python code is run
prog = "runu 1" # Run the first program loaded on the Jackbord
exitprog = "exitprog" # This will be sent to stop a program

# Connect to Jackbord
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker, on standby")
        client.publish(dest_topic, boot)  # Run "boot" command on connection
    else:
        print(f"Connection failed with code {rc}")

# Disconnect from Jackbord
def on_disconnect(client, userdata, rc):
    print("Disconnected from broker")

# Create a MQTT client instance
client_id = str(uuid.uuid4())
client = mqtt.Client(client_id, transport='websockets')

# Set username and password
client.username_pw_set(dest_username, dest_password)

# Assign the on_connect and on_disconnect callback functions
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# Configure SSL/TLS
ssl_context = ssl.create_default_context()
client.tls_set_context(ssl_context)

# Connect to the broker using WSS
client.ws_set_options(path="/mqtt")
client.tls_insecure_set(True)  # if the server uses a self-signed certificate, use this line carefully

# Start the MQTT client loop
client.connect(dest_broker, dest_port)
client.loop_start()

# Run "hi" then "run1" after 3 seconds
client.publish(dest_topic, boot)
time.sleep(3)
client.publish(dest_topic, prog)

# Exit program after 10 seconds
time.sleep(10)
print("Exiting program")
client.publish(dest_topic, exitprog)