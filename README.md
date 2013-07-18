ZIP-RAR_cracker
===============

A simple tool which bruteforces a protected Zip or Rar file.
You may need a dictionary.

FEATURE
====================================================================
- Supports both RAR 2.x and 3.x archives.
- Supports multi volume archives.
- Supports Unicode filenames.
- Supports password-protected archives.
- Supports archive and file comments.
- Archive parsing and non-compressed files are handled in pure Python code.
For compressed files runs unrar utility.
Works with both Python 2.x and 3.x.

Also gives you basic information about the file such as:

  Version needed to crack the archive
  System which created ZIP archive
  size of the compressed file (real size)
  Size of the uncompressed file (real size)
  Extract all the files of the archive into current directory
  Reveal the password


REQUIREMENT
========================================
-For Rar Files download a good library at https://pypi.python.org/pypi/rarfile/ cause not included in python

-For Rar FILE on WINDOWS
Set to full path of unrar.exe if it is not in PATH or include library (might be included in updates)

