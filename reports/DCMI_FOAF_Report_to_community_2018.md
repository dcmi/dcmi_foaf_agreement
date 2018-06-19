DCMI FOAF Agreement: 2018 status update

https://github.com/dcmi/dcmi_foaf_agreement/blob/master/reports/DCMI_FOAF_Report_to_community_2017.md

Tom Baker and Dan Brickley

----------------------------------------------------------------------
Context 

The DCMI FOAF Cooperation Task Group [1] is a result of the May 2011 Agreement
between DCMI and the FOAF Project [2].  The Task Group implements and monitors
the specific agreements [3] outlined in the DCMI FOAF Agreement. As of 2014, this
Task Group falls under the DCMI Technical Board [4].

The agreement is renewed annually with a report to the community (this text).
The status of specific agreements is reported below.

[1] http://wiki.dublincore.org/index.php/DCMI_FOAF_Cooperation <br>
[2] http://dublincore.org/documents/dcmi-foaf/  <br>
[3] http://wiki.dublincore.org/index.php/DCMI_FOAF_Cooperation/Specific_Agreements <br>
[4] http://wiki.dublincore.org/index.php/DCMI_Technical_Board <br>

----------------------------------------------------------------------
"Collaboration will be re-evaluated and re-affirmed annually."

* DCMI and the FOAF Project hereby re-affirm the agreement.

----------------------------------------------------------------------
"The FOAF Project will grant DCMI administrative and technical access to the domain xmlns.com."

* Dan Brickley, Libby Miller, and Tom Baker currently have the DNS password
* Tom has put the password into a password vault shared with DCMI managing director Paul Walk

----------------------------------------------------------------------
"DCMI will monitor payment of domain name fees by the FOAF Project."

* According to [whois.domaintools.com](http://whois.domaintools.com/xmlns.com),
  the domain `xmlns.com` is registered with GANDI SAS through 2024-09-07.

----------------------------------------------------------------------
"The FOAF Project will provide public notice of impending semantic changes in the FOAF vocabulary."

* The [current version of FOAF](http://xmlns/spec) is Version 0.99,
  "Paddington". A "1.0" release has been discussed on foaf-dev but no dates
  have been set.  Dan's work on schema.org may motivate a larger effort towards
  convergence of person-related structured data vocabularies, but there is
  nothing concrete to report at this stage.

----------------------------------------------------------------------
"DCMI will mirror the FOAF Subversion project."

* FOAF was copied from http://svn.foaf-project.org/foaf/ to
  https://github.com/foaf/foaf.  As of July 2017, the website explains:

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

* DCMI has forked the repository to
  [ https://github.com/dcmi/foaf ](https://github.com/dcmi/foaf).

* Dan wants to fix some issues with the migration of versioning information so
  has asked us to keep our snapshots of the Subversion repo.  These are
  archived in [a Github repo](https://github.com/dcmi/dcmi_foaf_agreement/tree/master/backups).
  The Github repo uses [Github Large File Support](https://git-lfs.github.com)
  for all files with the extension `.gz`.

----------------------------------------------------------------------
"DCMI will monitor for outages in availability of the FOAF vocabulary and make
a mirrored copy available if required."

* Tom occasionally pings the FOAF vocabulary spec http://xmlns.com/foaf/spec/

* TO DO: Ideally, we should find a way to automate the monitoring of downtime,
  maybe even logging the results.

