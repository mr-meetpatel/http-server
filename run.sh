#!/bin/sh

set -e

exec pipenv run python3 -m app.server.http_server "$@"