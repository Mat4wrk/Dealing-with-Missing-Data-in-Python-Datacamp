Impute airquality DataFrame with the frontward fill method.
# Impute airquality DataFrame with ffill method
ffill_imputed = airquality.fillna(method='ffill', inplace=True)


Create a red colored line plot of ffill_imputed with a 'dotted' line style.
# Impute airquality DataFrame with ffill method
ffill_imputed = airquality.fillna(method='ffill')

# Plot the imputed DataFrame ffill_imp in red dotted style 
ffill_imputed['Ozone'].plot(color='red', marker='o', linestyle='dotted', figsize=(30, 5))

plt.show()


Overlay the airquality DataFrame on top of your plot.
Set the title to 'Ozone' and set marker to 'o'.
# Impute airquality DataFrame with ffill method
ffill_imputed = airquality.fillna(method='ffill')

# Plot the imputed DataFrame ffill_imp in red dotted style 
ffill_imputed['Ozone'].plot(color='red', marker='o', linestyle='dotted', figsize=(30, 5))

# Plot the airquality DataFrame with title
airquality['Ozone'].plot(title='Ozone', marker='o', figsize=(30, 5))

plt.show()
