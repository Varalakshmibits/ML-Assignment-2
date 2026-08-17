Machine Learning Assignment 2

A. Problem Statement

The objective of this project is to predict whether a customer will subscribe to a term deposit using machine learning classification models. Various classification algorithms are implemented and compared based on their performance metrics to determine the best model for this dataset.

B. Dataset Description

Dataset Name: Bank Marketing Dataset

Source: UCI Machine Learning Repository

Problem Type: Binary Classification

Number of Records: 11,162

Number of Features: 16

Target Variable: deposit

Yes = Customer subscribed to term deposit
No = Customer did not subscribe to term deposit

The dataset satisfies the assignment requirements of having more than 500 records and more than 12 features.
C. GitHub Repository Link
https://github.com/YOUR_USERNAME/ML-Assignment-2
D. Models Used
Logistic Regression
Decision Tree Classifier
K-Nearest Neighbor Classifier
Gaussian Naive Bayes Classifier
Random Forest Classifier
E. Model Comparison Table
ML Model Name	Accuracy	AUC	Precision	Recall	F1 Score	MCCLogistic Regression	0.7900	0.8666	0.7931	0.7582	0.7753	0.5788
Decision Tree	0.7631	0.7621	0.7582	0.7404	0.7492	0.5249
KNN	0.7734	0.8451	0.7877	0.7198	0.7522	0.5461
Naive Bayes	0.7465	0.8106	0.7042	0.8097	0.7533	0.5004
Random Forest	0.8334	0.9097	0.8083	0.8538	0.8304	0.6679
F. Observations
Logistic Regression

Logistic Regression achieved good overall performance with balanced precision and recall and served as a strong baseline model.

Decision Tree

Decision Tree provided acceptable results but exhibited slightly lower performance compared to other models.

KNN

KNN performed better than Decision Tree and was able to classify customers reasonably well based on neighborhood similarity.

Naive Bayes

Naive Bayes achieved high recall but relatively lower precision due to its feature independence assumption.

Random Forest

Random Forest achieved the highest Accuracy, AUC, F1 Score, and MCC among all models and provided the most reliable performance.

Overall Winner

Random Forest Classifier
G. Streamlit Application Link
Paste Streamlit Application URL Here
