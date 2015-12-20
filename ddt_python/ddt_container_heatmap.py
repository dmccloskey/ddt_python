from .ddt_container import ddt_container
from .ddt_tile import ddt_tile
from .ddt_tile_html import ddt_tile_html

class ddt_container_heatmap(ddt_container):

    def make_data_heatmap(self,data_1):
        '''make default data
        INPUT:
        data_1 = [{},...] of database rows
        '''
        data1_keys = [
            'analysis_id',
            'row_label',
            'col_label',
            'row_index',
            'col_index',
            'row_leaves',
            'col_leaves',
            'col_pdist_metric',
            'row_pdist_metric',
            'col_linkage_method',
            'row_linkage_method',
            'value_units'
            ]
        data1_nestkeys = [
            'row_label',
            'col_label'
            ];
        self.add_data(data_1,data1_keys,data1_nestkeys);

    def make_keymap_heatmap(self):
        '''make default keymap
        INPUT:
        OUTPUT:
        '''
        
        data1_keymap = {
            'xdata':'row_leaves',
            'ydata':'col_leaves',
            'zdata':'value',
            'rowslabel':'row_label',
            'columnslabel':'col_label',
            'rowsindex':'row_index',
            'columnsindex':'col_index',
            'rowsleaves':'row_leaves',
            'columnsleaves':'col_leaves'
            };
        return data1_keymap;

    def make_container_heatmap(self,data_1,
            svgcolorcategory='blue2gold64RBG',
            svgcolordomain='min,0,max',
            ):
        '''make the heatmap container object
        INPUT:
        OUTPUT:
        '''
        #make the data
        self.make_data_heatmap(data_1);

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
            'colclass':"col-sm-6"});
        form.make_parameters_form_01();
        self.add_parameters(form.get_parameters());
        self.update_tile2datamap("filtermenu1",[0]);

        #make datalist
        datalist = ddt_tile_html();
        datalist.make_tileparameters(
            {'tileheader':'heatmap sort',
            'tiletype':'html',
            'tileid':"tile1",
            'rowid':"row2",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-4"}
            );
        datalist.make_parameters_datalist_01();
        self.add_parameters(datalist.get_parameters());
        self.update_tile2datamap("tile1",[0]);

        #make heatmap
        data1_keymap = self.make_keymap_heatmap();
        heatmap = ddt_tile();
        heatmap.make_tileparameters(
            tileparameters = {
                'tileheader':'heatmap',
                'tiletype':'svg',
                'tileid':"tile2",
                'rowid':"row3",
                'colid':"col1",
                'tileclass':"panel panel-default",
                'rowclass':"row",
                'colclass':"col-sm-12"}
            );
        heatmap.make_svgparameters(
            svgparameters = {
                "svgtype":'heatmap2d_01',
                "svgkeymap":[data1_keymap],
                'svgid':'svg1',
                'svgcellsize':18,
                'svgmargin':{ 'top': 200, 'right': 50, 'bottom': 100, 'left': 200 },
                'svgcolorscale':'quantile',
                'svgcolorcategory':svgcolorcategory,
                'svgcolordomain':svgcolordomain,
                'svgcolordatalabel':'value',
                'svgdatalisttileid':'tile1'}
            );
        self.add_parameters(heatmap.get_parameters());
        self.update_tile2datamap("tile2",[0]);

        #make cross-table
        crosstable = ddt_tile();
        crosstable.make_tileparameters(
            tileparameters = {
            'tileheader':'Cross Table',
            'tiletype':'table',
            'tileid':"tile3",
            'rowid':"row4",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"}
            );
        crosstable.make_tableparameters(
            tableparameters = {
                "tabletype":'responsivecrosstable_01',
                "tablekeymap":[data1_keymap],
                'tableid':'table1',
                "tablefilters":None,
                "tableclass":"table  table-condensed table-hover"}
            );
        self.add_parameters(crosstable.get_parameters());
        self.update_tile2datamap("tile3",[0]);