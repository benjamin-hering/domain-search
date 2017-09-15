#!/bin/bash

function check_com_net {
	whois $1 | grep "No match for" > /dev/null 
	if [ $? == 0 ]; then
		echo $1 "is unregistered"
	fi
}

function check_us {
	whois $1 | grep "Not found:" > /dev/null
	if [ $? == 0 ]; then
		echo $1 "is unregistered"
	fi
}

alphanum=({0..9} {a..z})

for a in {a..z} {0..9}; do
	for b in {a..z} {0..9}; do
		for c in {a..z}; do
			#check_com_net $a$b$c$d.com
			check_us $a$b$c.us
		done	
	done
done
