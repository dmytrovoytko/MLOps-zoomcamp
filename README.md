# MLOps-zoomcamp
[MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp/) 2024 homeworks 

1. [HW1](/01-intro/homework.md) Training a ride duration prediction model 

Dataset [NYC Taxi Trips](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)) Yellow

Linear regression with one-hot encoding

![Actual vs Prediction](/01-intro/Screenshot_2024-05-14_16-59-10.png)

2. [HW2](/02-experiment-tracking/homework.md) Use MLflow for experiment tracking and model management 

Dataset [NYC Taxi Trips](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)) Green

- Training model, saving it, experimenting to tune model hyperparameters
- Tracking all these processes with MLFlow via just several lines of Python code
- Choosing the best model (with hyperparameters) to use after testing

![Visualization of model hyperparameters experiments](/02-experiment-tracking/homework/20240526-135431.png)

![Visualization of final testing](/02-experiment-tracking/homework/20240526-151059.png)

[MLFlow](https://github.com/mlflow/mlflow) makes all this work so easy!