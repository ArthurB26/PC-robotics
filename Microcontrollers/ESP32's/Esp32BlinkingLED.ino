# Quick demo file that blinks the inbnuilt led of the esp32 dev module
#################################
# No extra hardware required, make sure the esp32 dev kit is selected and it is on the right port.

// initialize program
void setup() { 
  // Set GPIO2 as output (assuming onboard LED is connected to GPIO2)
  pinMode(2, OUTPUT);
}


# loop
void loop() {
  digitalWrite(2, HIGH);  // Turn the LED on
  delay(1000);             // Wait for 1 second
  digitalWrite(2, LOW);   // Turn the LED off
  delay(1000);             // Wait for 1 second
}
