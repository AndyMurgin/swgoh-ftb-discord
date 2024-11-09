#!/bin/sh

printf "Initializing application.properties...\n"
envsubst < "discord_bot/application.properties" | sponge "discord_bot/application.properties"
printf "application.properties has been updated.\n\n"

printf "Starting the bot...\n"
python3 ./main.py
