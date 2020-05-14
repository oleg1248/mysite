import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-auto-rest", # Replace with your own username
    version="0.0.0",
    author="olegkishenkov",
    author_email="oleg1248163264@gmail.com",
    description="an automatic REST API for all the models in a Django project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/olegkishenkov/mysite/tree/release-onthefly",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)