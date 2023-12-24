# from front_end.app import *
from algorithm.main_clingo import *
import random
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from datetime import datetime
from neo4j.time import DateTime

from flask_login import LoginManager, login_required, current_user


app = Flask(__name__)

CORS(app)

# Create an empty list to store patient data
patients = []


@app.route('/submit_patient_form', methods=['POST'])
def submit_patient_form():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    disease = request.form['disease']
    symptoms = request.form['symptoms']
    patients.clear()
    patients.append({
        'name': name,
        'age': age,
        'gender': gender,
        'disease': disease,
        'symptoms': symptoms.split(',')
    })

    print(name, age, gender, disease, symptoms)
    # 保存表单数据的代码
    return symptoms

tree_node = []


# 定义一个返回疾病数据的接口
@app.route('/diseases')
def get_diseases():
    diseases = []
    # test_has_symptoms = ['sore_throat', 'fever', 'cough']
    print('input symptoms', patients[0]['symptoms'])
    test_has_symptoms = patients[0]['symptoms']
    # print(test_has_symptoms)
    program = generate_program() + '\n' + get_has_symptom(test_has_symptoms) + '\n' + get_asp_rules()
    symbols = run_clingo(program)
    all_result = symbols_to_dict(symbols)
    # print(all_result)

    db = DB()
    driver = db.get_driver()
    disease_names = []

    if 'possible_disease' in all_result:
        print('successfully find')
        for disease in all_result['possible_disease']:
            # diseases.append({'name': disease})

            query = f"MATCH (n:knowledge {{name: '{disease}'}}) RETURN n.chinese_name AS chineseName, n.path AS path, n.link AS link"
            with db.get_driver().session(database='knowledge') as session:
                existing_node = session.execute_read(db._get_node_by_name, disease)
                type(existing_node)
                print('find knowledge', type(existing_node))
                # diseases.append({
                #     'name': disease,
                #     'chinese_name': str(record['chineseName']),
                #     'path': str(record['path']),
                #     'link': str(record['link'])
                # })
                disease_names.append(disease)
                diseases.append({
                    'name': disease,
                    'chinese_name': str(existing_node['chinese_name']),
                    'path': str(existing_node['path']),
                    'link': str(existing_node['link'])
                })

            tree_node.clear()

            for disease in diseases:
                print('finding tree', disease['name'])
                hierarchy = db.get_node_hierarchy(disease['name'])
                disease['treeNode'] = hierarchy
                tree_node.append({'name': disease['name'], 'treeNode': hierarchy})
                print('found tree', hierarchy)

                # result = session.run(query)
                # for record in result:

    # 使用 Flask 提供的 jsonify 函数将数据转换为 JSON 格式并返回
    else:
        diseases.append({'name': 'healthy'})
        disease_names.append('healthy')

    print(diseases)

    data = {
        "symptoms": patients[0]['symptoms'],
        "Mr_Id": random.randint(1, 10000),
        "Possible_disease": disease_names,
        "Name": patients[0]['name'],
        "time": datetime.now()
    }

    print(data)

    with driver.session(database="record") as session:
        label = 'mr'
        properties = data
        session.execute_write(db._create_node, label, properties)
        print('mr added')

    db.close()

    # cypher_query = """
    #     CREATE (:mr {
    #         symptoms: $symptoms,
    #         Mr_Id: $Mr_Id,
    #         Possible_disease: $Possible_disease,
    #         Name: $Name,
    #         time: $time
    #     })
    #     """
    # db = DB()
    # driver = db.get_driver()
    # with driver.session(database="record") as session:
    #     session.run(cypher_query, data)

    return jsonify(diseases)


@app.route('/tree')
def get_tree():
    return jsonify(tree_node)


@app.route('/symptoms', methods=['GET'])
def post_symptoms():
    db = DB()

    # symptom_types = ["Coughing", "Sneezing", "Fever", "Headache", "Fatigue", "Nausea", "Dizziness", "Chest Pain",
    #                  "Abdominal Pain", "Other"]
    # symptoms_list = {}

    symptom_types = ["发热类", "呼吸道上感类", "呼吸道症状类", "消化道症状类", '其他症状']
    symptoms = {
        "发热类": ["fever", "high_fever", "low_grade_fever"],
        "呼吸道上感类": ["upper_respiratory_tract_symptoms", "runny_nose", "nasal_congestion", "sore_throat",
                   "upper_respiratory_tract_infection_symptoms"],
        "呼吸道症状类": [
            "original_acute_exacerbation_of_chronic_lung_diseases", "chronic_cough", "recurrent_cough", "wheezing",
            "chest_pain", "shortness_of_breath", "decreased_breath_sounds", "hyperresonance_or_dullness_on_percussion",
            "tracheal_shift", "x_ray_pneumothorax_line", "x_ray_lung_compression", "local_compression_symptoms",
            "abnormal_bronchiectasis_changes", "lower_respiratory_tract_symptoms", "aggravated_cough",
            "significant_dyspnea",
            "fine_crackles", "respiratory_distress", "tachypnea", "prolonged_expiration", "expiratory_wheezing",
            "full_chest", "hyperresonance", "clubbing"
        ],
        "消化道症状类": ["diarrhea_or_vomiting", "diarrhea", "vomiting", "loss_of_appetite"],
        '其他症状': []
    }

    categorized_symptoms = symptoms.items()
    for symptom in db.find_all_symptom_list():
        if symptom not in categorized_symptoms:
            symptoms['其他症状'].append(symptom)
    # for symptom_type in symptom_types:
    #     symptoms_list[symptom_type] = []
    # symptoms_list["Other"] = db.find_all_symptom_list()
    data = {
        "symptomTypes": symptom_types,
        "symptomsList": symptoms
    }

    db.close()

    return jsonify(data)


@app.route('/history', methods=['GET'])
def get_history():
    db = DB()
    driver = db.get_driver()
    with driver.session(database="record") as session:
        result = session.run("MATCH (mr:mr) RETURN mr")
        records = []
        for record in result:
            data_time = record['mr']['time']
            if isinstance(record['mr']['time'], DateTime):
                data_time = record['mr']['time'].strftime('%Y-%m-%d %H:%M:%S')
            data = {
                "symptoms": record['mr']['symptoms'],
                "id": record['mr']['Mr_Id'],
                "diagnosisResult": record['mr']['Possible_disease'],
                "name": record['mr']['Name'],
                # "diagnosisTime": record['mr']['time'].isoformat()
                "diagnosisTime": data_time
            }
            records.append(data)
        db.close()
        return jsonify(records)


@app.route('/edit', methods=['POST'])
def handle_edit_data():
    data = request.get_json()
    print(data)
    db = DB()

    if data['label'] == 'disease' or data['label'] == 'item':
        edit_from = data.get('edit_from')
        edit_to = data.get('edit_to')
        result = db.update_node(edit_from, edit_to, data['label'])

    if data['label'] == 'symptom':
        if data['type'] == 'edit':
            edit_from = data['edit_from']
            edit_to = data['edit_to']
            query = f"MATCH (n) WHERE n.name = '{edit_from}' SET n.name = '{edit_to}' RETURN n"
            with db.get_driver().session(database="disease") as session:
                result = session.run(query)
                print(result.single())

        elif data['type'] == 'add':
            add_name = data['add']
            label = data['label']
            query = f"CREATE (n:{label} {{name: '{add_name}'}}) RETURN n"
            with db.get_driver().session(database="disease") as session:
                result = session.run(query)
                print(result.single())

        elif data['type'] == 'delete':
            delete_name = data['delete']
            query = f"MATCH (n) WHERE n.name = '{delete_name}' DETACH DELETE n"
            with db.get_driver().session(database="disease") as session:
                result = session.run(query)
                print(result.consume())

    if data['label'] in ['HAS_BRANCH', 'HAS_BRANCH_COMBINATION']:
        def convert_string_to_array(input_string):
            stripped_string = input_string.strip("()")  # 移除括号并去除空格
            sub_strings = stripped_string.split(",")  # 分割为子字符串列表
            string_array = [sub_string.strip() for sub_string in sub_strings]  # 去除子字符串中的空格并添加到数组中
            return string_array

        if data['type'] == 'edit':
            edit_from = convert_string_to_array(data['edit_from'])
            edit_to = convert_string_to_array(data['edit_to'])

            if edit_from == '' and edit_to == '':
                return jsonify({'message': 'Both edit_from and edit_to are empty.'})

            elif edit_from == '':
                # Delete the relationship C - [label] - D
                query = f"MATCH (c)-[r:{data['label']}]->(d) WHERE c.name = '{edit_to[0]}' AND d.name = '{edit_to[1]}' DELETE r"
                with db.driver.session(database="disease") as session:
                    session.run(query)
                return jsonify({'message': 'Relationship deleted successfully.'})

            elif edit_to == '':
                # Add the relationship A - [label] - B
                query = f"MATCH (a),(b) WHERE a.name = '{edit_from[0]}' AND b.name = '{edit_from[1]}' CREATE (a)-[r:{data['label']}]->(b) RETURN r"
                with db.driver.session(database="disease") as session:
                    session.run(query)
                return jsonify({'message': 'Relationship added successfully.'})

            # Update the relationship A - [label] - B to C - [label] - D
            query = f"MATCH (a)-[r:{data['label']}]->(b) WHERE a.name = '{edit_from[0]}' AND b.name = '{edit_from[1]}' SET a.name = '{edit_to[0]}', b.name = '{edit_to[1]}' RETURN r"
            with db.driver.session(database="disease") as session:
                session.run(query)
            return jsonify({'message': 'Relationship updated successfully.'})

    db.close()
    return 'Data received successfully'


app.run(port=8000)
