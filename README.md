# Python module template repository

This repo helps take care of the boilerplate in creating a new Python module. Based on [Richard Clatyon's wonderful blog post](https://rclayton.silvrback.com/templatizing-github-template-repos).

## Setup

1. Create a repo using this as a template.
* In the command line:
``` console
fox@arwing:~$ mkdir sample-project
fox@arwing:~$ cd sample-project
fox@arwing:~/sample-project$ gh repo create -p boilerjake/python-module sample-project
fox@arwing:~/sample-project$ git pull
```
* In the browser
  * Scroll up and click "Use this template"
2. Edit the template variables
``` console
fox@arwing:~/sample-project$ vim customize.json
```
3. Apply the template customization
``` console
fox@arwing:~/sample-project$ ./customize
```
**Done.** Now get back to work!
