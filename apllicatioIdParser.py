from typing import List, Set
def parse_app_ids(input_str:str):
    """Format: {length}{id}{length}{id}...0
    
    Example:
        Input:  "10A13414124218B124564356434567430"
        Output: ["A134141242", "B12456435643456743"]"""
    application_ids=[]
    i=0
    while i<len(input_str):
        length_str=""
        while i<len(input_str) and input_str[i].isdigit():
            length_str+=input_str[i]
            i+=1
        if not length_str:
            break
        length=int(length_str)
        if length==0:
            break
        if i+length<len(input_str):
            app_id=input_str[i:i+length]
            application_ids.append(app_id)
            i+=length
        else:
            break
    return application_ids
def filter_whitelisted_ids(input_string:str,whitelist:List[str]):
    all_ids=parse_app_ids(input_string)
    whitelist_set=set(whitelist)
    filtered_ids=[app_id for app_id in all_ids if app_id in whitelist_set]
    return filtered_ids
#test case
input_name="10A13414124218B124564356434567430"
result=parse_app_ids(input_name)
print(result)
result2=filter_whitelisted_ids(input_name,["A134141242", "B1hihrhprph"])
print(result2)


