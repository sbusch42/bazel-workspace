FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# Update and install packages
RUN apt-get -y -q update && \
	apt-get -y -q upgrade && \
	apt-get -y -q install sudo net-tools iputils-ping nano apt-transport-https curl gnupg python3 python3-yaml python3-jinja2 git && \
	curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > /usr/share/keyrings/bazel-archive-keyring.gpg && \
	echo "deb [arch=amd64 signed-by=/usr/share/keyrings/bazel-archive-keyring.gpg] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list && \
	apt-get -y -q update && \
	apt-get -y install bazel && \
	rm -rf /var/lib/apt/lists/*

RUN groupadd -r -g 1000 bazel && useradd -r --home-dir /bazel --create-home -g bazel -u 1000 bazel

USER bazel:bazel
WORKDIR /bazel

ENTRYPOINT /bin/bash
