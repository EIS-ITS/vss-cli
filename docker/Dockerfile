FROM hub.eis.utoronto.ca/vss/docker/python:3.9-alpine
# Defining env vars
ENV VSSCLI_VERSION="2024.9.0"
ARG CI_BUILD_REF
# Defininig tags
LABEL maintainer="Jose Manuel Lopez <jm@eis.utoronto.ca>" \
      ca.utoronto.eis.vsscli.description="This image includes the latest code of VSS-CLI" \
      ca.utoronto.eis.vsscli.vendor="University of Toronto" \
      ca.utoronto.eis.vsscli.version="${VSSCLI_VERSION}" \
      ca.utoronto.eis.vsscli.commit="$CI_BUILD_REF"
# move to app and copy src
WORKDIR /usr/src/app
COPY . .
# install OS reqs
RUN apk add --no-cache --virtual build-dependencies \
    gcc musl-dev bash man-pages git && \
    rm -rf /var/cache/apk/*
# install app
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir --no-use-pep517 -e .[dev]
# add man pages
RUN python3 setup.py install && sphinx-build -b man docs docs/_build/man && \
    cp docs/_build/man/_static/* /usr/share/man/man1
# define volumes
VOLUME ["/data"]
# define entrypoint
ENTRYPOINT ["vss-cli"]
