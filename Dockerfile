FROM ubuntu:latest
LABEL authors="dda"

ENTRYPOINT ["top", "-b"]
