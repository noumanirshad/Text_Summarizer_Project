import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"



REPO_NAME = "Text_Summarizer_Project"
AUTHOR_USER_NAME = "noumanirshad"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "noumanirshad564@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author= AUTHOR_USER_NAME, 
    author_email= AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content= "text/markdown",
    url = f"https://github.com/noumanirshad/Text_Summarizer_Project",
    project_urls = {
        "Bug Tracker": f"https://github.com/noumanirshad/Text_Summarizer_Project/issues",
    },
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    license="MMIT License",
    include_package_data=True,
    # install_requires=get_requirements('requirements.txt'),
    zip_safe=False,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

