import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [1000, 1500, 1700, 1200, 1800, 2000]

plt.bar(months, sales, color='skyblue')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales (Jan-Jun)")
plt.show()