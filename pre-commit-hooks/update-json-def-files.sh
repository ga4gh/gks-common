#!/bin/bash

REPO_ROOT=$(git rev-parse --show-toplevel)
cd "$REPO_ROOT/schema/gks-common" || exit 1

make_output=$(make all)

if [[ "$make_output" == "make: Nothing to be done for \`all\'." ]]; then
  echo "No changes to source files."
  exit 0
else
  echo "Source files updated, adding changes to commit."
  git add $(git ls-files --modified json defs)
  exit 0
fi
