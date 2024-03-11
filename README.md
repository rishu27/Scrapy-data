# Web-Scraping-using-Scrapy


Its basically about the Scrapy framework, in which we can scrap or crawl the data from websites using recursive spiders..

In this project I take a website named (https://www.reed.co.uk/jobs/data-analyst-jobs) and scrap the data related to jobs(including URL, TITLE, SALARY,CONTRACT, JOB TYPE, LOCATION).

--------**Install Scrapy**--------
- pip install scrapy


Make a folder as named Scrapy data inside it scrappingtask 

--------**In Visual Studio Code**--------
  
  Open that folder
  
  To start a project

- scarpy startproject scrappingtask


To creating first spider
Go to spiders folder and create a taskspider.py file

- touch taskspider.py
  


To scrap JOBS details

- scrapy crawl taskspider
- example : C:\Users\HP\Downloads\Scrapy data> scrapy crawl taskspider  

To saved parsing respone on Json file

- scrapy crawl taskspider -o taskdata.json


Thank you. 