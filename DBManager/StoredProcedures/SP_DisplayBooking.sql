DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_displaybooking`(IN p_uname VARCHAR(80))
BEGIN
select booking_id, uname, start_time, end_time, start_date, end_date, booking_status, booking_name, room_no from lrrs.bookings where uname = p_uname;
END$$
DELIMITER ;
