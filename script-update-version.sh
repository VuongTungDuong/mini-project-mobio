#/bin/bash

### run other scripts
#python3.8 -u ensure_indexes_mongo.py
#python3.8 -u ensure_kafka_topic.py

### Save new version
namespace=`cat /run/secrets/kubernetes.io/serviceaccount/namespace`
token=`cat /run/secrets/kubernetes.io/serviceaccount/token`
hostname=`hostname`
image=`curl -s -H "Authorization: Bearer $token" "https://kubernetes.default.svc/api/v1/namespaces/mobio/pods/$hostname" -k 2>&1 | grep -m 1 '"image"' | cut -d '"' -f 4` deployment=`echo $hostname | sed 's/deployment.*/deployment/'`
echo $image > $data_dir/image.version

curl -X PATCH -H "Content-Type: application/strategic-merge-patch+json" -H "Authorization: Bearer $token" --data '{"spec":{"replicas":0}}' "https://kubernetes.default.svc/apis/apps/v1/namespaces/$namespace/deployments/$deployment" -k
