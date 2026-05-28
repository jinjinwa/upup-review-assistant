# Architecture

This document describes the minimal public demo only.

## System Context

```mermaid
flowchart LR
  U["Local user"] --> W["Demo web page"]
  W --> A["FastAPI demo service"]
  A --> D["Synthetic sample data"]
  A --> S["Toy scoring"]
  W --> C["UPUP commercial CTA"]
```

## Demo Container

```mermaid
flowchart TB
  B["Browser on localhost:8080"] --> C["Docker Compose service"]
  C --> F["FastAPI app"]
  F --> H["Static files"]
  F --> M["Demo API routes"]
  M --> D["In-memory synthetic data"]
  M --> R["Toy review routine"]
```

## Local Request Sequence

```mermaid
sequenceDiagram
  participant User
  participant Page as Static Page
  participant API as Demo API
  participant Data as Synthetic Data
  participant Score as Toy Scoring
  User->>Page: Open localhost:8080
  Page->>API: GET /api/demo/market
  API->>Data: Read demo entries
  Data-->>API: Synthetic list
  API-->>Page: Market payload
  User->>Page: Run mock review
  Page->>API: POST /api/demo/review
  API->>Score: Score synthetic entries
  Score-->>API: Toy report
  API-->>Page: Demo summary
```

## Sample Data Flow

```mermaid
flowchart LR
  A["Handwritten sample entries"] --> B["Demo API"]
  B --> C["Static page"]
  B --> D["Toy review routine"]
  D --> E["Demo report"]
  E --> C
```

## Notes

No real market feed, production scoring, user account system, payment system, or production deployment topology is included.
