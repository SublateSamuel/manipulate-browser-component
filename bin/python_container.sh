#!/usr/bin/bash

red='\u001b[31m'
green='\e[92m'
yellow='\u001b[33m'
reset="\\033[0m \n"


printf "${yellow}into container pytbots...${reset}"
docker exec -it pyuser bash || true
