from auto_generate.auto_generate_nodes import *
from auto_generate.auto_generate_edges import *
from database.db import *


def get_nodes():
    db = DB()
    nodes = []
    diseases = db.find_all_disease()
    items = db.find_all_item()
    symptoms = db.find_all_symptom()
    for dic in diseases:
        nodes.append(Node('disease', dic))
    for dic in items:
        nodes.append(Node('item', dic))
    for dic in symptoms:
        nodes.append(Node('symptom', dic))
    db.close()
    return nodes


def get_edges():
    db = DB()
    edges = []
    has_branchs = db.find_all_has_branch()
    has_branch_combinations = db.find_all_has_branch_combination()
    for li in has_branchs:
        edges.append(Edge('has_branch', li[0], li[1]))
    for li in has_branch_combinations:
        edges.append(Edge('has_branch_combination', li[0], li[1]))
    db.close()
    return edges


def generate_program():
    nodes_asp = print_nodes(get_nodes())
    edges_asp = print_edges(get_edges())
    return nodes_asp + '\n' + edges_asp

