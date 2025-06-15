import pandas as pd

# Load the data
df = pd.read_csv('data/customers.csv')

# Analyze
total = df['PurchaseAmount'].sum()
average = df['PurchaseAmount'].mean()
top_customer = df.loc[df['PurchaseAmount'].idxmax()]

# Output results
with open('summary.txt', 'w') as f:
    f.write(f"Total Revenue: {total}\n")
    f.write(f"Average Purchase: {average:.2f}\n")
    f.write(f"Top Customer: {top_customer['Name']} ({top_customer['PurchaseAmount']})\n")
