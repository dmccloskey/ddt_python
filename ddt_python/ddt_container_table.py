from .ddt_container import ddt_container
from .ddt_tile import ddt_tile
from .ddt_tile_html import ddt_tile_html

class ddt_container_table(ddt_container):

    def make_container_queryRawForm(self,
            data_1=[{'Raw_SQL':''}],
            data1_keys=['Raw_SQL'],
            data1_nestkeys=['Raw_SQL'],
            data1_keymap=None,
            querytileheader='SQL Query',
            rowcnt=1,colcnt=1,
            datacnt=0,
            htmlalert=None,    
            ):
        '''make a query form
        ATTRIBUTES:
        text input form and execute button
        INPUT:
        querytileheader = string, e.g., "sql query"
        '''

        #make the data
        self.add_data(data_1,data1_keys,data1_nestkeys);

        #make the row and col ids
        rowid = 'row' + str(rowcnt);
        colid = 'col' + str(colcnt);

        #make form
        form = ddt_tile_html();
        form.make_tileparameters(
            {'tileheader':querytileheader,
            'tiletype':'html',
            'tileid':"htmlqueryraw01",
            'rowid':rowid,
            'colid':colid,
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"});
        form.make_parameters_formQueryRaw_01(alert=htmlalert);
        self.add_parameters(form.get_parameters());
        self.update_tile2datamap("htmlqueryraw01",[datacnt]);

    def make_container_table(self,
            data_1,
            data1_keys,
            data1_nestkeys,
            data1_keymap,
            tabletype='responsivetable_01',
            tabletileheader='Table',
            tablefilters=None,
            tableheaders=None,
            rowcnt=1,colcnt=1,
            datacnt = 0
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

        #make the row and col ids
        rowid = 'row' + str(rowcnt);
        colid = 'col' + str(colcnt);

        #make form
        form = ddt_tile_html();
        form.make_tileparameters(
            {'tileheader':'Filter menu',
            'tiletype':'html',
            'tileid':"filtermenu1",
            'rowid':rowid,
            'colid':colid,
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"});
        form.make_parameters_form_01();
        self.add_parameters(form.get_parameters());
        self.update_tile2datamap("filtermenu1",[datacnt]);

        #make the row and col ids
        rowcnt += 1;
        rowid = 'row' + str(rowcnt);
        colid = 'col' + str(colcnt);

        #make table
        crosstable = ddt_tile();
        crosstable.make_tileparameters(
            tileparameters = {
            'tileheader':tabletileheader,
            'tiletype':'table',
            'tileid':"tile1",
            'rowid':rowid,
            'colid':colid,
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
        self.update_tile2datamap("tile1",[datacnt]);