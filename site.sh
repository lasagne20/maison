#!/bin/sh

sudo rm ./logs/site.log
sudo systemctl stop apache2.service
echo "apache2 : stopped"
sudo systemctl start apache2.service
echo "apache2 : started"
sleep 2
cat logs/site.log
tail -f ./logs/site.log

#cat logs/site.log
#tail -f ./logs/site.log
