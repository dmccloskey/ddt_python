from .ddt_container import ddt_container
from .ddt_tile import ddt_tile
from .ddt_tile_html import ddt_tile_html

class ddt_container_nSvgTable_nDataColumns(ddt_container):
    '''SVG visualization per data column'''
    def make_nSvgTable(self,
        data1,
        data1_keys,data1_nestkeys,
        data1_keymap_svg,
        data1_keymap_table,
        svgkeymaps,
        svgtile2datamaps,
        tileheader,
        svgtypes,
        tabletype,
        ):
        '''Make a filter menu + n SVGs + Table
        INPUT:
        data1 = listDict of all data
        parameters for filtermenu, svgs, and table
            data1_keys
            data1_nestkeys
            data1_keymap_table
        parameters for the svg objects
            data2_keymap_svg (1 list per svg visualization to specify a different data column)
        parameters for the table objects
            data2_keymap_table
        svgkeymap = (1 list per svg visualization), e.g. [data1_keymap]
        svgtile2datamap= (1 list per svg visualization), e.g. [0]
        tileheader = title for each of the tiles
        svgtype = type of svg (1 type per svg visualization)
        tabletype = type of table      
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

        # tile 1-n features:
        rowcnt = 1;
        colcnt = 1;
        cnt = 0;
        for i in range(len(svgtile2datamaps)):
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
                "svgtype":svgtypes[i],
                "svgkeymap":svgkeymaps[i],
                'svgid':'svg'+str(cnt),
                "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                "svgwidth":500,
                "svgheight":350,
                "svgx1axislabel":data1_keymap_svg[i]['xdata'],
                "svgy1axislabel":data1_keymap_svg[i]['ydata']
                }
                    );
            self.add_parameters(svg.get_parameters());
            self.update_tile2datamap(svgtileid,svgtile2datamaps[i]);
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
            "tablekeymap":[data1_keymap_table],
            "tableheaders":None,}
            );
        self.add_parameters(crosstable.get_parameters());
        self.update_tile2datamap("tabletile1",[0]);