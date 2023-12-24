from front_end.app import *
from database.db import *


@app.route('/change_knowledge', methods=['POST'])
def change_knowledge():
    db = DB()

    # data = request.get_json()  # 获取前端发送的 JSON 数据
    disease_added = request.form['disease_added']
    symptoms_added = request.form['symptoms_added']
    item_added = request.form['item_added']
    branch_added = request.form['branch_added']
    branch_combination_added = request.form['branch_combination_added']


    # disease_added = data.get('disease_added', [])  # 获取疾病列表，如果没有则返回空列表
    # symptoms_added = data.get('symptoms_added', [])  # 获取症状列表，如果没有则返回空列表
    # item_added = data.get('item_added', [])  # 获取项目列表，如果没有则返回空列表
    # branch_added = data.get('branch_added', [])  # 获取科室列表，如果没有则返回空列表
    # branch_combination_added = data.get('branch_combination_added', [])  # 获取科室组合列表，如果没有则返回空列表

    # 在这里对这些列表进行处理，例如将它们存储到数据库中
    for disease in disease_added.splitlines():
        label = 'disease'
        properties = {'name': disease}
        with db.get_driver().session() as session:
            try:
                result = session.write_transaction(db._create_node, label, properties)
                print(f"Created node {result}")
            except ServiceUnavailable as ex:
                logging.error(f"Failed to create node: {ex}")
        # db._create_node('disease', {'name': disease})

    # 这里只是简单地打印出来列表的内容
    print('disease_added:', disease_added)
    print('symptoms_added:', symptoms_added)
    print('item_added:', item_added)
    print('branch_added:', branch_added)
    print('branch_combination_added:', branch_combination_added)

    # 返回响应，可以是一个成功的状态码或者其他数据
    return jsonify({'status': 'success'})