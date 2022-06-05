import argparse

from treeify.options import Options
from treeify.parse import parse
from treeify.generate import generate

def main():
    parser = argparse.ArgumentParser(description='Generates ASCII/Unicode trees')
    parser.add_argument('--ascii', action='store_true', help='Use ASCII characters only')
    parser.add_argument('--no-space', action='store_true', help='Omits the space before printed nodes')
    parser.add_argument('expr', type=str, help='The parenthesized tree expression')

    args = parser.parse_args()
    opts = Options(
        ascii_only=args.ascii,
        no_space=args.no_space
    )

    node = parse(args.expr)
    generated = generate(node, opts)

    print(generated)
