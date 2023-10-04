import json
import re


def keyword_callback(key: str, keyword: str):
    print(f'{key}: {keyword}')


def parse_json(json_str: str,
               required_fields=None,
               keywords=None,
               keyword_callback=keyword_callback):

    if not isinstance(json_str, str):
        raise TypeError("Wrong value for json_str")
    if not isinstance(keywords, list):
        raise TypeError("Wrong value for keywords")
    if not isinstance(required_fields, list):
        raise TypeError("Wrong value for required_fields")
    if not callable(keyword_callback):
        raise TypeError("keyword_callback is not a func")

    json_doc = json.loads(json_str)
    for field in required_fields:
        if field in json_doc:
            for k in keywords:
                pattern = fr'\b{k}\b'
                if re.search(pattern, str(json_doc[field]), flags=re.I):
                    keyword_callback(field, k)
