#!/usr/bin/bash

red='\u001b[31m'
green='\e[92m'
yellow='\u001b[33m'
reset="\\033[0m \n"

printf "${yellow}Preparando build...${reset}"
APP_PATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 || exit ; pwd -P )" && cd "$APP_PATH"/../ || exit

printf "${yellow}Create required network...${reset}"
docker network create selenoid || true

printf "${yellow}Download required webdriver CHROME...${reset}"
docker pull selenoid/chrome:latest
docker pull selenoid/firefox:latest
docker pull selenoid/video-recorder:latest-release

printf "${yellow}Subindo infraestrutura via docker-compose...${reset}"
if ! docker-compose up -d --force-recreate --build --remove-orphans; then
    printf "${red}ERROR: Ocorreu um erro ao subir o projeto${reset}"
    exit 1
fi
printf "${green}Build sucessfuly${reset}"