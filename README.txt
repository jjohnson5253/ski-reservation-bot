Created by Jake Johnson and Preston Windfeldt

Description

Software for automatically reserving Ikon mountain reservations when they become available. This uses python3 and selenium.

Usage
-Input dates you want to reserve in the text file datesToReserve.txt
	-format (all integers): [month] [day] [year]
	 ie: 3 1 2021
-Edit mountainsToCheck list in ikonScraperInterface.py to change which Ikon mountains to check
	-Make sure the name you input is the exact name used on Ikon site when you try to make a reservation
-Run src/main.py [email] [password] from top directory of project with python3
	$py src/main.py [email] [password]
-You can turn off headless mode to watch scraper click through site
	-set HEADLESS to 0 in top of main.py
	-note you might not be able to if you are running on an external server


Installation

Windows (follow this roughly for Mac as well)
-install python3
-install selenium
	-$py -m pip3 install selenium
-install chrome
-install chrome driver for the version of chrome you have (86/87/88/etc)
	-https://chromedriver.chromium.org/downloads
-add chromedriver file to PATH or put in top directory of this project

Ubuntu
-install python3
	$sudo apt-get install python3
-install pip
	$sudo apt-get install python3-pip
-install selenium for python
	$py -m pip3 install selenium
-install selenium and chrome driver for web server (just run this even if not using server)
	$py src/installSelenium.py
	-ctrl-c once this is done running
	-I followed this link if anything goes wrong: https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/
-install chrome
	$sudo apt-get install libxss1 libappindicator1 libindicator7
	$wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
	$sudo apt install ./google-chrome*.deb

-remove junk files
	$rm selenium-server-standalone-3.13.0.jar
	$rm chromedriver_linux64
	$rm testng-6.8.7.jar
	$rm testng-6.8.7.jar.zip
