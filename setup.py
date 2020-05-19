from setuptools import setup, find_packages
setup(
    include_package_data=True,
    name="KorApp",
    version="0.1",
    packages=find_packages(),
    scripts=["main.py"],
    package_data={
        "": ["*.ui", "*.png", ".jpeg"]
    },
    install_requires=["pyqt5","pyAesCrypt"],
    python_requires='>=3',
    author="Andrei Surugiu and Bogdan Caliman",
    description="Build package for Kor App",
    url="https://github.com/DeluxeOwl/KoR_app"
)
