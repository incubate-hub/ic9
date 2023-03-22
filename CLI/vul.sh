#!/bin/bash


echo -e """
\e[38;5;197m ꧁෴╔══════════════════❖•ೋ°៚°ೋ•❖══════════════════╗෴꧂
\e[1;91m    ➣Name       ⇶   RadiumX
\e[38;5;197m ꧁෴╚══════════════════❖•ೋ°៚°ೋ•❖══════════════════╝෴꧂
\e[1;93m               

              
"""
 read -p $'Enter the WebSite Name:' opv
 
 cd sqlifinder && python3 sqlifinder.py -d $opv

main_menu