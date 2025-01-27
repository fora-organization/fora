from app import (
    app,
    render_template
)

@app.route('/')
def default():
    return render_template('index.html')