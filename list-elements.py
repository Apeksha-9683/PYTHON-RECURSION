''''def list_elem(list,i):
    if i==0:
        return list[0]
    return '''

def list_elem(list,i=0):
    if i==len(list):
        return 
    print(list[i])
    list_elem(list,i+1)
    
data=input("Enter the elements of the list")
list=list(map(int,data.split(',')))
list_elem(list)
