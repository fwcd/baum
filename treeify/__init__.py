import argparse

from treeify.options import Options
from treeify.parse import parse
from treeify.generate import generate
from treeify.style import STYLES

def main():
    parser = argparse.ArgumentParser(description='Generates ASCII/Unicode trees')
    parser.add_argument('--style', type=str, default='unicode', choices=sorted(STYLES.keys()), metavar='STYLE', help=f"The tree style (one of {', '.join(sorted(STYLES.keys()))})")
    parser.add_argument('--spaces', type=int, default=1, help='Number of spaces before each label')
    parser.add_argument('expr', type=str, help='The parenthesized tree expression')

    args = parser.parse_args()
    opts = Options(
        style=STYLES[args.style],
        spaces=args.spaces
    )

    node = parse(args.expr)
    generated = generate(node, opts)

    print(generated)
