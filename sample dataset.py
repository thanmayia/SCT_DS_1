import matplotlib.pyplot as plt

# Step 1: Prepare the data from the image
# Categories for the x-axis
age_groups = ['0-20 Years', '21-64 Years', '65+ Years']

# Corresponding values (population in millions) for the y-axis
population_in_millions = [512, 807, 98]

# Assign colors similar to the example chart
colors = ['gold', 'deepskyblue', 'mediumvioletred']

# Step 2: Create the bar chart
# Create a figure and an axes object for the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the bar chart with specified colors
bars = ax.bar(age_groups, population_in_millions, color=colors)

# Step 3: Customize the plot with labels and a title
ax.set_xlabel('Age Groups', fontweight='bold')
ax.set_ylabel('Population (in Millions)', fontweight='bold')
ax.set_title("India's Population Distribution by Age in 2022", fontweight='bold', fontsize=14)
ax.grid(axis='y', linestyle='--', alpha=0.7) # Add a grid for better readability

# Step 4 (Optional): Add the population value on top of each bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, f'{int(yval)} Mn', va='bottom', ha='center') # va='bottom' places text above the bar

# Step 5: Display the plot
plt.tight_layout() # Adjusts plot to prevent labels from overlapping
plt.show()