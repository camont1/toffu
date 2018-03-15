# toffu geocode

Small package to simplify geoprocessing tasks for Public Health
researchers and general public.

## Basic usage

```python
import toffugeocode as tg

dataframe = tg.get_dataframe('filename')
dataframe_withgeoinfo = tg.get_geoinformation(dataframe,key=googleAPIkey)
```

## Requirements

- key API Google
- geopy
- pandas



