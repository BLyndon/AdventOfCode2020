import re
import networkx as nx


def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    bags = dict()
    for line in lines:
        line = line.replace("\n", "")
        if line.endswith("no other bags."):
            content = ['no bags']
        else:
            line = line.replace("bags", "").replace(
                "bag", "").replace(' , ', "").replace(".", "").strip()

            content = line.split("contain")[1]
            content = re.split(r'\d ', content)[1:]
        bag = line.split("contain")[0].strip()

        bags[bag] = content

    edges = set()
    for bag, content in bags.items():
        for inner_bag in content:
            edges.add((bag, inner_bag))

    return list(edges)


def solver_1(edges):
    G = nx.DiGraph()
    G.add_edges_from(edges)

    target = 'shiny gold'
    sources = list({edge[0] for edge in edges})

    container = set()
    for source in sources:
        for path in nx.all_simple_paths(G, source=source, target=target):
            container.add((path[0], path[-1]))

    return len(container)


def solver_2(lines):
    pass


if __name__ == '__main__':
    filename = '07.txt'

    edges = parser(loader(filename))

    sol1 = solver_1(edges)
    sol2 = solver_2(edges)

    print("Part 1: {}".format(sol1))
    print("Part 2: {}".format(sol2))
