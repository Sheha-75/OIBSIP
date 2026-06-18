#!/bin/bash

sudo ufw default deny incoming
sudo ufw default allow outgoing

sudo ufw allow ssh
sudo ufw deny 80/tcp

sudo ufw enable
sudo ufw status verbose
