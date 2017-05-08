USE LRRS;

INSERT  INTO user_info VALUES ( 'aparnami', '1234'), ('dshah27', '1234'), ('jma15', '1234'),
                              ('lramumee', '1234'),('achand12', '1234'), ('nyadav3', '1234');

INSERT INTO study_room(room_no, capacity, location, room_type)
    VALUES ('GS-1', 2, 'G', 'I'), ('GS-2', 3, 'G', 'I'), ('GS-3', 2, 'G', 'I'),
           ('100A', 2, 'M', 'I'), ('100B', 3, 'M', 'I'), ('100C', 2, 'M', 'I'),
           ('110A', 4, 'M', 'G'), ('110B', 5, 'M', 'G'), ('110C', 7, 'M', 'G'),
           ('200A', 2, 'S', 'I'), ('200B', 3, 'S', 'I'), ('200C', 2, 'S', 'I'),
           ('210A', 5, 'S', 'G'), ('210B', 6, 'S', 'G'), ('210C', 8, 'S', 'G')
