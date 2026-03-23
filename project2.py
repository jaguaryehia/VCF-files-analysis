import pandas as pd
import statsmodels.api as sm
from scipy.stats import ttest_ind

df=pd.read_csv('AssignmentData.csv')
print(df.isnull().sum())
print(df.notnull().sum())
print(df.isnull().mean())
print(df.notnull().mean())
cols=df.columns
for i in cols:
    df[i]=df[i].fillna("")
print(df.isnull().sum())

y = df['GDP']
x = df['Political Context_WPFI']
x = sm.add_constant(x)
model = sm.OLS(y, x).fit()
print(model.summary())

r2 = model.rsquared
print("Coefficient of determination (R-squared):", r2)
# Interpret the coefficients of the independent variables
coefficients = model.params[1:]
print("Coefficients of the independent variables:")
for i in range(len(coefficients)):
    print(x.columns[i+1], ":", coefficients[i])

# y2=df['Score_WPFI']
# x2=df['Legal Framework_WPFI']
# x2 = sm.add_constant(x2)
# model2 = sm.OLS(y2, x2).fit()
# print(model2.summary())

group1 = df[df['Safety Score_WPFI'] == 1]['Safety Score_WPFI']
group2 = df[df['Score_WPFI'] == 2]['Score_WPFI']

# Conduct a two-sample t-test assuming unequal variances
t_stat, p_val = ttest_ind(group1, group2, equal_var=False)

# Print the results
print('Test statistic: ', t_stat)
print('p-value: ', p_val)

# Interpret the results
alpha = 0.05  # significance level
if p_val < alpha:
    print('Reject null hypothesis - there is a significant difference between the two groups.')
else:
    print('Fail to reject null hypothesis - there is no significant difference between the two groups.')
