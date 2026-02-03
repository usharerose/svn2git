#!/usr/bin/env python3
"""
Convert Subversion to Git repository
"""
import argparse
import os
import subprocess
import sys
from typing import Optional
from urllib.parse import urlparse

def run(
    repository: str,
    directory: Optional[str] = None,
) -> bool:
    url = urlparse(repository)

    if directory is None:
        repo_name = os.path.basename(url.path)
        edir = os.path.join(os.getcwd(), repo_name)
    else:
        edir = os.fspath(directory)
        edir = os.path.abspath(os.path.expanduser(edir))

    cmd = [
        "git",
        "svn",
        "clone",
        repository,
        edir,
    ]
    print(f"Executing: {' '.join(cmd)}")

    try:
        process = subprocess.Popen(
             cmd,
             stdout=subprocess.PIPE,
             stderr=subprocess.STDOUT,
             text=True,
             bufsize=1,
             universal_newlines=True
        )
        for line in process.stdout:
            print(line.rstrip())
        process.wait()

        if process.returncode == 0:
            print(f"Successfully converted {repository} to {edir}")
            return True
        print(f"Failed to convert {repository} to {edir}, exit code: {process.returncode}")
        return False
    except KeyboardInterrupt:
        try:
            process.terminate()
        except:
            pass
        return False
    except Exception as e:
        print(f"Failed to convert {repository} to {edir}, error: {e}")
        return False


def main():
     parser = argparse.ArgumentParser(
         description="Convert Subversion to Git repository"
     )
     parser.add_argument(
         "repository",
         help="Subversion repository URL"
     )
     parser.add_argument(
         "directory",
         nargs="?",
         help="Output directory"
     )
     args = parser.parse_args()
     is_success = run(args.repository, args.directory)
     sys.exit(0 if is_success else 1)


if __name__ == "__main__":
    main()
