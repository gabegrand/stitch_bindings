from stitch_core import compress
def help():
    try:
        compress(["foo"],1,help=True)
        assert False
    except BaseException as e:
        text = str(e)
    return text.split("OPTIONS:\n",1)[1]

text = help()

entries = text.split("\n\n")


# We want each entry to look like this:
"""
* - ``abstraction_prefix``
        - ``str``
        - ``"fn_"``
        - Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem 
          Lorem i
"""

import re

indent = ' '*8

print(f"""
.. list-table::
{indent}:header-rows: 1
{indent}:widths: 30 70

{indent}* - Argument
{indent}  - Description""")

for entry in entries:
    lines = [l.strip() for l in entry.split('\n') if l.strip() != '']
    # --no-top-lambda becomes no_top_lambda
    arg = re.search(r'--((-|\w)+)', lines[0]).group(1).replace('-','_')
    takes_val = re.search(r'<(\w+)>', lines[0]) is not None
    val = ' <val>' if takes_val else ''
    print(f"{indent}* - ``{arg}{val}``")
    print(f"{indent}  - ", end="")

    lines = lines[1:]
    lines = [l.replace("`","``").replace('fn_]','fn\_]') for l in lines]

    if len(lines) > 0:
        print(f"{lines[0]}")
    for line in lines[1:]:
        print(f"{indent}    {line}")


