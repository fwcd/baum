# Treeify

[![Typecheck](https://github.com/fwcd/treeify/actions/workflows/typecheck.yml/badge.svg)](https://github.com/fwcd/treeify/actions/workflows/typecheck.yml)
[![Test](https://github.com/fwcd/treeify/actions/workflows/test.yml/badge.svg)](https://github.com/fwcd/treeify/actions/workflows/test.yml)

A small Python script that generates a Unicode or ASCII tree from a parenthesized expression.

## Examples

```sh
treeify "this [is [an, example, tree], with [a, bunch, of, nodes]]"
```

```
this
├─ is
│  ├─ an
│  ├─ example
│  └─ tree
└─ with
   ├─ a
   ├─ bunch
   ├─ of
   └─ nodes
```

In addition to the default style, which is `unicode`, a number of other styles are supported, which can be set via the `--style` flag, e.g.:

```sh
treeify --style ascii "this [is [an, example, tree], with [a, bunch, of, nodes]]"
```

```
this
+- is
|  +- an
|  +- example
|  \- tree
\- with
   +- a
   +- bunch
   +- of
   \- nodes
```

Or even emoji for visualizing file trees:

```sh
treeify --style emoji "this [is [an [], example [], tree []], with [a, bunch, of, nodes]]"
```

```
📁 this
  📁 is
    📁 an
    📁 example
    📁 tree
  📁 with
    📄 a
    📄 bunch
    📄 of
    📄 nodes
```

Run `treeify --help` for a complete overview.
