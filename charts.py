import  pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("employees.csv")
# Bar chart

avg_salary=df.groupby("department")["salary"].mean()
plt.figure(figsize=(8,5))
bars=plt.bar(avg_salary.index,avg_salary.values)
plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.bar_label(bars,fmt="%.0f")
plt.tight_layout()
plt.savefig("department_salary.png")
plt.close()

# HISTOGRAM

plt.figure(figsize=(8,5))
plt.hist(df["salary"],bins=5,edgecolor="black")
plt.title("Salary Deistribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees ")
plt.tight_layout()
plt.savefig("salary_histogram.png")
plt.close()


# Scatter Plot
plt.figure(figsize=(8,5))
for department in df["department"].unique():
    department_data=df[df["department"]==department]
    plt.scatter(
        department_data["id"],
        department_data["salary"],
        label=department
    )
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")
plt.tight_layout()
plt.savefig("employee_scatter.png")
plt.close()

# Line Chart
months=["Jan","Feb","Mar","Apr","May","Jun"]
sales=[12,15,14,18,22,25]

plt.figure(figsize=(8,5)
)
plt.plot(months,sales,marker="o",label="Monthly Sales")
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.close()
