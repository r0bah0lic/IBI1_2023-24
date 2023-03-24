#list the costs first
#then store it of sorted values
#print the sorted list
costs = [1,8,15,7,5,14,43,40]
costs.sort()
print(costs)

#import the matplotlib first
#Initializes shortcuts to graph and subgraph axes
#input the data of x axis and y axis
#set the color of the bars
#set the title of the diagram
#show the picture

cities = ['Los Angeles 1984','Sydney 2000','Atlanta 1996','Seoul 1988','Athens 2003','Barcelona 1992','London 2012','Beijing 2008']
import numpy
cities=numpy.array(cities)
costs=numpy.array(costs)
sortedcosts=costs.argsort()
sorted_cities=cities[sortedcosts]
sorted_costs=costs[sortedcosts]
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.xlabel("cities")
plt.ylabel("costs")
bar_colors=['tab:blue','tab:blue','tab:blue','tab:blue','tab:blue','tab:blue','tab:blue','tab:blue']
ax.bar(cities,costs, color=bar_colors)
ax.set_ylabel('Cost (in $ billions)')
ax.set_title('Olympic Costs')  
plt.show()

