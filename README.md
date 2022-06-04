# Treeify

A small Python script that generates a Unicode or ASCII tree from a parenthesized expression.

## Examples

```sh
treeify "this [is [an, example, tree], with [a, bunch, of, nodes]]"
```

```
this
├─is
│ ├─an
│ ├─example
│ └─tree
└─with
  ├─a
  ├─bunch
  ├─of
  └─nodes
```

Alternatively, the output can be configured to use ASCII characters only:

```sh
treeify --ascii "this [is [an, example, tree], with [a, bunch, of, nodes]]"
```

```
this
- is
  - an
  - example
  - tree
- with
  - a
  - bunch
  - of
  - nodes
```
