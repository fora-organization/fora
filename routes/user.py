from app import (
    app,
    render_template,
    redirect,
    url_for
)

from db_requsts import (
    get_all_users,
    get_user_for_id
)

@app.route('/users')
def show_all_users():
    users = get_all_users()
    return render_template('all_users.html', users=users)

@app.route('/user/<int:id>')
def user_details(id):
    user = get_user_for_id(id)
    if user:
        return render_template('user_details.html', user=user)
    else:
        return redirect(url_for('show_all_users'))
    