#!/usr/bin/env python

import os
import shutil
import subprocess

urls = '''
    https://zopedev.pareto.nl/svn/pareto/Compass/tags/2.2.2 Compass
    https://zopedev.pareto.nl/svn/pareto/CMFUrlSkinSwitcher/tags/2.0.0 CMFUrlSkinSwitcher
	https://zopedev.pareto.nl/svn/LevenLangLerenSkin/trunk LevenLangLerenSkin
	https://zopedev.pareto.nl/svn/LevenLangLerenTypes/trunk LevenLangLerenTypes
	https://zopedev.pareto.nl/svn/pareto/glitz/tags/1.0.0 glitz
'''.strip()

def run(cmd):
    print cmd
    assert subprocess.call(cmd, shell=True) == 0

orig = os.getcwd()

project = os.path.abspath('lll')

for line in urls.splitlines():
    url, target = line.strip().split()
    run('bzr branch svn+%s %s' % (url, target))
    os.chdir(target)
    run('mkdir %s' % target)
    run('bzr add %s' % target)
    for f in os.listdir('.'):
        if f in [target, '.bzr']:
            continue
        run('bzr mv %(file)s %(target)s/%(file)s' %
            {'file': f, 'target': target})
    run('bzr ci -m "Converting to bzr" %s' % target)
    os.chdir(project)
    run('bzr merge -r 0..-1 ../%s' % target)
    run('bzr ci -m "Merged %s"' % target)
    os.chdir(orig)
    shutil.rmtree(target)
