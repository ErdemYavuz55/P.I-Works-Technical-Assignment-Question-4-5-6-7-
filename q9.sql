SELECT 
    Device_Type,
    REGEXP_REPLACE(
        REGEXP_REPLACE(Stats_Access_Link, '<url>https?://', ''),
        '</url>', ''
    ) AS Pure_URL
FROM 
    your_table_name;
