#a simple implementation of hanoi 
def hanoi(n,src,buf,dst):
    i=0
    if n == 1:
        print src,'-->',dst
    else:
        hanoi(n-1,src,dst,buf)  #the order is crutial in recursion
        hanoi(1,src,buf,dst)
        hanoi(n-1,buf,src,dst)
#call the function
if __name__=='__main__':
    k=hanoi(4,'A','B','C')
