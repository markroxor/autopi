#!/bin/sh
killall ngrok
~/ngrok  tcp  22 > /dev/null &
sleep 2
ip="$(curl http://localhost:4040/api/tunnels | jq ".tunnels[0].public_url")"
curl -X POST -H 'Content-type: application/json' --data "{\"text\":"$ip"}" $WEBHOOK
