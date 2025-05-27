from setuptools import setup

setup(
    name="autosort-organizer",
    version="1.0.0",
    py_modules=["autosort"],
    entry_points={"console_scripts": ["autosort = autosort:main"]},
    install_requires=[],  # Add if GUI or other dependencies are introduced
    author="Your Name",
    description="A tool to automatically sort files in a directory.",
    license="MIT",
)
