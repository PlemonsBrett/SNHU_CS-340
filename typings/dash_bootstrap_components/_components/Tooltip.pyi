"""
This type stub file was generated by pyright.
"""

import typing
import numbers
from typing_extensions import Literal, NotRequired, TypedDict
from dash.development.base_component import Component, ComponentType, _explicitize_args

class Tooltip(Component):
    """A Tooltip component.
A component for adding tooltips to any element, no callbacks required!

Simply add the Tooltip to you layout, and give it a target (id of a
component to which the tooltip should be attached)

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this Tooltip.

- id (string; optional):
    The ID of the Tooltip.

- target (string | dict; optional):
    The id of the element to attach the tooltip to.

- is_open (boolean; optional):
    Whether the Tooltip is open or not.

- trigger (string; default 'hover focus'):
    Space separated list of triggers (e.g. \"click hover focus
    legacy\"). These specify ways in which the target component can
    toggle the tooltip. If omitted you must toggle the tooltip
    yourself using callbacks. Options are: - \"click\": toggles the
    popover when the target is clicked. - \"hover\": toggles the
    popover when the target is hovered over with the cursor. -
    \"focus\": toggles the popover when the target receives focus -
    \"legacy\": toggles the popover when the target is clicked, but
    will also dismiss the popover when the user clicks outside of the
    popover.  Default is \"hover focus\".

- placement (a value equal to: 'auto', 'auto-start', 'auto-end', 'top', 'top-start', 'top-end', 'right', 'right-start', 'right-end', 'bottom', 'bottom-start', 'bottom-end', 'left', 'left-start', 'left-end'; default 'auto'):
    How to place the tooltip.

- delay (dict; default {show: 0, hide: 50}):
    Control the delay of hide and show events.

    `delay` is a dict with keys:

    - show (number; optional)

    - hide (number; optional)

- flip (boolean; default True):
    Whether to flip the direction of the popover if too close to the
    container edge, default True.

- autohide (boolean; default True):
    Optionally hide tooltip when hovering over tooltip content -
    default True.

- fade (boolean; default True):
    If True, a fade animation will be applied when `is_open` is
    toggled. If False the Alert will simply appear and disappear.

- class_name (string; optional):
    Additional CSS classes to apply to the Tooltip.

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components  See
    https://react.dev/learn/rendering-lists#why-does-react-need-keys
    for more info.

- className (string; optional):
    **DEPRECATED** Use `class_name` instead.  Additional CSS classes
    to apply to the Tooltip."""
    _children_props = ...
    _base_nodes = ...
    _namespace = ...
    _type = ...
    Delay = TypedDict("Delay", { "show": NotRequired[typing.Union[int, float, numbers.Number]],"hide": NotRequired[typing.Union[int, float, numbers.Number]] })
    @_explicitize_args
    def __init__(self, children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = ..., id: typing.Optional[typing.Union[str, dict]] = ..., *, target: typing.Optional[typing.Union[str, dict]] = ..., is_open: typing.Optional[bool] = ..., trigger: typing.Optional[str] = ..., placement: typing.Optional[Literal["auto", "auto-start", "auto-end", "top", "top-start", "top-end", "right", "right-start", "right-end", "bottom", "bottom-start", "bottom-end", "left", "left-start", "left-end"]] = ..., delay: typing.Optional[Delay] = ..., flip: typing.Optional[bool] = ..., autohide: typing.Optional[bool] = ..., fade: typing.Optional[bool] = ..., style: typing.Optional[typing.Any] = ..., class_name: typing.Optional[str] = ..., key: typing.Optional[str] = ..., className: typing.Optional[str] = ..., **kwargs) -> None:
        ...
    


