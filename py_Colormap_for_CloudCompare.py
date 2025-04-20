from matplotlib import pyplot as plt
import numpy as np
import matplotlib.cm as cm
import uuid
from datetime import datetime as datetime_


#-----------------------------------------------------------------------------------------
def view_colormap(cmap_def):

    fig, ax = plt.subplots()
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    try:
        cmap = cm.get_cmap(cmap_def)
        ax.imshow(gradient, aspect='auto', cmap=cmap)
        ax.set_title(cmap_def, fontsize=8)
        ax.set_xticks([])
        ax.set_yticks([])
    except ValueError:
        print(f"Colormap: '{cmap_def}' not founded.")

    plt.tight_layout()
    plt.show()
#-----------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
def write_cm_xml(cmap_def,n_col_discr):

    if n_col_discr<5:
        n_col_discr = 5
        print(f'[LOG] {datetime_.now().strftime("%d/%m/%Y %H:%M:%S")} - ATTENTION!!! Minimum number of colors choosed for the discretization of the colormap is changed to 5')


    selected_cmap = cm.get_cmap(cmap_def)
    indices = np.linspace(0, 1, n_col_discr)
    simplified_colors_rgb_normalized = [selected_cmap(i) for i in indices]
    simplified_colors_rgb_255 = [(int(r * 255), int(g * 255), int(b * 255)) for r, g, b, _ in simplified_colors_rgb_normalized]

    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
    <CloudCompare>
        <ColorScale version="1">
            <Properties>
                <name>{cmap_def}_semplify_{n_col_discr}</name>
                <uuid>{{{uuid.uuid4()}}}</uuid>
                <absolute>1</absolute>
                <minValue>0</minValue>
                <range>360</range>
            </Properties>
            <Data>
    """

    for i, (r, g, b) in enumerate(simplified_colors_rgb_255):
        pos = i / (n_col_discr - 1) if n_col_discr > 1 else 0.0
        xml_content += f"""\
                <step r="{r}" g="{g}" b="{b}" pos="{pos}"/>
    """

    xml_content += """\
            </Data>
        </ColorScale>
    </CloudCompare>
    """

    # Write XML-file 
    file_name = f"{cmap_def}_semplify_{n_col_discr}.xml"
    with open(file_name, "w") as f:
        f.write(xml_content)

    print(f'[LOG] {datetime_.now().strftime("%d/%m/%Y %H:%M:%S")} - XML file {file_name} created successfully')
#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------
cmap_list = [
'Blues', 'BrBG', 'BuGn', 'BuPu', 'CMRmap', 'GnBu', 'Greens', 'Greys', 'OrRd', 'Oranges', 'PRGn', 'PiYG', 'PuBu', 'PuBuGn', 'PuOr', 'PuRd', 'Purples', 'RdBu', 'RdGy', 
'RdPu', 'RdYlBu', 'RdYlGn', 'Reds', 'Spectral', 'Wistia', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'binary', 'bone', 'brg', 'bwr', 'cividis', 'cool', 
'coolwarm', 'copper', 'cubehelix', 'gist_earth', 'gist_gray', 'gist_heat', 'gist_ncar', 'gist_rainbow', 'gist_stern', 'gist_yarg', 'gnuplot', 'gnuplot2', 'gray', 'hot', 
'hsv', 'inferno', 'jet', 'magma', 'nipy_spectral', 'ocean', 'pink', 'plasma', 'rainbow', 'seismic', 'spring', 'summer', 'terrain', 'turbo', 'twilight', 'twilight_shifted', 
'viridis', 'winter']
cmap_list_reverse = [
'Blues_r', 'BrBG_r', 'BuGn_r', 'BuPu_r', 'CMRmap_r', 'GnBu_r', 'Greens_r', 'Greys_r', 'OrRd_r', 'Oranges_r', 'PRGn_r', 'PiYG_r', 'PuBuGn_r', 'PuBu_r', 'PuOr_r', 'PuRd_r', 
'Purples_r', 'RdBu_r', 'RdGy_r', 'RdPu_r', 'RdYlBu_r', 'RdYlGn_r', 'Reds_r', 'Spectral_r', 'Wistia_r', 'YlGnBu_r', 'YlGn_r', 'YlOrBr_r', 'YlOrRd_r', 'afmhot_r', 'autumn_r', 
'binary_r', 'bone_r', 'brg_r', 'bwr_r', 'cividis_r', 'cool_r', 'coolwarm_r', 'copper_r', 'cubehelix_r', 'gist_earth_r', 'gist_gray_r', 'gist_heat_r', 'gist_ncar_r', 
'gist_rainbow_r', 'gist_stern_r', 'gist_yarg_r', 'gnuplot_r', 'gnuplot2_r', 'gray_r', 'hot_r', 'hsv_r', 'inferno_r', 'jet_r', 'magma_r', 'nipy_spectral_r', 'ocean_r', 
'pink_r', 'plasma_r', 'rainbow_r', 'seismic_r', 'spring_r', 'summer_r', 'terrain_r', 'turbo_r', 'twilight_r', 'twilight_shifted_r', 'viridis_r', 'winter_r']
#------------------------------------------------------------------------------------------




#------------------------------------------------------------------------------------------
# Select a colormap in cmap_list or cmap_list_reverse
cmap_choosed = 'plasma'

# Minimum number of colors choosed for the discretization of the colormap
n_colors= 5


view_colormap(cmap_choosed)
print(f'[LOG] {datetime_.now().strftime("%d/%m/%Y %H:%M:%S")} - Colormap choosed: {cmap_choosed}')

write_cm_xml(cmap_choosed,n_colors)
#------------------------------------------------------------------------------------------




