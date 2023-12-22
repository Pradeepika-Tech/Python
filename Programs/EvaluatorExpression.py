# import json
# import requests
# from typing import Dict
#
#
# def expression_evaluator(group: Dict) -> str:
#     final_str, variable_value = "", ""
#     # print(group.keys())
#     # print(group.values())
#     for k, v in group.items():
#         if k == 'groupName':
#             final_str = v
#         if k == 'expressions':
#             for i in v:
#                 for k1, v1 in i.items():
#                     if k1 == 'dependency' and len(v1) == 0:
#                         variable_value = i["expression"]
#                     if k1 == 'name':
#                         final_str += ':' + v1
#                     if k1 == 'expression' and 'DIRECT' in i.values():
#                         final_str += ':' + v1
#                     elif k1 == 'expression' and 'RS_EXPRESSION' in i.values():
#                         old_value = i['expression'].split('+')[1]
#                         new_value_in_same_format = "(" + variable_value + ' +' + old_value + ")"
#                         final_str += ':' + new_value_in_same_format
#                     elif k1 == 'expression' and 'DOLLAR_EXPRESSION' in i.values():
#                         old_value = i['expression'].split('+')[1]
#                         new_value_in_same_format = "(" + variable_value + ' +' + old_value + ") $"
#                         final_str += ':' + new_value_in_same_format
#     return final_str
#
#
# if __name__ == '__main__':
#     requests = requests.get("https://mocki.io/v1/01d9f80f-48b8-4703-910a-1203805193b8")
#     todos = json.loads(requests.text)
#     # print(todos)
#     for todo in todos:
#         print(expression_evaluator(todo))
#

import json
import requests
from typing import Dict


def expression_evaluator(group: Dict) -> str:
    final_str, variable_value = "", ""
    for k, v in group.items():
        if k == 'groupName':
            final_str = v
        if k == 'expressions':
            for i in v:
                for k1, v1 in i.items():
                    if k1 == 'dependency' and len(v1) == 0:
                        variable_value = i["expression"]
                    if k1 == 'name':
                        final_str += ':' + v1
                    if k1 == 'expression' and 'DIRECT' in i.values():
                        final_str += ':' + v1
                    elif k1 == 'expression' and 'RS_EXPRESSION' in i.values():
                        old_value = i['expression'].split('+')[1]
                        new_value_in_same_format = "(" + variable_value + ' +' + old_value + ")"
                        final_str += ':' + new_value_in_same_format
                    elif k1 == 'expression' and 'DOLLAR_EXPRESSION' in i.values():
                        old_value = i['expression'].split('+')[1]
                        new_value_in_same_format = "(" + variable_value + ' +' + old_value + ") $"
                        final_str += ':' + new_value_in_same_format
    return final_str


def process_large_dataset(url):
    batch_size = 10  # Number of expression groups to process at a time
    requests_data = requests.get(url)
    todos = json.loads(requests_data.text)

    for i in range(0, len(todos), batch_size):
        batch = todos[i:i+batch_size]
        for todo in batch:
            print(expression_evaluator(todo))


if __name__ == '__main__':
    url = "https://mocki.io/v1/01d9f80f-48b8-4703-910a-1203805193b8"
    process_large_dataset(url)

