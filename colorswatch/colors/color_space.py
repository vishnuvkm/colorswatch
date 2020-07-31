import matplotlib.colors as mcolors
from colour import Color


class ColorSpace:
    """
    Generic class to implement all color spaces
    """

    def __init__(self, color_space):
        self.color_space = color_space

    def get_components(self, color):
        if self.color_space == 'rgb':
            return self.get_rgb(color)
        if self.color_space == 'hsv':
            return self.get_hsv(color)

    def get_rgb(self, color):
        """
        Method to get rgb components
        :param color: Instance of colour.Color or color name from matplotlib.colors.cnames
        :return:
        """
        if isinstance(color, Color):
            convert_to_255 = [round(x * 255) for x in color.rgb]
        else:
            convert_to_255 = [round(x * 255) for x in mcolors.to_rgb(color)]
        return {
            "kind": self.color_space,
            "components": {
                "red": convert_to_255[0],
                "green": convert_to_255[1],
                "blue": convert_to_255[2]
            }
        }

    def get_hsv(self, color):
        """
        Method to get hsv components
        :param color: Instance of colour.Color or color name from matplotlib.colors.cnames
        :return:
        """
        if isinstance(color, Color):
            hsv = mcolors.rgb_to_hsv(color.rgb)
        else:
            hsv = mcolors.rgb_to_hsv(mcolors.to_rgb(color))
        return {
            "kind": self.color_space,
            "components": {
                "hue": hsv[0],
                "saturation": hsv[1],
                "value": hsv[2]
            }
        }
