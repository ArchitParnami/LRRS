DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_booking`(IN p_uname VARCHAR(80),IN p_startdate varchar(45),IN p_bookingname varchar(100)
,IN p_room varchar(45), IN p_starttime time, IN p_endtime time, IN p_enddate varchar(45))
BEGIN
INSERT INTO `lrrs`.`bookings`
(
`uname`,
`start_time`,
`end_time`,
`start_date`,
`end_date`,
`booking_status`,
`booking_name`,
`room_no`)
VALUES
(
p_uname,
p_starttime,
p_endtime,
p_startdate,
p_enddate,
'NS',
p_bookingname,
p_room);

SELECT last_insert_id();

END$$
DELIMITER ;
