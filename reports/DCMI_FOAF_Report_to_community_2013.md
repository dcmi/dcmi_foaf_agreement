---
title: Update 201308
date: '2017-09-01T16:21:09+01:00'
description: 
draft: false
creators: []
contributors: []
publisher: 
tags: []
aliases:
- "/collaborations/foaf/DCMI_FOAF_Cooperation/Update_201308.html"
---

## DCMI FOAF Agreement: August 2013 status update

Prepared by: Tom Baker and Dan Brickley
Published: 2013-08-29
See also: <a href="/collaborations/foaf/DCMI_FOAF_Cooperation/Update_201308/" class="external free" rel="nofollow">Update 2013 August</a> 

Context 

The DCMI FOAF Cooperation Task Group [1] is a result of the May 2011 Agreement
between DCMI and the FOAF Project [2]. The Task Group implements and monitors
the specific agreements [3] outlined in the DCMI FOAF Agreement.

Recent Developments

-- Tom and Dan met in September at DC-2012 [4] in Kuching.

-- As of October 1st 2012, Dan Brickley has been employed full-time at Google
    (UK). It is common for Google staff to contribute to external standards-related
    initiatives, his involvement with FOAF is expected to continue at current (ad
    hoc, occasional) level.

-- As of July 2013, DCMI has ceased operations as a company limited by
    guarantee in Singapore and currently operates as a project of ASIS&amp;T [5], the
    Association for Information Science and Technology. This change has no effect
    on DCMI's ongoing commitment to its agreement with the FOAF Project.

----------------------------------------------------------------------
"The FOAF Project will grant DCMI administrative and technical access to the domain xmlns.com."

-- Dan, Libby Miller, and Tom currently have the DNS password.

----------------------------------------------------------------------
"DCMI will monitor payment of domain name fees by the FOAF Project."

-- WHOIS (see also [6]):
 
    Domain Name: XMLNS.COM
    Registrar: GANDI SAS
    Whois Server: whois.gandi.net
    Referral URL: <a href="http://www.gandi.net" class="external free" rel="nofollow">http://www.gandi.net</a>
    Name Server: A.DNS.GANDI.NET
    Name Server: B.DNS.GANDI.NET
    Name Server: C.DNS.GANDI.NET
    Status: clientTransferProhibited
    Updated Date: 03-aug-2011
    Creation Date: 07-sep-1999
    Expiration Date: 07-sep-2015

-- Dan should update his contact information:

    nic-hdl: DB4349-GANDI
    owner-name: FOAF project
    organisation: FOAF project
    person: Dan Brickley
    address: '154-1 Stadionweg, Amsterdam'
    zipcode: 1077 TA
    city: Amsterdam
    country: Netherlands
    phone: +31.634036802
    fax: 
    email: ae30eb109318e1d3eadcc4472d0238cb-1050201@contact.gandi.net
    lastupdated: 2012-07-13 11:16:39

Quote: "The FOAF Project will provide public notice of impending semantic changes in the FOAF vocabulary."

-- Dan reports that the current version of FOAF ("Marco Polo"). A "1.0" release 
    has been discussed on foaf-dev but there is no current candidate design for
    this. Dan's work on schema.org may motivate a larger effort towards
    convergence of person-related structured data vocabularies, but there is
    nothing concrete to report at this stage.

----------------------------------------------------------------------
"DCMI will mirror the FOAF Subversion project."

-- DCMI's latest mirror of FOAF [7], dated 2013-05-16, is current as of the
    date of this report. This mirror was created by running the command:

       svn co <a href="http://svn.foaf-project.org/foaf/trunk/xmlns.com/htdocs/" class="external free" rel="nofollow">http://svn.foaf-project.org/foaf/trunk/xmlns.com/htdocs/</a>

    and turning the result into a compressed tarball. Tom also saves an SVN
    repository of the entire "foaf" project on his own machine:

       svn co <a href="http://svn.foaf-project.org/foaf/" class="external free" rel="nofollow">http://svn.foaf-project.org/foaf/</a>

    though this is technically not required by the agreement with DCMI.

    The above method does not provide a "complete" SVN snapshot. In 2012, Dan
    generated a [<a href="http://danbri.org/2012/foafsvn/latest-snapshot.gz" class="external free" rel="nofollow">http://danbri.org/2012/foafsvn/latest-snapshot.gz</a> "full" SVN
    snapshot] with the following script:

        svnadmin dump /mnt/foafdisk-sites/svn/foaf | gzip - &gt; foafsvn/latest-snapshot.gz

    Dan re-ran the command in July 2013:

        /var/sites/danbri.org/htdocs/2013/svnfiles$ svnadmin dump /mnt/foafdisk-sites/svn/foaf | gzip - &gt; foafsvn2013-07-05.gz

    resulting in:

        <a href="http://danbri.org/2013/svnfiles/foafsvn2013-07-05.gz" class="external free" rel="nofollow">http://danbri.org/2013/svnfiles/foafsvn2013-07-05.gz</a> 

    a dump of all 1,406 SVN revisions which can be used to recreate Subversion
    repository. DCMI has saved this snapshot at
    <a href="http://dublincore.org/FOAF/2013-07-05/foafsvn2013-07-05.gz" class="external free" rel="nofollow">http://dublincore.org/FOAF/2013-07-05/foafsvn2013-07-05.gz</a>.

----------------------------------------------------------------------
"DCMI will monitor for outages in availability of the FOAF vocabulary and make
a mirrored copy available if required."

-- Tom occasionally pings the FOAF vocabulary. On 2013-05-14, Tom reported to
    Dan that he was unable to access <a href="http://xmlns.com/foaf/0.1/" class="external free" rel="nofollow">http://xmlns.com/foaf/0.1/</a> or
    <a href="http://svn.foaf-project.org/foaf/trunk/xmlns.com/htdocs/" class="external free" rel="nofollow">http://svn.foaf-project.org/foaf/trunk/xmlns.com/htdocs/</a>. Dan responded that
    the server was overloaded and just needed a reboot, which fixed the problem.

-- Ideally, we should find a way to automate the monitoring of downtime, maybe
    even logging the results.

----------------------------------------------------------------------
"...consider the viability of the approach exemplified by this agreement as a
model for similar arrangements with other vocabularies"

-- The DCMI FOAF agreement is cited in a discussion paper [8] being prepared
    for a joint DCMI/W3C special session [9] on the long-term preservation and
    governance of RDF vocabularies at the DC-2013 conference in Lisbon in
    September.

-- There has been informal talk about extending the agreement to other
    vocabularies, as well as investigating the long term plans around purl.org
    and w3.org domains?

----------------------------------------------------------------------
"...propose the DCMI Generic Namespace Policy for RDF Vocabularies [10] as a
principled basis for such agreements, welcoming its extension or revision"

The discussion paper [8] for the DC-2013 special session on vocabulary
preservation cites the Generic Namespace Policy.

----------------------------------------------------------------------
"...identify candidate properties in the DCMI and FOAF vocabularies for
explicit semantic alignment."

-- No progress to report.

----------------------------------------------------------------------
"Collaboration will be re-evaluated and re-affirmed annually."

-- DCMI and the FOAF Project hereby re-affirm the agreement.

----------------------------------------------------------------------
Other issues

-- Dan plans to revisit the security of the FOAF Project servers to guard
    against compromise of the FOAF schemas.

----------------------------------------------------------------------
References

[1] <a href="/collaborations/foaf/" class="external free" rel="nofollow">DCMI FOAF Cooperation Task Group</a>
[2] <a href="/collaborations/foaf/good_neighbour_agreement/" class="external free" rel="nofollow">http://dublincore.org/documents/2011/05/02/dcmi-foaf/</a> 
[3] <a href="/collaborations/foaf/DCMI_FOAF_Cooperation/Specific_Agreements/" class="external free" rel="nofollow">Specific Agreements</a>
[4] <a href="/collaborations/foaf/DCMI_FOAF_Cooperation/Update_201308/" class="external free" rel="nofollow">Update 2013 August</a> 
[5] <a href="/collaborations/asist/" class="external free" rel="nofollow">Reshaping DCMI (2013)</a> 
[6] <a href="http://www.networksolutions.com/whois-search/xmlns.com" class="external free" rel="nofollow">http://www.networksolutions.com/whois-search/xmlns.com</a>
[7] <a href="https://github.com/dcmi/dcmi_foaf_agreement" class="external free" rel="nofollow">http://dublincore.org/FOAF/2013-05-16/svn.foaf-project.org_foaf_trunk_xmlns.com_htdocs.tar.Z</a>
[8] <a href="https://github.com/dcmi/repository/tree/master/wikis_pre2016" class="external free" rel="nofollow">Vocabulary Preservation discussion paper</a>
[9] <a href="http://dcevents.dublincore.org/IntConf/index/pages/view/vocPres" class="external free" rel="nofollow">http://dcevents.dublincore.org/IntConf/index/pages/view/vocPres</a> 
[10] <a href="/specifications/dublin-core/dcmi-namespace-generic/" class="external free" rel="nofollow">http://dublincore.org/documents/dcmi-namespace-generic/</a>
