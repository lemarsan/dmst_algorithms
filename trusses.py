import sys
text=sys.argv[1]
k=int(sys.argv[2])
lists=[]
j=-1
dictio={}
array={}
edge={}
edges=[]
g=open(text,'r')
for line in g:
	x, y=map(int,line.split())
	dictio.setdefault(x,[]).append(y)
numbers=[]	


def neighbours(a):
	return dictio[a]

def intersection (s1,s2):
	d=set(s1)
	c=set(s2)
	inter=d&c
	return inter

def size(w):
	sizes=len(w)
	return sizes

for x in dictio:
	for i in dictio:		
		if i in dictio[x]:
			j=j+i
			edges.append(x)
			edges.append(i)
			edge[j]=edges
			edges=[]
for t in edge:
	a=min(edge[t])
	b=max(edge[t])
	s1=neighbours(a)
	s2=neighbours(b)
	sizes=intersection(s1,s2)
	numbers=[int(q) for q in sizes]
	if (size(sizes)>=k-2):
		final=[]
		final.append(a)
		final.append(b)
		final.append(numbers)
		print (final)

    
	
