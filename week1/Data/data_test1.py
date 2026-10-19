"""
    Pyecharts基础入门：地图
"""
# 基础地图演示
from pyecharts.charts import Map
from pyecharts.options import *
# 准备地图对象
maap = Map()
# 准备数据
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("广东省", 499)
]
# 添加数据
maap.add("基础地图", data, "china")
# 设置全局选项
maap.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,  # 手动校准范围
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}
        ]
    )
)
# 生成地图
maap.render()
