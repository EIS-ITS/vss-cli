FROM hub.eis.utoronto.ca/vss/docker/uv:0.7.13-python3.13-alpine
#FROM ghcr.io/astral-sh/uv:0.7.13-python3.13-alpine
# Defining env vars
ENV VSSCLI_VERSION="2025.7.0-dev3"
ARG CI_BUILD_REF
# Defininig tags
LABEL maintainer="Jose Manuel Lopez <jm@eis.utoronto.ca>" \
      ca.utoronto.eis.vsscli.description="This image includes the latest code of VSS-CLI" \
      ca.utoronto.eis.vsscli.vendor="University of Toronto" \
      ca.utoronto.eis.vsscli.version="${VSSCLI_VERSION}" \
      ca.utoronto.eis.vsscli.commit="$CI_BUILD_REF"
# Install the project into `/app`
WORKDIR /app
# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy
# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
COPY . /app
# install OS reqs
RUN apk add --no-cache --virtual build-dependencies \
    gcc musl-dev bash man-pages git && \
    rm -rf /var/cache/apk/*
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --all-extras && uv pip install .
# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"
# add docs
RUN /app/.venv/bin/sphinx-build -b man docs docs/_build/man && \
    cp docs/_build/man/_static/* /usr/share/man/man1
# define default command
VOLUME ["/data"]
# define entrypoint
ENTRYPOINT ["vss-cli"]
