from app import (
    app,
    render_template,
    session
)

@app.route('/')
def default():
    return render_template('index.html', id=session['user_id'])