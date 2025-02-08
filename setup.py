from setuptools import setup, find_packages

setup(
  name="zTimer",
  version="0.1.0",
  description="A stopwatch app powered by Textual",
  author="Zedr0",
  # package_dir={"": "app"},
  # packages=find_packages(include=["app.*"]),
  # include_package_data=True,
  scripts=[
    "scripts/build.sh",
    "scripts/run.sh",
  ],
  install_requires=[
    "setuptools",
    "textual-dev",
  ],
  extras_require={
    "dev": ["debugpy", "ruff"],
  },
)
