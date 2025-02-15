## DCMI FOAF Agreement: 2024 update (__DRAFT__)

https://github.com/dcmi/dcmi_foaf_agreement/blob/master/reports/DCMI_FOAF_Report_to_community_2024.md


Tom Baker and Dan Brickley

----------------------------------------------------------------------
Context 

The [DCMI FOAF Cooperation Task Group](http://www.dublincore.org/collaborations/foaf/) reports to the community [(almost) every year](https://github.com/dcmi/dcmi_foaf_agreement/blob/master/reports/) about the status of [specific agreements](http://www.dublincore.org/collaborations/foaf/DCMI_FOAF_Cooperation/Specific_Agreements) under a [May 2011 "good neighbour" agreement between DCMI and the FOAF Project](http://www.dublincore.org/collaborations/foaf/good_neighbour_agreement/).

----------------------------------------------------------------------
"Collaboration will be re-evaluated and re-affirmed annually."

* DCMI and the FOAF Project hereby re-affirm the agreement.

----------------------------------------------------------------------
"The FOAF Project will grant DCMI administrative and technical access to the domain xmlns.com."

* Dan Brickley, Libby Miller, Tom Baker, and Paul Walk currently have the DNS password
* The password, stored in a password vault shared by DCMI managing director Paul Walk and assistant director Tom Baker, was recently verified.

----------------------------------------------------------------------
"DCMI will monitor payment of domain name fees by the FOAF Project."

* According to [whois.domaintools.com](http://whois.domaintools.com/xmlns.com),
  the domain `xmlns.com` is registered with GANDI SAS through 2030-09-07 
  (checked on 2021-11-05).

----------------------------------------------------------------------
"The FOAF Project will provide public notice of impending semantic changes in the FOAF vocabulary."

* The [current version of FOAF](http://xmlns.com/foaf/spec/) is Version 0.99,
  "Paddington". A "1.0" release has been discussed on foaf-dev but no dates
  have been set.  Dan's work on schema.org may motivate a larger effort towards
  convergence of person-related structured data vocabularies, but there is
  nothing concrete to report at this stage.
  * Given a widespread move to HTTPS, an update to the Web server to provide availability via HTTPS is planned.
   * No plans to change namespace URLs to HTTPS (or remove "0.1" etc.)

----------------------------------------------------------------------
"DCMI will mirror the FOAF Subversion project."

* FOAF was copied from http://svn.foaf-project.org/foaf/ to
  https://github.com/foaf/foaf .  Since July 2017, the website explains:

> This is a 2015 reflection of the main FOAF project Subversion repository into
> Github.
>
> Historically we had two repos: foaf/ which was the core specs, and foaftown/
> which was a more random scratchpad.
>
> We aim to ultimately treat this git repo as primary, and the svn as either
> frozen or (if someone does the work) something that can be sync'd with latest
> state of git master branch. However at the time of writing (2017) it is not
> 100% validated as fully representing the full history and most recent edits
> of our work.

* DCMI has forked the https://github.com/foaf/foaf repository to
  [https://github.com/dcmi/foaf](https://github.com/dcmi/foaf).

* Dan wants to fix some issues with the migration of versioning information so has asked DCMI to keep its snapshots of the Subversion repo.  These are archived in [a Github repo](https://github.com/dcmi/dcmi_foaf_agreement/tree/master/backups).  The Github repo uses [Github Large File Support](https://git-lfs.github.com) for all files with the extension `.gz`.

* With no tangible progress in the past year, this action is carried forward.

----------------------------------------------------------------------
"DCMI will monitor for outages in availability of the FOAF vocabulary and make
a mirrored copy available if required."

* Starting in May 2019, DCMI is monitoring the availablility of the [FOAF specification](http://xmlns.com/foaf/spec/) and [namespace document](http://xmlns.com/foaf/0.1/) using [Uptime Robot service](https://stats.uptimerobot.com/mEWkmuXlB).
* There have been no known significant outages. Hosting continues at Amazon AWS.

