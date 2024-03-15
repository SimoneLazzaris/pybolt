.PHONY: wheel


wheel: dist
	pip wheel --no-deps -w dist .

dist:
	mkdir -p dist
