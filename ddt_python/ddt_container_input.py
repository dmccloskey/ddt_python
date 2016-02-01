from .ddt_container_table import ddt_container_table
from .ddt_tile import ddt_tile
from .ddt_tile_html import ddt_tile_html

class ddt_container_input(ddt_container_table):
    def make_container_inputForm(self,
            data_1=[{'SQL_Query':''}],
            data1_keys=['SQL_Query'],
            data1_nestkeys=['SQL_Query'],
            data1_keymap=None,
            tileparameters_I={},
            tileheader='SQL Query',
            tileid="htmlqueryraw01",
            tileclass="panel panel-default",
            rowclass="row",
            colclass="col-sm-12",
            formparameters_I={},
            htmlid='htmlqueryform01',
            htmltype='formquery_01',
            formpostbuttonidtext={'id':'post1','text':'execute'},
            formurl='SQLQuery',
            htmlalert=None, 
            rowcnt=1,colcnt=1,
            datacnt=0,
            ):
        '''make a query form
        ATTRIBUTES:
        text input form and execute button
        INPUT:
        data_1,
        data1_keys,
        data1_nestkeys
        tileparameters_I = {} of tile parameters
            or each tile input parameter can be specified individually
        formparameters_I = {} of form parameters
            or each form input parameter can be specified individually
        '''

        #make the data
        self.add_data(data_1,data1_keys,data1_nestkeys);

        #make the row and col ids
        rowid = 'row' + str(rowcnt);
        colid = 'col' + str(colcnt);

        #make form
        form = ddt_tile_html();
        # handle the tile parameter input:
        if tileparameters_I:
            tileparameters = tileparameters_I;
            tileparameters['rowid']=rowid;
            tileparameters['colid']=colid;
            tileid = tileparameters_I['tileid'];
        else:
            tileparameters = {
            'tileheader':tileheader,
            'tiletype':'html',
            'tileid':tileid,
            'rowid':rowid,
            'colid':colid,
            'tileclass':tileclass,
            'rowclass':rowclass,
            'colclass':colclass
            };
        form.make_tileparameters(tileparameters);
        #handle the html parameter input:
        if formparameters_I:
            formparameters = formparameters_I;
        else: 
            formparameters = {
                'htmlid':htmlid,
                'htmltype':htmltype,
                "formpostbuttonidtext":formpostbuttonidtext,
                'formurl':formurl,
                'htmlalert':htmlalert,
                };
        form.make_htmlparameters(formparameters);

        self.add_parameters(form.get_parameters());
        self.update_tile2datamap(tileid,[datacnt]);