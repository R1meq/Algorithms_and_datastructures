class WeightedGraph:
    def __init__(self, vertex_list, client_vertex_list):
        self.vertex_list = vertex_list
        self.client_vertex_list = client_vertex_list

    def min_client_ping(self, server_vertex_list):
        clients_ping = []
        for server in server_vertex_list:
            clients_ping.append(self.dijkstra(server))

        return min(clients_ping)

    def dijkstra(self, source):
        current_vertex_list = list(self.vertex_list)
        clients_ping = []

        for node in current_vertex_list:
            if node == source:
                node.distance = 0
            else:
                node.distance = float('inf')

        while current_vertex_list:
            current_vertex = min(current_vertex_list, key=lambda x: x.distance)

            if current_vertex in self.client_vertex_list:
                clients_ping.append(current_vertex.distance)

            for neighbor in current_vertex.neighbors:
                if neighbor in current_vertex_list:
                    if current_vertex.weight_map[neighbor] + current_vertex.distance < neighbor.distance:
                        neighbor.distance = current_vertex.weight_map[neighbor] + current_vertex.distance
                        neighbor.parent = current_vertex

            current_vertex_list.remove(current_vertex)

        return max(clients_ping)

    def add_weighted_edge(self, first, second, distance):
        first = self.vertex_list[first - 1]
        second = self.vertex_list[second - 1]
        first.neighbors.append(second)
        first.weight_map[second] = distance
        second.neighbors.append(first)
        second.weight_map[first] = distance
