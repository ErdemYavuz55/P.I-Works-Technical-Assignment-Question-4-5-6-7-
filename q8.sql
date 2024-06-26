
UPDATE country_vaccination_stats cvs
SET daily_vaccinations = (
    SELECT COALESCE(
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY daily_vaccinations),
        0
    ) AS median_vaccination
    FROM country_vaccination_stats
    WHERE country = cvs.country
    AND daily_vaccinations IS NOT NULL
)
WHERE daily_vaccinations IS NULL;
