import argparse

from treeify.options import Options
from treeify.parse import parse
from treeify.generate import generate

def main():
    parser = argparse.ArgumentParser(description='Generates ASCII/Unicode trees')
    parser.add_argument('--ascii', action='store_true', help='Use ASCII characters only')
    parser.add_argument('--spaces', type=int, default=1, help='Number of spaces before each label')
    parser.add_argument('expr', type=str, help='The parenthesized tree expression')

    args = parser.parse_args()
    opts = Options(
        ascii_only=args.ascii,
        spaces=args.spaces
    )

    node = parse(args.expr)
    generated = generate(node, opts)

    print(generated)
