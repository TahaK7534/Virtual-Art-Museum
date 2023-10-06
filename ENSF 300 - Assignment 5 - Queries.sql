/* Function Testing with Main Queries */
/* Alter Function */
ALTER TABLE COUNTRY
ADD COLUMN Region VARCHAR(15);
/* Update Function */
UPDATE PARTICIPANT
SET Country = 'Canada';
/* Insert Function */
INSERT INTO TEAM (
        TeamId,
        Member1,
        Member2,
        Member3,
        Member4,
        Member5,
        Member6
    )
VALUES (
        'T2020_CanadaX',
        'T2020_008',
        'T2020_007',
        'T2020_006',
        'T2020_005',
        null,
        null
    );
/* Delete Function */
DELETE FROM TEAM
WHERE TeamID = 'T2020_CanadaX';
/* Create Table Function */
DROP TABLE IF EXISTS Trees;
CREATE TABLE Trees(Oak CHAR(15), Pine CHAR(15));
/* Create View Function */
DROP VIEW IF EXISTS TestView;
CREATE VIEW TestView AS
SELECT P.FName,
    P.OlympicID
FROM PARTICIPANT AS P;
/* Query Function */
SELECT P.FName,
    P.LName,
    P.Country
FROM PARTICIPANT AS P,
    ATHLETE AS A
WHERE A.OlympicID = P.OlympicID;
SELECT P.FName,
    P.LName,
    P.Country
FROM PARTICIPANT AS P,
    COACH AS C
WHERE C.OlympicID = P.OlympicID
    AND C.Orientation = 'Pending';
SELECT P.Country,
    COUNT(*) AS Number_of_Athletes
FROM PARTICIPANT AS P,
    ATHLETE AS A
WHERE A.OlympicID = P.OlympicID
GROUP BY P.Country
HAVING COUNT(*) >= 1;
SELECT P.OlympicID,
    A.BirthYear
FROM PARTICIPANT AS P
    LEFT OUTER JOIN ATHLETE AS A ON A.OlympicID = P.OlympicID
ORDER BY A.BirthYear ASC;
SELECT P.Country
FROM PARTICIPANT AS P,
    ATHLETE AS A
WHERE A.OlympicID = P.OlympicID
GROUP BY P.Country
HAVING COUNT(*) > 1;
SELECT DISTINCT P.FName,
    P.LName
FROM PARTICIPANT AS P
WHERE EXISTS (
        SELECT *
        FROM INDIVIDUAL_RESULTS AS IR
        WHERE IR.Medal IS NOT NULL
            AND IR.Olympian = P.OlympicID
    );
SELECT C.CName
FROM COUNTRY AS C
WHERE (AllTimeGold + AllTimeSilver + AllTimeBronze) >= 5;
SELECT CO.CName,
    SUM(CO.Medals_Won) AS Medals_Won
FROM (
        SELECT C.CName,
            COUNT(DISTINCT IR.Olympian) AS Medals_Won
        FROM PARTICIPANT AS P,
            INDIVIDUAL_RESULTS AS IR,
            COUNTRY AS C
        WHERE P.Country = C.CName
            AND IR.Olympian = P.OlympicID
        GROUP BY C.CName
        UNION ALL
        SELECT C.CName,
            COUNT(DISTINCT TR.Team) AS Medals_Won
        FROM PARTICIPANT AS P,
            TEAM_RESULTS AS TR,
            TEAM AS T,
            COUNTRY AS C
        WHERE TR.Team = T.TeamID
            AND P.Country = C.CName
            AND T.Member1 = P.OlympicID
        GROUP BY C.CName
    ) AS CO
GROUP BY CO.CName;
SELECT P.FName,
    P.LName
FROM PARTICIPANT AS P,
    ATHLETE AS A
WHERE A.OlympicID = P.OlympicID
    AND A.FirstGames LIKE '%2020';