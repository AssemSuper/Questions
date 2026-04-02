from collections import defaultdict
from typing import Optional, Dict
import heapq

class ShippingCalculator:
    def __init__(self,input_string:str):
        # self.input_string=input_string
        self.routes=self._parse_routes(input_string)
        self.graph=self._build_graph(input_string)
    def _parse_routes(self,input_string:str):
        routes={}
        route_strings=input_string.split(":")
        for route_str in route_strings:
            parts=[p.strip() for p in route_str.split(",")]
            if len(parts)==4:
                origin, destination,firm,cost=parts
                cost=int(cost)
                routes[(origin,destination)]=(firm,cost)
        return routes
    def _build_graph(self,input_string:str) ->Dict[str,list[tuple[str,int,str]]]:
        graph=defaultdict(list)
        route_strings=input_string.split(":")
        for route_str in route_strings:
            parts=[p.strip() for p in route_str.split(",")]
            if len(parts)==4:
                origin,destination,firm,cost=parts
                cost=int(cost)
            graph[origin].append((destination,cost,firm))
        return graph
    def get_direct_cost(self,origin,destination) -> Optional[int]:
        route=self.routes.get((origin,destination))
        if route:
            firm,cost=route
            return cost
        return None
    def get_direct_cost_info(self,origin,destination) -> Optional[Dict]:
        route=self.routes.get((origin,destination))
        if route:
            firm,cost=route
            return {'origin':origin,'destination':destination,'firm':firm,'cost':cost,'route':[origin,destination]}
        return None
    def get_cheapest_cost(self,origin,destination)-> Optional[int]:
        route=self.find_cheapest_route(origin,destination)
        if route:
            return route['total_cost']
        return None
    def find_cheapest_route(self,origin,destination) ->Optional[Dict]:
        pq=[(0,origin,[origin],0)]
        visited=set()
        while pq:
            current_cost,current_location,path,hops=heapq.heappop(pq)
            if current_location==destination:
                return {'total_cost':current_cost,'path':path,'hops':hops}
            if current_location in visited:
                continue
            visited.add(current_location)
            
        #     for next_location, cost, firm in self.graph[current_location]:
        #         if next_location not in visited:
        #             new_cost = current_cost + cost
        #             new_path = path + [next_location]
        #             new_hops = hops + 1
        #             heapq.heappush(pq, (new_cost, next_location, new_path, new_hops))
        # return None
input_string = "US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7"
test_case=ShippingCalculator(input_string)
print(test_case.get_cheapest_cost('CA','UK'))





 