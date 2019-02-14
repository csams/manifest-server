# manifest-server
This is a stubbed out manifest server for insights collection. I'm using it as
an excuse to play with kubernetes.

You can build a docker image for it and deploy it in minikube/kubernetes.

With [minikube and virtualbox][1] installed:
```bash
# set up minikube
minikube config set cpus 2
minikube config set memory 6144
minikube config set vm-driver virtualbox
minikube start

# sets up the docker environment variables so we can tag images in the minikube registry.
eval $(minikube docker-env)

# build the image and tag it
docker build -t csams/manifest-server -f Dockerfile .

# enables the nginx-ingress-controller that comes with minikube.
minikube addons enable ingress

# sets up a 3 replica pod, a service, and an ingress.
kubectl apply -f kube/

# http://<host>/collection/<machine-id>/manifest
wget $(minikube ip)/collection/12345/manifest -O manifest.json --no-check-certificate
```

The ingress would probably be handled by openshift routes or 3scale.

The same manifest is returned every time for all machine ids.

[1]: https://kubernetes.io/docs/tasks/tools/install-minikube/
