import pandas as pd
import pickle
#load pickled file
filename= 'dic.csv'
f= open(filename, 'rb')
dic= pickle.load(f)
#convert dictionary to dataframe
df = pd.DataFrame(data=dic)
#standard deviation
print(df.std())