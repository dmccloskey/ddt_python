from .ddt_container import ddt_container
from .ddt_tile import ddt_tile
from .ddt_tile_html import ddt_tile_html

class ddt_container_svg(ddt_container):

    def make_container_svg(self,
        data,
        data_keys,data_nestkeys,data_keymap,
        svgtype,
        svgtileheader='SVG',
        svgkeymap = [],
        svgtile2datamap=[0],
        svgfilters=None,
            ):
        '''make the table container object
        ATTRIBUTES:
        n bound data
        filtermenu and svg share the 1st data if len(data)>1

        INPUT:

        OUTPUT:

        TODO:  finish making method (if even required...)
        '''
        #validate input
        if len(data)!=data_keys:
            print('length of data does not match the length of the data keys');
            return;
        if len(data)!=data_nestkeys:
            print('length of data does not match the length of the data nestkeys');
            return;
        if type(data_keymap)!=list:
            print('data_keymap is not a list');
            return;
        
        #make the data
        for d_cnt,d in enumerate(data):
            self.add_data(d,data_keys[d_cnt],data_nestkeys[d_cnt]);

        #make form
        form = ddt_tile_html();
        form.make_tileparameters(
            {'tileheader':'Filter menu',
            'tiletype':'html',
            'tileid':"filtermenu1",
            'rowid':"row1",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"});
        form.make_parameters_form_01();
        self.add_parameters(form.get_parameters());
        self.update_tile2datamap("filtermenu1",[0]);

        #make svg
        cnt = 0;
        svgtileid = "tilesvg"+str(cnt);
        svgid = 'svg'+str(cnt);
        rowcnt = 2;
        colcnt = 1;
        # make the svg object
        svg = ddt_tile();
        svg.make_tileparameters(
            tileparameters={
            'tileheader':svgtileheader,
            'tiletype':'svg',
            'tileid':svgtileid,
            'rowid':"row"+str(rowcnt),
            'colid':"col"+str(colcnt),
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"
            });
        if not svgkeymap:
            svgkeymap = data_keymap;
        # make the svg parameters
        svg.make_svgparameters(
            svgparameters={
            "svgtype":svgtype,
            "svgkeymap":svgkeymap,
            'svgid':svgid,
            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
            "svgwidth":500,
            "svgheight":350,
            "svgfilters":svgfilters,
            "svgx1axislabel":data2_keymap['xdata'],
            "svgy1axislabel":data2_keymap['ydata']
            }
                );
        self.add_parameters(svg.get_parameters());
        self.update_tile2datamap(svgtileid,svgtile2datamap);
