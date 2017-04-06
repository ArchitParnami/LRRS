DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_searchroom`(IN p_roomtype VARCHAR(50), IN p_starttime varchar(45), In p_startdate varchar(45))
BEGIN

SELECT * 
	FROM  study_room 
    WHERE	study_room.room_type=p_roomtype and 
					room_no NOT IN (	SELECT room_no 
													FROM bookings 
													WHERE (p_starttime between TIME_FORMAT(start_time , '%h:%i %p') and TIME_FORMAT(end_time , '%h:%i %p') ) and
																	start_date = p_startdate and 
																	(booking_status = 'A' or booking_status = 'NS') and  
																	room_no IN (	SELECT room_no 
																							FROM study_room 
                                                                                            WHERE study_room.room_type=p_roomtype
																						)
												);


END$$
DELIMITER ;
