# Flight Delay Prediction

### Team Members
| Name   | Github Handle   |
|--------|----------------|
| Benny Grullon  | @bgrullon |
| Teagan Cordes  | @cordestd   |
| Nataliia Bondarenko  | @NatkaBond   |

## Project Descripton 
#### Comparing Historical Flight and Weather data to determine the propability of delay versus weather conditions.

## Research Questions to Answer
1. What is the correlation between precipitation and flight delays ?
2. What is the correlation between windspeed and flight delays ?
3. What is the correlation between temp and flight delays ? 

## Datasets to be used
[Flight data from Kaggle](https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018)

[Weather Data from Visual Crossing](https://www.visualcrossing.com/)

### Rough Breakdown of Tasks
- [x] Set up github
- [x] Gather Data
- [x] Clean Data
- [x] Describe Data
- [x] Answer Questions
- [x] Decide propapbility of Prediction
- [x] Create prediction
- [x] Put together analsys
- [x] Create Powerpoint
- [x] Go over 10min presentation

---

## Requirements
#### Kaggle and [Kaggle API key](https://www.kaggle.com/)
`pip install kaggle`
#### [Dotenv](https://pypi.org/project/python-dotenv/)
`pip install python-dotenv`
#### [Airport Data](https://pypi.org/project/airportsdata/)
`pip install -U airportsdata`

### Analsys conclusions based on Precipitation
​
## 1. With a correlation coefficient of 0.06 (precipitation/arrival delays), and a correlation coefficient of 0.05 (precipitation/departure delays) in dataset is very weak. A correlation coefficient close to zero indicates that changes in precipitation have minimal impact on departure delays. With an R-squared value of approximately 0.0042 (based on arrival delays) and 0.0026 (based on departure delays) it indicates that only a very small proportion of the variation in flight delays can be explained by changes in precipitation. 
​
## 2. 
# Based on origin airport data:
#### The airport with the highest precipitation is MYR with a value of 1.151.
#### The airport with the lowest precipitation is ABQ with a value of 0.0.
# Based on destinaion airport data:
#### The airport with the highest precipitation is ATL with a value of 1.151.
#### The airport with the lowest precipitation is AUS with a value of 0.0.
​
## 3. The summary statistics provided above pertain to the top 10 airports with the highest precipitation levels. These statistics are calculated based on the "Origin Precipitation" data for the selected airports. The data shows that the precipitation levels can vary significantly across these airports, with some airports experiencing much higher precipitation than others. The statistics help in understanding the range and variability of precipitation among these top airports.


# Flight Delay vs Windspeed

#### The questions I was seeking to answer was "Is there a correlation between destination windspeed and flight delay time?". To answer this question I used scatter plots and linear regression to identify correlating trends in the data. When Departure delays were compared to destination windspeeds the Pearson's coefficient was 0.101 showing a very weak correlation, and further the R^2 value was 0.0127 showing a very weak correlation. The same was the case for arrival delays vs windspeed with a Pearson's coefficient and R^2 value of 0.113 and 0.0079 respectively. I examined smaller subsets of the data like the upper quartile of windspeeds, and delays over 30 minutes and 60  minutes, and the correlations were still very weak. Because of this I conclude that there is little to no correlation between flight delays and destination wind speed.