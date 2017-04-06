CREATE DATABASE IF NOT EXISTS LRRS;

USE LRRS;

CREATE TABLE IF NOT EXISTS `user_info` (
  `uname` varchar(80) NOT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`uname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `study_room` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `room_no` varchar(45) DEFAULT NULL,
  `capacity` int(11) DEFAULT NULL,
  `location` varchar(45) DEFAULT NULL,
  `room_type` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


 CREATE TABLE IF NOT EXISTS `bookings` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(80) DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  `start_date` date default null,
  `end_date` date default null,
  `booking_status` varchar(45) DEFAULT NULL,
  `booking_name` varchar(100) DEFAULT NULL,
  `room_no` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `fk_uname_idx` (`uname`),
  CONSTRAINT `fk_uname` FOREIGN KEY (`uname`) REFERENCES `user_info` (`uname`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


