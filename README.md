Created by Jake Johnson and Preston Windfeldt

## Description

Software for automatically reserving Ikon mountain reservations when they become available. This uses python3, mysql, and selenium.

## Usage

- Run src/main.py [email] [password] with from top directory of project with python3
- Use the python scripts under sql/ to add or remove dates you want to automatically reserve
  - The scripts to insert dates can optionally take arguments for mountains and emails to which you want to restrict dates. The mountains and emails arguments should be in the form of a comma delimited string surrounded by quotes. (i.e. `$python sql/insertDateToReserve.py 3 10 2021 "Brighton,Arapahoe Basin" "billy.bob@yahoo.com,joe.mama@hotmail.com"`)
  - If you wish to add a value for emails but not for mountains, you must supply an empty string between quotes as the argument for mountains. (i.e. `$python sql/insertDateToReserve.py 3 10 2021 "" "billy.bob@yahoo.com,joe.mama@hotmail.com"`)

## Installation

Ubuntu
- install python3
	$sudo apt-get install python3
- install pip
	$sudo apt-get install python3-pip
- install selenium for python
	$py -m pip3 install selenium
- install selenium and chrome driver for web server (just run this even if not using server)
	$py setup/installSelenium.py
	- ctrl-c once this is done running
	- I followed this link if anything goes wrong: https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/
- install chrome
	$sudo apt-get install libxss1 libappindicator1 libindicator7
	$wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
	$sudo apt install ./google-chrome*.deb
- install mysql
	$sudo apt install mysql-server
	$sudo mysql_secure_installation
		- say yes to everything
		- make password "PurpleNapkin111$"
	$python3 -m pip install mysql
    $python3 -m pip install mysql-connector-python
    $python3 -m pip install mysql-connector-python-rf
- setup sql database
	- run mysql
	- run these commands in mysql
            CREATE USER 'reserver'@'localhost' IDENTIFIED BY 'PurpleNapkin111$';
            GRANT ALL PRIVILEGES ON * . * TO 'reserver'@'localhost';
            FLUSH PRIVILEGES;
            CREATE DATABASE mtnrez;
            USE mtnrez;
            CREATE TABLE datesToReserve(month int, day int, year int, mountains varchar(255), emails varchar(255));
- remove junk files
	$rm selenium-server-standalone-3.13.0.jar
	$rm chromedriver_linux64
	$rm testng-6.8.7.jar
	$rm testng-6.8.7.jar.zip

Windows
- install python3
- install selenium
	$py -m pip3 install selenium
- install chrome
- install xampp with mysql
- open up localhost/phpmyadmin in browser and run the sql commands in setup/sqlSetup.sql
- install chrome driver for the version of chrome you have (86/87/88/etc)
	- https://chromedriver.chromium.org/downloads
