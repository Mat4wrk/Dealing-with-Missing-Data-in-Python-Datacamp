Visualize the missingness matrix of diabetes.
# Visualize the missingness in the data
msno.matrix(diabetes)

# Display nullity matrix
display("/usr/local/share/datasets/matrix_diabetes.png")


Visualize the missingness heatmap of diabetes.
# Visualize the missingness in the data
msno.matrix(diabetes)

# Visualize the correlation of missingness between variables
msno.heatmap(diabetes)

# Show heatmap
plt.show()

Drop the all the cases where BMI is missing.
# Visualize the missingness in the data
msno.matrix(diabetes)

# Visualize the correlation of missingness between variables
msno.heatmap(diabetes)

# Show heatmap
plt.show()

# Drop rows where 'BMI' has a missing value
diabetes.dropna(subset=['BMI'], how='all', inplace=True)
