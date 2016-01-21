# create virtual environment
.env:
	virtualenv .env -p python2.7

# install all needed for development
develop: .env
	.env/bin/pip install -r requirements-dev.txt tox

test: develop
	.env/bin/py.test

# clean the development envrironment
clean:
	-rm -rf .env
