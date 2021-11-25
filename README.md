# toffu:  Geocoding map tool

Small package to simplify geoprocessing tasks for Public Health
researchers and general public.

## Create a virtual environment (venv):

To create a virtual environment run this command in your bash:
(usually we define the name venv as `.venv`, but you are free to decide what name you want)
```
python3 -m venv .name_of_venv
```

## Requirements

All requirements are in `requiremenst.txt`. To install you need run this command:

```bash
pip install -r requirements.txt
```

## How to use `pre-commit`

After install requirements, we need start pre-commit with:

```bash
pre-commit install
```

This command need run **JUST ONE TIME**

If you want run in all project:

```bash
pre-commit run --all-files
```

**BUT THIS COMMAND IS NOT NECESSARY** because before we commit the `pre-commit` will be run.

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

df = tfm.get_dataframe('filename')
df_geo = tfm.get_geoinformation(dataframe,key=googleAPIkey)

# heatmap is also stored @ mapa_heat.html
mapa,contagem = tfm.get_heatmap(df_geo)

tfm.set_markers(df_geo) # optional
```
