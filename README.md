# chamber-executive-network

executive network mapping engine for corporate officers and board members.

## install

```bash
pip install -e .
```

## run api

```bash
uvicorn chamber_executive_network.api:app --port 8003
```

## usage

```python
from chamber_executive_network import search_executives

result = search_executives("383474814")
print(result.result)
```


