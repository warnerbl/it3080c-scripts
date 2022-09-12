#!/bin/bash


greeting="This is a script. Hello!"
echo $greeting, thanks for joining us!
echo '$greeting, thanks for joining us! You owe me $20'
echo "$greeting, thanks for joining us!"
echo "$greeting, you owe me \$20

echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session length: $SECONDS
echo Home Dir: $HOME"

a=$(ip a | grep 'noprefixroute ens192'| awk '{print $2}')
echo My IP is $a
