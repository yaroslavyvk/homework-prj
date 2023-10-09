import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.show()

sns.boxplot(data=tips, x='day', y='total_bill')
plt.show()


sns.violinplot(data=tips, x='day', y='total_bill')
plt.show()


sns.histplot(data=tips, x='total_bill', bins=30)
plt.show()

sns.barplot(data=tips, x='day', y='total_bill')
plt.show()

sns.countplot(data=tips, x='day')
plt.show()

sns.pairplot(tips)
plt.show()

numeric_cols = tips.select_dtypes(include=['float64', 'int64'])
corr = numeric_cols.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

sns.lineplot(data=tips, x='total_bill', y='tip')
plt.show()
