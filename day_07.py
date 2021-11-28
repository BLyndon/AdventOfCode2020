import networkx as nx


def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    def expand_bags(bags):
        edges = set()
        for bag, content in bags.items():
            bag = [bag]
            for inner_bag in content:
                edges.add(tuple(bag + inner_bag))
        return list(edges)

    bags = dict()
    for line in lines:
        line = line.replace("\n", "").replace("bags", "").replace(
            "bag", "")
        if line.endswith("no other ."):
            content = [['no bags', 0]]
        else:
            line = line.replace(' , ', "-").replace(" .", "").strip()
            content = line.split("contain ")[1].split("-")
            content = list(map(lambda x: [
                " ".join(x.split()[1:]), int(x.split()[0])], content))
        bag = line.split("contain")[0].strip()

        bags[bag] = content

    return expand_bags(bags)


def solver_1(edges):
    edges1 = [(edge[0], edge[1]) for edge in edges]
    G = nx.DiGraph()
    G.add_edges_from(edges1)

    target = 'shiny gold'
    sources = list({edge[0] for edge in edges1})

    container = set()
    for source in sources:
        for path in nx.all_simple_paths(G, source=source, target=target):
            container.add((path[0], path[-1]))

    return len(container)


def solver_2(edges):
    pass


if __name__ == '__main__':
    filename = '07.txt'

    edges = parser(loader(filename))

    sol1 = solver_1(edges)
    sol2 = solver_2(edges)

    print("Part 1: {}".format(sol1))
    print("Part 2: {}".format(sol2))
