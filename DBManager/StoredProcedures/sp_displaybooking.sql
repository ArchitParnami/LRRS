DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_displaybooking`(IN p_uname VARCHAR(80))
BEGIN
select booking_name,room_no,start_date,start_time,end_time from lrrs.bookings where uname = p_uname;
END$$
DELIMITER ;
