#!/bin/sh
killall ngrok
/home/pi/ngrok start --config=/home/pi/.ngrok2/ngrok.yml ssh &

sleep 10
ip="$(curl http://localhost:4040/api/tunnels | jq ".tunnels[0].public_url")" && echo $ip

WEBHOOK=$(cat /home/pi/slack_webhook.pvt)
curl -X POST -H 'Content-type: application/json' --data "{\"text\":"$ip"}" $WEBHOOK
