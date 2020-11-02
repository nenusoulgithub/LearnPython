import argparse

parse = argparse.ArgumentParser()

# parse.add_argument("-n", "-name", type=str, help="请输入你的名字")
# parse.add_argument("-a", "-age", type=int, help="请输入你的年龄")

args = parse.parse_args()

print(args)