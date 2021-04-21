from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('base.html', **param)


@app.route('/training/<prof>')
def training_prof(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<param_list>')
def list_prof(param_list):
    profs = ['Инженер-исследователь', 'Пилот', 'Врач']
    return render_template('list_prof.html', param_list=param_list, profs=profs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')