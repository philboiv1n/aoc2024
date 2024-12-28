# Advent of Code 2024

Welcome to my **Advent of Code 2024** repository. 
This is my Python-powered journey through the 25 days of coding challenges.

As you explore the code, you may notice that some days are better structured than others—reflecting the days when I had more time and peace to focus on clean, maintainable solutions.

## Repository Structure

Here's how the repository is organized:

- **`/src`**:  
  Contains Python scripts for each challenge.  
  File naming convention: `YYYY-MM-DD[a|b].py` (e.g., `2024-12-01a.py` for Day 1, Part 1).

- **`/src/inputs`**:  
  Holds input text files for each challenge, including sample and test cases.

## Getting Started

1. I used **Python 3.13** to solve these challenges. Visit [Python's official website](https://www.python.org/downloads/) to download and install the appropriate version for your operating system. Ensure it's added to your PATH.

2. Clone the repository :
```bash
git clone https://github.com/philboiv1n/aoc2024.git
cd aoc2024
```

3. Run the first challenge :
```bash
python src/2024-12-01a.py
```

## Docker

You can also use [Docker](https://www.docker.com/) to run a Python container. This repository includes both a Dockerfile and a docker-compose.yml file for easy setup.

1. Build and Run the Container.
From the project directory, run the following command:
```bash
docker compose up --build
```

2. Run a Challenge Inside the Container.
Access the container’s shell and execute a script:
```bash
docker exec -it python-terminal python src/2024-12-01a.py
```