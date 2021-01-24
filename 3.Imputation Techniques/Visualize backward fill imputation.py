Impute airquality with the backward fill method.
# Impute airquality DataFrame with bfill method
bfill_imputed = airquality.fillna(method='bfill')

Create a red colored line plot of bfill_imp with a 'dotted' line style with 'o' for markers.
# Plot the imputed DataFrame bfill_imp in red dotted style 
bfill_imputed['Ozone'].plot(color='red', marker='o', linestyle='dotted', figsize=(30, 5))

plt.show()

Overlay the airquality DataFrame on top of your plot.
Set the title to 'Ozone' and set marker to 'o'
# Plot the airquality DataFrame with title
airquality['Ozone'].plot(title='Ozone', marker='o', figsize=(30, 5))

plt.show()
