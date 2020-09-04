.PHONY: quality style test test-examples docs

# Check that source code meets quality standards

quality:
	black --check --line-length 119 --target-version py35 tests onnx_transformers
	isort --check-only tests onnx_transformers
	flake8 tests onnx_transformers

# Format source code automatically

style:
	black --line-length 119 --target-version py35 tests onnx_transformers
	isort tests onnx_transformers

# Run tests for the library

test:
	python -m pytest -n auto --dist=loadfile -s -v ./tests/