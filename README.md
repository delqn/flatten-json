# flatten-json

The goal if this tiny script is to take an arbitrary JSON and flatten it into a one level dict.

For instance:
```json
    {
        "x.y": [
            {
                "x.1": 1,
                "n": {
                    "a":1,
                    "b":2,
                },
            },
            {
                "k":"l",
            },
        ],
        "b":"c",
        "0":1,
    }
```
will be converted to:
```json
     {
         "b": "c",
         "x\.y.0.n.a": "1",
         "x\.y.0.n.b": "2",
         "x\.y.0.x\.1": "1",
         "x\.y.1.k": "l",
         "0": "1",
    }
```
