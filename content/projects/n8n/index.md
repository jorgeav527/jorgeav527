+++
title = "Real production N8N"
date = 2026-04-01
description = "A highly available and production-ready N8N automation platform deployed within a private network environment. Built following cloud-native and SRE best practices, the project focuses on scalability, observability, reliability, security, and operational excellence."
[extra]
thumbnail = "thumbnail.png"
tags = ["devops", "cloud"]
+++

## Architecture

{{ d3_architecture(id="n8n-v2") }}

## Design decisions

**High availability.** Two N8N instances behind Traefik, sharing Redis for queue distribution and PostgreSQL for persistent state. If the primary fails, the replica seamlessly takes over.

**Security-first.** All traffic enters through WireGuard VPN. Traefik terminates TLS and handles rate limiting. The entire deployment lives in a private network — no exposed ports beyond the VPN endpoint.

**Observability built in.** Prometheus scrapes metrics from both N8N instances. Grafana provides dashboards for workflow health, execution latency, queue depth, and resource utilization.

**Automated resilience.** Redis handles workflow queuing and inter-instance broadcast. PostgreSQL is clustered for data durability. Daily automated backups ensure recovery capability.
