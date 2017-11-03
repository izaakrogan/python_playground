# fibonacci

def memfib(n):
    def inner(target,total,prev,current):
        if target == total: return current
        return inner(target,total+1,current,prev+current)
    return inner(n-1,0,0,1)
