echo ""
echo ""
echo "Welcome to the installer"

cd ~

echo ""
echo "Makind Sectools dir"
mkdir ~/Desktop/Sectools

echo ""
echo "Installing nmap"
sudo apt-get install nmap

echo ""
echo "Installing curl"
sudo apt-get install curl

echo ""
echo "Installing Security headers checker"
wget https://raw.githubusercontent.com/meliot/shcheck/master/shcheck.py
mv shcheck.py ~/Desktop/Sectools/shcheck.py

echo ""
echo "Installing wafw00f"
pip install wafw00f

echo ""
echo ""
echo ""
echo "All done here"

#dir scanner will be installed later
