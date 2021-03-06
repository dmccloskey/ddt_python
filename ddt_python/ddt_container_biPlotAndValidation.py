from .ddt_container import ddt_container
from .ddt_tile import ddt_tile
from .ddt_tile_html import ddt_tile_html

class ddt_container_biPlotAndValidation(ddt_container):
    def make_biPlotAndValidation(self,
        data1,data2,
        data1_keys,data1_nestkeys,data1_keymap,
        data2_keys,data2_nestkeys,data2_keymap,
        ):
        '''Make a biPlot and model validation plot
        INPUT:
        data1
        data2
        data1_keys
        data1_nestkeys
        data1_keymap
        data2_keys
        data2_nestkeys
        data2_keymap
        '''
        
        cnt = 0;

        #from 1: biplot
        form = ddt_tile();
        form.make_tileparameters(
            tileparameters={
            'tileheader':'Bi Plot filter menu',
            'tiletype':'html',
            'tileid':"filtermenu1",
            'rowid':"row1",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-4"}
            );
        form.make_htmlparameters(
            htmlparameters = {
            'htmlid':'filtermenuform1',
            "htmltype":'form_01',
            "formsubmitbuttonidtext":{'id':'submit1','text':'submit'},
            "formresetbuttonidtext":{'id':'reset1','text':'reset'},
            "formupdatebuttonidtext":{'id':'update1','text':'update'}},
            );
        self.add_parameters(form.get_parameters());
        self.update_tile2datamap("filtermenu1",[cnt]);
        self.add_filtermenu(
            {"filtermenuid":"filtermenu1",
            "filtermenuhtmlid":"filtermenuform1",
            "filtermenusubmitbuttonid":"submit1",
            "filtermenuresetbuttonid":"reset1",
            "filtermenuupdatebuttonid":"update1"}
            );

        #svg 1: biplot
        svg = ddt_tile();
        svg.make_tileparameters(
            tileparameters={
            'tileheader':'Bi Plot',
            'tiletype':'svg',
            'tileid':"tile1",
            'rowid':"row1",
            'colid':"col2",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-8"}
                );
        svg.make_svgparameters(
            svgparameters={
            "svgtype":'scatterlineplot2d_01',
            "svgkeymap":[data1_keymap,data1_keymap],
            'svgid':'svg1',
            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
            "svgwidth":500,"svgheight":350,
            "svgx1axislabel":"component",
            "svgy1axislabel":"variance explained",
    		'svgformtileid':'filtermenu1',}
            );
        self.add_parameters(svg.get_parameters());
        self.update_tile2datamap("tile1",[cnt,cnt]);

        # data 1:
        self.add_data(
            data1,
            data1_keys,
            data1_nestkeys
            );

        # increment the data counter
        cnt+=1;

        #form 2: validation
        form = ddt_tile();
        form.make_tileparameters(
            tileparameters={
            'tileheader':'Cross Validation filter menu',
            'tiletype':'html',
            'tileid':"filtermenu2",
            'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-4"}
            );
        form.make_htmlparameters(
            htmlparameters = {
            'htmlid':'filtermenuform2',
            "htmltype":'form_01',
            "formsubmitbuttonidtext":{'id':'submit2','text':'submit'},
            "formresetbuttonidtext":{'id':'reset2','text':'reset'},
            "formupdatebuttonidtext":{'id':'update12','text':'update'}},
            );
        self.add_parameters(form.get_parameters());
        self.update_tile2datamap("filtermenu2",[cnt]);
        self.add_filtermenu(
            {"filtermenuid":"filtermenu2",
            "filtermenuhtmlid":"filtermenuform2",
            "filtermenusubmitbuttonid":"submit2",
            "filtermenuresetbuttonid":"reset2",
            "filtermenuupdatebuttonid":"update2"}
            );

        #svg 2: validation
        svg = ddt_tile();
        svg.make_tileparameters(
            tileparameters={
            'tileheader':'Cross Validation',
            'tiletype':'svg',
            'tileid':"tile2",
            'rowid':"row2",
            'colid':"col2",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-8"
            });
        svg.make_svgparameters(
            svgparameters={
            "svgtype":'verticalbarschart2d_01',
            "svgkeymap":[data2_keymap],
            'svgid':'svg2',
            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
            "svgwidth":500,"svgheight":350,"svgy1axislabel":"Value",
            "svgfilters":None,
    		'svgformtileid':'filtermenu2',
            }
                );
        self.add_parameters(svg.get_parameters());
        self.update_tile2datamap("tile2",[cnt]);

        #table 2: validation
        crosstable = ddt_tile();
        crosstable.make_tileparameters(
            tileparameters = {
            'tileheader':'Cross Validation',
            'tiletype':'table',
            'tileid':"tile3",
            'rowid':"row3",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"}
            );
        crosstable.make_tableparameters(
            tableparameters = {
            "tablekeymap":[data2_keymap],
            "tabletype":'responsivetable_01',
            'tableid':'table2',
            "tablefilters":None,
            "tableheaders":None,
            "tableclass":"table  table-condensed table-hover"}
            );
        self.add_parameters(crosstable.get_parameters());
        self.update_tile2datamap("tile3",[cnt]);

        # add data 2
        self.add_data(
            data2,
            data2_keys,
            data2_nestkeys
            );
        # increment the data counter
        cnt+=1;
    def make_biPlot(self,
        data1,
        data1_keys,data1_nestkeys,data1_keymap,
        ):
        '''Make a biPlot
        INPUT:
        data1
        data1_keys
        data1_nestkeys
        data1_keymap
        '''
        
        cnt = 0;

        #from 1: biplot
        form = ddt_tile();
        form.make_tileparameters(
            tileparameters={
            'tileheader':'Bi Plot filter menu',
            'tiletype':'html',
            'tileid':"filtermenu1",
            'rowid':"row1",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-4"}
            );
        form.make_htmlparameters(
            htmlparameters = {
            'htmlid':'filtermenuform1',
            "htmltype":'form_01',
            "formsubmitbuttonidtext":{'id':'submit1','text':'submit'},
            "formresetbuttonidtext":{'id':'reset1','text':'reset'},
            "formupdatebuttonidtext":{'id':'update1','text':'update'}},
            );
        self.add_parameters(form.get_parameters());
        self.update_tile2datamap("filtermenu1",[cnt]);
        self.add_filtermenu(
            {"filtermenuid":"filtermenu1",
            "filtermenuhtmlid":"filtermenuform1",
            "filtermenusubmitbuttonid":"submit1",
            "filtermenuresetbuttonid":"reset1",
            "filtermenuupdatebuttonid":"update1"}
            );

        #svg 1: biplot
        svg = ddt_tile();
        svg.make_tileparameters(
            tileparameters={
            'tileheader':'Bi Plot',
            'tiletype':'svg',
            'tileid':"tile1",
            'rowid':"row1",
            'colid':"col2",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-8"}
                );
        svg.make_svgparameters(
            svgparameters={
            "svgtype":'scatterlineplot2d_01',
            "svgkeymap":[data1_keymap,data1_keymap],
            'svgid':'svg1',
            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
            "svgwidth":500,"svgheight":350,
            "svgx1axislabel":"component",
            "svgy1axislabel":"variance explained",
    		'svgformtileid':'filtermenu1',}
            );
        self.add_parameters(svg.get_parameters());
        self.update_tile2datamap("tile1",[cnt,cnt]);

        #table 1: Bi plot
        crosstable = ddt_tile();
        crosstable.make_tileparameters(
            tileparameters = {
            'tileheader':'Bi plot',
            'tiletype':'table',
            'tileid':"tile3",
            'rowid':"row3",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"}
            );
        crosstable.make_tableparameters(
            tableparameters = {
            "tablekeymap":[data1_keymap],
            "tabletype":'responsivetable_01',
            'tableid':'table1',
            "tablefilters":None,
            "tableheaders":None,
            "tableclass":"table  table-condensed table-hover"}
            );
        self.add_parameters(crosstable.get_parameters());
        self.update_tile2datamap("tile3",[cnt]);

        # data 1:
        self.add_data(
            data1,
            data1_keys,
            data1_nestkeys
            );

        # increment the data counter
        cnt+=1;
    def make_hyperparameter(self,
        data1,
        data1_keys,data1_nestkeys,data1_keymap,
        data_cnt=0,
        ):
        '''Make a hyperparameter bar plot
        INPUT:
        data1
        data1_keys
        data1_nestkeys
        data1_keymap
        '''

        #form 2: validation
        form = ddt_tile();
        form.make_tileparameters(
            tileparameters={
            'tileheader':'Cross Validation filter menu',
            'tiletype':'html',
            'tileid':"filtermenu1",
            'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-4"}
            );
        form.make_htmlparameters(
            htmlparameters = {
            'htmlid':'filtermenuform1',
            "htmltype":'form_01',
            "formsubmitbuttonidtext":{'id':'submit1','text':'submit'},
            "formresetbuttonidtext":{'id':'reset1','text':'reset'},
            "formupdatebuttonidtext":{'id':'update1','text':'update'}},
            );
        self.add_parameters(form.get_parameters());
        self.update_tile2datamap("filtermenu1",[data_cnt]);
        self.add_filtermenu(
            {"filtermenuid":"filtermenu1",
            "filtermenuhtmlid":"filtermenuform1",
            "filtermenusubmitbuttonid":"submit1",
            "filtermenuresetbuttonid":"reset1",
            "filtermenuupdatebuttonid":"update1"}
            );

        #svg 2: validation
        svg = ddt_tile();
        svg.make_tileparameters(
            tileparameters={
            'tileheader':'Cross Validation',
            'tiletype':'svg',
            'tileid':"tile2",
            'rowid':"row1",
            'colid':"col2",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-8"
            });
        svg.make_svgparameters(
            svgparameters={
            "svgtype":'verticalbarschart2d_01',
            "svgkeymap":[data1_keymap],
            'svgid':'svg2',
            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
            "svgwidth":500,"svgheight":350,"svgy1axislabel":"Value",
            "svgfilters":None,
    		'svgformtileid':'filtermenu1',
            }
                );
        self.add_parameters(svg.get_parameters());
        self.update_tile2datamap("tile2",[data_cnt]);

        #table 2: validation
        crosstable = ddt_tile();
        crosstable.make_tileparameters(
            tileparameters = {
            'tileheader':'Cross Validation',
            'tiletype':'table',
            'tileid':"tile3",
            'rowid':"row2",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"}
            );
        crosstable.make_tableparameters(
            tableparameters = {
            "tablekeymap":[data1_keymap],
            "tabletype":'responsivetable_01',
            'tableid':'table1',
            "tablefilters":None,
            "tableheaders":None,
            "tableclass":"table  table-condensed table-hover"}
            );
        self.add_parameters(crosstable.get_parameters());
        self.update_tile2datamap("tile3",[data_cnt]);

        # add data 1
        self.add_data(
            data1,
            data1_keys,
            data1_nestkeys
            );
        # increment the data counter
        data_cnt+=1;
    def make_impfeat(self,
        data1,
        data1_keys,data1_nestkeys,data1_keymap,
        data_cnt=0,
        ):
        '''Make a important feature bar plot
        INPUT:
        data1
        data1_keys
        data1_nestkeys
        data1_keymap
        '''

        #form 2: validation
        form = ddt_tile();
        form.make_tileparameters(
            tileparameters={
            'tileheader':'Important feature filter menu',
            'tiletype':'html',
            'tileid':"filtermenu1",
            'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-4"}
            );
        form.make_htmlparameters(
            htmlparameters = {
            'htmlid':'filtermenuform1',
            "htmltype":'form_01',
            "formsubmitbuttonidtext":{'id':'submit1','text':'submit'},
            "formresetbuttonidtext":{'id':'reset1','text':'reset'},
            "formupdatebuttonidtext":{'id':'update1','text':'update'}},
            );
        self.add_parameters(form.get_parameters());
        self.update_tile2datamap("filtermenu1",[data_cnt]);
        self.add_filtermenu(
            {"filtermenuid":"filtermenu1",
            "filtermenuhtmlid":"filtermenuform1",
            "filtermenusubmitbuttonid":"submit1",
            "filtermenuresetbuttonid":"reset1",
            "filtermenuupdatebuttonid":"update1"}
            );

        #svg 2: validation
        svg = ddt_tile();
        svg.make_tileparameters(
            tileparameters={
            'tileheader':'Important features',
            'tiletype':'svg',
            'tileid':"tile2",
            'rowid':"row1",
            'colid':"col2",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-8"
            });
        svg.make_svgparameters(
            svgparameters={
            "svgtype":'horizontalbarschart2d_01',
            "svgkeymap":[data1_keymap],
            'svgid':'svg2',
            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left':  250 },
            "svgwidth":450,"svgheight":900,
            "svgx1axislabel":"impfeat_value",
            "svgy1axislabel":"component_name",
    		'svgformtileid':'filtermenu1',
            }
                );
        self.add_parameters(svg.get_parameters());
        self.update_tile2datamap("tile2",[data_cnt]);

        #table 2: validation
        crosstable = ddt_tile();
        crosstable.make_tileparameters(
            tileparameters = {
            'tileheader':'Important features',
            'tiletype':'table',
            'tileid':"tile3",
            'rowid':"row2",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"}
            );
        crosstable.make_tableparameters(
            tableparameters = {
            "tablekeymap":[data1_keymap],
            "tabletype":'responsivetable_01',
            'tableid':'table1',
            "tablefilters":None,
            "tableheaders":None,
            "tableclass":"table  table-condensed table-hover"}
            );
        self.add_parameters(crosstable.get_parameters());
        self.update_tile2datamap("tile3",[data_cnt]);

        # add data 1
        self.add_data(
            data1,
            data1_keys,
            data1_nestkeys
            );
        # increment the data counter
        data_cnt+=1;
    def make_SPlot(self,
        data1,data_dict1,
        data1_keys,data1_nestkeys,data1_keymap,
        data_cnt=0,
        ):
        '''Make a important feature bar plot
        INPUT:
        data1
        data1_keys
        data1_nestkeys
        data1_keymap
        '''

        #form 2: validation
        form = ddt_tile();
        form.make_tileparameters(
            tileparameters={
            'tileheader':'S-Plot filter menu',
            'tiletype':'html',
            'tileid':"filtermenu1",
            'rowid':"row1",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-4"}
            );
        form.make_htmlparameters(
            htmlparameters = {
            'htmlid':'filtermenuform1',
            "htmltype":'form_01',
            "formsubmitbuttonidtext":{'id':'submit1','text':'submit'},
            "formresetbuttonidtext":{'id':'reset1','text':'reset'},
            "formupdatebuttonidtext":{'id':'update1','text':'update'}},
            );
        self.add_parameters(form.get_parameters());
        self.update_tile2datamap("filtermenu1",[data_cnt]);
        self.add_filtermenu(
            {"filtermenuid":"filtermenu1",
            "filtermenuhtmlid":"filtermenuform1",
            "filtermenusubmitbuttonid":"submit1",
            "filtermenuresetbuttonid":"reset1",
            "filtermenuupdatebuttonid":"update1"}
            );

        # add data 1
        self.add_data(
            data1,
            data1_keys,
            data1_nestkeys
            );

        #svg 2: validation
        svg = ddt_tile();
        for i in range(int(max(data_dict1.keys()))):
            axis = i+1;
            svgid = 'svg'+str(axis);
            colid = 'col'+str(axis+1);
            tileid = 'tile'+str(axis);
            svg.make_tileparameters(
                tileparameters={
                'tileheader':'S-Plot',
                'tiletype':'svg',
                'tileid':tileid,
                'rowid':"row1",
                'colid':colid,
                'tileclass':"panel panel-default",
                'rowclass':"row",
                'colclass':"col-sm-6"
                });
            svg.make_svgparameters(
                svgparameters={
                "svgtype":'volcanoplot2d_01',
                "svgkeymap":[data1_keymap],
                'svgid':'svg1',
                "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                "svgwidth":400,"svgheight":350,
                "svgx1axislabel":"loadings" + str(axis),
                "svgy1axislabel":"correlations" + str(axis),
                }
                    );
            self.add_parameters(svg.get_parameters());
            self.update_tile2datamap(tileid,[axis]);
            self.add_data(
                data_dict1[axis],
                data1_keys,
                data1_nestkeys
                );

        #table 2: validation
        crosstable = ddt_tile();
        crosstable.make_tileparameters(
            tileparameters = {
            'tileheader':'S-Plot',
            'tiletype':'table',
            'tileid':'tile'+str(axis+1),
            'rowid':"row2",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"}
            );
        crosstable.make_tableparameters(
            tableparameters = {
            "tablekeymap":[data1_keymap],
            "tabletype":'responsivetable_01',
            'tableid':'table1',
            "tablefilters":None,
            "tableheaders":None,
            "tableclass":"table  table-condensed table-hover"}
            );
        self.add_parameters(crosstable.get_parameters());
        self.update_tile2datamap('tile'+str(axis+1),[data_cnt]);
