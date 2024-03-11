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
- example : C:\Users\HP\Downloads\Scrapy data\scrappingtask\scrappingtask> scrapy crawl taskspider  

To saved parsing respone on Json file

- scrapy crawl taskspider -o taskdata.json

--------*Sample Data*------------
   
![Screenshot 2024-03-11 140907](https://github.com/rishu27/Scrapy-data/assets/95354739/fab32333-adf3-476d-b6f5-7f18df629787)


JSEON file :
![image](https://github.com/rishu27/Scrapy-data/assets/95354739/0493c650-058d-43cf-b9bd-e361409d2756)


Thank you. 
