from setuptools import setup
import os

name = 'mailjet-apiv3-python-stubs'
description = 'MAilJet stubs and mypy plugin'

install_instructions = """\
# Experimental MAilJet type stubs and mypy plugin
This package contains type stubs and mypy plugin to provide more precise
static types and type inference for the MailJet API. 
## Installation
```
pip install mailjet-apiv3-python-stubs
```
Important: you need to enable the plugin in your mypy config file:
```
[mypy]
plugins = mailjetmypy
```
"""


def find_stub_files():
    result = []
    for root, dirs, files in os.walk(name):
        for file in files:
            if file.endswith('.pyi'):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result


setup(name='mailjet-apiv3-python-stubs',
      version='0.1',
      description=description,
      long_description=install_instructions,
      long_description_content_type='text/markdown',
      author='Erik Williamson',
      author_email='erik@techsanity.ca',
      license='GPLv3 License',
      url="https://github.com/erik-at-techsanity/mailjet-apiv3-python-stubs",
      py_modules=['sqlmypy', 'sqltyping'],
      install_requires=[
          'mypy>=0.790'
      ],
      packages=['mailjet-apiv3-python-stubs'],
      package_data={'mailjet-apiv3-python-stubs': find_stub_files()},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3'
      ]
)