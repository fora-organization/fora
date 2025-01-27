from app import (
    app,
    render_template
)

from db_requsts import (
 get_all_users
)

@app.route('/users')
def show_all_users():
    users = get_all_users()
    return render_template('all_users.html', users=users)

@app.route('/user')
def user_details():
    return render_template('user_details.html')