"""
This type stub file was generated by pyright.
"""

import typing
import numbers
from typing_extensions import Literal
from dash.development.base_component import Component, ComponentType, _explicitize_args

class Tabs(Component):
    """A Tabs component.
Create Bootstrap styled tabs. Use the `active_tab` property to set, or get the
currently active tab in a callback.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this Tabs component. Each child should be a Tab
    component.

- id (string; optional):
    The ID of the Tabs.

- active_tab (string; optional):
    The tab_id of the currently active tab. If tab_id has not been
    specified for the active tab, this will default to tab-i, where i
    is the index (starting from 0) of the tab.

- class_name (string; optional):
    Additional CSS classes to apply to the Tabs.

- persistence (boolean | string | number; optional):
    Used to allow user interactions to be persisted when the page is
    refreshed. See https://dash.plotly.com/persistence for more
    details.

- persisted_props (list of a value equal to: 'active_tab's; optional):
    Properties whose user interactions will persist after refreshing
    the component or the page. Since only `active_tab` is allowed this
    prop can normally be ignored.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Where persisted user changes will be stored: - memory: only kept
    in memory, reset on page refresh. - local: window.localStorage,
    data is kept after the browser quit. - session:
    window.sessionStorage, data is cleared once the browser quit.

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components  See
    https://react.dev/learn/rendering-lists#why-does-react-need-keys
    for more info.

- className (string; optional):
    **DEPRECATED** Use `class_name` instead.  Additional CSS classes
    to apply to the Tabs."""
    _children_props = ...
    _base_nodes = ...
    _namespace = ...
    _type = ...
    @_explicitize_args
    def __init__(self, children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = ..., id: typing.Optional[typing.Union[str, dict]] = ..., *, active_tab: typing.Optional[str] = ..., style: typing.Optional[typing.Any] = ..., class_name: typing.Optional[str] = ..., persistence: typing.Optional[typing.Union[bool, str, typing.Union[int, float, numbers.Number]]] = ..., persisted_props: typing.Optional[typing.Sequence[Literal["active_tab"]]] = ..., persistence_type: typing.Optional[Literal["local", "session", "memory"]] = ..., key: typing.Optional[str] = ..., className: typing.Optional[str] = ..., **kwargs) -> None:
        ...
    


