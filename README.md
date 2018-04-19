# toffu:  Geocoding map tool

Small package to simplify geoprocessing tasks for Public Health
researchers and general public.

## Basic usage

```python
import toffu as tf

dataframe = tf.get_dataframe('filename')
dataframe_withgeoinfo = tf.get_geoinformation(dataframe,key=googleAPIkey)
```

## Maps

```python
import toffugeocode as tf
import toffugeocode.mapa as tfm

df    = tfm.get_dataframe('filename')
df_geo= tfm.get_geoinformation(dataframe,key=googleAPIkey)

# heatmap is also stored @ mapa_heat.html
mapa,contagem = tfm.get_heatmap(df_geo)

tfm.set_markers(df_geo) # optional
```

## Requirements

- key API Google
- geopy
- pandas
- folium
- numpy


