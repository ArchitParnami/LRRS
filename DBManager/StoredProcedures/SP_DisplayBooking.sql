DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_displaybooking`(IN p_uname VARCHAR(80))
BEGIN
update lrrsnew.bookings set booking_status = 'CO' where ((start_date< CURDATE() and booking_status='NS') or (start_date=CURDATE() and end_time<CURTIME() and booking_status='NS')) and uname = p_uname ;
update lrrsnew.bookings set  booking_status = 'AC' where start_date=CURDATE() and start_time<=CURTIME() and end_time>=CURTIME() and booking_status='NS' and uname = p_uname ;
select booking_id, uname, start_time, end_time, start_date, end_date, booking_status, booking_name, room_no from lrrs.bookings where uname = p_uname and booking_status != 'CA';
END$$
DELIMITER ;