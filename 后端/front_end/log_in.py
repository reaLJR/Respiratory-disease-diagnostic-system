from front_end.app import *


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # 验证用户名和密码并登录用户
    # TODO: 验证用户并登录

    # 在会话中保存用户信息
    session['username'] = username

    return 'Logged in successfully'

@app.route('/dashboard')
def dashboard():
    # 从会话中获取用户信息
    username = session.get('username')

    if username:
        # 显示仪表板页面
        return f'Welcome to the dashboard, {username}!'
    else:
        # 重定向到登录页面
        return 'Please log in first.'


# 在用户登录时，将用户的身份信息保存在会话中
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/submit_data', methods=['POST'])
@login_required # 需要用户认证才能访问
def submit_data():
    # 获取当前用户的 ID
    user_id = current_user.get_id()

    # 将用户提交的数据保存到数据库中
    data = request.json
    save_data_to_database(user_id, data)

    return jsonify({'status': 'ok'})

@app.route('/get_data', methods=['GET'])
@login_required # 需要用户认证才能访问
def get_data():
    # 获取当前用户的 ID
    user_id = current_user.get_id()

    # 从数据库中获取当前用户的数据
    data = get_data_from_database(user_id)

    # 处理数据并返回给前端
    processed_data = process_data(data)
    return jsonify(processed_data)