import json
import re


def keyword_callback(key: str, keyword: str):
    print(f'{key}: {keyword}')


def parse_json(json_str: str,
               required_fields=None,
               keywords=None,
               keyword_callback=keyword_callback):

    if not isinstance(json_str, str):
        raise TypeError("Неверное значение поля json_str")
    if not isinstance(keywords, list):
        raise TypeError("Неверное значение поля keywords")
    if not isinstance(required_fields, list):
        raise TypeError("Неверное значение поля required_fields")
    if not callable(keyword_callback):
        raise TypeError("keyword_callback не является функцией")

    json_doc = json.loads(json_str)
    for field in required_fields:
        if field in json_doc:
            for k in keywords:
                pattern = fr'\b{k}\b'
                if re.search(pattern, str(json_doc[field]), flags=re.I):
                    keyword_callback(field, k)
