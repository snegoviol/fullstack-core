<!--    
    ================================================================================================
    
    Copyright (c) 2026 Ilya Snegov
    
    Dedicated to the public domain under the Creative Commons
    CC0 1.0 Universal Public Domain Dedication (the "Dedication").
    You may obtain a copy of the Dedication at
    
    https://creativecommons.org/publicdomain/zero/1.0/legalcode.en

    ================================================================================================
    README.md
    ================================================================================================
-->

# Full-Stack Core

> *An educational project demonstrating how to build a production-grade server-side rendered web application with Python. While designed for learning, its comprehensive architecture — covering SSR, HTMX partial updates, background tasks, and uniform error handling — makes it a solid foundation for real-world full-stack applications.*

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](#license)
[![License: CC0 1.0](https://img.shields.io/badge/License-CC0%201.0-blue.svg)](#license)

<!--    
    ================================================================================================
-->

## Project Structure

```
fullstack-core/
├── packages/               # Monorepo root containing all independently deployable
│   │                       # Python modules and shared libraries. Each package
│   │                       # strictly follows the standard `src/` layout (e.g.
│   │                       # `packages/server/src/server/`) for clean imports and
│   │                       # packaging.
│   │
│   ├── server/             # FastHTML app: HTTP routing, server-rendered
│   │                       # pages, HTMX partial updates, database
│   │                       # interactions, and task delegation to the
│   │                       # workers.
│   │
│   ├── shared/             # Cross-process shared infrastructure. Contains base
│   │                       # configurations and unified client abstractions for
│   │                       # external services.
│   │
│   ├── services/           # Cross-process business logic built on top of shared
│   │                       # infrastructure. Contains self-contained service
│   │                       # modules that implement domain-specific behaviour.
│   │
│   ├── worker-inference/   # Dedicated GPU worker running text generation
│   │                       # inference via the Qwen model and Hugging Face
│   │                       # Transformers.
│   │
│   ├── worker-maintenance/ # Maintenance process package: general-purpose
│   │                       # CPU worker and Celery beat scheduler entry
│   │                       # point, running scheduled tasks (currently:
│   │                       # resetting per-user inference run quotas).
│   │
│   └── scripts/            # Standalone automation scripts for environment
│                           # bootstrapping, infrastructure initialization, and
│                           # auxiliary utility tasks.
│
├── migrations/             # Alembic migration environment and database schema
│                           # change scripts.
│
├── docs/                   # Technical documentation covering project dependencies,
│                           # codebase layout, and sequence diagrams for key user
│                           # flows.
│
├── LICENSES/               # Full texts of all licenses used in the project.
│
├── LICENSE.txt             # Licensing overview: which license applies to which files.
│
├── docker-compose.yml      # Docker Compose stack for running infrastructure
│                           # services (PostgreSQL, Redis) locally.
│
├── .env.example            # Environment variable template. Copied to .env during
│                           # bootstrapping with auto-generated credentials for
│                           # credential fields.
│
├── pixi.toml               # Pixi configuration defining feature-based
│                           # dependency groups for server, workers, and
│                           # ML inference.
│
├── pixi.lock               # Fully resolved and reproducible dependency
│                           # lockfile.
│
├── package.json            # Bun manifest declaring frontend asset dependencies.
│
├── bun.lock                # Fully resolved and reproducible JavaScript dependency
│                           # lockfile.
│
└── justfile                # Task runner: bootstrap commands, database
                            # migration targets, runtime process launchers,
                            # and Docker Compose shortcuts. Automatically
                            # manages the pixi environment per recipe.
```

<!--    
    ================================================================================================
-->

## Quick Start

### I. Prerequisites

| Component            | Requirement                               |
| :------------------- | :---------------------------------------- |
| **Operating System** | GNU/Linux-based system                    |
| **Architecture**     | `x86_64`                                  |
| **Package Manager**  | [`Pixi`](https://pixi.prefix.dev/latest/) |
| **Container Tools**  | [Docker and Docker Compose](https://docs.docker.com/engine/install/) |
| **GPU**              | NVIDIA GPU with a driver supporting CUDA `>= 12.8` |

> **Note: on these prerequisites**  
> These are not strict requirements, but rather the baseline environment where the code is 
guaranteed to run out of the box. Alternative setups are possible but may require manual 
configuration.

> **Note: on CUDA versions**  
> The `>= 12.8` constraint is enforced via Pixi's `system-requirements`, reflecting the default 
PyTorch CUDA build at the time of development. Newer driver versions are fully supported.

<!--    
    ================================================================================================
-->

### II. Setup

1. **Clone the repository**

    ```bash
    git clone https://github.com/snegoviol/fullstack-core.git
    cd fullstack-core
    ```

2. **Install dependencies**

    ```bash
    pixi run setup
    ```

3. **Activate environment**

    ```bash
    pixi shell
    ```

<!--    
    ================================================================================================
-->

### III. Launch

Once the environment is activated, the service can be launched with a single command:

```bash
just quick-start
```

The launch script will automatically execute all necessary setup steps, start the server, and open the landing page in your default web browser once the application is ready.

> **Want to see what happens under the hood?**  
> The launch script is fully documented with step-by-step comments explaining each action. You can find it here:
> - [Quick start script](./packages/scripts/src/scripts/quick_start.py)

<!--    
    ================================================================================================
-->

### IV. Cleanup

When you are done, stop the server, workers, and scheduler by terminating their terminal processes, then bring down the infrastructure containers:

```bash
just docker-down
```

<!--    
    ================================================================================================
-->

## License

Each file in this repository is licensed under one of the following licenses:

- [Apache License, Version 2.0](LICENSES/Apache-2.0.txt),
- [Creative Commons CC0 1.0 Universal Public Domain Dedication](LICENSES/CC0-1.0.txt).

The applicable license is stated in the header comment of each file. 
See [LICENSE.txt](LICENSE.txt) for details.ыы

<!--    
    ================================================================================================
-->
