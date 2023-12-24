class Edge:
    def __init__(self, edge_type, start_id, end_id):
        self.type = edge_type
        self.start_id = start_id
        self.end_id = end_id

    def getType(self):
        return self.type

    def getStartId(self):
        return self.start_id

    def getEndId(self):
        return self.end_id


def generate_edge_rule(edge_type, start_id, end_id):
    edge_rule = edge_type + '(' + start_id + ',' + end_id + ')' +'.'
    return edge_rule


def print_edges(edges):
    edges_rule = set()
    for edge in edges:
        edge_rule = generate_edge_rule(edge.getType(), edge.getStartId(), edge.getEndId())
        edges_rule.add(edge_rule)
    # print('\n'.join(edges_rule))
    return '\n'.join(edges_rule)


# test_edges = [Edge('has_branch', 'ichd_2_2', ['ichd_22_A', 'ichd_22_B']),
#          Edge('has_branch', 'ichd_22', ['ichd_22_C', 'ichd_22_D']),
#          Edge('has_branch_combination', 'ichd_2_2', ['logic33']),
#          Edge('has_branch', 'ichd_22_A', ['ichd_22_A', '32', '70']),
#          Edge('has_branch_combination', 'ichd_2_2', ['logic5']),
#          Edge('has_branch', 'ichd_22_A1', ['44', '45']),
#          Edge('has_branch_combination', 'ichd_2_2', ['logic20']),
#          Edge('has_branch', 'ichd_22_B', ['33']),
#          Edge('has_branch', 'ichd_22_C', ['34'])]

# test_edges = [Edge('has_branch', 'flu', 'flu_1'),
#               Edge('has_branch_combination', 'flu', 'and')]

# print_edges(test_edges)
