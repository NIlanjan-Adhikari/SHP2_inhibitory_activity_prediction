# SHP2_inhibitory_activity_prediction

This repository contains code and resources for predicting the inhibitory activity of SHP2 (Src homology 2 domain-containing protein tyrosine phosphatase 2) using machine learning techniques.

## Introduction
SHP2 is a protein phosphatase involved in various cellular processes and has emerged as a potential target for drug development. This project aims to develop a predictive model using machine learning algorithms to predict the inhibitory activity of compounds against SHP2.

## Repository Structure
The repository is organized as follows:<br>
10_fold_cross_validation: This directory contains the code for creating 10 folds.<br>
Data_processing: This directory contains the code for converting the raw data downloaded from BindingDB and Chembl databases to structured format.<br>
EDA: Jupyter notebooks are stored here for doing exploratory data analysis.<br>
Feature_selection: This directory contains the source code for implementing genetic algorithm for feature selection process.<br>
Final_data: This directory contains the final format of the dataset.<br>
Hyperparameter_tuning: This directory contains the code for implementation of Bayesian optimization for hyperparameter tuning for all the seven models.<br>
Model_development: This directory contains the code for training the seven models.<br>
Model_evaluation: This directory contains the code for evaluation curves like ROC curve, PR curve etc.<br>
Model_explainability: This directory contains the code for explainability of machine learning models using SHAP values.<br>
Raw_data: This directory contains the raw data downloaded from BindingDB, Chembl and literature [1,2]<br>
supplimentary: This directory contains some supplimentary analysis of the dataset.<br>
requirements.txt: A text file specifying the dependencies required to run the code.<br>

## Getting Started
To get started with this repository, follow the instructions below:

1. Clone the repository:

git clone https://github.com/NIlanjan-Adhikari/SHP2_inhibitory_activity_prediction.git

2. Install the required dependencies. It is recommended to use a virtual environment:
cd SHP2_inhibitory_activity_prediction
pip install -r requirements.txt

3. Explore the provided notebooks in the notebooks directory to understand the data and model training process.

## License
The code in this repository is licensed under the Apache License 2.0

## Contact
If you have any questions or inquiries, please contact the repository owner:

Name: NIlanjan Adhikari
Email: nilanjan.adhikari.phe17@itbhu.ac.in
Feel free to reach out with any questions or feedback!

## Reference
1. a
2. b
