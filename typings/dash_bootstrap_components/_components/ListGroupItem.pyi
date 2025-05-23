"""
This type stub file was generated by pyright.
"""

import typing
import numbers
from dash.development.base_component import Component, ComponentType, _explicitize_args

class ListGroupItem(Component):
    """A ListGroupItem component.
Create a single item in a `ListGroup`.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this ListGroupItem.

- id (string; optional):
    The ID of the ListGroupItem.

- n_clicks (number; default 0):
    The number of times the ListGroupItem has been clicked.

- class_name (string; optional):
    Additional CSS classes to apply to the ListGroupItem.

- tag (string; optional):
    HTML tag to use for the ListGroupItem, default: li.

- active (boolean; optional):
    Set to True to apply the \"active\" style to this item.

- disabled (boolean; optional):
    If True, the item will be disabled.

- color (string; optional):
    Item color, options: primary, secondary, success, info, warning,
    danger, or any valid CSS color of your choice (e.g. a hex code, a
    decimal code or a CSS color name). Default: secondary.

- action (boolean; optional):
    Apply list-group-item-action class for hover animation etc.

- href (string; optional):
    Pass a URL (relative or absolute) to make the list group item a
    link.

- external_link (boolean; optional):
    If True, clicking on the ListGroupItem will behave like a
    hyperlink. If False, the ListGroupItem will behave like a dcc.Link
    component, and can be used in conjunction with dcc.Location for
    navigation within a Dash app.

- target (string; optional):
    Target attribute to pass on to the link. Only applies to external
    links.

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components  See
    https://react.dev/learn/rendering-lists#why-does-react-need-keys
    for more info.

- className (string; optional):
    **DEPRECATED** Use `class_name` instead.  Additional CSS classes
    to apply to the ListGroupItem."""
    _children_props = ...
    _base_nodes = ...
    _namespace = ...
    _type = ...
    @_explicitize_args
    def __init__(self, children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = ..., id: typing.Optional[typing.Union[str, dict]] = ..., *, n_clicks: typing.Optional[typing.Union[int, float, numbers.Number]] = ..., style: typing.Optional[typing.Any] = ..., class_name: typing.Optional[str] = ..., tag: typing.Optional[str] = ..., active: typing.Optional[bool] = ..., disabled: typing.Optional[bool] = ..., color: typing.Optional[str] = ..., action: typing.Optional[bool] = ..., href: typing.Optional[str] = ..., external_link: typing.Optional[bool] = ..., target: typing.Optional[str] = ..., key: typing.Optional[str] = ..., className: typing.Optional[str] = ..., **kwargs) -> None:
        ...
    


