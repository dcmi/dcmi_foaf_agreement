import sys
import re
import urllib
import RDF


foaf = RDF.NS("http://xmlns.com/foaf/0.1/")
dc = RDF.NS('http://purl.org/dc/elements/1.1/')
rdf = RDF.NS('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
rdfs = RDF.NS('http://www.w3.org/2000/01/rdf-schema#')
owl = RDF.NS('http://www.w3.org/2002/07/owl#')
vs = RDF.NS('http://www.w3.org/2003/06/sw-vocab-status/ns#')

classranges = {}
classdomains = {}

def termlink(string):
    """FOAF specific: function which replaces <code>foaf:*</code> with a 
    link to the term in the document."""
    return re.sub(r"<code>foaf:(\w+)</code>", r"""<code><a href="#term_\1">foaf:\1</a></code>""", string)    

def return_name(m, urinode):
    "Trims the FOAF namespace out of a term to give a name to the term."
    return str(urinode.uri).replace("http://xmlns.com/foaf/0.1/", "")

def get_rdfs(m, urinode):
    "Returns label and comment given an RDF.Node with a URI in it"
    l = m.find_statements(RDF.Statement(urinode, rdfs.label, None))
    label = l.current().object.literal_value['string']
    c = m.find_statements(RDF.Statement(urinode, rdfs.comment, None))
    comment = c.current().object.literal_value['string']
    return label, comment

def get_status(m, urinode):
    "Returns the status text for a term."
    s = m.find_statements(RDF.Statement(urinode, vs.term_status, None))
    return s.current().object.literal_value['string']

def htmlDocInfo( t, termdir="../doc" ):
    """Opens a file based on the term name (t) and termdir (defaults to 
    current directory. Reads in the file, and returns a linkified 
    version of it."""
    doc = ""
    try:
        f = open("%s/%s.en" % (termdir, t), "r")
        doc = f.read()
        doc = termlink(doc)
    except:
        return "<p>No detailed documentation for this term.</p>"
    return doc

def rdfsPropertyInfo(term,m):
    """Generate HTML for properties: Domain, range, status."""
    doc = ""
    range = ""
    domain = ""
    # domain and range stuff (properties only)
    d = m.find_statements(RDF.Statement(term, rdfs.domain, None))
    if d.current():
        domain = d.current().object.uri
        domain = str(domain)
    else:
        domain = ""
    r = m.find_statements(RDF.Statement(term, rdfs.range, None))
    if r.current():
        range = r.current().object.uri
        range = str(range)
    if domain:
        if ("http://xmlns.com/foaf/0.1/" in domain):
            domain = domain.replace("http://xmlns.com/foaf/0.1/", "")
            domain = """<a href="#term_%s">foaf:%s</a>""" % (domain, domain)
        doc += "\t<tr><th>Domain:</th>\n\t<td>%s</td></tr>\n" % domain
    
    if range:
        if ("http://xmlns.com/foaf/0.1/" in range):
            range = range.replace("http://xmlns.com/foaf/0.1/", "")
            range = """<a href="#term_%s">foaf:%s</a>""" % (range, range)
        doc += "\t<tr><th>Range:</th>\n\t<td>%s</td></tr>\n" % range
    return doc

def rdfsClassInfo(term,m):
    """Generate rdfs-type information for Classes: ranges, and domains."""
    global classranges
    global classdomains
    doc = ""
    # Find out about properties which have rdfs:range of t
    r = classranges.get(str(term.uri), "")
    if r:
      rlist = ''
      for k in r:
        kname = k
        if ("http://xmlns.com/foaf/0.1/" in k):
            k = k.replace("http://xmlns.com/foaf/0.1/", "")
            k = """<a href="#term_%s">foaf:%s</a>""" % (k, k)
        rlist += "%s " % k
      doc += "<tr><th>in-range-of:</th><td>"+rlist+"</td></tr>"
    
    # Find out about properties which have rdfs:domain of t
    d = classdomains.get(str(term.uri), "")
    if d:
      dlist = ''
      for k in d:
        kname = k
        if ("http://xmlns.com/foaf/0.1/" in k):
            k = k.replace("http://xmlns.com/foaf/0.1/", "")
            k = """<a href="#term_%s">foaf:%s</a>""" % (k, k)
        dlist += "%s " % k
      doc += "<tr><th>in-domain-of:</th><td>"+dlist+"</td></tr>"

    return doc

def owlInfo(term,m):
    """Returns an extra table row if the term (an RDF.Node()) is an IFP."""
    o = m.find_statements(RDF.Statement(term, rdf.type, owl.InverseFunctionalProperty))
    if o.current():
        return("\t<tr><th>OWL Type:</th>\n\t<td>An InverseFunctionalProperty (uniquely identifying property)</td></tr>\n")
    return ''

def docTerms(category, list, m):
    """A wrapper class for listing all the terms in a specific class (either
    Properties, or Classes. Category is 'Property' or 'Class', list is a 
    list of term names (strings), return value is a chunk of HTML."""
    doc = ""
    nspre = "foaf"
    for t in list:
        term = foaf[t]
        doc += """<br /><div class="specterm" id="term_%s">\n<h3>%s: %s:%s</h3>\n""" % (t, category, nspre, t)
        label, comment = get_rdfs(m, term)    
        status = get_status(m, term)
        doc += "<em>%s</em> - %s <br />" % (label, comment)
        doc += """<table>\n\t<tr><th>Status:</th>\n\t<td>%s</td></tr>\n""" % status
        doc += owlInfo(term,m)
        if category=='Property': doc += rdfsPropertyInfo(term,m)
        if category=='Class': doc += rdfsClassInfo(term,m)
        doc += "</table>\n"
        doc += htmlDocInfo(t)
#danbri
        doc += "<p style=\"float: right; font-size: small;\">[<a href=\"#term_%s\">#</a>]</p>\n\n" % (return_name(m,term))
        doc += "<p style=\"float: right; font-size: small;\">[<a href=\"#glance\">back to top</a>]</p>\n\n"
        doc += "\n<br/>\n</div>\n\n"
    return doc

def buildazlist(classlist, proplist):
    """Builds the A-Z list of terms. Args are a list of classes (strings) and 
    a list of props (strings)"""
    azlist = """<div style="padding: 5px; border: solid; background-color: #ddd;">"""
    azlist = """%s\n<p>Classes: |""" % azlist
    classlist.sort()
    for c in classlist:
        azlist = """%s <a href="#term_%s">%s</a> | """ % (azlist, c.replace(" ", ""), c)
    azlist = """%s\n</p>""" % azlist
    azlist = """%s\n<p>Properties: |""" % azlist
    proplist.sort()
    for p in proplist:
        azlist = """%s <a href="#term_%s">%s</a> | """ % (azlist, p.replace(" ", ""), p)
    azlist = """%s\n</p>""" % azlist
    azlist = """%s\n</div>""" % azlist
    return azlist
def specInformation(m):
    """Read through the spec (provided as a Redland model) and return classlist
    and proplist. Global variables classranges and classdomains are also filled
    as appropriate."""
    global classranges
    global classdomains

    # Find the class information: Ranges, domains, and list of all names.
    classlist = []
    for classStatement in  m.find_statements(RDF.Statement(None, rdf.type, rdfs.Class)):
        for range in m.find_statements(RDF.Statement(None, rdfs.range, classStatement.subject)):
            classranges.setdefault(str(classStatement.subject.uri), []).append(str(range.subject.uri))
        for domain in m.find_statements(RDF.Statement(None, rdfs.domain, classStatement.subject)):
            classdomains.setdefault(str(classStatement.subject.uri), []).append(str(domain.subject.uri))
        classlist.append(return_name(m, classStatement.subject))

    # Create a list of properties in the schema.
    proplist = []
    for propertyStatement in  m.find_statements(RDF.Statement(None, rdf.type, rdf.Property)):
        proplist.append(return_name(m, propertyStatement.subject))
    return classlist, proplist
    
def main(specloc = "file:index.rdf"):
    """The meat and potatoes: Everything starts here."""
    m = RDF.Model()
    p = RDF.Parser()
    p.parse_into_model(m, specloc)
    
    classlist, proplist = specInformation(m)
    
    # Build HTML list of terms.
    azlist = buildazlist(classlist, proplist)

    # Generate Term HTML
    termlist = "<h3>Classes and Properties (full detail)</h3>"
    termlist += "<div class='termdetails'>"
    termlist += docTerms('Class',classlist,m)
    termlist += docTerms('Property',proplist,m)
    termlist += "</div>"

    # Generate RDF from original namespace.
    u = urllib.urlopen(specloc)
    rdfdata = u.read()
    rdfdata.replace("""<?xml version="1.0"?>""", "")
    
    # wip.template is a template file for the spec, python-style % escapes
    # for replaced sections.
    f = open("../0.1/template.html", "r")
    template = f.read()
    print template % (azlist.encode("utf-8"), termlist.encode("utf-8"), rdfdata)
    
if __name__ == "__main__":
    """Specification generator tool, created for FOAF schema maintenance."""
    if (len(sys.argv) >= 2):
        main(sys.argv[1])
    else:
        main()
