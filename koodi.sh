#!/bin/bash
echo "Hei, $(whoami) !"
echo "Olet hakemistossa: $(pwd)"
echo "Nyt on: $(date)"
echo "Anna ensimmäinen luku: "
read ekaluku
echo "Anna toinen luku: "
read tokaluku
summa=$(expr $ekaluku + $tokaluku) #expr ja välilyönnit
echo "Lukujen summa on: $summa"
