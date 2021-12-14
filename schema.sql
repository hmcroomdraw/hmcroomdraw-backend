CREATE TABLE Users (
    id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    class_year TEXT,
    priority_number INT,
    gender TEXT
);

CREATE TABLE Rooms (
    id TEXT PRIMARY KEY,
    residence_hall_name TEXT,
    floor_number INT,
    suite TEXT,
    room_number TEXT
);

