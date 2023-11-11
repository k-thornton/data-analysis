import pandas as pd
import matplotlib.pyplot as plt

# Load the Bitcoin price data from a CSV file
file_path = 'BTC-USD.csv'  # Replace with the path to your CSV file
btc_data = pd.read_csv(file_path)

# Plotting the Bitcoin price data with a logarithmic Y-axis
plt.figure(figsize=(10, 5))
plt.plot(pd.to_datetime(btc_data['Date']), btc_data['Close'], color='black', linewidth=2)

# Setting the Y-axis to logarithmic scale
plt.yscale('log')

# Setting custom ticks and labels for the Y-axis
plt.yticks([500, 5000, 50000], ['500', '5,000', '50,000'])

plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.gca().set_facecolor((0, 0, 0, 0))  # Setting transparent background

# Save the plot with a transparent background
plt.savefig('real_bitcoin_price_over_time_logarithmic_custom_labeled.png', transparent=True)

# Display the plot
plt.show()
