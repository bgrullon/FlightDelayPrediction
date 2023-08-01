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
3. What is the correlation between temp and flight delays ? min vs max ?
4. Trends of % flight delays/cancellations overall ?   

## Datasets to be used
[Flight data from Kaggle](https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018)

[Weather Data from Visual Crossing](https://www.visualcrossing.com/)

### Rough Breakdown of Tasks
- [x] Set up github
- [x] Gather Data
- [x] Clean Data
- [ ] Describe Data
- [ ] Answer Questions
- [ ] Decide propapbility of Prediction
- [ ] Create prediction
- [ ] Put together analsys
- [ ] Create Powerpoint
- [ ] Go over 10min presentation

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