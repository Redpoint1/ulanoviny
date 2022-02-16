#!/usr/bin/env sh
cd "$(dirname "$0")"
rsync -ruvpPtlz --delete --exclude venv \
      --exclude .idea \
      --exclude .git \
      --exclude __pycache__ \
      --exclude ulanoviny.db \
      --stats -h .. ulanoviny@remote.local:/home/ulanoviny/service
echo
ssh root@remote.local pip3 install -r /home/ulanoviny/service/src/requirements.txt