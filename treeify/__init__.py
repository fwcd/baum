import argparse

from treeify.parse import parse_expr
from treeify.generate import generate_tree

def main():
    parser = argparse.ArgumentParser(description='Generates ASCII/Unicode trees')
    parser.add_argument('--ascii', action='store_true', help='Use ASCII characters only')
    parser.add_argument('expr', type=str, help='The parenthesized tree expression')

    args = parser.parse_args()

    node = parse_expr(args.expr)
    generated = generate_tree(node, ascii_only=args.ascii)

    print(generated)
