CREATE TABLE IF NOT EXISTS Locations (
    address TEXT,
    geodata TEXT
);

SELECT geodata
FROM Locations
WHERE address = ?;

INSERT INTO Locations (address, geodata)
VALUES (?, ?);

SELECT *
FROM Locations;