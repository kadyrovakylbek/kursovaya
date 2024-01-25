from bokeh.plotting import figure, show
from bokeh.models import Slider, ColumnDataSource
from bokeh.layouts import layout
from ipwyidgets import interact
from IPython.display import display

# Создаем источник данных
source = ColumnDataSource(data=dict(x=[], y=[]))

# Создаем объект figure
plot = figure(plot_width=300, plot_height=600, title="Интерактивный график с Bokeh", tools="pan,box_zoom,reset,save", x_range=[0, 10], y_range=[0, 10])

# Добавляем линию используя данные из источника
line = plot.line('x', 'y', source=source, line_width=2, line_alpha=0.8)

# Создаем виджет
slider = Slider(title="Коэффицент маштабирования", value=1.0, start=0.1, end=2.0, step=0.1)

#Функция для обновления данных для графика
def update_data(scale):
    #Обновляем данные для графика
    x = [1, 2, 3, 4, 5] * scale
    y = [6, 7, 2, 4, 9] * scale
    source.data = dict(x=x, y=y)

#Связываем функцию обновления с изменениями в виджете
interact(update_data, scale=slider)

# Отображаем график
display(layout(plot, slider))