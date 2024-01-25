from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from bokeh.io import show 
from bokeh.layouts import column
from bokeh.models.widgets import Slider, Button

# Создаем источник данных
source = ColumnDataSource(data=dict(x=[1], y=[1]))

# Создаем график
plot = figure(plot_width=400, plot_height=400)
plot.circle(x='x', y='y', size=20, color='navy', alpha=0.5, source=source)

# Создаем слайдеры для управления координатами
x_slider = Slider(start=0, end=10, value=1, step=0.1, title="X-coordinate")
y_slider = Slider(start=0, end=10, value=1, step=0.1, title="Y-coordinate")

# Функция, вызываемая при изменении значения слайдеров
def update(attrname, old, new):
    source.data = dict(x=[x_slider.value], y=[y_slider.value])

# Связываем функцию с событием изменения значений слайдеров
x_slider.on_change('value', update)
y_slider.on_change('value', update)

# Создаем кнопку
button = Button(label="Click me!", button_type="success")

# Функция, вызываемая при нажатии кнопки
def button_click():
    source.data = dict(x=[5], y=[5])
    x_slider.value = 5
    y_slider.value = 5

# Связываем функцию с событием нажатия кнопки
button.on_click(button_click)

# Добавляем все элементы на макет
layout = column(x_slider, y_slider, button, plot)

# Показываем график
curdoc().add_root(layout)
