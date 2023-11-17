# PROBLEM 1
# How many artists are there?
# Return a single column called "count" with a single row containing the count.
query_1 = """
select count("ArtistId") as count from "Artist"
    """

# PROBLEM 2
# How many Artists do not have an Album associated with them?
# Return a single column called "count" with a single row containing the count.
query_2 = """
select
	count(ar."ArtistId")
from
	"Artist" ar
left join "Album" al
on
	ar."ArtistId" = al."ArtistId"
where
	al."ArtistId" is null
"""

# PROBLEM 3
# How many Albums do not have an artist in the Artist table associated with them?
# Return a single column called "count" with a single row containing the count.
query_3 = """
select
	count(al."AlbumId")
from
	"Artist" ar
full join "Album" al
on
	ar."ArtistId" = al."ArtistId"
where
	ar."ArtistId" is null
"""

# PROBLEM 4
# List the tracks by "AC/DC"
# Return a single column called "AC/DC Tracks",
# in any order.
query_4 = """
select
	t."Name" as "AC/DC Tracks"
from
	"Track" t
join "Album" al
on t."AlbumId" = al."AlbumId"
join "Artist" ar
on ar."ArtistId"  = al."ArtistId" 
where
	ar."Name" = 'AC/DC'
"""

# PROBLEM 5
# Find the total sales of AC/DC Tracks.
# Return a single column called "Total Sales" with a single row containing the total.

query_5 = """
select
	sum(t."UnitPrice" * il."Quantity") as "Total Sales"
from
	"Track" t
join "Album" al
on t."AlbumId" = al."AlbumId"
join "Artist" ar
on ar."ArtistId"  = al."ArtistId" 
join "InvoiceLine" il
on il."TrackId" = t."TrackId" 
where
	ar."Name" = 'AC/DC'
"""

# PROBLEM 6
# Calculate total sales for each artist,
# as defined by the "Artist" table,
# Return two columns, "Artist" and "Total Sales",
# for the artists with less than or equal to $5 in sales,
# in any order.

query_6 = """
select
    ar."Name" AS "Artist",
    SUM(t."UnitPrice" * il."Quantity") AS "Total Sales"
from
	"Track" t
join "Album" al
on t."AlbumId" = al."AlbumId"
join "Artist" ar
on ar."ArtistId"  = al."ArtistId" 
join "InvoiceLine" il
on il."TrackId" = t."TrackId" 
GROUP BY
    ar."Name"
HAVING
    SUM(t."UnitPrice" * il."Quantity") <= 5

"""

# PROBLEM 7
# Calculate total sales for each artist,
# as defined by the "Artist" table,
# Return two columns, "Artist" and "Total Sales",
# in descending order of "Total Sales".

query_7 = """
select
	ar."Name" as "Artist",
	SUM(t."UnitPrice" * il."Quantity") as "Total Sales"
from
	"Track" t
join
    "Album" al on
	t."AlbumId" = al."AlbumId"
join
    "Artist" ar on
	ar."ArtistId" = al."ArtistId"
join
    "InvoiceLine" il on
	il."TrackId" = t."TrackId"
group by
	ar."Name"
order by
	"Total Sales" desc;
"""

# PROBLEM 8
# Find all of "Michael Mitchell"'s direct reports.
# Return 2 columns called "Name" and "Title".
# "Name" should have the employee's name in the form "last name, first name",
# for example, someone with the last name "Smith" and first name "Bob" should be "Bob, Smith".
# Hint: this requires a self join, picking clear aliases will help.

query_8 = """
SELECT
    CONCAT(e."LastName", ', ', e."FirstName") AS "Name",
    e."Title"
FROM
    "Employee" e
WHERE
    e."ReportsTo" = 6;

"""

# PROBLEM 9
# Make a reporting chart. For each employee, find their name, title, manager's name and manager's title.
# Return 4 columns called "Employee Name" and "Employee Title", "Manager Name" and "Manager Title",
# "Employee Name" and "Manager Name" should have the employee's name as in the form "last name, first name",
# for example someone with the last name "Smith "and first name "Bob" should be "Bob, Smith".
# Hint: this requires a self join, picking clear aliases will help.

query_9 = """
SELECT
    CONCAT(e."LastName", ', ', e."FirstName") AS "Employee Name",
    e."Title" AS "Employee Title",
    CONCAT(m."LastName", ', ', m."FirstName") AS "Manager Name",
    m."Title" AS "Manager Title"
FROM
    "Employee" e
LEFT JOIN
    "Employee" m ON e."ReportsTo" = m."EmployeeId";

"""

# PROBLEM 10
# Find the most recently hired employee(s) and their hire date(s)
# Return two columns called "Name" and "Hire Date",
# in any order.
# "Name" should have the employee's name as in the form "last name, first name",
# for example someone with the last name "Smith "and first name "Bob" should be "Bob, Smith"

query_10 = """
SELECT
    CONCAT("LastName", ', ', "FirstName") AS "Name",
    "HireDate" AS "Hire Date"
FROM
    "Employee"
ORDER BY
    "HireDate" DESC
LIMIT 1;

"""

# PROBLEM 11
# Assume today is "2010-01-01", find every employee's tenure.
# Return 3 columns called "First Name" "Last Name", "Tenure",
# in any order.

query_11 = """
SELECT
    "FirstName" AS "First Name",
    "LastName" AS "Last Name",
    '2010-01-01' - "HireDate" AS "Tenure"
FROM
    "Employee";
"""
# PROBLEM 12
# Assume today is 2010-01-01, find every employee with a tenure of less than 7 365-day years.
# Return 3 columns called "First Name" "Last Name", "Tenure",
# in ascending order of tenure.

query_12 = """
SELECT
    "FirstName" AS "First Name",
    "LastName" AS "Last Name",
    '2010-01-01' - "HireDate" AS "Tenure"
FROM
    "Employee"
WHERE
    '2010-01-01' - "HireDate" < interval '2555 days'
ORDER BY
    "Tenure" ASC;
"""
