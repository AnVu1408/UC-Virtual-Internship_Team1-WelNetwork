# To  FIND HEALTHY COMMS
# READ DATA FROM CSV FILE
#FIND ROWS WITH ABOVE 80

import pandas as pd
import matplotlib.pyplot as plt 

# Read CSV file into DataFrame
df = pd.read_csv('./data/RURAL ICP with meter list.csv')  # replace with your actual file name

#if value of dc_day >100 assign it as 100
df['dc_day'] = df['dc_day'].clip(upper=100)

 # considering data completeness dc_day>80
healthy_comms =df[ df['dc_day'] > 80]

# Print rows where column 'dc_day' > 80
#print(df[healthy_comms])

#create a csv file for healthy_comms

healthy_comms.to_csv("healthy_comms2.csv")

# creating csv for unhealthy comms meter

unhealthy_comms = df[(df['dc_day'] > 0) & (df['dc_day'] <= 80)]
unhealthy_comms.to_csv("unhealthy_comms.csv")

# create a plot of meters
#data_completeness_0_with_antenna
#data_completeness_0_without_antenna
#unhealthy_with_antenna
#unhealthy_without_antenna
#healthy_with_antenna
#healthy_without_antenna


# Data
labels = ['dc_0_with_antenna', 'dc_0_without_antenna', 'unhealthy_with_antenna', 'unhealthy_without_antenna', 'healthy_with_antenna', 'healthy_without_antenna']
sizes = [20, 15, 10, 25, 5, 25]  # replace with your actual data

# Create pie chart
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart of Six Groups')
plt.show()


