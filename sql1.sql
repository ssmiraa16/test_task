WITH FirstReportIn2021 AS (
    SELECT DISTINCT user_id
    FROM reports
    WHERE EXTRACT(YEAR FROM created_at) = 2021
)
SELECT 
    fr.user_id,
    COALESCE(SUM(r.reward), 0) as reward
FROM FirstReportIn2021 fr
LEFT JOIN reports r ON fr.user_id = r.user_id AND EXTRACT(YEAR FROM r.created_at) = 2022
GROUP BY fr.user_id;