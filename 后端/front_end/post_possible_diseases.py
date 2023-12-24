from front_end.app import *
from algorithm.main_clingo import *
from database.db import *

# 定义一个返回疾病数据的接口
@app.route('/diseases')
def get_diseases():
    db = DB()
    # diseases = [
    #     {
    #         'name': '哮喘',
    #         'symptoms': ['咳嗽', '气喘', '胸闷', '气急'],
    #         'treatments': ['吸入短效β2受体激动剂', '吸入糖皮质激素']
    #     },
    #     {
    #         'name': '慢性支气管炎',
    #         'symptoms': ['咳嗽', '痰多', '气促', '胸闷'],
    #         'treatments': ['吸入短效β2受体激动剂', '吸入长效β2受体激动剂', '口服或静脉注射糖皮质激素']
    #     },
    #     {
    #         'name': '肺炎',
    #         'symptoms': ['咳嗽', '发热', '气促', '胸痛'],
    #         'treatments': ['抗生素', '氧疗']
    #     }
    # ]
    diseases = []
    # test_has_symptoms = ['sore_throat', 'fever', 'cough']
    # print(patients[0]['symptoms'])
    # test_has_symptoms = patients[0]['symptoms'].split(',')
    # print(test_has_symptoms)
    mr_id = session['mr_id']
    has_symptoms = db.find_all_symptom()

    program = generate_program() + '\n' + get_has_symptom(has_symptoms) + '\n' + get_asp_rules()
    symbols = run_clingo(program)
    all_result = symbols_to_dict(symbols)
    # print(all_result)
    for disease in all_result['possible_disease']:
        diseases.append({'name': disease})
    # 使用 Flask 提供的 jsonify 函数将数据转换为 JSON 格式并返回
    print(diseases)
    return jsonify(diseases)


