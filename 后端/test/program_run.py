from algorithm.main_clingo import *
from database.db import *

# Create an empty list to store patient data
patients = []

db = DB()

symptoms = ["no_symptom", "cough", "hemoptysis", "mild_chest_pain", "long-term_stable_condition", "secondary_infection_due_to_tumor_blocking_bronchus", "insignificant_signs_in_early_stage"]



# diseases = []
# program = generate_program() + '\n' + get_has_symptom(symptoms) + '\n' + get_asp_rules()
# print(program)
# symbols = run_clingo(program)
# all_result = symbols_to_dict(symbols)
# # print(all_result)
# for disease in all_result['possible_disease']:
#     diseases.append({'name': disease})
# # 使用 Flask 提供的 jsonify 函数将数据转换为 JSON 格式并返回
# print(diseases)

disease = 'noninvasive_thymoma'
tr = db.get_node_hierarchy(disease)
print(tr)

db.close()