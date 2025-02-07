from setuptools import setup, find_packages

setup(
    name="macso1i",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "macso1i = macso1i.mac_changer:start"
        ]
    },
    include_package_data=True,
)
