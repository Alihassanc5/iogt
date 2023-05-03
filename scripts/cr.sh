#!/bin/bash

REQ_FILES=(
  "/app/requirements"
  "/app/requirements.dev"
)

for f in "${REQ_FILES[@]}"; do
  rm ${f}.txt && pip-compile --generate-hashes --resolver=backtracking -o ${f}.txt ${f}.in || exit 1;
done
