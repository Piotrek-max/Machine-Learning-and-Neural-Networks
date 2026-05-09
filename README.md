# Machine Learning and Neural Networks

Fully completed Machine learning Pipeline based on "Bike Sharing Demand" dataset.
It is also the final project for the academic course of the same name.

# Introduction
1. Define the goal:
The goal of this project is to predict the demand for bike sharing in a city based on various.
2. Explore available data:
Features:
### **Bike Sharing Demand Dataset - Feature Overview**

| Feature        | Description | Values / Normalization                                  |
|:---------------| :--- |:--------------------------------------------------------|
| **season**     | Season | 1:springer, 2:summer, 3:fall, 4:winter                  |
| **year**       | Year | 0: 2011, 1:2012                                         |
| **month**      | Month | 1 to 12                                                 |
| **hour**       | Hour | 0 to 23                                                 |
| **holiday**    | Whether day is holiday or not | Extracted from http://dchr.dc.gov/page/holiday-schedule |
| **weekday**    | Day of the week | 0 to 6                                                  |
| **workingday** | If day is neither weekend nor holiday is 1, otherwise is 0 | 1: Working Day, 0: Weekend/Holiday                      |
| **weather**    | Weather situation | clear, heavy_rain, misty, rain                          |
| **temp**       | Normalized temperature in Celsius | Values are divided by 41 (max)                          |
| **feel_temp**  | Normalized feeling temperature in Celsius | Values are divided by 50 (max)                          |
| **humidity**   | Normalized humidity | Values are divided by 100 (max)                         |
| **windspeed**  | Normalized wind speed | Values are divided by 67 (max)                          |
| **count**      | **Total rental bikes** | **Total count (casual + registered)**                   |


# Dataset
The dataset is available on OpenML [Bike Sharing Demand](https://www.openml.org/d/42712)