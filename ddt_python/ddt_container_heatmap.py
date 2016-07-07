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

    def make_data_dendrogram(self,data_1):
        '''make default data
        INPUT:
        data_1 = [{},...] of database rows
        '''
        data1_keys = [
            'analysis_id','pdist_metric','linkage_method','value_units',
            ]
        data1_nestkeys = [
            'analysis_id'
            ];
        self.add_data(data_1,data1_keys,data1_nestkeys);

    def make_keymap_dendrogram(self):
        '''make default keymap
        INPUT:
        OUTPUT:
        '''
        
        data1_keymap = {
            'xdata':'length',
            'ydata':'length',
            'serieslabel':'color',
            'featureslabel':'name'
            };
        return data1_keymap;

    def make_container_heatmap(self,data_1,
            svgcolorcategory='blue2gold64RBG',
            svgcolordomain='min,0,max',
            data1_keymap=None,
            data1_nestkeys=None,
            data1_keys=None,
            svgparameters_I={}
            ):
        '''make the heatmap container object
        INPUT:
        OUTPUT:
        '''
        #make the data
        if data1_keys and data1_nestkeys:
            self.add_data(
                data_1,
                data1_keys,
                data1_nestkeys
                );
        else:
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
        if not data1_keymap:
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
        svgparameters.update(svgparameters_I)
        heatmap.make_svgparameters(
            svgparameters = svgparameters
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

    def make_container_dendrogram(self,data_1,data_2,
            svgcolorcategory='blue2gold64RBG',
            svgcolordomain='min,0,max',
            data1_keymap=None,
            data1_nestkeys=None,
            data1_keys=None,
            data2_keymap=None,
            data2_nestkeys=None,
            data2_keys=None,
            data1_svgparameters_I={},
            data2_svgparameters_I={},
            ):
        '''make the dendrogram container object
        INPUT:
        OUTPUT:
        '''
        data_cnt=0;
        row_cnt=1;

        form = ddt_tile_html();
        form.make_tileparameters(
            {'tileheader':'Filter menu',
            'tiletype':'html',
            'tileid':"filtermenu"+str(data_cnt),
            'rowid':"row"+str(row_cnt),
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-6"});
        form.make_parameters_form_01();
        self.add_parameters(form.get_parameters());
        self.update_tile2datamap("filtermenu"+str(data_cnt),[data_cnt]);

        row_cnt+=1;
        
        data_cnt,row_cnt=self._make_container_dendrogram(data_1,
            svgcolorcategory=svgcolorcategory,
            svgcolordomain=svgcolordomain,
            data1_keymap=data1_keymap,
            data1_nestkeys=data1_nestkeys,
            data1_keys=data1_keys,
            data1_svgparameters_I=data1_svgparameters_I,
            data_cnt=data_cnt,
            row_cnt=row_cnt
            );

        data_cnt,row_cnt=self._make_container_dendrogram(data_2,
            svgcolorcategory=svgcolorcategory,
            svgcolordomain=svgcolordomain,
            data1_keymap=data2_keymap,
            data1_nestkeys=data2_nestkeys,
            data1_keys=data2_keys,
            data1_svgparameters_I=data2_svgparameters_I,
            data_cnt=data_cnt,
            row_cnt=row_cnt,
            );

    def _make_container_dendrogram(self,data_1,
            svgcolorcategory='blue2gold64RBG',
            svgcolordomain='min,0,max',
            data1_keymap=None,
            data1_nestkeys=None,
            data1_keys=None,
            data1_svgparameters_I={},
            data_cnt=0,
            row_cnt=0,
            ):
        '''make the heatmap container object
        INPUT:
        OUTPUT:
        '''

        #make the data
        if data1_keys and data1_nestkeys:
            self.add_data(
                data_1,
                data1_keys,
                data1_nestkeys
                );
        else:
            self.make_data_dendrogram(data_1);

        #make dendrogram
        if not data1_keymap:
            data1_keymap = self.make_keymap_dendrogram();
        dendrogram = ddt_tile();
        dendrogram.make_tileparameters(
            tileparameters = {
                'tileheader':'dendrogram',
                'tiletype':'svg',
                'tileid':"tile"+str(row_cnt),
                'rowid':"row"+str(row_cnt),
                'colid':"col1",
                'tileclass':"panel panel-default",
                'rowclass':"row",
                'colclass':"col-sm-6"}
            );
        svgparameters = {
                "svgkeymap":[data1_keymap],
                'svgid':"svg"+str(data_cnt),
                #"svgtype":'verticaldendrogram2d_01',
                #"svgmargin":{ 'top': 50, 'right': 50, 'bottom': 250, 'left': 50 },
                #"svgwidth":350,
                #"svgheight":500,
                "svgtype":'radialdendrogram2d_01',
                "svgmargin":{ 'top': 100, 'right': 100, 'bottom': 100, 'left': 100 },
                "svgwidth":350,
                "svgheight":350,
                "svgduration":750,
                "svgradius":250,
                "svgstratifyid":'name',
                "svgstratifyparentid":'parent',
                #'svgcolorscale':'quantile',
                #'svgcolorcategory':svgcolorcategory,
                #'svgcolordomain':svgcolordomain,
                #'svgcolordatalabel':'value',
                }
        svgparameters.update(data1_svgparameters_I)
        dendrogram.make_svgparameters(
            svgparameters = svgparameters
            );
        self.add_parameters(dendrogram.get_parameters());
        self.update_tile2datamap("tile"+str(row_cnt),[data_cnt]);

        #update the counter
        row_cnt+=1;

        #make table
        crosstable = ddt_tile();
        crosstable.make_tileparameters(
            tileparameters = {
            'tileheader':'Table',
            'tiletype':'table',
            'tileid':"tile"+str(row_cnt),
            'rowid':"row"+str(row_cnt),
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-6"}
            );
        crosstable.make_tableparameters(
            tableparameters = {
                "tabletype":'responsivetable_01',
                "tablekeymap":[data1_keymap],
                'tableid':"table"+str(data_cnt),
                "tablefilters":None,
                "tableclass":"table  table-condensed table-hover"}
            );
        self.add_parameters(crosstable.get_parameters());
        self.update_tile2datamap("tile"+str(row_cnt),[data_cnt]);
        
        #update the counters
        data_cnt+=1;
        row_cnt+=1;

        return data_cnt,row_cnt;