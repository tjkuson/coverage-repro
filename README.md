On coverage v7.11.1, `coverage run --branch --module pytest` fails with

```
coverage.exceptions.NotPython: Couldn't parse '/Users/tjkuson/workspace/repro/src/repro/templates/greet.html' as Python source: 'invalid syntax' at line 1`.
```

This error do not occur on coverage v7.11.0, nor does it occur without `--branch`.
