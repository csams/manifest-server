FROM centos:7

RUN yum install -y epel-release
RUN yum install -y openssl-devel vim python36 wget && \
    yum clean all && \
	python3.6 -m ensurepip && \
	python3.6 -m pip install -U pip pyyaml requests six pyopenssl colorama jinja2                     

# TODO: find the real home
RUN git clone https://github.com/csams/manifest-server.git /opt
WORKDIR /opt/manifest-server
RUN python3.6 -m venv && source bin/activate && pip install -e .
EXPOSE 8080
ENTRYPOINT ["/opt/manifest-server/boot.sh"]
