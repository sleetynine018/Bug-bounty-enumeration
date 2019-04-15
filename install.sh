echo "Welcome to the installer"

cd ~

echo "Makind Sectools dir"
mkdir ~/Desktop/Sectools


echo "Installing nmap"
sudo apt-get install nmap

echo "Installing curl"
sudo apt-get install curl

echo "Installing Security headers checker"
wget https://raw.githubusercontent.com/meliot/shcheck/master/shcheck.py
mv shcheck.py ~/Desktop/Sectools/shcheck.py

#TODO: install waf00f

#dir scanner will be installed later