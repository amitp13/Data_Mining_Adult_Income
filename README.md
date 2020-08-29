# US Adult Income Analysis

The following jupyter notebook is an analysis into the Database for Adult Income in the United States. The Us Adult income dataset was extracted by Barry Becker from the 1994 US Census Database. The data set consists of anonymous information such as occupation, age, native country, race, capital gain, capital loss, education, work class and more. Each row is labelled as either having a salary greater than ">50K" or "<=50K". The main tasks here would be cleaning the data, Exploring it and building the appropriate model to predict the salary.  

#### Dataset
The dataset has 32534 rows and 16 columns. The variable are as follows:

| Column | Description |
| --- | --- |
| age  | Age of the adult |
| workclass | Sector of the job |
| fnlwgt | Final Weight |
| education | Last known degree of the Adult |
| education.num | No of years of Education |
| marital.status | Marital status of the Adult |
| occupation | Occupation of the Adult |
| relationship | Relationship of the Adult in the Family |
| race | Race of the Adult |
| sex | Gender of the Adult | 
| capital.gain | Capital Gain of the Adult |
| capital.loss | Capital Loss of the Adult |
| hours.per.week | No of hours worked per week |
| native.country | Native country of the Adult |
| income | Income of the Adult, read as above or below 50k |

#### Files in repository

| Column | Description |
| --- | --- |
| datacleaning.py  | Pyton file for data cleaning |
| EDA.py | Python file for Exploratory Data Analysis |
| model.py | Python File for Model building |
| adult_income.ipynb | Notebook for entire analysis |
| adult.csv | csv file conataining raw data |
