from collections import defaultdict
from typing import Dict
def parse_shipping_rates(input_string:str)->Dict:
    if not input_string:
        return {'direct':{},'graph':{}}
    direct_routes={}
    graph=defaultdict(list)
    for route in input_string.split(":"):
        parts=route.split(",")
        if len(parts)!=4:
            continue
        source=parts[0].strip()
        destination=parts[1].strip()
        carrier=parts[2].strip()
        cost=int(parts[3].strip())
        direct_routes[source,destination]=cost
        graph[source].append((destination,cost))
    return {'direct':direct_routes,'graph' :graph}
#Test_case
input_string="US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7"
test1=parse_shipping_rates(input_string)
# print(test1)
def directShippingCost(input_string:str,source,destination)->int:
    data=parse_shipping_rates(input_string)
    return data['direct'].get((source, destination))
    
#Test_case
test2=directShippingCost(input_string,'US','UK')
print(test2)
def cheapestShippingCost(intput_str, source,destination):
    if source== destination:
        return 0
    data= parse_shipping_rates(input_str)
    graph= data['graph']
    if source not in graph:
        return None
    #(total_cost_so_far, current_location)
    heap=[(0,source)]
    visited=set()
    #“What is the cheapest known cost to reach each location?”
    min_costs={source:0}
    while heap:
        current_cost,current_location=heapq.heappop(heap)
        if current_location==destination:
            return current_cost
        if current_location in visited:
            continue
        visited.add(current_location)
        for next_location, edge_cost in grapsh[current_location]:
            new_cost=edge_cost+current_cost
            if next_location not in min_costs or new_cost<min_cost[next_location]:
                min_cost[next_location]=new_cost
                heapq.heappush(heap,(new_cost,next_location))

