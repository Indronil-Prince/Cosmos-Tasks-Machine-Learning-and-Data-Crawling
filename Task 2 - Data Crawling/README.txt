COSMOS TASK - DATA CRAWLING

Hello. It is Indronil Bhattacharjee. I have tried to attempt the task to crawl data from Common Crawl archives. I tried two approaches here, some of the data with approach 1 and some with approach 2.

I have searched the months of JULY 2020 to DECEMBER 2020.

Approach 1:
1) First I have chosen some specific domains manually where I can get economic news, like World Bank, Asian Development Bank, World Economic Forum, etc.
2) Next the indices of the months of 2020, which I am considering,  are collected and stored as an index list. 
3) Then for each specific domain, the function crawl_link() has been called.
4) The crawl_link() function searches links with domain and downloads from the specific index client.
5) Then the HTML of the result had been extracted and COVID-related words and the root word 'Econom' of the economy are searched in the title of the page. If found, that had been stored and returned.
6) Finally, a workbook sheet had been created and stored in the excel worksheet.

Approach 2:
Steps 1, 2, and 3 are the same.
4) The crawl_link() function searches links with domain and does not download from the specific index client.
5) Then the COVID-related words and the root word 'Econom' of the economy are searched in the URL of the page. If found, the page content was requested with the URL and  the HTML of the result had been extracted. If the specific words were found in the title, those were stored and returned.
Step 6 is also the same

Thank you. 
