python app for Ikon mountain reservations.

TODO: write what this does

NOTE: 

run this:

sudo apt-get install python3
sudo 

-prereqs:
sudo apt-get update
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
sudo apt-get install default-jdk 

-install chrome driver:
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable

wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar
wget http://www.java2s.com/Code/JarDownload/testng/testng-6.8.7.jar.zip
unzip testng-6.8.7.jar.zip

-do we need this?
xvfb-run java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone.jar



-must install python3
-must install selenium (if using windows)
-if using virtual server: must install standalone selenium server virtual server
	-follow this:
		https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/
	-run this to start the selenium server:
		$ xvfb-run -a java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone-3.13.0.jar
-must install chrome and correct chromedriver for system (linux/windows/mac)
	-add to PATH
-must install mysql
	-must create database called "mtnrez"
	-create user yourmom with password Yourmom123! and grant insert/delete privileges
	-create table called datesToReserve with month int, day int, year int

TODO:
-make it so php doesn't show the username and password for the sql database on website php files


















