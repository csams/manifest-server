FROM centos:7

RUN yum install -y epel-release
RUN yum install -y openssl-devel python36 git && \
    yum clean all && \
	python3.6 -m ensurepip

RUN git clone https://github.com/csams/manifest-server.git /opt/manifest-server
RUN cd /opt/manifest-server && \
    python3.6 -m venv . && \
    source bin/activate && \
    pip install -U pip && \
    pip install -e .
