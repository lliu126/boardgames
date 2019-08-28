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

#min, max, median, deviation for each rating
df = pd.DataFrame(data=geekrating)
print('Geek Rating Stats:')
print('Min: ', df.stack().min())
print('Max: ', df.stack().max())
print('Median: ', df.stack().median())
print('Standard Deviation: ', df.stack().std())
print()
df = pd.DataFrame(data=avgrating)
print('Average Rating Stats:')
print('Min: ', df.stack().min())
print('Max: ', df.stack().max())
print('Median: ', df.stack().median())
print('Standard Deviation: ', df.stack().std())
print()
df = pd.DataFrame(data=voters)
print('Voters Stats:')
print('Min: ', df.stack().min())
print('Max: ', df.stack().max())
print('Median: ', df.stack().median())
print('Standard Deviation: ', df.stack().std())

