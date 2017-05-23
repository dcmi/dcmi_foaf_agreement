#!/bin/sh

echo 'Making new DRAFT spec, draft.html'

/usr/bin/python2.4 ../0.1/specgen.py file:index.rdf > draft.html
