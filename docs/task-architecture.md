# Task Architecture

The public demo uses an in-memory task abstraction so users can see the shape of an async review flow without running external services.

## Mock Task Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Submitted
  Submitted --> Processing
  Processing --> Completed
  Completed --> [*]
```

## Queue Abstraction

```mermaid
flowchart LR
  A["Review request"] --> B["Task facade"]
  B --> C["In-memory demo task"]
  C --> D["Toy scoring"]
  D --> E["Demo report"]
```

## Production Boundary

The commercial product may use dedicated workers and backing infrastructure for long-running jobs. This public demo does not include those implementations or any production configuration.
