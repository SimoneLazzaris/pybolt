.PHONY: wheel clean pypi-test pypi


wheel: dist
	pip wheel --no-deps -w dist .

dist:
	mkdir -p dist

clean:
	rm -rf dist/*

pypi-test: wheel
	python3 -m twine upload --repository testpypi dist/*

pypi: wheel
	python3 -m twine upload dist/*
