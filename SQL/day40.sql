Draw The Triangle 1

SET @NUMBER = 21;
SELECT REPEAT('* ', @NUMBER := @NUMBER - 1)
    FROM information_schema.tables LIMIT 20;
