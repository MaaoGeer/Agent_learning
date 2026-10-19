"""
    可视化需求1: 折线图开发
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, LabelOpts
# 处理数据
f_us = open("E:/pytest/pythonProject/Data/可视化案例数据/折线图数据/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
f_jp = open("E:/pytest/pythonProject/Data/可视化案例数据/折线图数据/日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()
f_in = open("E:/pytest/pythonProject/Data/可视化案例数据/折线图数据/印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()

# 去掉不合JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "", 1)
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "", 1)
in_data = in_data.replace("jsonp_1629350745930_63180(", "", 1)
# 去掉结尾，若使用replace函数可能会删除有效数据
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# JSON转为Python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取trend key
us_trend_key = us_dict['data'][0]['trend']
jp_trend_key = jp_dict['data'][0]['trend']
in_trend_key = in_dict['data'][0]['trend']

us_x_data = us_trend_key['updateDate'][:314]
us_y_data = us_trend_key['list'][0]['data'][:314]

jp_x_data = jp_trend_key['updateDate'][:314]
jp_y_data = jp_trend_key['list'][0]['data'][:314]

in_x_data = in_trend_key['updateDate'][:314]
in_y_data = in_trend_key['list'][0]['data'][:314]

# 生成图表
line = Line()
# 添加x轴
line.add_xaxis(us_x_data)   # x轴三个国家通用
# 添加y轴
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))    # LabelOpts:是否显示数据,也可修改数据显示位置
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

# 设置全局配置
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美日印三国确诊人数", pos_left="center", pos_bottom="1%"),  # 标题修改
    legend_opts=LegendOpts(is_show=True),    # 图例
    toolbox_opts=ToolboxOpts(is_show=True),  # 工具箱
    # visual_map_opts=VisualMapOpts(is_show=True)  视觉映射
)

# 生成图表  生成html文件
line.render()

# 关闭文件
f_us.close()
f_jp.close()
f_in.close()
