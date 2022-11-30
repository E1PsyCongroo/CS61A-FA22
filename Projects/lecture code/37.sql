.open --new

/* Create & Drop */
CREATE TABLE ints(n UNIQUE, prime DEFAULT 1);

/* Insert */
INSERT INTO ints VALUES (2, 1), (3, 1);
INSERT INTO ints(n) VALUES (4), (5), (6), (7), (8);
INSERT INTO ints(n) SELECT n+7 FROM ints;
INSERT INTO ints(n) SELECT n+14 FROM ints;
SELECT * FROM ints;

/* Update */
UPDATE ints SET prime=0 WHERE n > 2 AND n % 2 = 0;
UPDATE ints SET prime=0 WHERE n > 3 AND n % 3 = 0;
UPDATE ints SET prime=0 WHERE n > 5 AND n % 5 = 0;
SELECT * FROM ints;

/* Delete */
DELETE FROM ints WHERE prime=0;
SELECT n FROM ints;

.exit

/* Blackjack */
SELECT * FROM cards;
SELECT * FROM cards WHERE place != "Discard";
SELECT card, count(*) FROM cards GROUP BY card;
UPDATE cards SET card="A" WHERE card=6 AND place="Player";
