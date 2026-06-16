+++
title = "Kroma App"
date = 2026-02-01
description = "An end-to-end serverless platform that brings together healthcare consulting, educational services, and e-commerce experiences. Built on AWS using Terraform, with a Vue-based frontend and FastAPI backend services, the project showcases how modern cloud architectures can deliver scalable, cost-effective, and highly automated solutions across multiple business domains."
[extra]
thumbnail = "thumbnail.png"
tags = ["devops", "programming", "cloud"]
+++

## Architecture

{{ d3_architecture(id="kroma-app") }}

## Design

**Serverless-first.** Every component scales independently. API Gateway triggers Lambda on demand — no servers to manage, no idle cost.

**Vue.js on S3 + CloudFront.** The frontend is fully static, served from S3 with CloudFront for global low-latency delivery. Route53 handles DNS at the edge.

**Cognito for auth.** User pools manage healthcare practitioners, students, and customers. Tokens flow through API Gateway to Lambda authorizers.

**Multi-model storage.** DynamoDB for session and transactional data. RDS (PostgreSQL) for relational schemas. S3 for file assets. SES for transactional email.



