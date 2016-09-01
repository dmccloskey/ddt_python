from .ddt_container import ddt_container
from .ddt_tile import ddt_tile
from .ddt_tile_html import ddt_tile_html

class ddt_container_filterMenuAndChart2dAndTable(ddt_container):
    def make_filterMenuAndChart2dAndTable(self,
        data_filtermenu,
        data_filtermenu_keys,data_filtermenu_nestkeys,data_filtermenu_keymap,
        data_svg_keys,data_svg_nestkeys,data_svg_keymap,
        data_table_keys,data_table_nestkeys,data_table_keymap,
        data_svg,
        data_table,
        svgtype,
        tabletype,
        svgx1axislabel='',
        svgy1axislabel='',
        tablekeymap = [],
        svgkeymap = [],
        formtile2datamap=[0],
        tabletile2datamap=[0],
        svgtile2datamap=[0],
        svgfilters=None,
        svgtileheader=None,
        svgparameters_I={},
        tablefilters=None,
        tableheaders=None
        ):
        '''Make a filter menu + n SVGs + Table
        INPUT:
        data_filtermenu = listDict of all data
        data_svg = listDict of all data (single plot with a different data from data 1 or a single plot with data 1/2)
                dictColumn of all data (dictionary of data split into different SVGs, required for multiple plots);
        data_table = listDict of table data
        parameters for filtermenu and table
            data_x_keys
            data_x_nestkeys
            data_x_keymap
        parameters for the svg objects
            data2_keys
            data2_nestkeys
            data2_keymap
        tileheader = title for each of the tiles
        svgtype = type of svg (TODO: add optional input for specifying specific svgs for multiple plots)
        tabletype = type of table
        OPTIONAL INPUT for single plot:        
        svgkeymap = default, [data2_keymap],
        svgtile2datamap= default, [0],

        svgparameters_I = additional parameters to add or override default parameters

        '''

        data_filtermenu,data_svg,data_table,add_svg_data,add_table_data = self.parse_data(data_filtermenu,data_svg,data_table);

        data_filtermenu_keys,data_filtermenu_nestkeys,data_filtermenu_keymap,\
            data_svg_keys,data_svg_nestkeys,data_svg_keymap,\
            data_table_keys,data_table_nestkeys,data_table_keymap = self.parse_keys(
                data_filtermenu_keys,data_filtermenu_nestkeys,data_filtermenu_keymap,
                data_svg_keys,data_svg_nestkeys,data_svg_keymap,
                data_table_keys,data_table_nestkeys,data_table_keymap);

        #initialize data counter
        datacnt = 0;

        #make the form
        form = ddt_tile();
        form.make_tileparameters(
            tileparameters={
            'tileheader':'Filter menu',
            'tiletype':'html',
            'tileid':"filtermenu1",
            'rowid':"row1",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-6"}
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
        self.update_tile2datamap("filtermenu1",formtile2datamap);
        self.add_filtermenu(
            {"filtermenuid":"filtermenu1",
            "filtermenuhtmlid":"filtermenuform1",
            "filtermenusubmitbuttonid":"submit1",
            "filtermenuresetbuttonid":"reset1",
            "filtermenuupdatebuttonid":"update1"}
            );

         # filtermenu data:
        self.add_data(
            data_filtermenu,
            data_filtermenu_keys,
            data_filtermenu_nestkeys
            );
        datacnt += 1;

        #make the svg objects
        if type(data_svg) is dict:
            rowcnt = self.make_nChart2dDictList(
                data_svg,
                data_svg_keys,
                data_svg_nestkeys,
                data_svg_keymap,
                svgtype,
                svgkeymap,
                svgtile2datamap,
                svgfilters,
                svgtileheader,
                svgparameters_I=svgparameters_I);
        elif type(svgtile2datamap[0]) is list:
            rowcnt = self.make_nChart2dListDict(
                add_svg_data,
                data_svg,
                data_svg_keys,
                data_svg_nestkeys,
                data_svg_keymap,
                svgtype,
                svgkeymap,
                svgtile2datamap,
                svgfilters,
                svgtileheader,
                svgparameters_I=svgparameters_I);
        else:
            rowcnt = self.make_chart2dListDict(
                add_svg_data,
                data_svg,
                data_svg_keys,
                data_svg_nestkeys,
                data_svg_keymap,
                svgtype,
                svgkeymap,
                svgtile2datamap,
                svgfilters,
                svgtileheader,
                svgparameters_I=svgparameters_I
                );
            
        # make the table object
        crosstable = ddt_tile();
        crosstable.make_tileparameters(
            tileparameters = {
            'tileheader':'Table',
            'tiletype':'table',
            'tileid':"tabletile1",
            'rowid':"row"+str(rowcnt+1),
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"
            }
            );
        crosstable.make_tableparameters(
            tableparameters = {
            "tabletype":tabletype,
            'tableid':'table1',
            "tablefilters":tablefilters,
            "tableclass":"table  table-condensed table-hover",
    		'tableformtileid':'tile1',
            "tablekeymap":tablekeymap,
            "tableheaders":tableheaders,}
            );
        self.add_parameters(crosstable.get_parameters());
        self.update_tile2datamap("tabletile1",tabletile2datamap);

        if add_table_data:
            self.add_data(
                data_table,
                data_table_keys,
                data_table_nestkeys
                );
            datacnt += 1;

    def make_nChart2dDictList(self,
            data_svg,
            data_svg_keys,
            data_svg_nestkeys,
            data_svg_keymap,
            svgtype,
            svgkeymap,
            svgtile2datamap,
            svgfilters,
            svgtileheader,
            svgparameters_I={},):
        '''make the SVG objects from a dictList
        USE:
        large data set partitioned into individual data sets
        same svgtype
        same keys, nestkeys, and keymaps
        
        TODO: add support for scatter line plot
        '''
        
        rowcnt = 1;
        colcnt = 1;
        cnt = 0;
        for k,v in data_svg.items():
            svgtileid = "tilesvg"+str(cnt);
            svgid = 'svg'+str(cnt);
            iter=cnt+1; #start at 1
            if (cnt % 2 == 0): 
                rowcnt = rowcnt+1;#even 
                colcnt = 1;
            else:
                colcnt = colcnt+1;
            # svg
            svg = ddt_tile();
            svg.make_tileparameters(
                tileparameters={
                'tileheader':svgtileheader + ' ' + str(k),
                'tiletype':'svg',
                'tileid':svgtileid,
                'rowid':"row"+str(rowcnt),
                'colid':"col"+str(colcnt),
                'tileclass':"panel panel-default",
                'rowclass':"row",
                'colclass':"col-sm-6"
                });
            svg.make_svgparameters(
                svgparameters={
                "svgtype":svgtype,
                "svgkeymap":[data_svg_keymap],
                'svgid':'svg'+str(cnt),
                "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                "svgwidth":500,
                "svgheight":350,
                "svgx1axislabel":data_svg_keymap['xdata'],
                "svgy1axislabel":data_svg_keymap['ydata']
                }
                    );
            svg.specificparameters.update(svgparameters_I);
            self.add_parameters(svg.get_parameters());
            self.update_tile2datamap(svgtileid,[iter]);
            self.add_data(
                v,
                data_svg_keys,
                data_svg_nestkeys
                );
            cnt+=1;

        return rowcnt;
    def make_nChart2dListDict(self,
            add_svg_data,
            data_svg,
            data_svg_keys,
            data_svg_nestkeys,
            data_svg_keymap,
            svgtype,
            svgkeymap,
            svgtile2datamap,
            svgfilters,
            svgtileheader,
            svgparameters_I={},):
        '''make the SVG objects from a listDict
        USE:
        multiple views of the same data set
        multiple svgtypes
        multiple keys, nestkeys, and keymaps
        '''
        rowcnt = 1;
        colcnt = 1;
        cnt = 0;
        for i in range(len(svgtile2datamap)):
            svgtileid = "tilesvg"+str(cnt);
            svgid = 'svg'+str(cnt);
            iter=cnt+1; #start at 1
            if (cnt % 2 == 0): 
                rowcnt = rowcnt+1;#even 
                colcnt = 1;
            else:
                colcnt = colcnt+1;
            # svg
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
                'colclass':"col-sm-6"
                });
            svg.make_svgparameters(
                svgparameters={
                "svgtype":svgtype[i],
                "svgkeymap":svgkeymap[i],
                'svgid':'svg'+str(cnt),
                "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                "svgwidth":500,
                "svgheight":350,
                "svgx1axislabel":data_svg_keymap[i]['xdata'],
                "svgy1axislabel":data_svg_keymap[i]['ydata']
                }
                    );
            svgparameters.update(svgparameters_I);
            self.add_parameters(svg.get_parameters());
            self.update_tile2datamap(svgtileid,svgtile2datamap[i]);
            cnt+=1;
        return rowcnt;

        if add_svg_data:
            self.add_data(
                data_svg,
                data_svg_keys,
                data_svg_nestkeys
                );

    def make_chart2dListDict(self,
            add_svg_data,
            data_svg,
            data_svg_keys,
            data_svg_nestkeys,
            data_svg_keymap,
            svgtype,
            svgkeymap,
            svgtile2datamap,
            svgfilters,
            svgtileheader,
            svgparameters_I={},
            ):
        '''make a single SVG object from a listDict
        '''
        
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
            'colclass':"col-sm-6"
            });
        # make the svg parameters
        svgparameters={
            "svgtype":svgtype,
            "svgkeymap":svgkeymap,
            'svgid':svgid,
            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
            "svgwidth":350,
            "svgheight":250,
            "svgx1axislabel":data_svg_keymap['xdata'],
            "svgy1axislabel":data_svg_keymap['ydata']
            };
        svgparameters.update(svgparameters_I);
        svg.make_svgparameters(
            svgparameters=svgparameters
                );
        self.add_parameters(svg.get_parameters());
        self.update_tile2datamap(svgtileid,svgtile2datamap);

        #add data 2
        if add_svg_data:
            self.add_data(
                data_svg,
                data_svg_keys,
                data_svg_nestkeys
                );
            cnt+=1;
        return rowcnt;

    def parse_data(self,data_filtermenu,data_svg,data_table):
        '''parse out the data'''
        
        add_svg_data = True;
        add_table_data = True;
        #parse out the data
        if data_filtermenu is None or not data_filtermenu:
            print('no filtermenu data provided.');
            #exit(-1);
            data_filtermenu = [];
            data_svg = data_filtermenu;
            add_svg_data = False;
            data_table = data_filtermenu;
            add_table_data = False;
        if data_svg is None or not data_svg:
            data_svg = data_filtermenu;
            add_svg_data = False;
        if data_table is None or not data_table:
            data_table = data_filtermenu;
            add_table_data = False;
        return data_filtermenu,data_svg,data_table,add_svg_data,add_table_data;

    def parse_keys(self,
        data_filtermenu_keys,data_filtermenu_nestkeys,data_filtermenu_keymap,
        data_svg_keys,data_svg_nestkeys,data_svg_keymap,
        data_table_keys,data_table_nestkeys,data_table_keymap,
        ):
        '''parse out the data keys'''
       
        if data_filtermenu_keys is None or not data_filtermenu_keys:
            print('no filtermenu keys provided.');
            exit(-1);
        if data_svg_keys is None or not data_svg_keys:
            data_svg_keys = data_filtermenu_keys;
            data_svg_nestkeys = data_filtermenu_nestkeys;
            data_svg_keymap = data_filtermenu_keymap;
        if data_table_keys is None or not data_table_keys:
            data_table_keys = data_filtermenu_keys;
            data_table_nestkeys = data_filtermenu_nestkeys;
            data_table_keymap = data_filtermenu_keymap;

        return data_filtermenu_keys,data_filtermenu_nestkeys,data_filtermenu_keymap,\
            data_svg_keys,data_svg_nestkeys,data_svg_keymap,\
            data_table_keys,data_table_nestkeys,data_table_keymap