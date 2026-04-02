def process_transactions_basic(input_string):
    parts=[p.strip() for p in input_string.split(",")]
    transactions=[]
    for i in range(0,len(parts),5):
        if i+4<len(parts):
            transaction={'InputId':int(parts[i]),'UserId':parts[i+1],'Amount':float(parts[i+2]),'timestamp':int(parts[i+3]),'risk_score':int(parts[i+4])}
            transactions.append(transaction)
    transactions.sort(key=lambda x:x['InputId'])
    result=[]
    RISK_THRESHOLD=70
    for txn in transactions:
        status="REJECTED" if txn['risk_score']>RISK_THRESHOLD else "ACCEPTED"
        output=f"{txn['InputId']} {txn['UserId']} {txn['Amount']:.2f} {status}"
        # output = f"{txn['inputID']} {txn['userID']} {txn['amount']:.2f} {status}"
        result.append(output)
    return result
#test 
test_case1="5, R1, 5.60, 155968950, 45, 10, R2, 46.4, 133545, 100"
# print(process_transactions_basic(test_case1))
# LEVEL 2: Add Balance Tracking
def process_transactions_with_balance(input_string, initial_balances=None):
    parts=[p.strip() for p in input_string.split(",")]
    transactions=[]
    for i in range(0,len(parts),5):
        if i+4<len(parts):
            transaction={'InputId':int(parts[i]),'UserId':parts[i+1],'Amount':float(parts[i+2]),'timestamp':int(parts[i+3]),"risk_score":int(parts[i+4])}
            transactions.append(transaction)
            #     transactions.append({
            #     'inputID': int(parts[i]),
            #     'userID': parts[i + 1],
            #     'amount': float(parts[i + 2]),
            #     'timestamp': int(parts[i + 3]),
            #     'risk_score': int(parts[i + 4])
            # })
    transactions.sort(key=lambda x :x['InputId'])
    if initial_balances is None:
        initial_balances={}
    balance=initial_balances.copy()
    result=[]
    Risk_threshold=70
    for txn in transactions:
        user=txn["UserId"]
        amount=txn['Amount']
        curent_balance=balance.get(user,1000)
        if txn['risk_score']>Risk_threshold:
            status='Rejected'
            reason="High Risk"
        elif curent_balance<amount:
            status='Rejected'
            reason='Insufficient Funds'
        else:
            status='Accepted'
            reason='Ok'
            balance[user]=curent_balance-amount
        output=f"{txn['InputId']} {txn['UserId']} {txn['Amount']:.2f} {status}"
        result.append(output)
    return result, balance

# def process_transactions_with_balance(input_string, initial_balances=None):
#     """
#     Level 2: Add user balance tracking
#     Reject if insufficient funds
    
#     Args:
#         input_string: CSV-like string with transaction data
#         initial_balances: Dict of userID -> balance
#     """
#     # Parse transactions
#     parts = [p.strip() for p in input_string.split(',')]
#     transactions = []
    
#     for i in range(0, len(parts), 5):
#         if i + 4 < len(parts):
#             transactions.append({
#                 'inputID': int(parts[i]),
#                 'userID': parts[i + 1],
#                 'amount': float(parts[i + 2]),
#                 'timestamp': int(parts[i + 3]),
#                 'risk_score': int(parts[i + 4])
#             })
    
#     # Sort by inputID
#     transactions.sort(key=lambda x: x['inputID'])
    
#     # Initialize balances
#     if initial_balances is None:
#         initial_balances = {}
#     balances = initial_balances.copy()
    
#     results = []
#     RISK_THRESHOLD = 70
    
#     for txn in transactions:
#         user = txn['userID']
#         amount = txn['amount']
        
#         # Get current balance (default to 1000 if new user)
#         current_balance = balances.get(user, 1000.0)
        
#         # Determine status
#         if txn['risk_score'] > RISK_THRESHOLD:
#             status = "REJECTED"
#             reason = "HIGH_RISK"
#         elif current_balance < amount:
#             status = "REJECTED"
#             reason = "INSUFFICIENT_FUNDS"
#         else:
#             status = "APPROVED"
#             reason = "OK"
#             # Deduct from balance only if approved
#             balances[user] = current_balance - amount
        
#         output = f"{txn['inputID']} {txn['userID']} {txn['amount']:.2f} {status} {reason}"
#         results.append(output)
    
#     return results, balances

input_string= "5, R1, 5.60, 155968950, 45, 10, R2, 46.4, 133545, 60"
test2=process_transactions_with_balance(input_string)
print(test2)

def process_transactions_with_velocity(initial_string, time_window=60,max_transaction=3):
    parts= [p.strip() for p in initial_string.split(",")]
    transactions=[]
    for i in range(0,len(parts),5):
        if i+4<len(parts):
            transaction={'inputId':int(parts[i]),'userId':parts[i+1],'amount':float(parts[i+2]),'timestamp':int(parts[i+3]),'riskscore':int(parts[i+4])}
            transactions.append(transaction)
    transactions.sort(key=lambda x:x['inputId'])
    user_history={}
    balances={}
    result=[]
    RISK_THRESHOLD=70
    for txn in transactions:
        user=txn['userId']
        amount=txn['amount']
        timestamp=txn['timestamp']
        if user not in user_history:
            user_history[user]=[]
            balances[user]=1000
        recenttxn= [t for t in user_history[user]
                    if timestamp-t<=time_window]
        status='Approved'
        reason='Ok'
        if txn['riskscore']>RISK_THRESHOLD:
            status='Rejected'
            reason='High Risk'
        elif len(recenttxn)>=max_transaction:
            status="Rejected"
            reason="Excessive Transactiions"
        elif balances[user]<amount:
            status="Rejected"
            reason="Insufficient funds"
        if status=="Approved":
            balances[user]-=amount 
            user_history[user].append(timestamp)
            output=f"{txn['inputId']} {txn['userId']} {txn['amount']:.2f} {status}"
            result.append(output)
        
    return result, balances, user_history
input_string= "5, R1, 5.60, 155968950, 45, 10, R2, 46.4, 133545, 60"
test3=process_transactions_with_velocity(input_string)
print("test3",test3)

