import json
import re

with open('data.json', 'r') as f:
    data: list = json.load(f)

pattern1 = re.compile(r'고양시')
pattern2 = re.compile(r'요양병원')
pattern3 = re.compile(r'전문의')


def func(param):
    print(param)
    if param['doctors'] is None:
        param.update({'doctors': None})
        return param
    if re.search(pattern3, param['doctors']):
        param.update({'doctors': param['doctors']})
        return param
    else:
        param.update({'doctors': None})
        return param


datas = list(
    filter(lambda item: re.search(pattern1, item['address']) and re.search(pattern2, item['flag_title']), data))
datas = list(map(func, datas))

with open('filter.json', 'w') as f:
    json.dump(datas, f, ensure_ascii=False)