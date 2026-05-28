# Scoring Framework

The public scorer is deliberately generic:

```text
score = weighted average of caller-supplied demo dimensions
```

It demonstrates service boundaries, request validation, and API shape. It does not include commercial factors, weights, stock pool logic, trend logic, backtest logic, or trading signals.

The admin users endpoint also shows an N+1-safe aggregate query by loading report counts in one grouped SQL statement.
