# Efficient Load Balancing of Dockerized Web Applications Using Nginx Reverse Proxy

This repository implements an efficient load balancing solution for Dockerized web applications using an Nginx reverse proxy, optimized through trace-driven analysis of NASA HTTP server logs. The NASA logs, a key component, provide detailed insights into real-world HTTP request patterns, while Google traces simulate containerized workload demands. A web-based visualization tool (`index.html`) enables interactive analysis of the NASA logs, displaying metrics such as request distribution by handler ID, path frequency, and resource types. This project demonstrates how trace analysis informs Nginx configuration for scalable, high-performance load balancing.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Datasets](#datasets)
- [NASA HTTP Logs](#nasa-http-logs)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Visualization Tool](#visualization-tool)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
Modern web applications demand robust load balancing to handle dynamic traffic and ensure low latency. This project uses Nginx as a reverse proxy to distribute HTTP requests across Dockerized web application instances. The load balancing strategy is informed by analyzing two real-world datasets:
- **NASA HTTP Logs**: Historical server access logs from a NASA website, capturing request timestamps, handler IDs, and URL paths.
- 

The NASA logs are central to understanding request patterns, such as handler load distribution and frequently accessed paths, which guide Nginx’s routing decisions. A visualization dashboard (`index.html`) provides interactive charts and tables to explore these patterns, aiding in the design of efficient load balancing algorithms. The project is extensible, allowing integration of additional datasets or advanced Nginx configurations.

## Features
- **Nginx Reverse Proxy**: Dynamic load balancing with weighted routing and health checks for Docker containers.
- **Dockerized Web Applications**: Scalable sample web apps in containers for testing load balancing.
- **NASA Log Analysis**: Detailed insights into HTTP request patterns, handler performance, and resource types.
- 
- **Visualization Dashboard**: Interactive web app (`index.html`) with:
  - Bar chart of requests by handler ID (prominently displayed).
  - Tables for requests per path, handlers per path, resource types, and log details.
  - Charts for request frequency over time and path distribution.
- **Modular Design**: Easily adaptable for new datasets, algorithms, or containerized applications.

## Datasets
The project leverages two datasets to analyze workloads and optimize load balancing:
- **NASA HTTP Logs**: Server access logs from a NASA web server, used to study HTTP request patterns and handler performance.
- **Google Cluster Data**: Assumed to be Google’s publicly available cluster traces (e.g., task events, resource usage), simulating Docker container workloads. *Update this section if you used a different Google dataset.*

The NASA logs are the primary focus for log analysis and visualization, while Google traces inform container scaling and resource allocation strategies.

## NASA HTTP Logs
The NASA HTTP logs are a historical dataset from a NASA web server, originally collected between July and August 1995, and widely used in web server research. For this project, a sample subset is provided in `server_log.txt`, with timestamps backdated to May 11, 2025, to align with modern contexts. The logs capture HTTP requests to a NASA website, including paths related to the Space Shuttle program (e.g., STS-73 mission) and static assets like images.

### Log Format
Each log entry follows the format:
