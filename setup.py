from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

extras = {}
extras["testing"] = ["pytest", "pytest-xdist", "timeout-decorator", "psutil"]
extras["quality"] = ["black >= 20.8b1", "isort >= 5", "flake8"]
extras["dev"] = extras["testing"] + extras["quality"]

setup(
    name="onnx_transformers",
    version="0.1.0",
    description="Accelerated nlp pipelines using Transformers and ONNX Runtime",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Suraj Patil",
    author_email="surajp815@gmail.com",
    packages=find_packages(),
    keywords =["ONNX", "onnxruntime", "NLP", "transformer", "transformers", "inference", "fast inference",],
    license="Apache",
    url="https://github.com/patil-suraj/onnx_transformers",
    install_requires=[
        "onnxruntime>=1.4.0",
        "transformers>=3.1.0",
        "psutil",
    ],
    extras_require=extras,
    python_requires=">=3.6.0",
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    project_urls={
        'Documentation': "https://github.com/patil-suraj/onnx_transformers",
        'Source': "https://github.com/patil-suraj/onnx_transformers",
    },
)