# This is a sample Python script.
import clingo
from auto_generate.auto_generate_program import *
from auto_generate.auto_generate_mrs import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def get_has_symptom(symptoms):
#     has_symptoms = set()
#     for symptom in symptoms:
#         has_symptom = 'has_symptom(' + symptom + ').'
#         has_symptoms.add(has_symptom)
# #     has_symptom = '''
# # has_symptom(fever).
# # has_symptom(cough).
# # has_symptom(sore_throat).
# #     '''
#     return '\n'.join(has_symptoms)


def get_asp_rules():
    rules ='''
    
% Define what symptoms does disease not have
not_has_symptom(Disease, Symptom) :-
    disease(Disease),
    symptom(Symptom),
    has_branch(Disease, Symptom),
    not has_symptom(Symptom).

not_has_all_symptoms(Disease) :-
    disease(Disease),
    symptom(Symptom),
    has_branch(Disease, Symptom),
    not_has_symptom(Disease, Symptom).

has_missing_symptoms(Disease) :-
    disease(Disease),
    symptom(Symptom),
    has_branch(Disease,Symptom),
    not_has_all_symptoms(Disease).

% Define what items does disease not have
not_has_item(Disease, Item) :-
    item(Item),
    disease(Disease),
    has_branch(Disease, Item),
    not has_item(Item).

not_has_all_items(Disease) :-
    item(Item),
    disease(Disease),
    has_branch(Disease, Item),
    not_has_item(Disease, Item).

has_missing_items(Disease) :-
    item(Item),
    disease(Disease),
    has_branch(Disease,Item),
    not_has_all_items(Disease).

% Define what symptoms does item not have
not_has_symptom(Item, Symptom) :-
    item(Item),
    symptom(Symptom),
    has_branch(Item, Symptom),
    not has_symptom(Symptom).

not_has_all_symptoms(Item) :-
    item(Item),
    symptom(Symptom),
    has_branch(Item, Symptom),
    not_has_symptom(Item, Symptom).

has_missing_symptoms(Item) :-
    item(Item),
    symptom(Symptom),
    has_branch(Item,Symptom),
    not_has_all_symptoms(Item).

% Define what items does item not have
not_has_item(Item, Item1) :-
    item(Item),
    item(Item1),
    has_branch(Item, Item1),
    not has_item(Item1).

not_has_all_items(Item) :-
    item(Item),
    item(Item1),
    has_branch(Item, Item1),
    not_has_item(Item, Item1).

has_missing_items(Item) :-
    item(Item),
    item(Item1),
    has_branch(Item,Item1),
    not_has_all_items(Item).

% Define item constrain
% logic 'and'
has_item(Item) :-
    item(Item),
    has_branch_combination(Item, and),
    not has_missing_symptoms(Item),
    not has_missing_items(Item).

% logic 'or'
has_item(Item) :-
    item(Item),
    has_branch(Item, Symptom),
    has_branch_combination(Item, or),
    has_symptom(Symptom).

has_item(Item) :-
    item(Item),
    has_branch(Item, Item1),
    has_branch_combination(Item, or),
    has_item(Item1).

% Define disease constrain
% Define 'and' rules
possible_disease(Disease) :-
    disease(Disease),
    has_branch_combination(Disease, and),
    not has_missing_symptoms(Disease),
    not has_missing_items(Disease).


% Define 'or' rules
possible_disease(Disease) :-
    disease(Disease),
    has_branch_combination(Disease, or),
    has_branch(Disease, Symptom),
    has_symptom(Symptom).

possible_disease(Disease) :-
    disease(Disease),
    has_branch_combination(Disease, or),
    has_branch(Disease, Item),
    has_item(Item).

% Define 'not_' rules
possible_disease(Disease) :-
    disease(Disease),
    has_branch_combination(Disease, not_),
    symptom(Symptom),
    has_branch(Disease, Symptom),
    not_has_symptom(Disease, Symptom).

possible_disease(Disease) :-
    disease(Disease),
    has_branch_combination(Disease, not_),
    item(Item),
    has_branch(Disease, Item),
    not_has_item(Disease, Item).

#show possible_disease/1.
    '''
    rules1 = '''
% Define what symptoms does disease not have
not_has_symptom(Disease, Symptom) :-
    disease(Disease),
    symptom(Symptom),
    has_branch(Disease, Symptom),
    not has_symptom(Symptom).

not_has_all_symptoms(Disease) :-
    disease(Disease),
    symptom(Symptom),
    has_branch(Disease, Symptom),
    not not_has_symptom(Disease, Symptom).

has_missing_symptoms(Disease) :-
    disease(Disease),
    symptom(Symptom),
    has_branch(Disease,Symptom),
    not_has_all_symptoms(Disease).

% Define what items does disease not have
not_has_item(Disease, Item) :-
    item(Item),
    disease(Disease),
    has_branch(Disease, Item),
    not has_item(Item).

not_has_all_items(Disease) :-
    item(Item),
    disease(Disease),
    has_branch(Disease, Item),
    not not_has_item(Disease, Item).

has_missing_items(Disease) :-
    item(Item),
    disease(Disease),
    has_branch(Disease,Item),
    not_has_all_items(Disease).

% Define what symptoms does item not have
not_has_symptom(Item, Symptom) :-
    item(Item),
    symptom(Symptom),
    has_branch(Item, Symptom),
    not has_symptom(Symptom).

not_has_all_symptoms(Item) :-
    item(Item),
    symptom(Symptom),
    has_branch(Item, Symptom),
    not not_has_symptom(Item, Symptom).

has_missing_symptoms(Item) :-
    item(Item),
    symptom(Symptom),
    has_branch(Item,Symptom),
    not_has_all_symptoms(Item).

% Define what items does item not have
not_has_item(Item, Item1) :-
    item(Item),
    item(Item1),
    has_branch(Item, Item1),
    not has_item(Item1).

not_has_all_items(Item) :-
    item(Item),
    item(Item1),
    has_branch(Item, Item1),
    not not_has_item(Item, Item1).

has_missing_items(Item) :-
    item(Item),
    item(Item1),
    has_branch(Item,Item1),
    not_has_all_items(Item).

% Define item constrain
% logic 'and'
has_item(Item) :-
    item(Item),
    has_branch_combination(Item, and),
    not has_missing_symptoms(Item),
    not has_missing_items(Item).

% logic 'or'
has_item(Item) :-
    item(Item),
    has_branch(Item, Symptom),
    has_branch_combination(Item, or),
    has_symptom(Symptom).

has_item(Item) :-
    item(Item),
    has_branch(Item, Item1),
    has_branch_combination(Item, or),
    has_item(Item1).

% Define disease constrain
% Define 'and' rules
possible_disease(Disease) :-
    disease(Disease),
    has_branch_combination(Disease, and),
    not has_missing_symptoms(Disease),
    not has_missing_items(Disease).


% Define 'or' rules
possible_disease(Disease) :-
    disease(Disease),
    has_branch_combination(Disease, or),
    has_branch(Disease, Symptom),
    has_symptom(Symptom).

possible_disease(Disease) :-
    disease(Disease),
    has_branch_combination(Disease, or),
    has_branch(Disease, Item),
    has_item(Item).

% Define 'not_' rules
possible_disease(Disease) :-
    disease(Disease),
    has_branch_combination(Disease, not_),
    symptom(Symptom),
    has_branch(Disease, Symptom),
    not_has_symptom(Disease, Symptom).

possible_disease(Disease) :-
    disease(Disease),
    has_branch_combination(Disease, not_),
    item(Item),
    has_branch(Disease, Item),
    not_has_item(Disease, Item).

#show possible_disease/1.
    '''
    return rules


test_program = generate_program() + '\n' + get_has_symptom(['sore_throat','fever','cough']) + '\n' + get_asp_rules()
# print(program)

# program = get_asp_rules()

# control = clingo.Control()
#
# control.add("base", [], program)


# def on_model(model):
#     print(model.symbols(shown=True))


# def run_clingo(program):
#     control = clingo.Control()
#     control.add("base", [], program)
#     control.ground([("base", [])])
#     control.solve(on_model=on_model)

def run_clingo(program):
    control = clingo.Control()
    control.add("base", [], program)
    control.ground([("base", [])])

    # Create an empty list to store the model symbols
    model_symbols = []

    # Define a new on_model function that appends the model symbols to the list
    def on_model(model):
        model_symbols.extend(model.symbols(shown=True))

    # Solve the program and call the on_model function for each model
    control.solve(on_model=on_model)

    # Return the list of model symbols
    return model_symbols


# def symbols_to_dict(symbols):
#     symbol_dict = {}
#
#     for symbol in symbols:
#         if symbol.name not in symbol_dict:
#             symbol_dict[symbol.name] = []
#
#         if symbol.arguments:
#             args = tuple(arg.number if arg.type == clingo.SymbolType.Number else str(arg) for arg in symbol.arguments)
#             symbol_dict[symbol.name].append(args)
#         else:
#             symbol_dict[symbol.name].append(())
#
#     return symbol_dict

def symbols_to_dict(symbols):
    symbol_dict = {}

    for symbol in symbols:
        if symbol.name not in symbol_dict:
            symbol_dict[symbol.name] = []

        if symbol.arguments:
            args = [str(arg) for arg in symbol.arguments]
            symbol_str = f"{', '.join(args)}"
            symbol_dict[symbol.name].append(symbol_str)
        else:
            symbol_dict[symbol.name].append(symbol.name)

    return symbol_dict

# diseases = [
#         {
#             'name': '哮喘',
#             'symptoms': ['咳嗽', '气喘', '胸闷', '气急'],
#             'treatments': ['吸入短效β2受体激动剂', '吸入糖皮质激素']
#         },
#         {
#             'name': '慢性支气管炎',
#             'symptoms': ['咳嗽', '痰多', '气促', '胸闷'],
#             'treatments': ['吸入短效β2受体激动剂', '吸入长效β2受体激动剂', '口服或静脉注射糖皮质激素']
#         },
#         {
#             'name': '肺炎',
#             'symptoms': ['咳嗽', '发热', '气促', '胸痛'],
#             'treatments': ['抗生素', '氧疗']
#         }
#     ]
# test_has_symptoms = ['sore_throat', 'fever', 'cough']
# program = generate_program() + '\n' + get_has_symptom(test_has_symptoms) + '\n' + get_asp_rules()
# symbols = run_clingo(program)
# all_result = symbols_to_dict(symbols)
# print(all_result)
# for disease in all_result['possible_disease']:
#     diseases.append({'name': disease})
# print(diseases)
# run_clingo()
# print(symbols_to_dict(run_clingo(test_program)))