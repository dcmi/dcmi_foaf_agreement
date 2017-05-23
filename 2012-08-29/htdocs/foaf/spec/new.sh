#!/bin/sh

echo 'Making new spec'

rm -f index.html
/usr/bin/python2.4 ../0.1/specgen.py file:index.rdf > index.html
