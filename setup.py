from pathlib import Path
from setuptools import setup, find_packages

readme = Path(__file__).resolve().parent.joinpath("README.md").read_text()

setup(
    name="molesq",
    url="https://github.com/clbarnes/molesq",
    author="Chris L. Barnes",
    description=(
        "Implementation of moving least squares for ND point and image deformation"
    ),
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["molesq"]),
    install_requires=[
        "numpy>=1.20",
        "scipy",
        # "backports.strenum; python_version < '3.10'"
    ],
    test_requires=["pytest", "pytest-benchmark"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8, <4.0",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
)
