row=0
col=0
for i in range (5):
  s=list(map(int,input().split()))  
  for j in range (5):
    if s[j]==1:
      row=i
      col=j
moves=abs(row-2)+abs(col-2)
print(moves)
