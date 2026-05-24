# WodiMask

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE) [![PyPI Version](https://img.shields.io/pypi/v/wodimask?color=blue)](https://pypi.org/project/wodimask)

WodiMask is a network identity and policy engine.

It defines how traffic behaves on the network by modeling identity, context, and intent, then producing a deterministic routing decision.

This repository contains the control layer.

## What WodiMask Does

WodiMask models network behavior before execution.

Given:
- a network identity
- a runtime context
- a set of policies

WodiMask produces:
- a behavior profile
- IP rotation intent
- regional intent
- logging posture
- risk flags

The output is a RoutingDecision.

That decision is designed to be consumed by a lower execution layer.

## Core Model

Network behavior should be programmable.

Traditional VPNs operate as binary tunnels:
connect or disconnect.

WodiMask is built around a single flow:

Identity + Context + Policy → RoutingDecision

This flow is pure, deterministic, and testable.

## Identity

Identity represents a network persona.

It encodes:
- how stable the identity should be
- how exposed it is allowed to be
- which region it prefers to appear from

Identity answers one question:

How should this traffic look from the outside?

## Context

Context represents what is happening right now.

It includes:
- which app initiated the request
- the target domain
- the current network environment
- time
- risk profile

Context is evaluated per request or per session.

## Policy

Policy is declarative intent.

Policies map runtime context to behavior rules.

A rule defines:
- which profile to use
- whether IP rotation is allowed or required
- how much logging is acceptable

Policies contain no execution logic.
They describe intent only.

## Decision Engine

The decision engine is the core.

It:
- takes identity, context, and policy
- applies deterministic logic
- emits a routing decision

The engine has:
- no network access
- no side effects
- no hidden state

Given the same inputs, it always produces the same output.

## Execution Boundary

This repository ends at decision making.

Execution is expected to happen elsewhere:
- a local proxy
- a tunnel adapter
- a routing service
- a future data plane

The control layer remains isolated by design.

## Current State

- Identity model implemented
- Context model implemented
- Declarative policy system implemented
- Deterministic decision engine implemented
- Unit tests in place

This is the foundation layer.

## License

This project is License under Apache 2.0. See [LICENSE](LICENSE) for details

## Author

Caleb Wodi