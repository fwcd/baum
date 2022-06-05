from dataclasses import dataclass

@dataclass
class Style:
    indent_prefix: str
    t_prefix: str
    last_prefix: str

STYLES = {
    'ascii': Style(indent_prefix='|', t_prefix='+', last_prefix='+'),
    'ascii2': Style(indent_prefix='|', t_prefix='+', last_prefix='\\'),
    'yaml': Style(indent_prefix='', t_prefix='-', last_prefix='-'),
    'unicode': Style(indent_prefix='│', t_prefix='├─', last_prefix='└─'),
}
