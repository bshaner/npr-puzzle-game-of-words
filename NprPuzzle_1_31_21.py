import json
from typing import List


def recursive_state_network(network, node: str, root_path: List[str], depth: int, blacklist: List[str]):
    """
    Searches the network for all permutations of all paths leaving the starting node, without revisiting any node
    :param network: a graph of nodes, given as a dictionary where keys are node labels and values are a list of edges by
        neighboring node name
    :param node: the node to start the search
    :param root_path: prefix added to the resulting paths
    :param depth: number of nodes to traverse from the start node
    :param blacklist: any nodes to ignore, used recursively to prevent revisiting nodes
    :return: List of lists of node labels
    """
    local_path = root_path.copy()
    local_blacklist = blacklist.copy()
    if depth == 1:
        local_path.append(node)
        return local_path

    list_of_paths = []
    local_path.append(node)
    local_blacklist.append(node)
    for next_step in network[node]:
        if next_step not in blacklist:
            subresult = recursive_state_network(network, next_step, local_path, depth-1, local_blacklist)
            if depth == 2:
                list_of_paths.append(subresult)
            else:
                list_of_paths.extend(subresult)
    return list_of_paths


def road_trip_pretty_print(network, states: List[str]) -> str:
    """
    Formatter for a *valid* path (states[]) through the given graph (network{})
    """
    simplified_graph = {}
    for node in states:
        reduced_vals = [v for v in network[node] if v in states]
        simplified_graph[node] = reduced_vals

    ordered_trip = []
    for node in states:
        paths = recursive_state_network(simplified_graph, node, [], len(states), [])
        if len(paths) > 0:
            ordered_trip = paths[0]

    if len(ordered_trip) == len(states):
        return "->".join(ordered_trip)
    else:
        return "Error: Unable to connect nodes {}".format(states)


def main():
    n_states = 4
    unique_road_trips = []

    with open("StateConnections.json") as f:
        state_map = json.load(f)

    # find all the paths possible with the given length
    for state in state_map.keys():
        road_trips = recursive_state_network(state_map, state, [], n_states, [])
        for trip in road_trips:
            sort_trip = "".join(sorted(trip))  # sorted so we can deduplicate
            unique_road_trips.append(sort_trip)

    unique_road_trips = list(set(unique_road_trips))

    print(unique_road_trips)
    print(len(unique_road_trips))

    # read in and format a list of common words
    eight_l_words = []
    with open('eight_l_word_bank.txt', 'r') as f:
        all_lines = f.readlines()
        for line in all_lines:
            eight_l_words.extend(line.upper().split())

    print(eight_l_words)
    print(len(eight_l_words))

    # compare unique road trips to list of common words
    matches = {}

    for target in eight_l_words:
        for rt in unique_road_trips:
            if sorted(target) == sorted(rt):
                if target not in matches.keys():
                    matches[target] = rt
                elif isinstance(matches[target], List):
                    matches[target].append(rt)
                else:
                    matches[target] = [matches[target], rt]

    print("found {} matches".format(len(matches.keys())))

    # walk the graph again, starting at any state, find neighbors to make a chain (any) and return a 4 state chain
    #   in a better order (not just alphabetical)
    for match in matches.keys():
        print("----------------------")
        print(match)
        rt = matches[match]
        if isinstance(rt, List):
            for my_trip in rt:
                list_trip = [my_trip[i:i + 2] for i in range(0, len(my_trip), 2)]
                print(road_trip_pretty_print(state_map, list_trip))
        elif isinstance(rt, str):
            list_trip = [rt[i:i + 2] for i in range(0, len(rt), 2)]
            print(road_trip_pretty_print(state_map, list_trip))


if __name__ == "__main__":
    main()
