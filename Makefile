.PHONY: wheel clean


wheel: dist
	pip wheel --no-deps -w dist .

dist:
	mkdir -p dist

clean:
	rm -rf dist/*
