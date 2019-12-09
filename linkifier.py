# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join, isdir

where = 'highlights/'
base_url_git = "https://github.com/ljdcvda/data-science-projects/blob/master/highlights/"
base_url_viewer = "https://nbviewer.jupyter.org/github/ljdcvda/data-science-projects/blob/master/highlights/"
markdown = """"""
for project in listdir(where):
    if isdir(join(where,project)):
        for notebook in listdir(join(where,project)):
            if notebook.endswith('.ipynb'):
                url1=join(base_url_git, project, notebook).replace('\\','/')
                url2=join(base_url_viewer, project, notebook).replace('\\','/')
                line = "* [{0} Project]({1}) [(mirror link)]({2})".format(project.capitalize(), url1, url2)
                markdown= markdown + (line+'\n')

print(markdown)