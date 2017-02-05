from matplotlib import pyplot
import random
import sys
import pdb

def generate_graph(filename, node_size, avg_degree=None):
    """
    generate a BA model
    # concept: https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model
    # method: https://github.com/ladamalina/coursera-sna/blob/master/Week%202.%20Random%20Graph%20Models/Lecture%202C%20Advanced.pdf
    """
    # initialize an empty graph
    # each index represents a node and its neighbors
    graph = [[] for _ in range(node_size+1)]
    degrees = 0
    # endpoints
    endpoints = []

    # avg_degree is the least number of edges of newcomer
    if avg_degree is None:
        avg_degree = 2
    # generate a complete graph of size 5 as the seed graph
    seed_size = 2 * avg_degree + 1
    for i in range(1, seed_size):
        for j in range(i+1, seed_size+1):
            if i != j:
                degrees += 1
                graph[i].append(j)
                graph[j].append(i)
                endpoints.append(i)
                endpoints.append(j)
    # print graph, degrees
    # generate the entire graph
    for new_comer in range(seed_size+1, node_size+1):
        old_friends = select_elements(endpoints, avg_degree)
        # pdb.set_trace()
        for old_friend in old_friends:
            degrees += 1
            graph[new_comer].append(old_friend)
            graph[old_friend].append(new_comer)
            endpoints.append(new_comer)
            endpoints.append(old_friend)
    # print graph, degrees

    pyplot.hist(endpoints, bins=100)
    pyplot.title("Graph Degree Histogram")
    pyplot.xlabel("Degree")
    pyplot.ylabel("Number")

    pyplot.show()

    with open(filename, "w") as file:
        for i in range(1, len(graph)):
            for j in range(len(graph[i])):
                if i < graph[i][j]:
                    file.write(str(i) + "," + str(graph[i][j]) + "\n")

def select_elements(endpoints, avg_degree):
    """
    select avg_degree elements from endpoint, without duplicate values
    """
    result = set()
    while len(result) < avg_degree:
        result.add(random.choice(endpoints))
    return result

if __name__ == "__main__":


    if len(sys.argv) < 3:
        raise Exception("not empty arguments")
    elif len(sys.argv) == 3:
        generate_graph(sys.argv[1], int(sys.argv[2]))
    else:
        generate_graph(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

    print "output finished, check: " + sys.argv[1]
