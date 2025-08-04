import matplotlib.pyplot as plt

# Data
companies = ['A', 'B', 'C', 'D']
shares = [35, 25, 25, 15]

# Create pie chart
plt.pie(shares, labels=companies, autopct='%1.1f%%', 
        startangle=90)

# Add title
plt.title("Company Market Shares")

# Make the chart a circle
plt.axis('equal')

# Display the chart
plt.show()