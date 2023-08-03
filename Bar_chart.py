import pandas as pd
import matplotlib.pyplot as plt
# with open(r'D:\2暂存文件\GitHub\Draw_diagram\Bar_chart_data.csv', mode='w', newline='') as file:
#     pass
bar_chart_data = pd.read_csv(r'D:\2暂存文件\GitHub\Draw_diagram\Bar_chart_data.csv') # Load data for bar chart plotting
plt.rcParams['font.sans-serif'] = ['SimSun'] # Display Chinese characters using SimSun font
plt.rcParams['axes.unicode_minus'] = False # Resolve the negative sign issue on the coordinate axes
sorted_data = bar_chart_data.sort_values(by='Number',inplace=False,ascending=False) # descending order and not change the ordinary data
plt.bar(sorted_data.Class,sorted_data.Number,width=0.6,label='Number',color='blue',alpha=0.6)
plt.legend(loc='upper right')
plt.xlabel('Classes')
plt.ylabel('Number')
plt.xticks(sorted_data.Class,rotation=45)
plt.title('The Numbers Of Student in 10 Classes')
diagram = plt.gcf()
diagram.subplots_adjust(left=0.1,bottom=0.2) # the left margin space will be 10% of the figure width,it is same with bottom
plt.savefig(r'D:\2暂存文件\GitHub\Draw_diagram\Bar_chart.png',dpi=600)
plt.show()
