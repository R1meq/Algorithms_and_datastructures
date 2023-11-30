import unittest

from lab_5.src.weighted_graph import WeightedGraph
from lab_5.src.weighted_vertex import WeightedVertex


class TestMinClientPing(unittest.TestCase):
    def test_min_client_ping_1(self):
        with open("test_data_1/gamsrv_input_1.txt", 'r') as file:
            n, m = map(int, file.readline().split())
            numbers_list = list(map(int, file.readline().split()))
            connections_list = [list(map(int, line.split())) for line in file.readlines()]

            vertex_list = []
            clients = []
            servers = []

            for index in range(1,n+1):
                vertex_list.append(WeightedVertex(index))

            for item in vertex_list:
                if item.index in numbers_list:
                    clients.append(item)
                else:
                    servers.append(item)

            graph = WeightedGraph(vertex_list,clients)
            for item in connections_list:
                first,second,distance = item
                graph.add_weighted_edge(first,second,distance)

            self.assertEqual(100,graph.min_client_ping(servers))
            with open("../test/test_data_1/gamsrv_output_1.txt", "w") as output_file:
                output_file.write(str(graph.min_client_ping(servers)))

    def test_min_client_ping_2(self):
        with open("test_data_2/gamsrv_input_2.txt", 'r') as file:
            n, m = map(int, file.readline().split())
            numbers_list = list(map(int, file.readline().split()))
            connections_list = [list(map(int, line.split())) for line in file.readlines()]

            vertex_list = []
            clients = []
            servers = []

            for index in range(1, n + 1):
                vertex_list.append(WeightedVertex(index))

            for item in vertex_list:
                if item.index in numbers_list:
                    clients.append(item)
                else:
                    servers.append(item)

            graph = WeightedGraph(vertex_list, clients)
            for item in connections_list:
                first, second, distance = item
                graph.add_weighted_edge(first, second, distance)

            self.assertEqual(10, graph.min_client_ping(servers))
            with open("../test/test_data_2/gamsrv_output_2.txt", "w") as output_file:
                output_file.write(str(graph.min_client_ping(servers)))



    def test_min_client_ping_3(self):
        with open("test_data_3/gamsrv_input_3.txt", 'r') as file:
            n, m = map(int, file.readline().split())
            numbers_list = list(map(int, file.readline().split()))
            connections_list = [list(map(int, line.split())) for line in file.readlines()]

            vertex_list = []
            clients = []
            servers = []

            for index in range(1, n + 1):
                vertex_list.append(WeightedVertex(index))

            for item in vertex_list:
                if item.index in numbers_list:
                    clients.append(item)
                else:
                    servers.append(item)

            graph = WeightedGraph(vertex_list, clients)
            for item in connections_list:
                first, second, distance = item
                graph.add_weighted_edge(first, second, distance)

            self.assertEqual(1000000000, graph.min_client_ping(servers))
            with open("../test/test_data_3/gamsrv_output_3.txt", "w") as output_file:
                output_file.write(str(graph.min_client_ping(servers)))

if __name__ == '__main__':
    unittest.main()
