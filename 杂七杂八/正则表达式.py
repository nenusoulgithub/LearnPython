import re

if __name__ == '__main__':
    rel = re.findall('\d', "jsdf7s8d7f8sgsad76asdf3" * 100)
    print(rel)

    items = re.finditer('\d', "jsdf7s8d7f8sgsad76asdf3" * 100)
    for item in items:
        print(item.group())


