class Node:
    def __init__(self, node_type, attr_dict):
        self.type = node_type
        self.attrs = attr_dict

    @classmethod
    def from_neo4j_node(self, neo4j_node):
        self.type = neo4j_node.labels[0]
        self.attrs = {}
        for key in neo4j_node.keys():
            self.attrs[key] = neo4j_node[key]

    def getType(self):
        return self.type

    def getAttr(self, attr_type):
        if attr_type in self.attrs:
            return self.attrs[attr_type]
        else:
            return None


# def generate_node_rule(node_type, attr_type_values):
#     basics = {"basic_Symptom": ["id", "name", "type"],
#               "basic_Frequency": ["id", "start", "end", "unit", "type"],
#               "basic_AttackTime": ["id", "value", "type"],
#               "basic_Duration": ["id", "start", "end", "type"],
#               "basic_Nature": ["id", "value", "type"],
#               "basic_Severity": ["id", "value", "type"],
#               "item": ["id"],
#               "logic": ["id", "op", "type"],
#               "symptom":["id"],
#               "disease":["name"]}
#     node_rule = []
#     node_rule.append(node_type)
#     for attr_type, attr_value in attr_type_values.items():
#         if attr_type in basics[node_type]:
#             node_rule.append(attr_value)
#         else:
#             node_rule.append("")
#     return node_rule
#
#
# def print_nodes(nodes):
#     for node in nodes:
#         node_rule = generate_node_rule(node.getType(), node.attrs)
#         # print("{}({}).".format(node_rule[0], ",".join(str(x) for x in node_rule[1:])))
#         return "{}({}).".format(node_rule[0], ",".join(str(x) for x in node_rule[1:]))

def generate_node_rule(node_type, attr_type_values):
    node_rule = node_type + "(" + attr_type_values['name'] + ")" +'.'
    return node_rule

def print_nodes(nodes):
    nodes_rule = set()
    for node in nodes:
        node_rule = generate_node_rule(node.type, node.attrs)
        nodes_rule.add(node_rule)
    return '\n'.join(nodes_rule)

# 示例


# print_nodes(nodes)
