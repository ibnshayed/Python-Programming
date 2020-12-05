import sys

n, m = [int(x) for x in input().split(' ')]
ans = 0
 
if( m % n != 0):
    print(-1)
    sys.exit()
    
div = m / n
 
while(div%2==0):
    div /= 2
    ans += 1
 
while(div%3==0):
    div /= 3
    ans += 1
	
if(div==1):
    print(ans)
else:
    print(-1)
    
