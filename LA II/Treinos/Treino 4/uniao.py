def complete(nums, candidate):
    union = []
    
    for set in candidate:
        for num in set:
            union.append(num)
            
    for num in nums:
        if num not in union:
            return False
        
    return True

def extensions(sets, candidate):
    ext = []
    
    for set in sets:
        if set not in candidate:
            ext.append(set)
            
    return ext

def valid(resp, candidate):
    return len(resp) == 0 or min(resp) > len(candidate)

def search(sets, nums):
    candidate = []
    resp = aux(sets, nums, candidate, [])
    print(resp)
    return min(resp)
 
def aux(sets, nums, candidate, resp):
    
    if(not valid(resp, candidate)):
        return resp
        
    if complete(nums, candidate):
        if(valid(resp, candidate)):
            resp.append(len(candidate))
            return resp
    for x in extensions(sets, candidate):
        new_candidate = candidate.copy()
        new_candidate.append(x)
        aux(sets, nums, new_candidate, resp)
    return resp

def uniao(sets):
    nums = []
    
    if len(sets) == 0:
        return 0
    
    for set in sets:
        for num in set:
            if num not in nums:
                nums.append(num)
                
    return search(sets, nums)

# 70 % 
#penso que a solução esteja certa, mas deve estar pouco eficiente