import json
# 将Python数据类型转换为JSON字符串
data = [{'name': '张大帅', 'age': 18}, {'name': '王大锤', 'age': 17}, {'name': '赵啸虎', 'age': 16}]
json_str = json.dumps(data, ensure_ascii=False)      # 为了正确显示中文，传入参数ensure_ascii=False
print(type(json_str))
print(json_str)
# 将JSON字符串转换为Python数据类型 JSON数据类型内的引号为双引号
s = '[{"name": "张大帅", "age": 18}, {"name": "王大锤", "age": 17}, {"name": "赵啸虎", "age": 16}]'
l = json.loads(s)   # 可转换为列表，字典等，根据JSON数据自动选择
print(type(l))
print(l)
