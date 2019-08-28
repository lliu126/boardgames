import pickle
import pandas as pd
import matplotlib.pyplot as plt

#load ratings files
filename= 'geek.csv'
f= open(filename, 'rb')
geekrating= pickle.load(f)
#print(geekrating)
filename= 'avg.csv'
g= open(filename, 'rb')
avgrating= pickle.load(g)
#print(avgrating)
filename= 'voters.csv'
h= open(filename, 'rb')
voters= pickle.load(h)
#print(geekrating)

#plot1
plt.plot([geekrating],[voters],'ro')
plt.ylabel("Number of Voters")
plt.xlabel("Geek Member Ratings")
plt.show()

#plot2
plt.plot([avgrating],[voters],'ro')
plt.ylabel("Number of Voters")
plt.xlabel("Average Ratings ")
plt.show()

