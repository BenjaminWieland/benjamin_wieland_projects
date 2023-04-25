# Create pandas data frame from csv file
import pandas as pd
budget = pd.read_csv("budget.csv", sep=';')
budget_df = pd.DataFrame(budget)

# Analyze a personal budget
# Calculate sums of income and expenses
sum_income = pd.DataFrame.sum(budget_df["In"])
sum_expenses = pd.DataFrame.sum(budget_df["Out"])
# Calculate possible savings
savings = sum_income - sum_expenses

# Calculate highest expenses per category with pandas
highest_expenses = budget_df[["Category", "Out"]].groupby("Category").sum()
print(highest_expenses.sort_values(by= "Out", ascending=False))
highest_expenses_df = pd.DataFrame(highest_expenses)
print(highest_expenses_df.info())

# Visualize analyses with seaborn
import seaborn as sns
sns.set_theme()
expenses_plot = sns.barplot(data= highest_expenses_df, x="Out", y=highest_expenses.index, errorbar=None)
expenses_plot.figure.savefig("expenses_per_category.png", bbox_inches= "tight")

# Analyze monthly changes in expenses and visualize them with seaborn
budget_df["Date"] = pd.to_datetime(budget_df["Date"])
groups = budget_df[["Date", "Out"]].groupby(pd.Grouper(key= "Date", freq= "M")).sum()
print(groups)

groups_plot = sns.barplot(groups, x=groups.index.month_name(), y= "Out", errorbar=None )
groups_plot.figure.savefig("expenses_per_month.png", bbox_inches= "tight")