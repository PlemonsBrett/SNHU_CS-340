"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class ErrorY(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def array(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the data corresponding the length of each error bar.
        Values are plotted relative to the underlying data.

        The 'array' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @array.setter
    def array(self, val): # -> None:
        ...
    
    @property
    def arrayminus(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the data corresponding the length of each error bar in the
        bottom (left) direction for vertical (horizontal) bars Values
        are plotted relative to the underlying data.

        The 'arrayminus' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @arrayminus.setter
    def arrayminus(self, val): # -> None:
        ...
    
    @property
    def arrayminussrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for
        `arrayminus`.

        The 'arrayminussrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @arrayminussrc.setter
    def arrayminussrc(self, val): # -> None:
        ...
    
    @property
    def arraysrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `array`.

        The 'arraysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @arraysrc.setter
    def arraysrc(self, val): # -> None:
        ...
    
    @property
    def color(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the stroke color of the error bars.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        ...
    
    @color.setter
    def color(self, val): # -> None:
        ...
    
    @property
    def symmetric(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines whether or not the error bars have the same length
        in both direction (top/bottom for vertical bars, left/right for
        horizontal bars.

        The 'symmetric' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @symmetric.setter
    def symmetric(self, val): # -> None:
        ...
    
    @property
    def thickness(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the thickness (in px) of the error bars.

        The 'thickness' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @thickness.setter
    def thickness(self, val): # -> None:
        ...
    
    @property
    def traceref(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'traceref' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        ...
    
    @traceref.setter
    def traceref(self, val): # -> None:
        ...
    
    @property
    def tracerefminus(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'tracerefminus' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        ...
    
    @tracerefminus.setter
    def tracerefminus(self, val): # -> None:
        ...
    
    @property
    def type(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines the rule used to generate the error bars. If
        *constant`, the bar lengths are of a constant value. Set this
        constant in `value`. If "percent", the bar lengths correspond
        to a percentage of underlying data. Set this percentage in
        `value`. If "sqrt", the bar lengths correspond to the square of
        the underlying data. If "data", the bar lengths are set with
        data set `array`.

        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['percent', 'constant', 'sqrt', 'data']

        Returns
        -------
        Any
        """
        ...
    
    @type.setter
    def type(self, val): # -> None:
        ...
    
    @property
    def value(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the value of either the percentage (if `type` is set to
        "percent") or the constant (if `type` is set to "constant")
        corresponding to the lengths of the error bars.

        The 'value' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @value.setter
    def value(self, val): # -> None:
        ...
    
    @property
    def valueminus(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the value of either the percentage (if `type` is set to
        "percent") or the constant (if `type` is set to "constant")
        corresponding to the lengths of the error bars in the bottom
        (left) direction for vertical (horizontal) bars

        The 'valueminus' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @valueminus.setter
    def valueminus(self, val): # -> None:
        ...
    
    @property
    def visible(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines whether or not this set of error bars is visible.

        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @visible.setter
    def visible(self, val): # -> None:
        ...
    
    @property
    def width(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the width (in px) of the cross-bar at both ends of the
        error bars.

        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @width.setter
    def width(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., array=..., arrayminus=..., arrayminussrc=..., arraysrc=..., color=..., symmetric=..., thickness=..., traceref=..., tracerefminus=..., type=..., value=..., valueminus=..., visible=..., width=..., **kwargs) -> None:
        """
        Construct a new ErrorY object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.bar.ErrorY`
        array
            Sets the data corresponding the length of each error
            bar. Values are plotted relative to the underlying
            data.
        arrayminus
            Sets the data corresponding the length of each error
            bar in the bottom (left) direction for vertical
            (horizontal) bars Values are plotted relative to the
            underlying data.
        arrayminussrc
            Sets the source reference on Chart Studio Cloud for
            `arrayminus`.
        arraysrc
            Sets the source reference on Chart Studio Cloud for
            `array`.
        color
            Sets the stroke color of the error bars.
        symmetric
            Determines whether or not the error bars have the same
            length in both direction (top/bottom for vertical bars,
            left/right for horizontal bars.
        thickness
            Sets the thickness (in px) of the error bars.
        traceref

        tracerefminus

        type
            Determines the rule used to generate the error bars. If
            *constant`, the bar lengths are of a constant value.
            Set this constant in `value`. If "percent", the bar
            lengths correspond to a percentage of underlying data.
            Set this percentage in `value`. If "sqrt", the bar
            lengths correspond to the square of the underlying
            data. If "data", the bar lengths are set with data set
            `array`.
        value
            Sets the value of either the percentage (if `type` is
            set to "percent") or the constant (if `type` is set to
            "constant") corresponding to the lengths of the error
            bars.
        valueminus
            Sets the value of either the percentage (if `type` is
            set to "percent") or the constant (if `type` is set to
            "constant") corresponding to the lengths of the error
            bars in the bottom (left) direction for vertical
            (horizontal) bars
        visible
            Determines whether or not this set of error bars is
            visible.
        width
            Sets the width (in px) of the cross-bar at both ends of
            the error bars.

        Returns
        -------
        ErrorY
        """
        ...
    


