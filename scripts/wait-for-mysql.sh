#!/bin/sh
# wait-for-mysql.sh

set -e

host="$1"
shift
cmd="$@"

until MYSQL_PASSWORD=$MYSQL_PASSWORD mysql -h "$host" -U "etitango" -c '\q'; do
  >&2 echo "MYSQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MYSQL is up - executing command"
exec $cmd
