import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Verify the current working directory
print(f"Current working directory: {os.getcwd()}")

# Define the path to the CSV file
file_path = 'Order_details(masked).csv'

# Check if the file exists
if not os.path.isfile(file_path):
    raise FileNotFoundError(f"The file '{file_path}' does not exist. Please check the file path and name.")

# Load the data
Order_Details = pd.read_csv(file_path)

# Convert 'Transaction Date' to datetime
Order_Details['Time'] = pd.to_datetime(Order_Details['Transaction Date'])

# Extract hour from 'Transaction Date'
Order_Details['Hour'] = Order_Details['Time'].dt.hour

# Get top 24 busy hours
timemost1 = Order_Details['Hour'].value_counts().index.tolist()[:24]
timemost2 = Order_Details['Hour'].value_counts().values.tolist()[:24]

# Combine hour and counts into an array
tmost = np.column_stack((timemost1, timemost2))

# Print hours and counts
print("Hour Of Day\tCumulative Number of Purchases")
print('\n'.join('\t\t'.join(map(str, row)) for row in tmost))

# Prepare data for plotting
timemost = Order_Details['Hour'].value_counts().sort_index()
timemost1 = list(range(24))
timemost2 = timemost.tolist()

# Plot the data
plt.figure(figsize=(20, 10))
plt.title('Sales Happening Per Hour (Spread Throughout The Week)', fontdict={'fontname': 'monospace', 'fontsize': 30}, y=1.05)
plt.ylabel("Number Of Purchases Made", fontsize=18, labelpad=20)
plt.xlabel("Hour", fontsize=18, labelpad=20)
plt.plot(timemost1, timemost2, color='m')
plt.grid()
plt.show()