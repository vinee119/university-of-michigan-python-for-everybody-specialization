DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER PRIMARY KEY,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
);

INSERT OR IGNORE INTO User (name)
VALUES (?);

SELECT id
FROM User
WHERE name = ?;

INSERT OR IGNORE INTO Course (title)
VALUES (?);

SELECT id
FROM Course
WHERE title = ?;

INSERT OR REPLACE INTO Member
(user_id, course_id, role)
VALUES (?, ?, ?);

SELECT User.name,
       Course.title,
       Member.role
FROM User
JOIN Member
JOIN Course
ON User.id = Member.user_id
AND Member.course_id = Course.id
ORDER BY User.name DESC,
         Course.title DESC,
         Member.role DESC
LIMIT 2;

SELECT 'XYZZY' ||
       hex(User.name || Course.title || Member.role) AS X
FROM User
JOIN Member
JOIN Course
ON User.id = Member.user_id
AND Member.course_id = Course.id
ORDER BY X
LIMIT 1;