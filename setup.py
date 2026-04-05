from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.1.0",
    author="Deepin",
    author_email="deepin1506@gmail.com",
    install_requires=["openai", "langchain","streamlit", "python-dotenv","PyPDF2"],
    packages= find_packages()
)