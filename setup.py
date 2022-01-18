import setuptools


with open("README.md", "r") as fh:
    long_desc = fh.read()

setuptools.setup(
    name = "xless",
    version = 'v1.7',
    author = "Zhentian Kai",
    author_email = "zhentian.kai@outlook.com",
    packages = setuptools.find_packages(),
    license = 'MIT',
    description = 'Display excels directly on linux cmd line',
    long_description = long_desc,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ZKai0801/xless",
    install_requires = ['pandas', 'openpyxl'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux'
    ],
    scripts = ['xless'],
    python_requires = '>=3.5',
    keywords = ["less", "more", "pager", "excel"]
)

