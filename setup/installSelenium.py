import os

# prereqs
os.system('sudo apt-get update')
os.system('sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4')
os.system('sudo apt-get install default-jdk ')

# install chrome driver
os.system('sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add')
os.system('sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list')
os.system('sudo apt-get -y update')
os.system('sudo apt-get -y install google-chrome-stable')
os.system('wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip')
os.system('unzip chromedriver_linux64.zip')
os.system('sudo mv chromedriver /usr/bin/chromedriver')
os.system('sudo chown root:root /usr/bin/chromedriver')
os.system('sudo chmod +x /usr/bin/chromedriver')

# download jar files
os.system('wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar')
os.system('wget http://www.java2s.com/Code/JarDownload/testng/testng-6.8.7.jar.zip')
os.system('unzip testng-6.8.7.jar.zip')

# run selenium. User should ctrl-c out of this once its running
os.system('xvfb-run java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone-3.13.0.jar &')
