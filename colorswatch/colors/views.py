import random
from rest_framework import viewsets
from rest_framework.response import Response
from colour import Color
from matplotlib import colors

from .serializers import ColorSpaceSerializer
from .constants import AVAILABLE_COLOR_SPACES, DEFAULT_COLOR_SPACE
from .color_space import ColorSpace


class ConstantGenerationStrategy(viewsets.ViewSet):
    """
    Constant swatch generation strategy would return single color for all entries in the swatch
    All the entries in the color swatch(5 colors) are picked random from matplotlib.colors.cnames
    """

    def list(self, request):
        color_space = request.query_params.get('space', DEFAULT_COLOR_SPACE)
        if color_space and color_space not in AVAILABLE_COLOR_SPACES:
            raise NotImplementedError('Invalid color space')

        # Get all color names
        base_colors = colors.cnames.keys()
        # Choose 5 random colors form the list
        random_colors = random.choices(list(base_colors), k=5)

        response = []
        # Initialize ColorSpace with given color space
        color_space = ColorSpace(color_space)
        # Get the components given color space for all 5 colors
        for color in random_colors:
            response.append(color_space.get_components(color))

        results = ColorSpaceSerializer(response, many=True).data
        return Response(results)


class LinearGenerationStrategy(viewsets.ViewSet):
    """
    Linear generation strategy, where a starting color and an ending color are chosen,
    and all other entries in the swatch are linearly interpolated between those two colors
    Used https://pypi.org/project/colour/ to get the color range between two colors
    """

    def list(self, request):
        color_space = request.query_params.get('space', DEFAULT_COLOR_SPACE)
        if color_space and color_space not in AVAILABLE_COLOR_SPACES:
            raise NotImplementedError('Invalid color space')

        start_color = self.request.query_params.get('start_color', None)
        end_color = self.request.query_params.get('end_color', None)
        if not start_color or not end_color:
            raise Exception('start_color and end_color is required')

        # Get list of 5 colors ranging from starting to ending color
        color_range = list(Color(start_color).range_to(Color(end_color), 5))

        response = []
        # Initialize ColorSpace with given color space
        color_space = ColorSpace(color_space)
        # Get the components given color space for all 5 colors
        for color in color_range:
            response.append(color_space.get_components(color))

        results = ColorSpaceSerializer(response, many=True).data
        return Response(results)
