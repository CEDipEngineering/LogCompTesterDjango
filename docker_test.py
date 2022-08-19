#!/usr/bin/python3
import docker

client = docker.from_env()

# Can run scripts inside containers
out = client.containers.run("ubuntu", "echo helloworld")
print(out)

# Containers can receive kwargs, such as cpu_count and environment

# List images available
out = client.images.list()
print(out)


# see https://docker-py.readthedocs.io/en/stable/