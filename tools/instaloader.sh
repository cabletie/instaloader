#!/bin/bash -e
date
cd $HOME/Pictures
echo "MESSAGE=[instaloader]" `instaloader --quiet --fast-update eia365 2>&1`|logger --tag instaloader --journald 
$HOME/.local/bin/instaloader --quiet --fast-update eia365 |logger --journald
cd eia365
LATEST=`ls -t 2020*.jpg | head -n 1`
echo $LATEST
ln -sf $LATEST latest.jpg
echo "MESSAGE=[instaloader] Linked file:" $LATEST |logger --tag instaloader --journald
scale.py
