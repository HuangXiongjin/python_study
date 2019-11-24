"""---author==hxj---"""
import json


def text_read(file_path: str):
    """
    读文本文件中的内容
    :param file_path: 文件路径
    :return: 文件中的内容
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def json_read(file_path: str):
    """
    读json文件中的数据
    :param file_path: 文件路径
    :return: json内容对应的python数据
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # return json.loads(f.read())
            return json.load(f)
    except FileNotFoundError:
        return None


def json_write(data, file_path: str):
    """
    将python数据转换成json写入文件中
    :param data: 需要写入的数据
    :param file_path: 写入的文件的路径
    :return: 是否写入成功
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            # f.write(json.dumps(data))
            json.dump(data, f)
            return True
    except:
        return False
