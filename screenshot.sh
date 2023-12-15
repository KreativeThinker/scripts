#! /bin/bash

#-- screenshot --#
# Clean script to take a screenshot
# copy to clipboard, and display a notification
# if the user would like to save it.
# Dependencies:
#	- dunst
#	- maim
#	- slop
# ~ ADIGEN

scrot='maim -squl -b 3 -m 10 -c 0.8,0.6,0.9,0.3'
notifier='dunstify'
filenameFormat='%Y-%m-%d-%T.png'
fileSaveLoc=`echo $HOME/Pictures/Screenshots/$(date +${filenameFormat})`
fileCacheLoc="/tmp/screenshot_cache_temp.png"

${scrot} ${fileCacheLoc} &&
xclip -selection clipboard -t image/png -i ${fileCacheLoc} &&
cp ${fileCacheLoc} ${fileSaveLoc} &&
save=`${notifier} -t 5000 -r '12345' Screenshot "Copied to clipboard!<br><b>Right click to save</b>" -i ${fileCacheLoc} -A "yes, "`

if [[ ${save} = "yes" ]]; then
	cp ${fileCacheLoc} ${fileSaveLoc}
	${notifier} -t 3000 -r '12345' Screenshot "Saved to ${fileSaveLoc}!"
fi
