Created by Jake Johnson and Preston Windfeldt

Description

Software for automatically reserving Ikon mountain reservations when they become available. This uses python3, mysql, and selenium.

Installation

Ubuntu
* install python3
	$sudo apt-get install python3
* install pip
	$sudo apt-get install python3-pip
-install selenium for python
	$py -m pip3 install selenium
-install selenium and chrome driver for web server (just run this even if not using server)
	$py setup/installSelenium.py
	-ctrl-c once this is done running
	-I followed this link if anything goes wrong: https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/
-install chrome
	$sudo apt-get install libxss1 libappindicator1 libindicator7
	$wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
	$sudo apt install ./google-chrome*.deb
-install mysql
	-sudo apt install mysql-server
	-sudo mysql_secure_installation
		-say yes to everything
		-make password "PurpleNapkin111$"
	-python3 -m pip install mysql
-setup sql database
	-run mysql
	-run the commands located in setup/sqlSetup.sql
-remove junk files
	$rm selenium-server-standalone-3.13.0.jar
	$rm chromedriver_linux64
	$rm testng-6.8.7.jar
	$rm testng-6.8.7.jar.zip

Windows
-install python3
-install selenium
	-$py -m pip3 install selenium
-install chrome
-install xampp with mysql
-open up localhost/phpmyadmin in browser and run the sql commands in setup/sqlSetup.sql
-install chrome driver for the version of chrome you have (86/87/88/etc)
	-https://chromedriver.chromium.org/downloads