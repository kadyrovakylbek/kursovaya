from bokeh.plotting import figure, show
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource, HoverTool, RangeSlider, NumeralTickFormatter
from bokeh.io import curdoc
import pandas as pd

# Пример данных (вам нужно заменить этот блок на ваши собственные данные)
data = {
    'Date': pd.date_range(start='2022-01-01', end='2022-01-31'),
    'Open': [150, 152, 153, 148, 147, 145, 149, 152, 155, 158, 160, 162, 161, 159, 156, 154, 153, 152, 150, 148, 147],
    'Close': [152, 153, 148, 147, 145, 149, 152, 155, 158, 160, 162, 161, 159, 156, 154, 153, 152, 150, 148, 147, 149],
}

df = pd.DataFrame(data)
source = ColumnDataSource(df)

# Создаем график временного ряда
time_series_plot = figure(plot_width=800, plot_height=300, x_axis_type="datetime", title="Stock Prices")
time_series_plot.line(x='Date', y='Close', line_width=2, line_color="blue", legend_label="Closing Price", source=source)
time_series_plot.circle(x='Date', y='Close', size=8, color="blue", alpha=0.5, source=source)

# Создаем график баров для отображения изменения цен
bar_plot = figure(plot_width=800, plot_height=200, x_axis_type="datetime", title="Daily Price Change")
bar_plot.vbar(x='Date', top='Close-Open', width=0.8, color="green", legend_label="Daily Change", source=source)
bar_plot.yaxis[0].formatter = NumeralTickFormatter(format="0.0f")

# Добавляем интерактивные элементы управления
date_range_slider = RangeSlider(start=df['Date'].min(), end=df['Date'].max(), value=(df['Date'].min(), df['Date'].max()), step=1, title="Date Range")
date_range_slider.on_change('value', lambda attr, old, new: update_data())

# Добавляем подсказки при наведении на графики
hover_tool = HoverTool(
    tooltips=[
        ("Date", "@Date{%F}"),
        ("Close Price", "@Close{0.2f}")
    ],
    formatters={
        'Date': 'datetime',  # используем формат даты для подсказок
        'Close': 'printf',   # формат для Close
    },
    mode='vline'  # подсказки по вертикали
)

time_series_plot.add_tools(hover_tool)
bar_plot.add_tools(hover_tool)

# Обновление данных в источнике данных при изменении диапазона дат
def update_data():
    start_date, end_date = date_range_slider.value
    filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    source.data = ColumnDataSource(filtered_data).data

# Создаем макет
layout = layout([[time_series_plot], [bar_plot], [date_range_slider]])

# Обновляем данные при запуске документа
update_data()

# Добавляем макет в документ
curdoc().add_root(layout)

# Запускаем сервер Bokeh (bokeh serve --show filename.py) для отображения дашборда
