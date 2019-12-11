#!/bin/bash
# We want to change the backlight of monitor by a integer argument
# which stand for the value of backlight
# range: 0 ~ 937

pkexec /usr/lib/gnome-settings-daemon/gsd-backlight-helper --set-brightness $1
echo "The backlight has successfully set to $1 !"
