install:
	uv	sync

build:
	uv	build 

package-install:
	uv tool install --force dist/hexlet_code-0.3.0-py3-none-any.whl	

lint-fix:
	uv	run	ruff	check	--fix	.

check:	lint	test

lint:
	uv	run	ruff	check	.

test:
	uv	run	pytest	--maxfail=1	--disable-warnings	-q

test-coverage:
	uv	run	pytest	--maxfail=1	--disable-warnings	-q	--cov=gendiff	--cov-report=xml

.PHONY:	lint	install	build	package-install	lint-fix