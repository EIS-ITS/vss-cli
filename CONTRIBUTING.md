# Contributing 

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change. 

Please note we have a [code of conduct](CODE_OF_CONDUCT.md), please follow it in all your 
interactions with the project.

## Reporting issues

- Describe what you expected to happen.
- If possible, include a [minimal, complete, and verifiable example][mcve] to help
  us identify the issue. This also helps check that the issue is not with your
  own code.
- Describe what actually happened. Include the full traceback if there was an
  exception.
- List your Python, ``py-vss``, ``vss-cli`` and other relevant versions. 
  If possible, check if this issue is already fixed in the repository (`develop` branch).
  
[mcve]: https://stackoverflow.com/help/mcve

## First time setup

1. Download and install the [latest version of git][latest version of git].
2. Configure git with your `username` and `email` matching your GitLab account:

        git config --global user.name 'your name'
        git config --global user.email 'your email'
        
3. Fork the ``vss-cli`` repository by clicking the [Fork][Fork] button.
4. Clone your fork locally:
    
        git clone git@gitlab-ee.eis.utoronto.ca:{username}/vss-cli.git
        cd vss-cli

5. Add the main repository as a remote to update later:
        
        git remote add vss git@gitlab-ee.eis.utoronto.ca:vss/vss-cli.git
        git fetch vss

6. Create virtualenv:

        python3 -m venv vss-cli
        . vss-cli/bin/activate
   
7. Refer to the [Readme](README.md) guide to install requirements


## Start coding

1. Create a branch to identify the issue you would like to work on (e.g. ``issue-999``):

        cd vss-cli
        git checkout -b issue-999
    
2. Using your favorite editor, make your changes, [committing as you go][committing as you go].
3. Follow [PEP8][PEP8].
4. Push your commits to GitLab and [create a merge request][create a merge request].

        git push origin issue-999
    
5. Celebrate 🎉


## Synchronizing your fork with the main project

1. Fetch changes from upstream
    
        git fetch vss main

2. Rebase local repository:

        git rebase vss/main

3. Commit changes to your fork

        git push origin main


[PEP8]: https://pep8.org/
[create a merge request]: https://docs.gitlab.com/ee/gitlab-basics/add-merge-request.html
[latest version of git]: https://git-scm.com/downloads
[commit as you go]:  http://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html#commit-your-changes
[Fork]: https://gitlab-ee.eis.utoronto.ca/help/gitlab-basics/fork-project.md