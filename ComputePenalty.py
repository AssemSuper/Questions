# def compute_penalty(log, closing_time):
#     data=log.split()
#     n=len(data)
#     penalty=0
#     for i in range(closing_time):

#         if d=="N":
#             penalty+=1
#     for d in range(closing_time, n ):
#         if d=="Y":
#             penalty+=1
#     return penalty
# test_case1="Y N Y N"
# result=compute_penalty(test_case1,2)


def compute_penalty(log, closing_time):
    customers=log.split()
    penalty=0
    for i in range(closing_time):
        if i<len(customers) and customers[i]=="N":
            penalty+=1
    for i in range( closing_time, len(customers)):
        if customers[i]=="Y":
            penalty+=1
    return penalty
def getClosingWithMinPenalty(logs):
    customers=logs.split()
    n=len(customers)
    best_closing_time=0
    min_penalty=float('inf')
    for closing_time in range(n+1):
        penalty=compute_penalty(logs,closing_time)
        if penalty<min_penalty:
            min_penalty=penalty
            best_closing_time=closing_time
    # return min_penalty,best_closing_time
    return best_closing_time



