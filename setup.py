# python setup.py build_ext -i
import numpy as np
from setuptools import Extension, setup
from Cython.Build import cythonize
import pathlib
import os.path
import os
from os import path

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

exec(open("plaster/version.py").read())

assert path.exists("./plaster_root")
plaster_root = "."

extensions = [
    Extension(
        "sim_v2",
        [f"{plaster_root}/plaster/run/sim_v2/csim_v2_fast.c"],
        include_dirs=[f"{plaster_root}/plaster/run/sim_v2", np.get_include()],
        extra_compile_args=[
            "-Wno-unused-but-set-variable",
            "-Wno-unused-label",
            "-Wno-cpp",
            "-pthread",
            "-DNDEBUG",
        ],
    )
]


setup(
    name="erisyon.plaster",
    version=__version__,
    description="Erisyon's Fluoro-Sequencing Platform",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/erisyon/plaster",
    author="Erisyon",
    author_email="plaster+pypi@erisyon.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["plaster"],
    include_package_data=True,
    install_requires=[
        "arrow",
        "bokeh",
        "cython",
        "ipython",
        "jupyter",
        "munch",
        "nbstripout",
        "nptyping",
        "numpy",
        "opencv-python",
        "pandas",
        "plumbum",
        "psf",
        "pudb",
        "pyyaml",
        "requests",
        "retrying",
        "scikit-image",
        "scikit-learn",
        "twine",
        "wheel",
        "zbs-zest",
    ],
    entry_points={"console_scripts": ["plaster=plaster.plaster_main:main",]},
    python_requires=">=3.6",
    ext_modules=cythonize(extensions, language_level="3"),
)
