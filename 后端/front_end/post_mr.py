from front_end.app import *
from database.db import *


@app.route('/submit_patient_form', methods=['POST'])
def submit_patient_form():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    # disease = request.form['disease']
    symptoms = request.form['symptoms']
    print(name, age, gender, symptoms)

    db = DB()
    label = 'MR'
    properties = {
        'name': name,
        'age': age,
        'gender': gender,
        'symptom': symptoms.split(',')  # str list
    }
    with db.get_driver().session() as session:
        try:
            result = session.write_transaction(db._create_node, label, properties)

            print(f"Created node {result}")
        except ServiceUnavailable as ex:
            logging.error(f"Failed to create node: {ex}")

    session['mr_id'] = 'mr114514'

    # 关闭数据库连接
    db.close()

    return 'OK'

# app.run()
