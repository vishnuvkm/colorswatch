**Django color swatch server**

Color swatch server created using `django and django-rest-framework` to provide colors in variety of color spaces.
Each color space is generated using multiple generation strategies.

Color spaces currently supported:
- rgb
- hsv

Generation strategies supported:
- Constant, where a single color is returned for all entries in the swatch.
- Linear, where a starting color and an ending color are chosen, and all other entries in the swatch are linearly interpolated between those two colors.

Installation steps:
- Prerequisite
    - Python3
    - virtualenv
- `git clone https://github.com/vishnuvkm/colorswatch.git`
- `cd colorswatch`
- `virtualenv -p <python3 path> venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py runserver`
- open browser navigate to `http://127.0.0.1:8000/`
