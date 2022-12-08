drop database if exists AquaTech;
create database AquaTech;
use AquaTech;

create table TankData (
    qte float not null,
    date datetime not null,
    level float not null,
    pressure float not null
);

CREATE user "AquatechUser"@"%" identified by "aquatech";
grant all privileges on AquaTech.* to "Aquatech"@"%";
