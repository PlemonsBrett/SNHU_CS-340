"""
This type stub file was generated by pyright.
"""

import typing
from dash.development.base_component import Component, ComponentType, _explicitize_args

class InputGroup(Component):
    """An InputGroup component.
A component for grouping together inputs and buttons, dropdowns or text.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this InputGroup.

- id (string; optional):
    The ID of the InputGroup.

- size (string; optional):
    Set the size of the Input. Options: 'sm' (small), 'md' (medium) or
    'lg' (large). Default is 'md'.

- class_name (string; optional):
    Additional CSS classes to apply to the InputGroup.

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components  See
    https://react.dev/learn/rendering-lists#why-does-react-need-keys
    for more info.

- className (string; optional):
    **DEPRECATED** Use `class_name` instead.  Additional CSS classes
    to apply to the InputGroup."""
    _children_props = ...
    _base_nodes = ...
    _namespace = ...
    _type = ...
    @_explicitize_args
    def __init__(self, children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = ..., id: typing.Optional[typing.Union[str, dict]] = ..., *, size: typing.Optional[str] = ..., style: typing.Optional[typing.Any] = ..., class_name: typing.Optional[str] = ..., key: typing.Optional[str] = ..., className: typing.Optional[str] = ..., **kwargs) -> None:
        ...
    


