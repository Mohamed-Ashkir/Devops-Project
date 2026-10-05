# Docker 

> [!TIP]
> ## 🚀 Featured project: Flask + Redis multi-container app
> A Python web app and a Redis database running together with Docker Compose.
> **[→ View the project](challenge/)**


Tool that builds, ships and runs applications. It packages an app into an image and runs that image as a container, so they run the same way anywhere.

Important Rule for Docker in MacOs, Windows and non-linux operating systems 

Container- an isolated process running on the host, a program with walls around it

Docker containers are linux program; they make request (system calls) that only a linux kernel understand and the rest MacOs or windows kernel don’t understand. 

Docker Desktop installs a hidden Linux VM. The **VM** brings the Linux kernel. Docker runs inside the VM, so the containers share the VM's
- Non-Linux OS (Mac kernel) → hidden Linux VM (Linux kernel) → Docker → containers
- Linux server (Linux kernel) → Docker → containers (no VM needed)

My Mac runs 2 kernels when Docker Desktop is open, but the containers only use the 1  kernel the linux kernel.

Linux host:containers use the host's kernel directly. No VM.
Mac or Windows:containers use the hidden VM's Linux kernel.

- Docker Images- read only template that holds everything an app needs to run: the code, dependency ( software needed by application to work properly and you didn’t write it), libraries (specific type of dependency, pre-written code that you can import into your own program to solve a specific problem.) and the settings
- Docker Containers- **live, running instance( living copy)**  of a Docker image. When you tell Docker to run an image, it unwraps that read-only template, creates an isolated space in your computer's memory, and starts running the application

# Benefits of container vs Virtual machines

|  | VM | Container |
| --- | --- | --- |
| **Startup** | Minutes | Seconds |
| **Resources** | Heavy, because each VM has a full guest OS | Light, because containers share the host kernel |
| **Portability** | Low | High: runs anywhere Docker runs |
| **Isolation** | Strong: a full separate OS | Process-level: lighter, but weaker |


VM run on hypervisor which fakes an entire computer, hardware and all

container has no hypervisor. It runs straight on the host's kernel.

# Kernel- the brain

A software program that acts as a bridge, it connects software application to physical computer hardware. 

kernel's jobs:

1. Runs programs:** starts them, stops them, and decides which one gets the CPU.
2. Manages memory:** gives each program its own RAM and stops them touching each other's.
3. Handles files:** reading from and writing to the disk.
4. Handles the network:** sending and receiving data.

# Containers share host kernel this means:

- Nothing to boot as the kernel is already running mean containers are faster than VM
- Lightweight as it only has the apps and its dependencies not OS inside a container
- multiple container run can run on one kernel whilst VM needs 10 kernel for each one

Isolation is the one place VMs win for strong security wall 

#Dockerfile

A Dockerfile is a simple text file that contains the commands a user could call to assemble an image. Example below: 
screenshot here 
```yaml
FROM ubuntu:latest
MAINTAINER john doe

RUN apt-get update
RUN apt-get install -y python python-pip wget
RUN pip install Flask

ADD hello.py /home/hello.py

WORKDIR /home

```

| Instruction | What it does |
| --- | --- |
| **FROM** | The starting point, or **base image**. You don't build from nothing; you start from an image that already has, say, Node or Python installed. |
| **WORKDIR** | Sets the folder inside the image where the next steps happen. Like `cd`. |
| **COPY** | Copies files from **your machine** into the image. |
| **RUN** | Runs a command **while building** the image, such as installing dependencies. |
| **CMD** | The command that runs **when a container starts** from the image. |

 #Docker Networking

Docker networking decides who a container can talk to: other containers, your mac, the internet or nobody.

Importance- real apps they are split into pieces: web app container, database container, a cache container, each has it own containers;  they need to talk to each others. 

# The 3 default network types

| Type | What it means | Isolation | When to use it |
| --- | --- | --- | --- |
| **Bridge** | Containers get their own private network on the machine and can talk to each other. The **default**. | Isolated from the host | Almost always: the normal case |
| **Host** | The container uses the host's network directly. No separate network at all. | **None.** It *is* the host's network. | When an app needs direct access to the host's network, or maximum network speed |
| **None** | No network at all | **Total.** Nothing in or out. | Security: jobs that should never touch a network |

**On your Mac, "host" means the hidden VM.** Remember the two-kernel lesson: Docker runs inside the hidden Linux VM. So in host mode, the container gets **the VM's** network, not your Mac's. That's why host mode behaves differently on a Mac than on a Linux server. Same rule as the kernel: **the host is wherever Docker is actually running.**

# The 3 commands it mentions

- `docker network ls`
- `docker network create`
- `docker network connect`

#Docker Compose

a tool that runs **multiple containers together** from **one file**, with **one command**. Example below:

```yaml
version: "3"
services:
  web:
    build: .
    ports:
    - '5000:5000'
    volumes:
    - .:/code
    - logvolume01:/var/log
    links:
    - redis
  redis:
    image: redis
    volumes:
      logvolume01: {}
```

| Without Compose | With Compose |
| --- | --- |
| Several long commands | 1 command |
| Easy to mistype | Written once in a file |
| Create the network yourself | Network created for you |
| Hard to share the setup | Share one file, and anyone can run it |
| Lives in your terminal history | Lives in **git**, alongside your code |

Dockerfile vs Compose, a common mix-up:**

- **Dockerfile:** how to build **one image**
- **Compose file:** how to run **several containers together**

Dockerfile used for image and docker compose used to manage multi-container application

Importance in Devops

- makes development and testing easier
- Ensures consistency
- improves teamwork- new developer joins they don’t need to spend days setting up. Compose: the YAML file(plain text format for writing settings and configuration) lives in the git repo

#One sentence to remember

**Compose = your whole multi-container setup, written in one file, in git, started with one command.**

### #Docker Registries

**docker registry is system for storage and sharing service for Docker images.** It's like GitHub, but for images instead of code. A Docker registry like amazon ECR **actually stores the image itself**, all the files and layers

 #Public vs private

|  | Public | Private |
| --- | --- | --- |
| **Who can pull** | Anyone | Only people you allow |
| **Example** | Docker Hub public images (`mysql`, `python`, `nginx`) | **AWS ECR**, private Docker Hub repos |
| **Use for** | Open-source and base images | **Your company's own apps** |

# The 3 commands

- **`docker login`**: proves who you are to the registry
- **`docker push`**: uploads your image
- **`docker pull`**: downloads an image

### #Why it matters in DevOps

1. **Consistency:** every server pulls the **exact same image**, built once.
2. **Collaboration:** the team shares images instead of rebuilding them.
3. **Streamlined deployment:** CI/CD builds the image, pushes it, and the server pulls it. No manual copying.

To store and share your docker image you use **Docker Hub** 

# #Image commands

| Command | What it does |
| --- | --- |
| **`docker images`** | Lists all images on your machine: name, tag, ID, size |
| **`docker inspect`** | Shows **full details** about an image (or container): config, env variables, layers |
| **`docker rmi`** | **Removes an image.** RMI stands for "remove image." |

### #Container commands

| Command | What it does |
| --- | --- |
| **`docker ps`** | Lists **running** containers |
| **`docker stop`** | Stops a running container. It **still exists**, just switched off. |
| **`docker rm`** | **Deletes** a container completely |

# #Clean-up command

| Command | What it does |
| --- | --- |
| **`docker system prune`** | Deletes **everything unused at once**: stopped containers, unused networks, dangling images, build cache |

 **Be careful with `prune`.** It deletes **all stopped containers**. 

# #Three things to remember

**1. `rm` vs `rmi`:** this is the one people mix up most.

- `rm` removes a **container**.
- `rmi` removes an **image**.

**The order matters.** Docker won't delete an image while a container still uses it. That's the error in the video. So it's always: **stop the container → remove the container → remove the image.**

# #Multi-stage builds

Scenario:** your Docker image is too big, say 471 MB for a small Flask app.

Why it's big:** build tools like gcc and dev libraries are needed to **install or compile** dependencies, but they stay in the final image even though the app never uses them when it runs.

**Fix: a multi-stage build.** Use **two FROM lines** in one Dockerfile:

- **Stage 1 (build):** install the build tools and compile the dependencies.
- **Stage 2 (production):** a clean base image. Copy in **only** what the app needs to run, using `COPY --from=<stage name>`.
- Stage 1 is thrown away. Only stage 2 becomes the final image.

**Result:** a much smaller image (471 MB → 151 MB in the video). That means it's faster to push, pull and deploy, uses less storage, and is more secure.
