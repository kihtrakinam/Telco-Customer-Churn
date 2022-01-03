import pickle
import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.naive_bayes import BernoulliNB

churn_df_details = pickle.load(open('churn_df_details.pkl','rb'))
X, Y = churn_df_details['df_final'], churn_df_details['y']

smt = SMOTE(random_state=7, k_neighbors=5)
xsmt, ysmt = smt.fit_resample(X, Y)

model_final = BernoulliNB()
model_final.fit(xsmt,ysmt)

with open('model.pkl', 'wb') as f:
    pickle.dump(model_final, f)
    f.close()

model = pickle.load(open('model.pkl','rb'))
