"""
    可视化需求3: 动态GDP柱状图
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType     # 主题设置模块

f = open("E:/pytest/pythonProject/Data/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
data_lines.pop(0)
f.close()

# 将数据转换为字典储存
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])     # split函数处理字符串后返回列表类型
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 排序年份
time_line = Timeline({"theme": ThemeType.LIGHT})
sorted_year_list = sorted(data_dict.keys())

for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][0:8]

    x_data = []
    y_data = []

    for country_gdp in year_data:
        x_data.append(country_gdp[0])     # 添加x轴数据
        y_data.append(country_gdp[1]/100000000)     # 添加y轴数据
    bar = Bar()
    x_data.reverse()        # 反转数据
    y_data.reverse()        # 反转数据

    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()

    #
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    time_line.add(bar, str(year))

# 自动播放设置
time_line.add_schema(
    play_interval=1000,     # 自动播放时间间隔，单位毫秒
    is_timeline_show=True,      # 是否在自动播放的时候显示时间线
    is_auto_play=True,      # 是否自动播放
    is_loop_play=True       # 是否循环自动播放
)

# 绘图
time_line.render("2019-2020年全球GDP前八国家柱状图.html")
