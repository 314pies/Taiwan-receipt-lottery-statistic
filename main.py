#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import FigGenerator
import io
import ast

app = Flask(__name__)

period_list = ['10201', '10203', '10205', '10207', '10209', '10211',
               '10301', '10303', '10305', '10307', '10309', '10311',
               '10401', '10403', '10405', '10407', '10409', '10411',
               '10501', '10503', '10505', '10507', '10509', '10511',
               '10601', '10603', '10605', '10607', '10609', '10611',
               '10701', '10703', '10705', '10707', '10709',
               '10801', '10803', '10805', '10807', '10809']

@app.route('/')
def index():
    data = []
    for period in reversed(period_list):
        data.append({'name':period})

    return render_template(
        'index.html',
        data = data)

@app.route("/result" , methods=['GET', 'POST'])
def result():
    error = None
    select = request.form.getlist('comp_select')
    print('Received req for:'+ str(select))
    data = {
        'periodList': select,
        'name': select
    }

    if len(select) == 1:
        data['name'] = select[0]


    return render_template(
        'result.html',
        data=data,
        error=error)

@app.route('/plot.png')
def plot_png():
    _p = request.args.get('period')
    print('get req data: ' + _p)
    periodList = ast.literal_eval(str(_p))
    print('Generating Fig for: ' + str(periodList))
    fig = FigGenerator.GenerateFig(periodList)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    print('Fig generation completed: ' + str(periodList))
    return Response(output.getvalue(), mimetype='image/png')

if __name__=='__main__':
    app.run(debug=True)