import json
import re


def keyword_callback(key: str, keyword: str):
    return f'{key}: {keyword}'


def parse_json(json_str: str,
               required_fields=None,
               keywords=None,
               callback=keyword_callback):

    if not isinstance(json_str, str):
        raise TypeError("Wrong value for json_str")
    if not (isinstance(keywords, list) or keywords is None):
        raise TypeError("Wrong value for keywords")
    if not (isinstance(required_fields, list) or required_fields is None):
        raise TypeError("Wrong value for required_fields")
    if not callable(callback):
        raise TypeError("keyword_callback is not a func")

    if keywords is None or required_fields is None:
        return

    try:
        json_doc = json.loads(json_str)
    except json.decoder.JSONDecodeError:
        print("json_str should be a json-file of the str type")
        raise

    for field in required_fields:
        if field in json_doc:
            for k in keywords:
                pattern = fr'\b{k}\b'
                if res := re.search(pattern, str(json_doc[field]), flags=re.I):
                    callback(field, res[0])
