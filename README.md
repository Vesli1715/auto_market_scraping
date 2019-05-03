# auto_market_scraping
Step 1 

Parsing data from website with lib BeautifulSoup and request (in scraping_data.py)

Step 2 

In file recording_in_db.py i'm  formatting and recording this data in two tables. 
As database used MYSQL server.
First table is all results from parsing, second table is average value of all results, groupt by years.

Step 3

In main.py  we get data from second table and draw graph of dependence
(axis x - years, axis y - prices). In graph we can compare diferent model o cars.
for this task i used matplotlib library
