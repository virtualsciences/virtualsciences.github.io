Plone update
============
When the Plone moves up a version, create a copy of the latest branch and pin 
the Plone version in base.cfg.

For example if 4.3-latest moves from 4.3.2 to 4.3.3, copy cmaas/4.3-latest to 
cmaas/4.3.2 and in cmaas/4.3.2/base.cfg replace '4.3-latest' with '4.3.2'.

New hotfix
==========
When a new plone hotfix is released add the hotfix to hotfix.cfg for the 
relevant Plone versions.

