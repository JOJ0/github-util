#!/usr/bin/env python
from github import Github
from getpass import getpass

def ask(question):
    return getpass(question)

# user hardcoded, ask password, repo hardcoded
password = ask('password: ')
g = Github("joj0", password)
repo = 'user/repo'

project = g.get_repo(repo).get_projects().get_page(0)[0]
#print(dir(project))
print(project)
print("")


for column in  project.get_columns().get_page(0):
    print(column)
    print('______________________')

    cards = column.get_cards()
    for x in cards:
        #print(dir(x))
        print('#####################')
        print(x.note)
        print('#####################')

