"""
This type stub file was generated by pyright.
"""

import typing
from dash.development.base_component import Component, ComponentType, _explicitize_args

class FormFloating(Component):
    """A FormFloating component.
A component for adding float labels to form controls in forms.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this FormFloating.

- id (string; optional):
    The ID of the FormFloating.

- html_for (string; optional):
    Set the `for` attribute of the label to bind it to a particular
    element.

- class_name (string; optional):
    Additional CSS classes to apply to the FormFloating.

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components  See
    https://react.dev/learn/rendering-lists#why-does-react-need-keys
    for more info.

- className (string; optional):
    **DEPRECATED** Use `class_name` instead.  Additional CSS classes
    to apply to the FormFloating."""
    _children_props = ...
    _base_nodes = ...
    _namespace = ...
    _type = ...
    @_explicitize_args
    def __init__(self, children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = ..., id: typing.Optional[typing.Union[str, dict]] = ..., *, html_for: typing.Optional[str] = ..., style: typing.Optional[typing.Any] = ..., class_name: typing.Optional[str] = ..., key: typing.Optional[str] = ..., className: typing.Optional[str] = ..., **kwargs) -> None:
        ...
    


