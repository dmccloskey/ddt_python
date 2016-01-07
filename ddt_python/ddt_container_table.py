from .ddt_container import ddt_container
from .ddt_tile import ddt_tile
from .ddt_tile_html import ddt_tile_html

class ddt_container_table(ddt_container):

    def make_container_table(self,
            data_1,
            data1_keys,
            data1_nestkeys,
            data1_keymap,
            tabletype='responsivetable_01',
            tabletileheader='Table',
            tablefilters=None,
            tableheaders=None
            ):
        '''make the table container object
        ATTRIBUTES:
        bound data
        filtermenu and table share the same data

        INPUT:

        OUTPUT:

        '''
        
        #make the data
        self.add_data(data_1,data1_keys,data1_nestkeys);

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

        #make table
        crosstable = ddt_tile();
        crosstable.make_tileparameters(
            tileparameters = {
            'tileheader':tabletileheader,
            'tiletype':'table',
            'tileid':"tile1",
            'rowid':"row2",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"}
            );
        crosstable.make_tableparameters(
            tableparameters = {
                "tabletype":tabletype,
                "tablekeymap":[data1_keymap],
                'tableid':'table1',
                "tablefilters":tablefilters,
                "tableheaders":tableheaders,
                "tableclass":"table  table-condensed table-hover"}
            );
        self.add_parameters(crosstable.get_parameters());
        self.update_tile2datamap("tile1",[0]);