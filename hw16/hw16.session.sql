

CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    user_type ENUM('Host', 'Guest') NOT NULL
);

CREATE TABLE Rooms (
    room_id SERIAL PRIMARY KEY,
    host_id INT ,
    price DECIMAL NOT NULL,
    max_residents INT NOT NULL,
    has_AC BOOLEAN,
    has_refrigerator BOOLEAN,
    FOREIGN KEY (host_id) REFERENCES Users(user_id) 
);


CREATE TABLE Reservations (
    reservation_id SERIAL PRIMARY KEY,
    room_id INT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);


CREATE TABLE Reviews (
    review_id SERIAL PRIMARY KEY,
    reservation_id INT,
    rating INT NOT NULL,
    comment TEXT,
    FOREIGN KEY (reservation_id) REFERENCES Reservations(reservation_id)
);


CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY,
    reservation_id INT,
    amount DECIMAL NOT NULL,
    FOREIGN KEY (reservation_id) REFERENCES Reservations(reservation_id)
);


INSERT INTO Users (username, user_type) VALUES
('alex', 'Guest'),
('olena', 'Guest'),
('maria', 'Host');


INSERT INTO Rooms (host_id, price, max_residents, has_AC, has_refrigerator) VALUES
(3, 100.0, 2, true, false),
(3, 200.0, 4, true, true),
(3, 150.0, 3, false, true);


INSERT INTO Reservations (room_id, start_date, end_date) VALUES
(1, '2023-10-01', '2023-10-03'),
(2, '2023-11-15', '2023-11-20'),
(3, '2023-12-01', '2023-12-02');


INSERT INTO Reviews (reservation_id, rating, comment) VALUES
(1, 5, 'Excellent !'),
(2, 4, 'Very good.'),
(3, 3, 'Not so good.');


INSERT INTO Payments (reservation_id, amount) VALUES
(1, 200.0),
(2, 1000.0),
(3, 150.0);

SELECT Users.username AS username, Users.user_id AS user_id
FROM Users
JOIN Rooms ON Users.user_id = Rooms.host_id
JOIN Reservations ON Rooms.room_id = Reservations.room_id
GROUP BY Users.user_id, Users.username
ORDER BY COUNT(Reservations.reservation_id) DESC
LIMIT 1;



SELECT Users.username AS hostname, Users.user_id AS user_id 
FROM Users
JOIN Rooms ON Users.user_id = Rooms.host_id
JOIN Reservations ON Rooms.room_id = Reservations.room_id
JOIN Payments ON Reservations.reservation_id = Payments.reservation_id
WHERE Users.user_type = 'Host' AND DATE_TRUNC('month', current_date) - INTERVAL '1 month' <= Reservations.start_date
GROUP BY Users.user_id
ORDER BY SUM(Payments.amount) DESC
LIMIT 1;



SELECT Users.username AS hostname, Users.user_id AS user_id 
FROM Users
JOIN Rooms ON Users.user_id = Rooms.host_id
JOIN Reservations ON Rooms.room_id = Reservations.room_id
JOIN Reviews ON Reservations.reservation_id = Reviews.reservation_id
WHERE Users.user_type = 'Host'
GROUP BY Users.user_id
ORDER BY AVG(Reviews.rating) DESC
LIMIT 1;
