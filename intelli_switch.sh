#!/bin/sh
set -e

exit_()
{
    exit
}

check_phone=false
while true
do
    ping -w 1 192.168.0.100 &> /dev/null && phone_connected=true || phone_connected=false

    if [[ $(date +%H:%M) = '06:00' ]]
    then
        python pi_gpio.py 1
        check_phone=true

    elif [[ $check_phone = false ]] || [[ $phone_connected = true ]]
    then
        # ping -w 1 192.168.0.100 &> /dev/null && python pi_gpio.py 1 || python pi_gpio.py 0
        check_phone=false
    fi

    sleep 0.1
    trap exit_ int
done
