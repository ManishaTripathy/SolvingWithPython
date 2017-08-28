
# Remove duplicates from a string, do it in-place

T=int(input())
in_strings=[]
def remdup(s):
    result=''
    for i in s:
        if i not in result:
            result= result + i
        else:
            continue
    return result
    
for i in range(0,T):
    in_strings.append(input())
	
output=[]
for s in in_strings:
    output.append(remdup(s))
	
for o in output:
    print(o)
    