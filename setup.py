from setuptools import setup, find_packages

setup(
    name="late_show_api",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-migrate',
        'flask-jwt-extended', 
        'psycopg2-binary'
    ],
)