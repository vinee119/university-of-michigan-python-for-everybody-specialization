CREATE TABLE Ages (
    name VARCHAR(128),
    age INTEGER
);

DELETE FROM Ages;

INSERT INTO Ages (name, age) VALUES ('Rio', 31);
INSERT INTO Ages (name, age) VALUES ('Bully', 23);
INSERT INTO Ages (name, age) VALUES ('Marla', 36);
INSERT INTO Ages (name, age) VALUES ('Anmar', 19);
INSERT INTO Ages (name, age) VALUES ('Jasveer', 15);

SELECT hex(name || age) AS X
FROM Ages
ORDER BY X;