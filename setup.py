from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='<<[.cus.package.name.pypi]>>',
    version='<<[.cus.package.version]>>',
    description='<<[.cus.package.description]>>',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='<<[.cus.author.name]>>',
    author_email='<<[.cus.author.email]>>',
    url='https://github.com/<<[.cus.author.github]>>/<<[.cus.package.name.pypi]>>',
    license='GNU General Public License v2.0',
    packages=find_packages(exclude=('tests', 'docs'))
)
