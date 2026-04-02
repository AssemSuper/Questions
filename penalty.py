from typing import List, Tuple
def compute_penalty(log:str,closing_time:int)->int:
    penalty=0
    costumers=log.split()
    # Count penalties during OPEN hours (0 to closing_time-1)
    # Penalty = number of N's (no customers when open)
    for i in range(closing_time):
        if costumers[i]=="N":
            penalty+=1
    # Count penalties during CLOSED hours (closing_time onwards)
    # Penalty = number of Y's (customers when closed)
    for i in range(closing_time,len(costumers)):
        if costumers[i]=="Y":
            penalty+=1
    return penalty

# ============================================================================
# PART 2: Find Closing Time with Minimum Penalty
# ============================================================================
def getClosingWithMinPenalty(log:str)->int:
    costumers=log.split()
    n=len(costumers)
    min_penalty=float('inf')
    best_closing=0
    for closing_time in range(n+1):
        penalty_compute=compute_penalty(log,closing_time)
        if penalty_compute<min_penalty:
            min_penalty=penalty_compute
            best_closing=closing_time
    return best_closing
log = "Y Y N Y"
print(getClosingWithMinPenalty(log))
# ============================================================================
# PART 3: Handle Multiple Stores with BEGIN/END
# ============================================================================
def getAllClosing(log:str)->List[int]:
    tokens=log.split()
    stack=[]
    result=[]
    for token in tokens:
        if token=="BEGIN":
            stack.append([])

        elif token=="END":
            if stack:
                store_log=' '.join(stack.pop())
                optimal_closing=getClosingWithMinPenalty(store_log)
                result.append(optimal_closing)
        else:
            stack[-1].append(token)
    return result
i="BEGIN BEGIN Y Y N END Y N N END"
print(getAllClosing(i))

#Test Cases
# assert compute_penalty("Y Y N Y", 4) == 3
# assert compute_penalty("Y Y N Y", 5) == 2
log="Y Y N Y"
for i in range(5):
    print(compute_penalty(log,i))