import flask
from flask import Flask, render_template

from model.tempp import pred, pred2

app = Flask(__name__, template_folder='templates')

@app.route('/')
@app.route('/index')
def index():
    return(render_template('index.html'))

@app.route('/trial')
def trial():
    return(render_template('trial.html'))

@app.route('/data')
def data():
    return(render_template('data.html'))

@app.route('/data2')
def data2():
    return(render_template('data2.html'))

@app.route('/general')
def general():
    return(render_template('general.html'))


@app.route('/model', methods=['GET', 'POST'])
def model():
    if flask.request.method == 'GET':
        return(render_template('ymodel.html'))
    if flask.request.method == 'POST':
        state = 'State_' + flask.request.form['state']
        dist = 'Dist_' + flask.request.form['dist']
        crop = 'Crop_' + flask.request.form['crop']
        area = flask.request.form['area']
        gca = flask.request.form['gca']
        rain = flask.request.form['rain']
        temp = flask.request.form['temp']
        fert = flask.request.form['fert']
        soil = 'Soil_' + flask.request.form['soil']

        p = pred(state, dist, crop, area, gca, rain, temp, fert, soil)

        return render_template('ymodel.html', result=p)
@app.route('/model2', methods=['GET', 'POST'])
def model2():
    if flask.request.method == 'GET':
        return(render_template('ymodel2.html'))
    if flask.request.method == 'POST':
        state = 'State_' + flask.request.form['state']
        dist = 'Dist_' + flask.request.form['district']
        crop = 'Crop_' + flask.request.form['crop']
        yieldd = flask.request.form['yieldd']
        area = flask.request.form['area']
        gca = flask.request.form['gca']
        rain = flask.request.form['rain']
        temp = flask.request.form['temp']
        fert = flask.request.form['fert']
        soil = 'Soil_' + flask.request.form['soil']

        p2 = pred2(state, dist, crop, yieldd, area, gca, rain, temp, fert, soil)

        return render_template('ymodel2.html', result=p2)

@app.route('/state1')
def state1():
    return(render_template('state1.html'))

@app.route('/state2')
def state2():
    return(render_template('state2.html'))


@app.route('/state3')
def state3():
    return(render_template('state3.html'))

@app.route('/state4')
def state4():
    return(render_template('state4.html'))

@app.route('/state5')
def state5():
    return(render_template('state5.html'))

@app.route('/state6')
def state6():
    return(render_template('state6.html'))

@app.route('/state7')
def state7():
    return(render_template('state7.html'))

@app.route('/state8')
def state8():
    return(render_template('state8.html'))

@app.route('/state9')
def state9():
    return(render_template('state9.html'))

@app.route('/state10')
def state10():
    return(render_template('state10.html'))

@app.route('/state11')
def state11():
    return(render_template('state11.html'))

@app.route('/state12')
def state12():
    return(render_template('state12.html'))

@app.route('/state13')
def state13():
    return(render_template('state13.html'))

@app.route('/state14')
def state14():
    return(render_template('state14.html'))

@app.route('/state15')
def state15():
    return(render_template('state15.html'))

@app.route('/state16')
def state16():
    return(render_template('state16.html'))

@app.route('/state17')
def state17():
    return(render_template('state17.html'))

@app.route('/state18')
def state18():
    return(render_template('state18.html'))

@app.route('/state19')
def state19():
    return(render_template('state19.html'))

@app.route('/state20')
def state20():
    return(render_template('state20.html'))

@app.route('/crop1')
def crop1():
    return(render_template('crop1.html'))

@app.route('/crop2')
def crop2():
    return(render_template('crop2.html'))

@app.route('/crop3')
def crop3():
    return(render_template('crop3.html'))

@app.route('/crop4')
def crop4():
    return(render_template('crop4.html'))

@app.route('/crop5')
def crop5():
    return(render_template('crop5.html'))

@app.route('/crop6')
def crop6():
    return(render_template('crop6.html'))

@app.route('/crop7')
def crop7():
    return(render_template('crop7.html'))

@app.route('/crop8')
def crop8():
    return(render_template('crop8.html'))

@app.route('/crop9')
def crop9():
    return(render_template('crop9.html'))

@app.route('/crop10')
def crop10():
    return(render_template('crop10.html'))

@app.route('/crop11')
def crop11():
    return(render_template('crop11.html'))

@app.route('/crop12')
def crop12():
    return(render_template('crop12.html'))

@app.route('/crop13')
def crop13():
    return(render_template('crop13.html'))

@app.route('/crop14')
def crop14():
    return(render_template('crop14.html'))

@app.route('/crop15')
def crop15():
    return(render_template('crop15.html'))

@app.route('/general1')
def general1():
    return(render_template('general1.html'))

@app.route('/general2')
def general2():
    return(render_template('general2.html'))

@app.route('/general3')
def general3():
    return(render_template('general3.html'))

@app.route('/general4')
def general4():
    return(render_template('general4.html'))

@app.route('/general5')
def general5():
    return(render_template('general5.html'))

@app.route('/general6')
def general6():
    return(render_template('general6.html'))

@app.route('/general7')
def general7():
    return(render_template('general7.html'))

@app.route('/general8')
def general8():
    return(render_template('general8.html'))

 

if __name__ == '__main__':
    app.run(debug=True)
