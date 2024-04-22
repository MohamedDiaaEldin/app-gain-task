#!/usr/bin/bash
docker run -d -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=user -e POSTGRES_DB=appgain --net="host" -v $(pwd)/../database:/var/lib/postgresql/data postgres