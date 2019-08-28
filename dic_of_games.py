from bs4 import BeautifulSoup
import requests
import pickle
def dicOfGames():
#scrapes top 100 board game names into a list names
	names=[]
	for i in soup.find_all(style='z-index:1000;'):
		try:
			line=i.a.text
			names.append(line)
		except:
			continue

#scrapes all variables of geekrating, avgrating and voters into a list lis
	lis=[]
	for j in soup.find_all(class_='collection_bggrating'):
		try:
			some= j.text
			lis.append(some)
		except:
			continue
	lis = [''.join(item.split()) for item in lis]
	for i in range(4):
		del(lis[0])
	lis=[float(i) for i in lis]
	#print(lis)

#from lis, divides geekrating, avgrating and voters into individual lists, puts all into new list lis2
	lis2=[]
	for a in range(100):
		lis2.append([lis[0], lis[1], lis[2]])
		del(lis[2])
		del(lis[1])
		del(lis[0])
	#print(lis2)

#using a loop to define new dic with name as the key and sets of lis2 as values
	dic={}
	for l in range(100):
		dic[names[l]]=lis2[l]
#save dictionary to pickled file for use in other programs
	filename= 'dic.csv'
	f= open(filename, 'wb')
	pickle.dump(dic,f)
	print('saved successful')

def ratingsList():
	lis=[]
		
	for j in soup.find_all(class_='collection_bggrating'):
		try:
			some= j.text
			lis.append(some)
		except:
			continue
	lis = [''.join(item.split()) for item in lis]
	for i in range(4):
		del(lis[0])
	lis=[float(i) for i in lis]
		
	names=[]
	for i in soup.find_all(style='z-index:1000;'):
		try:
			line=i.a.text
			names.append(line)
		except:
			continue
	#print('Names: ', names)
		
	#make lists of geekrating, avgrating and voters
	geekrating=(lis[0::3])
	avgrating=(lis[1::3])
	voters=(lis[2::3])
	
	#Save ratings to pickled files for use in other project programs
	filename= 'geek.csv'
	f= open(filename, 'wb')
	pickle.dump(geekrating,f)
	filename= 'avg.csv'
	g= open(filename, 'wb')
	pickle.dump(avgrating,g)
	filename= 'voters.csv'
	h= open(filename, 'wb')
	pickle.dump(voters,h)
	print('saved successful')
#main()
x= requests.get('https://boardgamegeek.com/browse/boardgame')
y= x.text
soup=BeautifulSoup(y,'lxml')

dicOfGames() #function creates dic with name and values of floats which are: Geek Rating, Avg Rating and Num Voters --> then prompts answer
ratingsList()