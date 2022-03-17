#!/usr/bin/env just --justfile
# ^ A shebang isn't required, but allows a justfile to be executed
#   like a script, with `./justfile test`, for example.


default:
  @just -l

setuptest directory="/tmp/venv":
  #!/usr/bin/env sh
  python -m venv "{{directory}}"
  "{{directory}}/bin/pip3" install -e .
  echo "use: source {{directory}}/bin/active to test with python"


setuptest-dev directory="/tmp/venv":
  #!/usr/bin/env sh
  python -m venv "{{directory}}"
  "{{directory}}/bin/pip3" install -e .
  "{{directory}}/bin/pip3" install -r requirements-dev.txt
  "{{directory}}/bin/pip3" install -r requirements-flake8.txt
  echo "use: source {{directory}}/bin/active to test with python"

githook:
  #!/usr/bin/env sh
  echo -e "#\!/bin/bash\n\ntox\ntox -e flake8" >.git/hooks/pre-commit
  chmod a+x .git/hooks/pre-commit

flake8:
  @tox -e flake8

coverage:
  @tox -e coverage

# clean some work directories
clean:
  rm -rf .tox

# build python package
build:
  #!/usr/bin/env sh
  export PKG_NAME="$(python setup.py --name)"
  export PKG_VERSION="$(python setup.py --version)"
  export PKG_FILE="dist/${PKG_NAME}-${PKG_VERSION}.tar.gz"
  echo ">>$PKG_FILE<<"
  if test -f "$PKG_FILE"; then
   echo "$PKG_FILE allready exists..."
   exit 1
  fi

  echo "continue"
  if ! tox -p; then
    echo "tox error."
    exit 1
  fi

  python setup.py sdist

# publish package to pypi (build first)
publish:
  #!/usr/bin/env sh
  export PKG_NAME="$(python setup.py --name)"
  export PKG_VERSION="$(python setup.py --version)"
  export PKG_FILE="dist/${PKG_NAME}-${PKG_VERSION}.tar.gz"
  twine upload "$PKG_FILE"
  # twine upload dist/*

pytest-failure:
  tox -e py310 -- --lf --trace

