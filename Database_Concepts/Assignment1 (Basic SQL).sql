-- PROBLEM 1

CREATE TABLE Reserves
(
  SId integer,
  BId integer,
  Day character(10),
  FOREIGN KEY (BId)
      REFERENCES Boat(BId)
  FOREIGN KEY (SId)
      REFERENCES Sailor(SId)
)

CREATE TABLE Boat
(
  BId integer NOT NULL,
  Bname character(20),
  Color character(15),
  PRIMARY KEY (BId)
)

CREATE TABLE Sailor
(
  SId integer NOT NULL,
  Sname character(20),
  Rating integer,
  Age integer,
  PRIMARY KEY ("SId")
)

INSERT INTO Boat VALUES(
    (101 'Interlake' 'blue'),
    (102 'Interlake' 'red'),
    (103 'Clipper' 'green'),
    (104 'Marine' 'red')
)

INSERT INTO Sailor VALUES(
    (22 'Dustin' 7 45),
    (29 'Brutus' 1 33),
    (31 'Lubber' 8 55),
    (32 'Andy' 8 25),
    (58 'Rusty' 10 35),
    (64 'Horatio' 7 35),
    (71 'Zorba' 10 16),
    (74 'Horatio' 9 35,
    (85 'Art' 3 25),
    (95 'Bob' 3 63)
)

INSERT INTO Reserves VALUES(
    (22 101 'Monday'),
    (22 102 'Tuesday'),
    (22 103 'Wednesday'),
    (31 102 'Thursday'),
    (31 103 'Friday'),
    (31 104 'Saturday'),
    (64 101 'Sunday'),
    (64 102 'Monday'),
    (74 103 'Tuesday')
)

-- PROBLEM 2

--a
SELECT B.BId, B.Bname
FROM Boat B
WHERE B.Color='red'

--b
SELECT S.Sname
FROM Sailor S
WHERE S.SId IN(SELECT R.SId
               FROM Reserves R
               WHERE R.BId=103)

--c
SELECT B.Bname
FROM Boat B
WHERE B.BId IN(SELECT R.BId
               FROM Reserves R
               WHERE R.SId IN(SELECT S.SId
                              FROM Sailor S
                              WHERE S.Rating>8))
--d
SELECT S.Sname
FROM Sailor S
WHERE S.SId IN(SELECT R.SId
               FROM Reserves R
               WHERE R.BId IN(SELECT B.BId
                              FROM Boat B
                              WHERE B.Color='red'
                              OR B.Color='green'))

--e
SELECT S.Sname
FROM Sailor S
WHERE S.SId IN(SELECT R.SId
               FROM Reserves R
               WHERE R.BId IN(SELECT B.BId
                              FROM Boat B
                              WHERE B.Color='blue'))
AND S.SId IN(SELECT R.SId
               FROM Reserves R
               WHERE R.BId IN(SELECT B.BId
                              FROM Boat B
                              WHERE B.Color='green'))
--f
SELECT S.Sname
FROM Sailor S, Reserves R1, Reserves R2
WHERE S.SId=R1.SId
AND S.SId=R2.SId
AND R2.SId<>R1.SId

--g
SELECT S.SId
FROM Sailor S
WHERE NOT EXISTS(SELECT R.SId
                FROM Reserves R
                WHERE R.SId=S.SId)
