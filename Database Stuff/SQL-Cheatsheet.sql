/*-------------------------------------------------------------------------------------------------------------
 Last Updated : 09/01/2024
 Name: Aerry Asmani
-------------------------------------------------------------------------------------------------------------*/

--- Statement to retrieve all the data from tablename
select *
from tablename

--- Statement to retrieve  the data from specific header in the tablename
select header1
from tablename

--- Statement to retrieve specifc data from specific header in the tablename
select header1
from tablename
where header1 =''

--- Statement to retrieve multiple  data from specifics headers in the tablename
select header1 , header2
from tablename

--- Statement to retrieve multiple  data from specifics headers with 1 or more conditions and is group by
select header1 , header2
from tablename
where header1='' and header2=''
Group by header1 , header2

--- Statement to combine 2 table 
SELECT t1.header1, t1.header2
FROM table1 t1
    JOIN table2 t2 ON t1.common_column = t2.common_column
-- Replace 'common_column' with the column both tables share
WHERE t1.header1 = '' AND t1.header2 = ''
    AND t2.header1 = '' AND t2.header2 = ''
GROUP BY t1.header1, t1.header2;

--- Statement to sort by asc/dsc
SELECT t1.header1, t1.header2
FROM table1 t1
    JOIN table2 t2 ON t1.common_column = t2.common_column
-- Replace 'common_column' with the column both tables share
WHERE t1.header1 = '' AND t1.header2 = ''
    AND t2.header1 = '' AND t2.header2 = ''
GROUP BY t1.header1, t1.header2
ORDER BY t1.header1 ASC, t1.header2 ASC;

--- Statement to  calculate distinct item in a for specific header
SELECT
    COUNT(DISTINCT CASE WHEN [header2] = 'Condition1' THEN [header1] END) AS NewHeader_Name_Condition1,
    COUNT(DISTINCT CASE WHEN [header2] = 'Condition2' THEN [header1] END) AS NewHeader_Name_Condition2,
    COUNT(DISTINCT CASE 
                    WHEN [header2] IN ('Condition1', 'Condition2')
        AND inserted_date >= 'start_date'
        AND inserted_date <= 'end_date' 
                    THEN [header2] 
                END) AS headerNewItem
FROM table1
WHERE [header1] IN ('Condition1', 'Condition2')
    AND inserted_date >= 'start_date'
    AND inserted_date <= 'end_date';

---Statement to calculate column value and convert it to percentage
SELECT
    COUNT(DISTINCT [Header1]) AS NewHeaderName,
    COUNT(DISTINCT [Header1]) * 100.0 / (
        SELECT COUNT(DISTINCT [Header1])
    FROM [Table1]
    ) AS NewHeaderName2
FROM [Table1]
WHERE [Header2] = 'condition'

--- Statement to calculate reminder when divide
SELECT
    date,
    SUM(
        (CAST((((CAST(column1 AS FLOAT) / CAST(NULLIF(Column2, 0) AS FLOAT)) / 200.0) * 100.0) AS DECIMAL(10, 2)) / 100.0) 
        * column3 
    ) AS Your_Temp_Column_Name
FROM
    your_table_name
GROUP BY
    date