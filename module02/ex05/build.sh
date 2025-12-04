#!/bin/bash

# create dist folder cleanly
rm -rf dist
mkdir -p dist

# ensure build tools are up to date
# pip install --upgrade pip setuptools wheel build
pip install build
# build
# build the package
python -m build

# move results into dist/
mv ./dist/*.whl ./dist/*.tar.gz dist/ > /dev/null 2>&1 || true
