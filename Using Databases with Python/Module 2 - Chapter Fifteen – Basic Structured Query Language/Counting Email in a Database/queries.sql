DROP TABLE IF EXISTS Counts;

CREATE TABLE Counts (
    org TEXT,
    count INTEGER
);

SELECT count
FROM Counts
WHERE org = ?;

INSERT INTO Counts (org, count)
VALUES (?, 1);

UPDATE Counts
SET count = count + 1
WHERE org = ?;

SELECT org, count
FROM Counts
ORDER BY count DESC
LIMIT 10;