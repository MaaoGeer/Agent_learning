"""
    可视化需求3: 河南疫情可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

# 读取数据文件
f = open("E:/pytest/pythonProject/Data/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()

# 取到各省数据
# 将JSON数据转换为Python字典
data_dict = json.loads(data)
# 取出各个省份数据
city_data_list = data_dict["areaTree"][0]["children"][3]["children"]
# 组装各个省份的数据为元组，并将各个省份的数据都封装在列表内
data_list = []  # 绘图所需的数据列表
for city_data in city_data_list:
    city_name = city_data["name"] + "市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name, city_confirm))

# 创建地图对象
maap = Map()
maap.add("河南疫情地图", data_list, "河南")

# 设置全局配置，定制分段视觉映射
maap.set_global_opts(
    title_opts=TitleOpts(title="河南疫情地图"),  # 地图标题
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,  # 手动校准范围
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000人及以上", "color": "#990033"}

        ]
    )
)

# 绘图
maap.render("河南疫情地图.html")
