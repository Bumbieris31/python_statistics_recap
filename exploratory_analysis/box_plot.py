# Specify array of percentiles: percentiles
percentiles = np.array([2.5, 25, 50, 75, 97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length, percentiles)

# Print the result
print(ptiles_vers)

# Plot the ECDF
# GET THE ECDF DATA

_ = plt.plot(x_vers, y_vers, '.')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
_ = plt.plot(ptiles_vers, percentiles/100, marker='D', color='red',
         linestyle='none')

# Show the plot
plt.show()

# Box plot
# Create box plot with Seaborn's default settings
_ = sns.boxplot(df['species'], df['petal length (cm)'])

# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length')

# Show the plot
plt.show()


