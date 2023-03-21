#first make a directionary
#import matplotlib first
#type the total number,data,lables,colors,sizes and expodes one by one
#print plt.show() to show the pie diagram

movie = {'Comedy':73,'Action':42,'Romance':38,'Fantasy':28,'Science-fiction':22,'Horror':19,'Crime':18,'Documentary':12,'History':8,'War':7}

import matplotlib.pyplot as plt
Num = 267
data = [73,42,38,28,22,19,18,12,8,7]
labels = ['Comedy','Action','Romance','Fantasy','Science-fiction','Horror','Crime','Documentary','History','War']
colors = ['red','orange','yellow','green','purple','blue','black','grey','pink','brown']
sizes = [data[0]/Num*100,data[1]/Num*100,data[2]/Num*100,data[3]/Num*100,data[4]/Num*100,data[5]/Num*100,data[6]/Num*100,data[7]/Num*100,data[8]/Num*100,data[9]/Num*100]
expodes = (0,0,0,0,0,0,0,0,0,0)
plt.pie(sizes,explode=expodes,labels=labels,shadow=False,colors=colors,autopct='%1.1f%%')
plt.title("Favourite movie genres among Chinese university students")
plt.axis('equal')
plt.show()
