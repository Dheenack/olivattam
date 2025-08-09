from setuptools import setup,find_packages

with open("README.md","r+",encoding="utf-8") as f:
    long_description = f.read()
setup(
    name='Olivattam',
    version="0.0.3",
    description="A package for color extraction from image",
    packages=find_packages(),
    author="Dheena Krishna",
    author_email="dheenakrishna2020@gmail.com",
    maintainer="Dheena krishna",
    maintainer_email="dheenakrishna2020@gmail.com",
    install_requires=[
        "pillow>=7.0.0"
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)