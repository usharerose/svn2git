# svn2git

A Python-based service for one-way conversion from Subversion to Git repositories

## Features

- Convert Subversion repositories to Git

## Prerequisites

- Python 3.10+
- Git with `git-svn` support

## Usage

```bash
# Convert local Subversion repository (output directory named after repository)
python svn2git/app.py file:///path/to/svn/repo

# Convert with custom output directory
python svn2git/app.py file:///path/to/svn/repo ./output

# Convert remote Subversion repository
python svn2git/app.py svn://example.com/repo ./my-repo

# Convert with HTTPS
python svn2git/app.py https://svn.example.com/repo/trunk ./output
```
