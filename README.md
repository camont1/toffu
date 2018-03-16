# toffu geocode

Small package to simplify geoprocessing tasks for Public Health
researchers and general public.

## Basic usage

```python
import toffugeocode as tg

dataframe = tg.get_dataframe('filename')
dataframe_withgeoinfo = tg.get_geoinformation(dataframe,key=googleAPIkey)
```

## Maps

```python
import toffugeocode as tg
import toffugeocode.mapa as tgm

df    = tg.get_dataframe('filename')
df_geo= tg.get_geoinformation(dataframe,key=googleAPIkey)

# heatmap is also stored @ mapa_heat.html
mapa,contagem = tgm.get_heatmap(df_geo)

tgm.set_markers(df_geo) # optional
```

## Requirements

- key API Google
- geopy
- pandas
- folium
- numpy


