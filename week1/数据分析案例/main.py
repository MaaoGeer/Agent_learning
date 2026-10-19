from file_define import FileReader, TextReader, JsonReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, TitleOpts, InitOpts

test_file_reader = TextReader("E:/pytest/pythonProject/数据分析案例/2011年1月销售数据.txt")
json_file_reader = JsonReader("E:/pytest/pythonProject/数据分析案例/2011年2月销售数据JSON.txt")

jan_data: list[Record] = test_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
# 将两个月份的数据合并
all_data = jan_data + feb_data

# 数据计算
data_dict = {}
for data in all_data:
    try:
        data_dict[data.date] += data.money
    except KeyError:
        data_dict[data.date] = data.money

#
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=TitleOpts("每日销售额"),
)

bar.render("每日销售额柱状图.html")
