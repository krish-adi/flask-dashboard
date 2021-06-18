import flask.json as json
import random
import datetime


colors = { 'red': 'rgb(255, 99, 132)', 'orange': 'rgb(255, 159, 64)',
            'yellow': 'rgb(255, 205, 86)', 'green': 'rgb(75, 192, 192)',
            'blue': 'rgb(54, 162, 235)', 'purple': 'rgb(153, 102, 255)',
            'grey': 'rgb(201, 203, 207)' }

colors_half = { 'red': 'rgba(255, 99, 132, 0.5)', 'orange': 'rgba(255, 159, 64, 0.5)',
            'yellow': 'rgba(255, 205, 86, 0.5)', 'green': 'rgba(75, 192, 192, 0.5)',
            'blue': 'rgba(54, 162, 235, 0.5)', 'purple': 'rgba(153, 102, 255, 0.5)',
            'grey': 'rgba(201, 203, 207, 0.5)' }

def bar():
    type = 'bar'

    lastNdays = 5
    labels = [(datetime.date.today()-datetime.timedelta(days=day)).strftime("%d-%m-%Y") for day in range(lastNdays-1,-1,-1)]
    dataset_1 = { 'label': 'Dataset 1', 'backgroundColor': colors['red'], 'data': [random.randint(-100, 100) for i in range(lastNdays)]}
    dataset_2 = { 'label': 'Dataset 2', 'backgroundColor': colors['blue'], 'data': [random.randint(-100, 100) for i in range(lastNdays)]}
    dataset_3 = { 'label': 'Dataset 3', 'backgroundColor': colors['green'], 'data': [random.randint(-100, 100) for i in range(lastNdays)]}
    datasets = [dataset_1, dataset_2, dataset_3]
    data = {'labels': labels, 'datasets': datasets}

    legend = { 'display': True, 'position': 'top', 'labels': { 'fontSize': 14} }
    tooltips =  { 'mode': 'index', 'intersect': False }
    scales = { 'xAxes': [{ 'stacked': False , 'ticks': {'fontSize': 14} }], 'yAxes': [{ 'stacked': False }] }
    options = {'legend': legend, 'tooltips': tooltips, 'scales': scales, 'responsive': True, 'maintainAspectRatio': False}

    chart_config = json.dumps({'type': type, 'data': data, 'options': options})

    return chart_config

def polar():
    type = 'polarArea'

    lastNdays = 5
    labels = [(datetime.date.today()-datetime.timedelta(days=day)).strftime("%d-%m-%Y") for day in range(lastNdays-1,-1,-1)]
    dataset_1 = { 'label': 'Dataset 1', 'backgroundColor': [colors_half['red'], colors_half['orange'], colors_half['green'], colors_half['blue'], colors_half['purple']],
                    'data': [random.randint(-100, 100) for i in range(lastNdays)]}
    datasets = [dataset_1]
    data = {'labels': labels, 'datasets': datasets}

    legend = { 'display': True, 'position': 'top', 'labels': { 'fontSize': 14} }
    animation = { 'animateScale': True, 'animateRotate': True }
    scale = { 'ticks': { 'beginAtZero': True }, 'reverse': False }
    options = {'legend': legend, 'responsive': True, 'animation': animation, 'scale': scale, 'maintainAspectRatio': False}

    chart_config = json.dumps({'type': type, 'data': data, 'options': options})

    return chart_config

def doughnut():
    type = 'doughnut'

    lastNdays = 5
    labels = [(datetime.date.today()-datetime.timedelta(days=day)).strftime("%d-%m-%Y") for day in range(lastNdays-1,-1,-1)]
    dataset_1 = { 'label': 'Dataset 1', 'backgroundColor': [colors['red'], colors['orange'], colors['green'], colors['blue'], colors['purple']],
                    'data': [random.randint(-100, 100) for i in range(lastNdays)]}
    datasets = [dataset_1]
    data = {'labels': labels, 'datasets': datasets}

    legend = { 'display': True, 'position': 'top', 'labels': { 'fontSize': 14} }
    animation = { 'animateScale': True, 'animateRotate': True }
    options = {'legend': legend, 'responsive': True, 'animation': animation, 'maintainAspectRatio': False}

    chart_config = json.dumps({'type': type, 'data': data, 'options': options})

    return chart_config

def mixed():
    type = 'bar'

    lastNdays = 10
    labels = [(datetime.date.today()-datetime.timedelta(days=day)).strftime("%d-%m-%Y") for day in range(lastNdays-1,-1,-1)]
    dataset_bar = { 'order': 1, 'yAxisID': 'A', 'label': 'Rainfall', 'backgroundColor': colors['blue'], 'data': [random.randint(0, 30) for i in range(lastNdays)]}
    dataset_line = { 'order': 2, 'yAxisID': 'B', 'type': 'line', 'label': 'Temperature', 'backgroundColor': colors['orange'], 'data': [random.randint(15, 25) for i in range(lastNdays)], 'fill': False}

    datasets = [dataset_bar, dataset_line]
    data = {'labels': labels, 'datasets': datasets}

    legend = { 'display': True, 'position': 'top', 'labels': { 'fontSize': 14} }
    scales = { 'yAxes': [{ 'id': 'A', 'type': 'linear', 'position': 'left' }, { 'id': 'B', 'type': 'linear', 'position': 'right' }] }
    tooltips =  { 'mode': 'index', 'intersect': False }
    options = {'legend': legend, 'responsive': True, 'maintainAspectRatio': False, 'scales': scales, 'tooltips': tooltips}

    chart_config = json.dumps({'type': type, 'data': data, 'options': options})

    return chart_config

def line():
    type = 'line'

    lastNdays = 10
    labels = [(datetime.date.today()-datetime.timedelta(days=day)).strftime("%d-%m-%Y") for day in range(lastNdays-1,-1,-1)]
    dataset_1 = {'label': 'Parameter 1', 'yAxisID': 'A', 'backgroundColor': colors['green'], 'borderColor': colors['green'], 'fill': False, 'data': [random.randint(0, 30) for i in range(lastNdays)]}
    dataset_2 = {'label': 'Parameter 2', 'yAxisID': 'B', 'backgroundColor': colors['yellow'], 'borderColor': colors['yellow'], 'fill': False, 'data': [random.randint(15, 25) for i in range(lastNdays)]}

    datasets = [dataset_1, dataset_2]
    data = {'labels': labels, 'datasets': datasets}

    legend = { 'display': True, 'position': 'top', 'labels': { 'fontSize': 14} }
    tooltips =  { 'mode': 'index', 'intersect': False }
    scales = { 'yAxes': [{ 'id': 'A', 'type': 'linear', 'position': 'left' }, { 'id': 'B', 'type': 'linear', 'position': 'right' }] }
    options = {'legend': legend, 'responsive': True, 'maintainAspectRatio': False,'scales': scales, 'tooltips': tooltips}

    chart_config = json.dumps({'type': type, 'data': data, 'options': options})

    return chart_config
