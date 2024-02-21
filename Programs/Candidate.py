#dataset is in the repository named as enjoysport.csv
n=len(data.columns)-1
G=[['?' for i in range(n)]for j in range(n)]
d=list(data.values)
S=d[1][:-1]
for i in d:
  if i[-1]=='Yes':
    for j in range(n):
      if(i[j]!=S[j]):
        S[j]='?'
        G[j][j]='?'
  elif i[-1]=='No':
    for j in range(n):
      if(i[j]!=S[j]):
        G[j][j]=S[j]
      else:
        G[j][j]='?'
h=[]
for i in G:
  for j in i:
    if j!='?':
      h.append(i)
      break
print(S)
print(h)
