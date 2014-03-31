Create a new CMaaS project
==========================
Below the steps for starting a new CMaaS project are descibed. The tkh cmaas site is used as an example.

Create project directory
------------------------
$ mkdir tkh
$ cd tkh

Get the necessary files
-----------------------
$ wget http://downloads.buildout.org/2/bootstrap.py
$ wget http://virtualsciences.github.io/cmaas/buildout.cfg
$ wget http://virtualsciences.github.io/cmaas/production.cfg
$ wget http://virtualsciences.github.io/cmaas/testing.cfg
$ wget http://virtualsciences.github.io/cmaas/settings.cfg

Set up necessary structure
--------------------------
$ mkdir src
$ cd src

Create the theme product
------------------------
$ paster create -t plone3_theme cmaas.tkh

Selected and implied templates:
  ZopeSkel#basic_namespace  A basic Python project with a namespace package
  ZopeSkel#plone            A project for Plone add-ons
  ZopeSkel#plone3_theme     A theme for Plone 3

Variables:
  egg:      cmaas.tkh
  package:  cmaastkh
  project:  cmaas.tkh
Expert Mode? (What question mode would you like? (easy/expert/all)?) ['easy']: expert
Namespace Package Name (Name of outer namespace package) ['cmaas']:
Package Name (Name of the inner namespace package) ['tkh']:
Skin Name (Name of the theme (human facing, added to portal_skins)) ['']: TKH
Skin Base (Name of the theme from which this is copied) ['Plone Default']: CMaaS
Empty Styles? (Override default public stylesheets with empty ones?) [False]:
Include Documentation? (Include in-line documentation in generated code?) [True]:
Version (Version number for project) ['1.0']: 0.1
Description (One-line description of the project) ['An installable theme for Plone 3']: TKH CMaaS

or in one go:

$ paster create -t plone3_theme cmaas.test \
                   expert_mode=easy \
                   skinbase=CMaaS \
                   skinname=Test \
                   include_doc=False \
                   version=0.1 \
                   url=http://virtualsciences.github.io/cmaas \
                   keywords='web zope plone cmaas' \
                   description='Test CMaaS' \
                   author=THijs \
                   author_email=thijs.jonkman@virtualsciences.nl \
                   empty_styles=False \
                   include_doc=False

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

