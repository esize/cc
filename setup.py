from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="evan-cc",
    version="0.1.0",
    author="Evan Sizemore",
    author_email="evan@wool.homes",
    description="A Django project template with cookiecutter support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your-django-template",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "cookiecutter>=1.7.0",
    ],
    entry_points={
        "console_scripts": [
            "your-django-template=your_django_template.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
)
