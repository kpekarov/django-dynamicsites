from distutils.core import setup

setup(
    version='0.1',
    name='django_dynamicsites',
    description="Host multiple sites from a single django project",
    url='https://github.com/kpekarov/django-dynamicsites',
    platforms=['any'],
    package_dir={'django_dynamicsites': "dynamicsites"},
    packages=['django_dynamicsites'],
)
