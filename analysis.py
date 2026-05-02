import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel(r'C:\AML-2\cbi_enforcement_data.csv.xlsx')
df = df.rename(columns={'Type_of _Company': 'Type_of_Company'})
df['Fine_Amount'] = pd.to_numeric(df['Fine_Amount'], errors='coerce').fillna(0)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Year'] = df['Date'].dt.year
print("Columns now:", df.columns.tolist())
print("Year sample:", df['Year'].tolist())

yearly = df.groupby('Year')['Fine_Amount'].sum().reset_index()
plt.figure(figsize=(10,5))
plt.bar(yearly['Year'], yearly['Fine_Amount'], color='#003366', width=0.5)
plt.title('Total CBI Fines Per Year')
plt.savefig('chart1.png', dpi=150)
plt.show()
print("Chart 1 done")

by_type = df.groupby('Type_of_Company')['Fine_Amount'].sum().reset_index().sort_values('Fine_Amount', ascending=True)
plt.figure(figsize=(10,6))
plt.barh(by_type['Type_of_Company'], by_type['Fine_Amount'], color='#2E86C1')
plt.title('Total Fines by Institution Type')
plt.savefig('chart2.png', dpi=150)
plt.show()
print("Chart 2 done")

breach = df['Breach_Category'].value_counts().reset_index()
breach.columns = ['Breach_Category','Count']
plt.figure(figsize=(10,5))
plt.barh(breach['Breach_Category'], breach['Count'], color='#C0392B')
plt.title('Cases by Breach Type')
plt.savefig('chart3.png', dpi=150)
plt.show()
print("Chart 3 done")

actions = df.groupby('Year').size().reset_index(name='Count')
plt.figure(figsize=(10,5))
plt.plot(actions['Year'], actions['Count'], marker='o', color='#003366', linewidth=2.5)
plt.title('Enforcement Actions Per Year')
plt.savefig('chart4.png', dpi=150)
plt.show()
print("Chart 4 done")

df.to_csv(r'C:\AML-2\cbi_powerbi.csv', index=False)
print("FINISHED - cbi_powerbi.csv saved")