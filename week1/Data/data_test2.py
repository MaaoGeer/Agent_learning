"""
    Pyecharts基础入门：柱状图
"""
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

# 构建柱状图对象
bar = Bar()

# 添加数据
bar.add_xaxis(["中国", "美国", "英国"])
bar.add_yaxis("GDP", [30, 20, 15], label_opts=LabelOpts(position="right"))

# 反转x,y轴
bar.reversal_axis()

# 绘图
bar.render("基础柱状图.html")
