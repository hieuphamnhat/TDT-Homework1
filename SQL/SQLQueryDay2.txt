CREATE TABLE PERSON(
	ID int,
	Name varchar(255),
	Age int
);
INSERT INTO PERSON(id, Name, Age)
VALUES ('1', 'Tom B. Erichsen', '20');
INSERT INTO PERSON(id, Name, Age)
VALUES ('2', 'Tom jerry', '17');
INSERT INTO PERSON(id, Name, Age)
VALUES ('3', 'Tom ', '10');
select * from PERSON
/* 1. Tạo 1 view  trong sql server ( gọi ra nhiều trường(> 2)) */

CREATE VIEW [Profiles] AS
SELECT Name, Age
FROM Person
WHERE id < 3;
/* 2. Tạo 1 table function trong sql server (tra ra view vừa tạo) */			
CREATE FUNCTION udfProfiles (
    @id INT
)
RETURNS TABLE
AS
RETURN
    SELECT 
        Name,
		Age
    FROM
        PERSON
    WHERE
        id < @id;


select * from udfProfiles(3)
/* 3. Tạo 1 store proseduce có gọi table function trong sql server */ 			
CREATE PROCEDURE uspProfiles
AS
BEGIN
    SELECT
        *
    FROM
        udfProfiles(3)
END;

exec uspProfiles

