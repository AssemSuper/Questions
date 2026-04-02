def expand_braces(expression:str):
    open_idx=expression.find('{')
    close_idx=expression.find("}")
    if not is_valid_pattern(expression, open_idx,close_idx):
        return expression
    prefix=expression[:open_idx]
    token_str=expression[open_idx+1:close_idx]
    suffix=expression[close_idx+1]
    tokens=token_str.split(",")
    if len(tokens)<2:
        return expression
    result=[]
    for token in tokens:
        expanded=prefix+token+suffix
        result.append(expanded)

def is_valid_pattern(expression, open_idx, close_idx):
    if open_idx==-1 or close_idx==-1:
        return False
    if open_idx>=close_idx:
        return False
    if expression.count('{')==1 or expression.count('}')==1:
        return False
    return False 
