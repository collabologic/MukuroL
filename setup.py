from setuptools import setup, find_packages
import os

this_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(this_directory, "requirements.txt"), encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="MukuroL",
    version="0.1.5",
    author="collabologic",
    author_email="",  # 必要に応じてメールアドレスを追加してください
    description="MukuroL is a lightweight markup language, designed exclusively for wireframe creation using simple code.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="",  # 必要に応じてプロジェクトのURLを追加してください
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'mkl = MukuroL.mkl:main',
        ],
    },
)