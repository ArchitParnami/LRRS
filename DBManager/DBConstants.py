class DBConstants(object):
    DBNAME = 'LRRS'
    TABLE_USER = 'user_info'
    TABLE_ROOM = 'study_room'
    TABLE_BOOKING = 'bookings'

    USER_USERNAME = 'uname'
    USER_PASSWORD = 'password'

    ROOM_ID = 'ID'
    ROOM_NUMBER = 'room_no'
    ROOM_CAPACITY = 'capacity'
    ROOM_LOCATION = 'location'
    ROOM_TYPE = 'room_type'

    BOOKING_ID = 'booking_id'
    BOOKING_USER = 'uname'
    BOOKING_START_TIME = 'start_time'
    BOOKING_END_TIME = 'end_time'
    BOOKING_START_DATE = 'start_date'
    BOOKING_END_DATE = 'end_date'
    BOOKING_STATUS = 'booking_status'
    BOOKING_NAME = 'booking_name'
    BOOKING_ROOM_NUMBER = 'room_no'

    SP_SEARCH_ROOMS = 'sp_searchrooms'
    SP_BOOKING = 'sp_booking'
    SP_GET_USER_BOOKINGS = 'sp_displaybooking'
    SP_GET_CURRENT_INACTIVE_BOOKINGS = 'sp_current_inactive_bookings'

DBC = DBConstants()