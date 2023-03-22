#!/bin/bash


echo -e """
\e[38;5;197m ꧁෴╔══════════════════❖•ೋ°៚°ೋ•❖══════════════════╗෴꧂
\e[1;91m    ➣Name       ⇶   RadiumX
\e[38;5;197m ꧁෴╚══════════════════❖•ೋ°៚°ೋ•❖══════════════════╝෴꧂
\e[1;93m               

              
"""
 read -p $'Enter the WebSite Name:' opv
 
 cd Sitadel && python3 sitadel.py $opv
}
main_menu