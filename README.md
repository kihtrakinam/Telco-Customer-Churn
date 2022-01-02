# Telco-Customer-Churn
* ML Classification problem to derive business insights and identify potential customers who might churn
* **Objective:** To help the telecom company to identify the potential churning customers in advance so that they can do proactive steps in customer retention like custom targeted advertising and customer care / grievance services.
* Use Statistics and Visualization techniques to understand the important factors which affect the target class and get business inferences.
* Final Model building

## Code and Resources Used
**Python Version:** 3.7  
**Packages:** pandas, numpy, statsmodel, scipy, matplotlib, seaborn, sklearn, imblearn, flask
**Tableau Public**

## Dataset Features and Description
* The data set is a sample dataset that tracks a fictional telco company's customer churn based on various factors.
* It contains 7043 records and includes 21 features 
* The churn column indicates whether the customer departed within the last month. 
* Other features represent gender, dependents, monthly charges, and many with information about the types of services each customer has.

## Data Cleaning steps
* Redundant Columns removal
*	Data Encoding

## EDA steps
* **Five point Descriptive Statistics** - Univariate description of both the numerical and categorical variables
* **Correlation and Pair plot** - Distribution and the relation between the numerial variables
* **Univariate, Bivariate and Multivariate Analysis** - Plotting Countplots, Barplots and 100% stacked barplots to visualize and infer the importance of the features

## Important EDA Questions
- To be updated

## Complexity observed
- Class imbalance
- Overlapping

## Feature Selection
* VIF Factor for multi collinearity
* Mann Whitney statistical Test for numerical features
* Chi-Square Yate's Correction statistical Test for categorical features
* Reverse Backward Elimation method

## Final Model building Approach
* Model building – 4 base models, 7 Bernoulli Naive Bayes model with different sampling techniques
* Model performance metrics – (Precision, Recall) of churn == 1
* Model selection – 10 fold Cross Validation scores
* Final model – Bernoulli Naive Bayes with SMOTE sampling technique

## Final Model Performance
- To be updated

## Business Conclusion
The final model had a recall of 65% to 80% and a precision of 46% to 57% within 95% confidence interval based on the Cross validation scores. Thus, we are able to identify atmost 80% of the customers who are potential to churn in advance. Since, the precision is less, we can contact all these customers with generic mail or call and further advertise or understand their requirements.
