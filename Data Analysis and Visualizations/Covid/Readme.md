## About Project

Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.

Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.  Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.

This is an visualisation and analysis project for the impact of Corona Virus across the globe till 7th July,2020 using Jupyter Notebook and libraries like Seaborn, Pandas and Matplotlib.

### Dataset Informations:
- df_total: This Dataset Contains all information of COVID cases on the day 7th July, 2020 across the globe.
- df_confirmed,df_death,df_recovered: These Dataset contains the confirmed cases,deaths,recoveries due on everyday basis till the day of 7th July, 2020 across the globe at country level repectively.

### Final Observations
AS PER BASE ON RECORDS TILL 7th July,2020

- When looking at the number of death per million, San Marino is now the country with the highest number of Deaths per Million. The ranking would be as follows:
   1. San Marino 
   2. Belgium 
   3. United Kingdom 
   4. Andorra 
   5. Spain
   
Countries such as Belgium, Italy and Spain have rates around 500-900 Death per Million, the state of New York has 1259 Deaths per Million.

- Qatar is the country with most confirmed cases per million inhabitants. Most other countries in the "top" 10 of countries with the highest numbers of cases per million inhabitants are Western European countries.

- The US,Brazil are the countries with the highest (absolute) number of confirmed cases and unfortunately the trend is steep upward. Over the past weeks the US has also passed Spain and Italy regarding the total number of Deaths.

- When looking the the time series of the cumulative numbers of deaths while taking the day of the first reported death as "Day Zero", we can see that China managed to flatten the curve while in Italy and Spain the number of victims really exploded after 15-20 days after the first casualty. Although more "delayed", the trend is now looking very bad for especially the US.

- Belarus, Saudi Arabia and United Arab Emirates are doing best when looking at the number of deadly victims relative to the number of confirmed cases.
