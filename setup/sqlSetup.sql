# once sql is installed run these sql commands to setup user
CREATE USER 'reserver'@'localhost' IDENTIFIED BY 'PurpleNapkin111$';
GRANT ALL PRIVILEGES ON * . * TO 'reserver'@'localhost';
FLUSH PRIVILEGES;
CREATE DATABASE mtnrez;
CREATE TABLE datesToReserve(month int, day int, year int, mountains varchar(255), emails varchar(255));
