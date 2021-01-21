Created by Jake Johnson and Preston Windfeldt

Description

Software for automatically reserving Ikon mountain reservations when they become available. This uses python3, mysql, and selenium.

Usage

-Run src/main.py [email] [password] with from top directory of project with python3
-Input dates you want to reserve in the text file datesToReserve.txt
	-format (all integers): [month] [day] [year]
	 ie: 3 1 2021
-Turn off headless mode to watch scraper click through site
	-set HEADLESS to 0 in top of main.py
	-note you might not be able to if you are running on an external server
-Edit mountainsToCheck list in ikonScraperInterface.py to change which Ikon mountains to check

Installation

Ubuntu
-install python3
	$sudo apt-get install python3
-install pip
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
        -python3 -m pip install mysql-connector-python
        -python3 -m pip install mysql-connector-python-rf

-setup sql database
	-run mysql
	-run these commands in mysql
            CREATE USER 'reserver'@'localhost' IDENTIFIED BY 'PurpleNapkin111$';
            GRANT ALL PRIVILEGES ON * . * TO 'reserver'@'localhost';
            FLUSH PRIVILEGES;
            CREATE DATABASE mtnrez;
            USE mtnrez;
            CREATE TABLE datesToReserve(month int, day int, year int);
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
