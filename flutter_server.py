from flask import Flask, request, jsonify
import json
import RPi.GPIO as GPIO

def toggle_pin(pin, toggle=True):
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(pin, GPIO.OUT)
  state = GPIO.input(pin)

  if toggle and state == 0:
      GPIO.output(pin,GPIO.HIGH)
  elif toggle:
      GPIO.output(pin,GPIO.LOW)
  return int(not state)

app = Flask(__name__)

def return_text(text):
    response = json.dumps({"status": text})
    return str(response)


@app.route("/status/", methods=["POST"])
def get_status():
    if request.method == "POST":
          json_request = request.get_json()
          pin = json_request['pin']
          status = toggle_pin(pin, False)
          return return_text(status), 200


@app.route("/toggle/", methods=["POST"])
def toggle():
    if request.method == "POST":
          json_request = request.get_json()
          pin = json_request['pin']
          toggle_pin(pin, True)
          return return_text('Toggled..'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
