import pandas as pd
import numpy as np
from faker import Faker
import matplotlib.pyplot as plt

# Initialize Faker with Indian locale
fake = Faker('en_IN')

# Set seed for reproducibility
np.random.seed(42)

# Number of customers to simulate
num_customers = 1000

# Generate data
data = {
    'CustomerID': [fake.uuid4() for _ in range(num_customers)],
    'Name': [fake.name() for _ in range(num_customers)],  # Indian names
    'Age': np.random.randint(18, 70, size=num_customers),
    'Gender': np.random.choice(['Male', 'Female', 'Other'], size=num_customers),
    'Location': np.random.choice(
        ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Kolkata', 'Pune', 'Ahmedabad'], 
        size=num_customers
    ),
    'TotalOrders': np.random.randint(1, 50, size=num_customers),  # Total orders placed
    'AverageOrderValue': np.round(np.random.uniform(200, 2000, size=num_customers), 2),  # ₹200 to ₹2000
    'TimeSinceLastPurchase': np.random.randint(0, 90, size=num_customers),  # Days since last purchase
    'AppLogins': np.random.randint(0, 30, size=num_customers)  # App logins in the last month
}

# Create DataFrame
df = pd.DataFrame(data)

# Define Churn based on business logic
# Example: Customers who haven't purchased in the last 30 days are considered churned
df['Churn'] = df['TimeSinceLastPurchase'].apply(lambda x: 1 if x > 30 else 0)

# Save to CSV
df.to_csv('simulated_indian_customer_data.csv', index=False)

# Display basic statistics
print("Dataset Overview:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Visualize churn distribution
df['Churn'].value_counts().plot(kind='bar', color=['blue', 'orange'])
plt.title('Churn Distribution')
plt.xlabel('Churn')
plt.ylabel('Count')
plt.show()

print("\nSimulated Indian Customer Dataset has been successfully created and saved as 'simulated_indian_customer_data.csv'.")