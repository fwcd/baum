import argparse

from treeify.parse import parse
from treeify.generate import generate

def main():
    parser = argparse.ArgumentParser(description='Generates ASCII/Unicode trees')
    parser.add_argument('--ascii', action='store_true', help='Use ASCII characters only')
    parser.add_argument('expr', type=str, help='The parenthesized tree expression')

    args = parser.parse_args()

    node = parse(args.expr)
    generated = generate(node, ascii_only=args.ascii)

    print(generated)
