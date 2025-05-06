#/bin/bash

token=`cat /run/secrets/kubernetes.io/serviceaccount/token`
hostname=`hostname`
image=`curl -s -H "Authorization: Bearer $token" "https://kubernetes.default.svc/api/v1/namespaces/mobio/pods/$hostname" -k 2>&1 | grep -m 1 '"image"' | cut -d '"' -f 4`

while [[ true ]]; do
  saved_image=`cat "$data_dir/image.version"`
  if [[ $image == $saved_image ]]; then
    break
  fi
  sleep 5
done