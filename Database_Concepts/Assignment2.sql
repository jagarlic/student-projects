CREATE DATABASE "Assignment2"
WITH OWNER = postgres
ENCODING = 'UTF8'
TABLESPACE = pg_default
LC_COLLATE = 'English_United States.1252'
LC_CTYPE = 'English_United States.1252'
CONNECTION LIMIT = -1;

CREATE TABLE Student
(SId INTEGER,
Sname VARCHAR(15),
PRIMARY KEY(SId));

CREATE TABLE Major
(SId INTEGER,
Major VARCHAR(15)
FOREIGN KEY(SId) REFERENCES
Student(SId));

CREATE TABLE Book
(BookNo INTEGER,
Title VARCHAR(30),
Price INTEGER,
PRIMARY KEY(BookNo));

CREATE TABLE Cites
(BookNo INTEGER,
CitedBookNo INTEGER,
FOREIGN KEY(CitedBookNo) REFERENCES
Book(BookNo),
FOREIGN KEY(BookNo) REFERENCES
Book(BookNo));

CREATE TABLE Buys
(SId INTEGER,
BookNo INTEGER,
FOREIGN KEY(SId) REFERENCES
Student(SId)
FOREIGN KEY(BookNo) REFERENCES
Book(BookNo));

COPY Student FROM 'C:/Users/Jack Garlick/Downloads/student.csv' DELIMITER ',' CSV;

COPY Major FROM 'C:/Users/Jack Garlick/Downloads/major.csv' DELIMITER ',' CSV;

COPY Book FROM 'C:/Users/Jack Garlick/Downloads/book.csv' DELIMITER ',' CSV;

COPY Cites FROM 'C:/Users/Jack Garlick/Downloads/cites.csv' DELIMITER ',' CSV;

COPY Buys FROM 'C:/Users/Jack Garlick/Downloads/buys.csv' DELIMITER ',' CSV;

-- Miscellaneous Problems

-- 1
-- Write a SQL statement that determines whether it is true or not if A − B

SELECT Exists((SELECT a.x
              FROM A a)
              INTERSECT
              (SELECT b.x
              FROM B b)) AS empty_a_intersection_b,
            Exists((SELECT a.x
               FROM A a)
               EXCEPT
               (SELECT b.x
                FROM B b)) AS empty_a_minus_b,
            Exists((SELECT b.x
               FROM B b)
               EXCEPT
               (SELECT a.x
                FROM A a)) AS empty_b_minus_a

-- 2
-- Write a SQL statement that produces a table that,
-- for each x ∈ A, listthe tuple (x, √x, x2, 2x, x!, ln x).

SELECT a.x AS x, SQRT(a.x) AS square_root_x, a.x * a.x AS x_squared,
power(2, a.x) AS two_to_the_power_x, a.x ! AS x_facatorial, ln(a.x) AS logarithm_x
FROM problem1 a

--3
-- Write a SQL statement that generates the 3-valued truth table for the
-- Propositional Logic formula
 --      ¬(p ∧ ¬q) ∧ ¬r

SELECT p.x AS p, q.x as q, r.x as r,
NOT(p.x AND NOT q.x) AND NOT r.x as value
FROM P p, Q q, R r

--4
--a
-- Write a SQL statement that determines whether it is
-- true or not if A ∩ B != {}

SELECT
EXISTS((SELECT a.x
FROM A a)
INTERSECT
(SELECT b.x
FROM B b)) AS answer

SELECT EXISTS(
    SELECT a.x, b.x
    FROM A a, B b
    WHERE (a.x, b.x) IN (
        SELECT b.x, a.x
        FROM B b, A a
    ))


--b
-- Write a SQL statement that determines whether it is
-- true or not if A ∩ B = {}

SELECT
NOT EXISTS((SELECT a.x
FROM A a)
INTERSECT
(SELECT b.x
FROM B b)) AS answer

SELECT NOT EXISTS(
    SELECT a.x, b.x
    FROM A a, B b
    WHERE (a.x, b.x) IN (
        SELECT a.x, b.x
        FROM A a, B b
    ))

--c
-- Write a SQL statement that determines whether it is true
-- or not if A ⊆ B

SELECT NOT EXISTS((SELECT a.x
FROM A a)
EXCEPT
(SELECT b.x
FROM B b)) AS answer

SELECT NOT EXISTS(
    SELECT a.x, b.x
    FROM A a, B b
    WHERE (a.x, b.x) NOT IN(
        SELECT a.x, b.x
        FROM A a, B b
    )
)

--d
-- Write a SQL statement that determines whether it is true
-- or not if A = B

SELECT NOT EXISTS((SELECT a.x
FROM A a)
EXCEPT
(SELECT b.x
FROM B b)) AND NOT EXISTS((SELECT b.x
FROM B b)
EXCEPT
(SELECT a.x
FROM A a))

SELECT CASE WHEN
    A = B
    THEN 't' ELSE 'f'

--e
-- Write a SQL statement that determines whether it is true
-- or not if A != B

SELECT EXISTS((SELECT a.x
FROM A a)
EXCEPT
(SELECT b.x
FROM B b)) OR EXISTS((SELECT b.x
FROM B b)
EXCEPT
(SELECT a.x
FROM A a))

--f
-- Write a SQL statement that determines whether it is
-- true or not if |A ∩ B| ≥ 2

SELECT 2 <= len((SELECT a.x
FROM A a)
INTERSECT
(SELECT b.x
FROM B b)) AS Answer

--g
-- Write a SQL statement that determines whether it is true
-- or not if |A ∩ B| = 1.

SELECT 1=len((SELECT a.x
    FROM A a)
    INTERSECT
    (SELECT b.x
    FROM B b)) AS Answer

--h
-- Write a SQL statement that determines whether it is true
-- or not if (A ∪ B) ⊇ C.

SELECT NOT EXISTS(
    (SELECT ab.x
    FROM AunionB AS ab)
    EXCEPT
    (SELECT c.x
    FROM C c))

CREATE VIEW AunionB AS
    (SELECT a.x
    FROM A a)
    UNION
    (SELECT b.x
    FROM B b)

--i
-- Write a SQL statement that determines whether it is true
-- or not if |(A − B) ∪ (B ∩ C)| = 2

CREATE VIEW AexceptB AS
    (SELECT a.x
    FROM A a)
    EXCEPT
    (SELECT b.x
    FROM B b)

CREATE VIEW BandC AS
    (SELECT b.x
    FROM B b)
    INTERSECT
    (SELECT c.x
    FROM C c)

SELECT 2 = len(
    (SELECT AeB.x
    FROM AexceptB AS AeB)
    UNION
    (SELECT BaC
    FROM BandC as AeB) AS Answer

--5

--a
-- Write a SQL query that returns the pairs of points that are farthest
-- away in distance from each other

CREATE FUNCTION distance(x1 float, y1 float, x2 float, y2 float)
    RETURNS float AS
$$
    SELECT sqrt(power(x1-x2,2) + power(y1-y2, 2));
$$ LANGUAGE SQL;

CREATE VIEW distances AS
    SELECT distance(p1.x, p1.y, p2.x, p2.y) as d, p1.pid as pid1, p2.pid as pid2
    FROM Point p1, Point p2

SELECT MAX(
    SELECT distances.d
    FROM distances
    WHERE distances.pid=p1.pid)
FROM Point p1, distances

--b
-- Write a SQL query that returns the pairs of points that
-- are at the next to longest distance away from each other.

CREATE VIEW distances AS
    SELECT distance(p1.x, p1.y, p2.x, p2.y) as d, p1.pid as pid, p2.pid as pid2
    FROM Point p1, Point p2

SELECT d.pid, d.pid2
FROM distances d
SELECT MAX(
    SELECT d2.d
    FROM distances d2
    WHERE d2.d < MAX(
        SELECT d3.d
        FROM distances d3
        WHERE d3.d))

--6
-- Write a SQL query with returns the A-values of tuples in W if A is a
-- primary key of W.

SELECT a.x as A
FROM removedDuplicatesA rda, A a
WHERE NOT EXISTS(rda EXCEPT a)

SELECT b.x as B
FROM removedDuplicatesB, B b
WHERE NOT EXISTS(rdb EXCEPT b)

CREATE VIEW removedDuplicatesA AS
    SELECT DISTINCT x FROM A a

CREATE VIEW removedDuplicatesB AS
    SELECT DISTINCT x FROM B b

--Translate this to work with HW variables
SELECT S.c
FROM R r, S s
UNION ((
SELECT t.c
FROM T t)
EXCEPT (
SELECT T.c
FROM R r, T t)
)
-- this does the job much faster
SELECT s.c
FROM S s
WHERE EXISTS(
    SELECT 1
    FROM R r)
UNION
SELECT t.c
FROM C t
WHERE NOT EXISTS(
    SELECT 1
    FROM R r
)

-- SQL Problems

--7
-- Find the titles of books that cost between $20 and $40

SELECT b.Title
FROM book b
WHERE b.Price>20 AND b.Price<40

--8
-- Find the Sid’s and Sname’s of students who bought a book
-- that cites another book of a lower price.

SELECT s.Sname, s.Sid
FROM student s
WHERE EXISTS (SELECT b.Sid
              FROM buys b
              WHERE EXISTS (SELECT c.BookNo
                            FROM cites c, book book
                            WHERE c.CitedBookNo = book.BookNo AND book.Price))

--9
-- Find the Bookno’s of books that are cited by a book (or books)
-- that is (are) itself (themselves) cited by another (other) books

SELECT c1.BookNo
FROM cites c1, cites c2, cites c3
WHERE c1.BookNo=c2.CitedBookNo
AND c2.BookNo=c3.CitedBookNo
AND c1.BookNo<>c2.BookNo

--10
-- Find the BookNo’s of books that are not cited by another
-- (other) books

SELECT b.BookNo
FROM book b
WHERE b.BookNo NOT IN (
    SELECT c.CitedBookNo
    FROM cites c
)

--11
-- Find Sid’s and Sname’s of students who have at least two
-- majors and who only bought books that were cited by other books

SELECT S.Sname, S.Sid
FROM Student S1, Student S2, Major M
WHERE S1.Sname=S2.Sname AND
S1.Sid=M.Sid AND
S2.Sid=M.Sid

--12
-- Find Sid’s and majors of students who did not buy any books
-- that cost less than $30.

SELECT m.Major as Major, b.Sid as Sid
FROM buys c, book b, major m
WHERE b.Price>=30 AND
b.Sid=m.Sid

--13
-- Find each (s, b) pair where s is the Sid of a student and b is the Bookno of a book whose price
-- is the cheapest among the books bought by that student.

CREATE FUNCTION booksBoughtBy(Sid integer)
    RETURNS TABLE AS
    $$
        SELECT b.Price, b.Bookno
        FROM buys b, book book
        WHERE book.Sid = Sid AND
        b.Bookno = book.Bookno AND
        b.Sid = Sid
    $$

SELECT s.Sid, b.Bookno
FROM student s, book b
WHERE MIN(booksBoughtBy(s.Sid).Bookno) = b.Bookno

--14
-- Without using the ALL predicate, list the Bookno’s of the cheapest
-- books.

SELECT b.Bookno
FROM book b
WHERE b.Price < 30

--15
-- Find the triples (s1,s2,b) where s1 and s2 are different Sid’s of
-- student and b is the BookNo of a book that was bought by student s1 or
-- by student s2, but not by both students.

SELECT s.Sid AS s1, s2.Sid AS s2, b.Bookno AS b
FROM student s, student s2, buys b
WHERE s.Sid=b.Sid AND
s2.Sid<>b.Sid AND
s.Sid<>s2.Sid

--16
-- Find the tuples (s1,s2) where s1 and s2 are different Sid’s of
-- students and such that student s1 and student s2 bought exactly one book
-- in common.

SELECT s1.Sid AS s1, s2.Sid AS s2
FROM student s1, student s2, buys b

CREATE FUNCTION exactlyOne(
)
--I have no idea how to create this function without using a built in
--Count helper function

--17
-- Find the Bookno’s of books that where bought by all students who major in ’Biology’

SELECT b.Bookno
FROM major m, buys b
WHERE m.Major='biology' AND
m.Sid=b.Sid

--18
-- Find the Bookno’s of books that where not bought by any students.

SELECT books.Bookno
FROM buy b, book books
WHERE NOT EXISTS(
    SELECT b.Bookno
) AND EXISTS(
    SELECT books.Bookno
)

--19
-- Find the Bookno’s of books that where bought buy all but one student.

SELECT b.Bookno
FROM buys b, student s
WHERE len(allButOne)=len(b)

CREATE VIEW allButOne AS
    RETURN TABLE
    $$
        SELECT b.Bookno
        FROM buys b, student s
        WHERE b.Sid = s.Sid
    $$

--20
-- Find the pairs (s1,s2) of Sid’s of students such that if student
-- s1 bought a book then student s2 also bought that book.

SELECT s1.Sid AS s1, s2.Sid AS s2
FROM student s1, buys b
WHERE EXISTS(
    SELECT *
    FROM student s2
    WHERE s1.Sid = b.Sid AND s2.Sid = b.Sid AND s1.Sid<>s2.Sid)
