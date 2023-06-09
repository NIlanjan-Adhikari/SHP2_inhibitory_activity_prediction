# SHP2 Enzyme Inhibitory Activity Prediction

This repository contains code and resources for predicting the inhibitory activity of SHP2 (Src homology 2 domain-containing protein tyrosine phosphatase 2) using machine learning techniques.

## Introduction
SHP2 is a protein phosphatase involved in various cellular processes and has emerged as a potential anticancer target for drug development. This project aims to develop predictive model using machine learning algorithms(Artificial neural networks, support vector machine, K nearest neighbour, Naive Bayes, Decision trees, XGBoost, Logistic regression)s. Developing an accurate and reliable machine learning based QSAR model can greatly aid in predicting the inhibitory activity of compounds against the SHP2 enzyme, facilitating the identification of potential drug candidates.

## Repository Structure
The repository is organized as follows:<br>

<b>10_fold_cross_validation:</b> This directory contains the code for creating 10 folds.<br>
<b>Data_processing:</b> This directory contains the code for converting the raw data downloaded from BindingDB and Chembl databases to structured format.<br>
<b>EDA:</b> Jupyter notebooks are stored here for doing exploratory data analysis.<br>
<b>Feature_selection:</b> This directory contains the source code for implementing genetic algorithm for feature selection process.<br>
<b>Final_data:</b> This directory contains the final format of the dataset.<br>
<b>Hyperparameter_tuning:</b> This directory contains the code for implementation of Bayesian optimization for hyperparameter tuning for all the seven models.<br>
<b>Model_development:</b> This directory contains the code for training the seven models.<br>
<b>Model_evaluation:</b> This directory contains the code for evaluation curves like ROC curve, PR curve etc.<br>
<b>Model_explainability:</b> This directory contains the code for explainability of machine learning models using SHAP values.<br>
<b>Raw_data:</b> This directory contains the raw data downloaded from BindingDB, Chembl and literature [1,2]<br>
<b>supplimentary:</b> This directory contains some supplimentary analysis of the dataset.<br>
<b>requirements.txt:</b> A text file specifying the dependencies required to run the code.<br>

## Getting Started
To get started with this repository, follow the instructions below:

1. Clone the repository:

     git clone https://github.com/NIlanjan-Adhikari/SHP2_inhibitory_activity_prediction.git

2. Install the required dependencies. It is recommended to use a virtual environment:
   
    pip install -r requirements.txt

4. Explore the provided notebooks for analysing results and developing models.

## License
The code in this repository is licensed under the Apache License 2.0

## Contact
If you have any questions or inquiries, please contact the repository owner:

Name: NIlanjan Adhikari<br>
Email: nilanjan.adhikari.phe17@itbhu.ac.in<br>
Feel free to reach out with any questions or feedback!

## Reference
1. Mitra, R., Ayyannan, S.R. (2021). Small-Molecule Inhibitors of Shp2 Phosphatase as Potential Chemotherapeutic Agents for Glioblastoma: A Minireview. ChemMedChem 16:777–787. https://doi.org/10.1002/CMDC.202000706
2. Tripathi, R.K.P., Ayyannan, S.R. (2021). Emerging chemical scaffolds with potential SHP2 phosphatase inhibitory capabilities – A comprehensive review. Chem Biol Drug Des 97:721–773. https://doi.org/10.1111/CBDD.13807
