# WodiMask: Roadmap

WodiMask evolves in layers.

Each version expands execution capability while preserving a stable decision core.

The decision engine is the anchor.  
Everything else grows around it.

## v0.1.0 - Decision Core (Current)

WodiMask produces deterministic routing decisions from:

Identity + Context + Policy

Capabilities:
- Network persona modeling
- Runtime context evaluation
- Declarative policy rules
- Pure decision engine
- Unit-tested logic

At this stage, WodiMask defines behavior.
Execution is external.

## v0.2.x - Externalized Policy

Objective:
Move policy from code into configuration.

Work:
- YAML-based policy definitions
- Schema validation
- Environment-aware policy loading
- Profile presets

Impact:
Behavior becomes configurable without modifying engine logic.

WodiMask becomes deployable across environments.

## v0.3.x - Local Enforcement Adapter

Objective:
Bind routing decisions to real traffic.

Work:
- Local HTTP/SOCKS proxy wrapper
- Middleware invoking DecisionEngine per request
- Structured logging layer
- Rotation trigger interface

Impact:
WodiMask begins influencing live network flows.

The engine remains pure.  
Adapters execute.

## v0.4.x - Identity Management Layer

Objective:
Support multiple personas per user.

Work:
- Identity registry
- Runtime identity switching
- Scheduled persona rotation
- Context-triggered identity selection

Impact:
Traffic behavior becomes profile-driven.

WodiMask transitions from single persona to identity orchestration.

## v0.5.x - Transport Integration

Objective:
Attach decision output to real transport mechanisms.

Work:
- WireGuard integration wrapper
- Provider API adapters
- Region-aware routing hooks
- Execution boundary contracts

Impact:
Decisions translate into enforced routing behavior.

Identity-driven routing becomes operational.

## v0.6.x - Intelligence Expansion

Objective:
Refine decision quality through feedback.

Work:
- Risk scoring heuristics
- Detection feedback signals
- Fingerprint alignment modeling
- Policy suggestion engine

Impact:
WodiMask adapts based on observed network responses.

Behavior becomes strategic, not static.

## v1.0.0 - Identity-Driven Routing System

WodiMask at 1.0 delivers:

- Deterministic decision core
- Configurable policies
- Multi-identity orchestration
- Live traffic enforcement
- Transport integration
- Structured observability

At this stage, WodiMask governs how traffic behaves across environments.

## Architectural Guardrails

- The decision engine remains side-effect free.
- Identity modeling remains explicit.
- Execution layers remain replaceable.
- Policy remains declarative.

If any future feature requires merging execution into the engine, the boundary has been broken.

## Long-Term Direction

WodiMask becomes:

- A programmable network behavior layer
- An identity control system for developers
- A routing governor for automated agents
- A compliance-aligned network abstraction

The core remains stable.  
Capabilities expand outward.

## Release Philosophy

Ship small.
Lock abstractions.
Expand outward.
Never collapse layers.