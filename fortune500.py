import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# Load the dataset
data = pd.read_csv('fortune500_with_ceo_data.csv')

# Convert the Year and CEO Birth Year to integers for calculation
data['Year'] = pd.to_numeric(data['Year'], errors='coerce')
data['CEO Birth Year'] = pd.to_numeric(data['CEO Birth Year'], errors='coerce')

# Calculate CEO's age
data['CEO Age'] = data['Year'] - data['CEO Birth Year']

# Plotting
plt.figure(figsize=(12, 8))
sns.regplot(x='Year', y='CEO Age', data=data, scatter=True, fit_reg=True, scatter_kws={'alpha':0.5})
plt.title('CEO Ages over the Years in Fortune 500 Companies')
plt.xlabel('Year')
plt.ylabel('CEO Age')
plt.grid(True)
plt.savefig('fortune500_ceo_ages.png')

# Perform linear regression analysis
regression_result = linregress(data['Year'].dropna(), data['CEO Age'].dropna())

# Print insights
print(f"Slope: {regression_result.slope}")
# print(f"Intercept: {regression_result.intercept}")
print(f"P-value: {regression_result.pvalue}")

if regression_result.pvalue < 0.05:
    print("The trend of increasing CEO age over time is statistically significant.")
else:
    print("There is no statistically significant trend in CEO age over time.")
