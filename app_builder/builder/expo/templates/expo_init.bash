#!/bin/bash

name="template"
sudo npm install -g expo-cli
sudo npm install axios
sudo expo init $name

# dont work run by hand
#cd $name

sudo npm start
sudo chown -R idegtyarev:idegtyarev ./