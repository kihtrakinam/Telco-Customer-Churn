# Telco-Customer-Churn
* ML Classification problem to derive business insights and identify potential customers who might churn
* **Objective:** To help the telecom company to identify the potential churning customers in advance so that they can do proactive steps in customer retention like customized targeted advertising and customer care / grievance services.
* Use Statistics and Visualization techniques to understand the important factors which affect the target class and get business inferences.
* Final Model building

## Code and Resources Used
**Python Version:** 3.7  
**Packages:** pandas, numpy, statsmodel, scipy, matplotlib, seaborn, sklearn, imblearn, flask, gunicorn
**Model Deployment:** Flask, Github, Heroku 

**Deployed model link** : https://telco-churn-bnb.herokuapp.com/
![alt text](https://github.com/kihtrakinam/Telco-Customer-Churn/blob/91198b6473d213b6a063f71c75ad431b9f53e5d2/Images/9_Model_deployment_heroku.JPG "Deployed model in Heroku")

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

## Important EDA Observations
1. **How does the distribution of tenure varies for churned customers?**
![alt text](https://github.com/kihtrakinam/Telco-Customer-Churn/blob/774110fa0e0c2be0c3702e6bfc722ace5292f7e6/Images/1_Tenure_vs_Churn.jpg "Tenure Distribution")
- Median age of existing customers is just below 40. Whereas, it drops to 10 for the churned customers
2. **Is there any significant change in churning based on subscription to PhoneService?**
![alt text](https://github.com/kihtrakinam/Telco-Customer-Churn/blob/774110fa0e0c2be0c3702e6bfc722ace5292f7e6/Images/2_PhoneService_vs_Churn.jpg "Phone Service vs Churn")
- In actual numbers, customers who are subscribed to Phone service have churned high but there is no difference in churn rate
3. **Related to Internet and Premium Services**
![alt text](https://github.com/kihtrakinam/Telco-Customer-Churn/blob/774110fa0e0c2be0c3702e6bfc722ace5292f7e6/Images/3_Internet-PremiumServices_vs_Churn.jpg "Internet Service vs Churn")
  A. **Is there any significant change in churning based on subscription to InternetService?**<br>
  Yes, Customers opting for Fiber Optic Internet Service are the majority who churned<br><br>
  B. **Does non subscription to premium non-streaming services impact churning?**<br>
  Yes, Approximately 56% of the customers who have not subscribed to Premimum non-streaming services have churned<br><br>
  C. **Does non subscription to premium streaming services impact churning?**<br>
  No, there is no significant impact<br><br>
4. **Do Senior Citizens churn more?**
![alt text](https://github.com/kihtrakinam/Telco-Customer-Churn/blob/774110fa0e0c2be0c3702e6bfc722ace5292f7e6/Images/4_SeniorCitizen_vs_Churn.jpg "Senior Citizen vs Churn")
- Even though churn ratio is high for Senior citizens, in absolute numbers, non senior citizens are high
5. **Does contract type help to infer churning?**
![alt text](https://github.com/kihtrakinam/Telco-Customer-Churn/blob/774110fa0e0c2be0c3702e6bfc722ace5292f7e6/Images/5_ContractType_vs_Churn.jpg "Contract Type vs Churn")
- Yes, Clearly customers with Month-to-month contract are churning high both in absolute numbers and ratio
6. **Does preferred Payment method help to infer churning?**
![alt text](https://github.com/kihtrakinam/Telco-Customer-Churn/blob/774110fa0e0c2be0c3702e6bfc722ace5292f7e6/Images/6_PaymentMethod_vs_Churn.jpg "Payment method vs Churn")
- Yes, Customers who prefer to pay using manual Electronic Check method are churning high both in absolute numbers and ratio
7. **Does preference to PaperlessBilling has any impact on Churning?**
![alt text](https://github.com/kihtrakinam/Telco-Customer-Churn/blob/774110fa0e0c2be0c3702e6bfc722ace5292f7e6/Images/7_PaperlessBilling_vs_Churn.jpg "PaperlessBilling vs Churn")
- Yes, customers who prefer Paperless Billing are churning high

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
![alt text](https://github.com/kihtrakinam/Telco-Customer-Churn/blob/774110fa0e0c2be0c3702e6bfc722ace5292f7e6/Images/8_Final_model_performance_crosstab.jpg "Final model performance crosstab")
-	The model predicts approximately 39% of the total customers as in risk to be churned this quarter which is 1.4 times more than the actual who churned
-	The model is able to capture 75% of the people who actually churned
-	If the model predict a customer as risky for churning, there is 52% chance that he/she will actually churn. 
-	On the other hand, if the model predict a customer safe from churning, there is only 11% chance that he/she will churn

## Business Conclusion
The final model had a recall of 65% to 80% and a precision of 46% to 57% within 95% confidence interval based on the Cross validation scores. Thus, we are able to identify atmost 80% of the customers who are potential to churn in advance. Since, the precision is less, we can contact all these customers with generic mail or call and further advertise or understand their requirements.
