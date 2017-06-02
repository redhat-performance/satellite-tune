#!/bin/bash

set -x
set -e

spec="rel-eng/satellite-tune.spec"
name=$( grep '^Name:' $spec | sed 's/^Name:\s*\([a-z-]\+\)\s*$/\1/' )
version=$( grep '^Version:' $spec | sed 's/^Version:\s*\([0-9a-z.]\+\)\s*$/\1/' )
directory="$name-$version"
archive="$directory.tar.gz"

if [ -z "$name" -o -z "$version" ]; then
  echo "ERROR: Unable to determine name '$name' or version '$version'" >&2
  exit 1
fi

if [ "$version" = 'master' ]; then
  echo "ERROR: Make sure you are in release branch and update version number in $spec first" >&2
  exit 1
fi

# Prepare directory
rm -rf /tmp/$directory
mkdir /tmp/$directory

# Copy content to the directory
cp -r * /tmp/$directory/

# Create tarball
tar -czf $archive -C /tmp $directory
rm -rf /tmp/$directory

# Put files to rpmbuild directories
cp $archive ~/rpmbuild/SOURCES/
rm $archive
cp $spec ~/rpmbuild/SPECS/

# Build rpm
rpmbuild -ba ~/rpmbuild/SPECS/$( basename $spec )
