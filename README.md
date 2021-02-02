### Created by Jake Johnson and Preston Windfeldt
Special thanks to Anthony Cudzinovica and Alex Hirst

## Description

Software for automatically reserving Ikon mountain reservations when they become available. This uses python3, mysql, and selenium.

## Usage

- Input reservations you want in the text file datesToReserve.txt
  - format: [month],[day],[year],[mountain],[email]
  - ie: 3,7,2021,Arapahoe Basin,billybob<span>@</span>gmail.com
  - if you input the same reservation but with a different mountain, the script will reserve first one that opens up
  - You can add different emails to datesToReserve.txt but you must run the script with the email account you want to get the reservation on. Adding different emails is just for the convenience of being able to run the script simultaneously for different accounts
- Make sure the mountain name you input is the exact name used on Ikon site
- Run src/main.py [email] [password] from top directory of project with python3
  - `$py src/main.py [email] [password]`
- You can turn off headless mode to watch scraper click through site
  - set HEADLESS to 0 in top of main.py
  - note you might not be able to if you are running on an external server

## Installation

#### Windows (roughly same for Mac)
- install python3
- install selenium
	- `$py -m pip install selenium`
	- use equivalent command for Mac ^
- install chrome
- install chrome driver for the version of chrome you have (86/87/88/etc) and system you are using (windows/mac)
	- Download chrome driver here: https://chromedriver.chromium.org/downloads
	- you can see your chrome version here: chrome://settings/help
- add chromedriver file to PATH or put in top directory of this project

#### Ubuntu
- install python3
	- `$sudo apt-get install python3`
- install pip
	- `$sudo apt-get install python3-pip`
- install selenium for python
	- `$py -m pip3 install selenium`
- install selenium and chrome driver for web server (just run this even if not using server)
	- `$py setup/installSelenium.py`
	- ctrl-c once this is done running
	- follow this link if anything goes wrong: https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/
- install chrome
	- `$sudo apt-get install libxss1 libappindicator1 libindicator7`
	- `$wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`
	- `$sudo apt install ./google-chrome*.deb`
- remove junk files
	- `$rm selenium-server-standalone-3.13.0.jar`
	- `$rm chromedriver_linux64`
	- `$rm testng-6.8.7.jar`
	- `$rm testng-6.8.7.jar.zip`
