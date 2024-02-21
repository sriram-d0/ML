#dataset is named as data available in repositry as enjoysport.csv
n=len(data.columns)-1
h=['O' for i in range(n)]
d=list(data.values)
for i in d:
  if i[-1]=='Yes':
    for j in range(n):
      if i[j]!='O':
        if h[j]=='O':
          h[j]=i[j]
        elif h[j]!=i[j]:
          h[j]='?'
print(h)
