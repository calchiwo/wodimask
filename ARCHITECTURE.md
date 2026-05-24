# WodiMask: Architecture

## 1. System Positioning

WodiMask is a network identity policy engine.

It does not move packets.
It does not encrypt traffic.
It does not implement a tunnel.

It decides how traffic should appear before any routing happens.

This is the control plane.

A future data plane will execute its decisions.

## 2. Core Principle

Network behavior should be programmable.

Traditional VPNs operate as binary tunnels:
connect or disconnect.

WodiMask operates as a decision engine:
Identity + Context + Policy → RoutingDecision

The engine produces a deterministic output that a lower layer can enforce.

## 3. Architectural Layers

### Layer 0: Identity Model

Represents a network persona.

Identity defines:
- mask_id
- exposure level
- stability (stable vs rotating)
- region intent

Identity answers:
“How should this traffic be perceived externally?”

Identity is static or semi-static.

### Layer 1: Context Model

Represents runtime information.

Context includes:
- app
- domain
- timestamp
- network environment
- risk profile

Context answers:
“What is happening right now?”

Context is dynamic per request or session.

### Layer 2: Policy

Policy is declarative.

Policy maps:
app → behavioral rule

A rule defines:
- profile
- rotate_ip
- log_level

Policy is configuration.
Policy contains no execution logic.

### Layer 3: Decision Engine

Pure logic.

Inputs:
- Identity
- Context
- Policy

Outputs:
RoutingDecision:
- `profile`
- `rotate_ip`
- `region`
- `log_level`
- `risk_flag`

The engine contains:
- no I/O
- no network calls
- no persistence
- no crypto

It is deterministic and testable.

## 4. Separation of Concerns

WodiMask intentionally separates:

Control Plane:
- reasoning
- identity modeling
- routing decisions

Data Plane (future):
- packet routing
- tunneling
- proxying
- encryption

This separation prevents early architectural lock-in.

## 5. Non-Goals (Phase 1)

WodiMask does not:
- Implement WireGuard
- Perform packet inspection
- Rotate IPs
- Connect to providers
- Store telemetry
- Claim anonymity

It only decides.

## 6. Determinism and Testability

The engine must remain:

- Pure
- Side-effect free
- Fully unit-testable

Given the same identity, context, and policy,
it must produce the same decision.

## 7. Extensibility Direction

Future integrations may include:

- Local HTTP/SOCKS proxy adapter
- YAML or database-backed policies
- Remote policy distribution
- Telemetry hooks
- Distributed routing nodes

The core engine must remain stable
while integrations evolve around it.

## 8. Architectural Constraint

If future development requires network access
inside the decision engine,
the architecture has been violated.

The engine must stay pure.

Execution happens elsewhere.

## 9. Long-Term Vision

WodiMask becomes:

- An identity control layer
- A programmable network behavior engine
- A zero-trust client policy brain
- A routing governor for AI agents
- A compliance-first developer network layer

It is not a tunnel.
It is the brain above the tunnel.