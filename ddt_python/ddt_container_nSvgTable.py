from .ddt_container import ddt_container
from .ddt_tile import ddt_tile
from .ddt_tile_html import ddt_tile_html

class ddt_container_nSvgTable(ddt_container):
    def make_nSvgTable(self,
        data1,data2,
        data1_keys,data1_nestkeys,data1_keymap,
        data2_keys,data2_nestkeys,data2_keymap,
        tileheader,
        svgtype,
        tabletype,
        single_plot_I=True,
        svgx1axislabel='',
        svgy1axislabel='',
        ):
        '''Make a filter menu + n SVGs + Table
        INPUT:
        data1 = listDict of all data
        data2 = dictionary of data split into different SVGs (optional)
        parameters for filtermenu and table
            data1_keys
            data1_nestkeys
            data1_keymap
        parameters for the svg objects
            data2_keys
            data2_nestkeys
            data2_keymap
        single_plot_I = plot all data on a single svg or partition into seperate SVGs
                        True, only data1 will be used
                        False, data2 must specified
        '''
        
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
        self.update_tile2datamap("filtermenu1",[0]);
        self.add_filtermenu(
            {"filtermenuid":"filtermenu1",
            "filtermenuhtmlid":"filtermenuform1",
            "filtermenusubmitbuttonid":"submit1",
            "filtermenuresetbuttonid":"reset1",
            "filtermenuupdatebuttonid":"update1"}
            );

         # data 1:
        self.add_data(
            data1,
            data1_keys,
            data1_nestkeys
            );

        # tile 1-n features: count
        if not single_plot_I:
            rowcnt = 1;
            colcnt = 1;
            cnt = 0;
            for k,v in data2.items():
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
                    'tileheader':tileheader,
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
                    "svgkeymap":[data2_keymap],
                    'svgid':'svg'+str(cnt),
                    "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "svgwidth":500,
                    "svgheight":350,
                    "svgx1axislabel":data2_keymap['xdata'],
                    "svgy1axislabel":data2_keymap['ydata']
                    }
                        );
                self.add_parameters(svg.get_parameters());
                self.update_tile2datamap(svgtileid,[iter]);
                self.add_data(
                    v,
                    data2_keys,
                    data2_nestkeys
                    );
                cnt+=1;
        else:
            cnt = 0;
            svgtileid = "tilesvg"+str(cnt);
            svgid = 'svg'+str(cnt);
            rowcnt = 2;
            colcnt = 1;
            # make the svg object
            svg = ddt_tile();
            svg.make_tileparameters(
                tileparameters={
                'tileheader':tileheader,
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
                "svgkeymap":[data2_keymap],
                'svgid':'svg'+str(cnt),
                "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                "svgwidth":350,
                "svgheight":250,
                "svgx1axislabel":data2_keymap['xdata'],
                "svgy1axislabel":data2_keymap['ydata']
                }
                    );
            self.add_parameters(svg.get_parameters());
            self.update_tile2datamap(svgtileid,[1]);

            #add data 2
            if data2:
                self.add_data(
                    data2,
                    data2_keys,
                    data2_nestkeys
                    );
            cnt+=1;
            
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
            "tablefilters":None,
            "tableclass":"table  table-condensed table-hover",
    		'tableformtileid':'tile1',
            "tablekeymap":[data2_keymap],
            "tableheaders":None,}
            );
        self.add_parameters(crosstable.get_parameters());
        self.update_tile2datamap("tabletile1",[0]);