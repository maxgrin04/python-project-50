install:
	uv	sync

build:
	uv	build 

package-install:
	uv tool install --force dist/hexlet_code-0.1.2-py3-none-any.whl	

lint:
	uv	run	ruff	check	.

lint-fix:
	uv	run	ruff	check	--fix	.

check:	lint	test

lint:
	ruff	check .

test:
	pytest	--maxfail=1	--disable-warnings	-q

test-coverage:
	pytest	--maxfail=1	--disable-warnings	-q	--cov=gendiff	--cov-report=xml

.PHONY:	lint	install	build	package-install	lint-fix