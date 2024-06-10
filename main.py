import network
from machine import (Pin, PWM)
from micropyserver import MicroPyServer

# Motor configuration
class Motor:
    def __init__(self, pin1, pin2, pwm_pin):
        self.pin1 = Pin(pin1, Pin.OUT)
        self.pin2 = Pin(pin2, Pin.OUT)
        self.pwm = PWM(Pin(pwm_pin), freq=1000)

    def control(self, direction, speed):
        if direction == 'clockwise':
            self.pin1.on()
            self.pin2.off()
        elif direction == 'counterclockwise':
            self.pin1.off()
            self.pin2.on()
        else:  # stop
            self.pin1.off()
            self.pin2.off()
        self.pwm.duty(speed)

# Instantiating motors
right_motor = Motor(2, 15, 16)
left_motor = Motor(0, 4, 17)

# Wi-Fi configuration
SSID = 'xxxxx'
PASSWORD = 'xxxxx'
MAX_RETRIES = 3

# Wi-Fi connection function
def connect_wifi(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)

    retries = 0
    while not station.isconnected() and retries < MAX_RETRIES:
        retries += 1
        print(f"Trying to connect... ({retries}/{MAX_RETRIES})")
    if station.isconnected():
        print("Connected to network:", ssid)
        print("Network configuration:", station.ifconfig())
        return station
    else:
        raise RuntimeError("Failed to connect to Wi-Fi.")

try:
    station = connect_wifi(SSID, PASSWORD)
except RuntimeError as e:
    print(e)
    raise SystemExit("Check Wi-Fi settings and restart the device.")

# HTML page with control interface
html_base = """
<!DOCTYPE html>
<html>
<head>
    <title>Car Control</title>
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
        button {{ padding: 15px 30px; margin: 10px; font-size: 18px; cursor: pointer; }}
    </style>
</head>
<body>
    <h1>Car Control</h1>
    <button onclick="location.href='/forward'">Forward</button>
    <button onclick="location.href='/reverse'">Reverse</button>
    <br>
    <button onclick="location.href='/left'">Left</button>
    <button onclick="location.href='/stop'">Stop</button>
    <button onclick="location.href='/right'">Right</button>
</body>
</html>
"""

# Control functions
def control_motors(right_direction, right_speed, left_direction, left_speed, title):
    right_motor.control(right_direction, right_speed)
    left_motor.control(left_direction, left_speed)
    print(f"{title}: right={right_direction} ({right_speed}), left={left_direction} ({left_speed})")
    return html_base.replace("{title}", title)

# Server routes
def index(request):
    app.send(html_base.replace("{title}", "Car Control"))

def right(request):
    response = control_motors('clockwise', 950, 'stop', 0, "Right")
    app.send(response)
def left(request):
    response = control_motors('stop', 0, 'clockwise', 950, "Left")
    app.send(response)
def stop(request):
    response = control_motors('stop', 0, 'stop', 0, "Stop")
    app.send(response)
def forward(request):
    response = control_motors('clockwise', 950, 'clockwise', 950, "Forward")
    app.send(response)
def reverse(request):
    response = control_motors('counterclockwise', 950, 'counterclockwise', 950, "Reverse")
    app.send(response)


# Server initialization
app = MicroPyServer()

app.add_route("/", index)

app.add_route("/right", right)
app.add_route("/stop", stop)
app.add_route("/left", left)
app.add_route("/forward", forward)
app.add_route("/reverse", reverse)

print("Server started. Access the IP:", station.ifconfig()[0])
app.start()