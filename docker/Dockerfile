FROM python:3.6-alpine
# Defining env vars
ENV VSSCLI_VERSION="0.1.0-dev0"
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
    gcc musl-dev bash \
    libxml2-dev libxslt-dev && \
    rm -rf /var/cache/apk/*
# install app
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -e .
# define volumes
VOLUME ["/data"]
# define entrypoint
ENTRYPOINT ["vss-cli"]