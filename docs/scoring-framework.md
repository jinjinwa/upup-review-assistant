# Example Scoring Framework

The community scorer is a generic example service:

```text
score = weighted average of caller-supplied demo dimensions
```

It demonstrates service boundaries, request validation, API shape, and a clean place to plug in your own domain-specific scoring dimensions.

The admin users endpoint also shows an N+1-safe aggregate query by loading report counts in one grouped SQL statement.
