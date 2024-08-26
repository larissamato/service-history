#!/bin/sh

/home/app/.local/bin/alembic upgrade head && \
exec python3 -m app

