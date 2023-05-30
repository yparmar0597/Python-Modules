### Recursion
'''
def revlist(lst):
    if not lst:
        return []
    return [lst[-1]] + revlist(lst[:-1])

print(revlist([1,2,3,4,5]))
'''

   


