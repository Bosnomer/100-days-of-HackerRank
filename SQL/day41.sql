# Draw The Triangle 2

SET @NUMBER = 0;
SELECT REPEAT('* ', @NUMBER := @NUMBER + 1)
    FROM information_schema.tables LIMIT 20;
