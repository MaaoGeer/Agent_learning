"""
    可视化需求2: 全国疫情可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

namemap = {'黑龙江省': '黑龙江', '吉林省': '吉林', '辽宁省': '辽宁', '北京市': '北京', '天津市': '天津',
           '河北省': '河北', '山西省': '山西', '内蒙古自治区': '内蒙古', '上海市': '上海', '江苏省': '江苏',
           '山东省': '山东', '浙江省': '浙江', '安徽省': '安徽', '江西省': '江西',
           '福建省': '福建', '广东省': '广东', '澳门特别行政区': '澳门', '台湾省': '台湾', '香港特别行政区': '香港',
           '西藏自治区': '西藏',
           '广西壮族自治区': '广西', '海南省': '海南', '河南省': '河南', '湖北省': '湖北', '湖南省': '湖南',
           '陕西省': '陕西', '新疆维吾尔自治区': '新疆',
           '宁夏回族自治区': '宁夏', '甘肃省': '甘肃', '青海省': '青海', '重庆市': '重庆', '四川省': '四川',
           '贵州省': '贵州', '云南省': '云南'}

# 读取数据文件
f = open("E:/pytest/pythonProject/Data/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()

# 取到各省数据
# 将JSON数据转换为Python字典
data_dict = json.loads(data)
# 取出各个省份数据
province_data_list = data_dict["areaTree"][0]["children"]
# 组装各个省份的数据为元组，并将各个省份的数据都封装在列表内
data_list = []  # 绘图所需的数据列表
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))

# 创建地图对象
maap = Map()
maap.add("全国疫情地图", data_list, "china", name_map=namemap)

# 设置全局配置，定制分段视觉映射
maap.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),  # 地图标题
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
maap.render("全国疫情地图.html")
