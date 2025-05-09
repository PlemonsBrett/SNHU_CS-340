"""
This type stub file was generated by pyright.
"""

import typing
from dash.development.base_component import Component, ComponentType, _explicitize_args

class ModalTitle(Component):
    """A ModalTitle component.
Add a title to any Modal. Should be used as a child of the ModalHeader.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this ModalTitle.

- id (string; optional):
    The ID of the ModalTitle.

- class_name (string; optional):
    Additional CSS classes to apply to the ModalTitle.

- tag (string; optional):
    HTML tag to use for the ModalTitle, default: div.

- className (string; optional):
    **DEPRECATED** Use `class_name` instead.  Additional CSS classes
    to apply to the ModalTitle."""
    _children_props = ...
    _base_nodes = ...
    _namespace = ...
    _type = ...
    @_explicitize_args
    def __init__(self, children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = ..., id: typing.Optional[typing.Union[str, dict]] = ..., *, style: typing.Optional[typing.Any] = ..., class_name: typing.Optional[str] = ..., tag: typing.Optional[str] = ..., className: typing.Optional[str] = ..., **kwargs) -> None:
        ...
    


