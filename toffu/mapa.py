import folium
import numpy as np
from folium.plugins import HeatMap

default_map_coords = [-22.3145, -49.0587]


def get_heatmap(dataframe, coords=default_map_coords, name="mapa_heat"):
    """
    cria-se um heatmap centrado nas coordenadas coords.
    A contagem por coordenada também é enviada como output.

    além disso, cria-se o arquivo mapa_heat.html com o heatmap
    """
    dataframe2 = dataframe[
        dataframe["lat"].apply(lambda y: isinstance(y, float) and not np.isnan(y))
    ]

    mapa = get_map(coords)
    # obtem todos os pares (lat,lon) únicos dentro de um dataframe
    points = list(zip(dataframe2["lat"], dataframe2["lon"]))
    counts = {point: 0 for point in set(points)}
    for point in points:
        counts[point] += 1
    data = [(point[0], point[1], counts[point]) for point in counts]
    heat = HeatMap(data, min_opacity=0.5, max_val=max(counts.values()))
    mapa.add_child(heat)
    mapa.save(name + ".html")

    return mapa, counts


def set_markers(mapa, dataframe, col_name="nome", name="mapa_markers"):
    """
    para cada linha em dataframe com coordenadas (lat,lon),
    adiciona-se um marcador ao mapa

    além disso, cria-se o arquivo mapa_markers.html com o mapa+markers
    """
    for k in range(len(dataframe)):
        set_marker_person(mapa, dataframe.iloc[k], col_name=col_name)
    return mapa.save("%s.html" % (str(name)))


def set_marker_person(mapa, linha_df=None, col_name="nome"):
    """
    adiciona-se um marcador ao mapa se linha_df possuir (lat,lon)
    """
    if "lat" in linha_df:
        if len(str(linha_df["lat"])) > 0:
            folium.Marker(
                [linha_df["lat"], linha_df["lon"]], popup=linha_df[col_name]
            ).add_to(mapa)
    return None


def get_map(coords=default_map_coords, tiles="Stamen Toner"):
    """
    retorna um mapa folium centrado em coords
    """
    return folium.Map(location=coords, zoom_start=6, tiles=tiles)
