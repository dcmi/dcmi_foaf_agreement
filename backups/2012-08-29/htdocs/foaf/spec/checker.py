#!/usr/bin/env python

from rdflib.graph import ConjunctiveGraph
import re
g = ConjunctiveGraph("Sleepycat")
g.open("_tmpdb", create=True)
#g.parse("index.html", format='rdfa', lax=True)
#g.parse("index.rdf" )
q1 = 'SELECT distinct ?x FROM <file:index.rdf> WHERE { ?x <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>     <http://xmlns.com/foaf/0.1/> } ORDER BY ?x'
#q1 = 'SELECT distinct ?x ?src FROM <file:index.rdf> WHERE { GRAPH ?src { ?x <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>     <http://xmlns.com/foaf/0.1/> } } ORDER BY ?x'
i = 1
for x in  g.query(q1):
#    print  "[" , i,  "] src ", src, " - ", x
    i = i + 1
    regexp = re.compile( "^(.*/0.1/)\s*(.*)$" )
    rez = regexp.search( x )
    if rez == None:
      print "Failed to parse ",x
    else:
      term = rez.group(2)
      print "Redirect 303 /foaf/0.1/"+term+" http://xmlns.com/foaf/spec/"
g.close()
