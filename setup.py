from setuptools import setup, find_packages

setup(
    name='mdisk',
    version='0.0.1',
    description='Unofficial python api wrapper from https://mdisk.me',
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    keywords="api mdisk video hosting unlimited",
    url='https://github.com/HeimanPictures/mdisk',
    author='Akkil',
    author_email='heimanpicturesofficial@gmail.com',
    packages=['mdisk'],
    install_requires=[
          'requests',
          'click',
      ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent"
      ],
    entry_points = {
        'console_scripts': ['mdisk=mdisk.mdisk:main'],
    },
    zip_safe=False
)
