from .ddt_container_table import ddt_container_table
from .ddt_tile import ddt_tile
from .ddt_tile_html import ddt_tile_html

class ddt_container_SQL(ddt_container_table):

    def make_container_queryForm(self,
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

    def make_container_querySelectForm(self,
            data_1=[
                {'SELECT':'',
                    'FROM':'',
                    'WHERE':'',
                    'GROUP_BY':'',
                    'HAVING':'',
                    'ORDER_BY':'',
                    'LIMIT':'',
                    'OFFSET':'',
                    }],
            htmlalert=None, 
            rowcnt=1,
            colcnt=1,
            datacnt=0,
            ):
        '''default tile and form parameters for a sql select form'''
        #data
        data1_keys=['SELECT','FROM','WHERE','GROUP_BY','HAVING','ORDER_BY','LIMIT','OFFSET'];
        data1_nestkeys=['SELECT'];
        data1_keymap=None;

        #tileparameters
        tileheader='SQL SELECT';
        tileid="htmlqueryselect01";
        tileclass="panel panel-default";
        rowclass="row";
        colclass="col-sm-6";
        tileparameters={
            'tiletype':'html',
            'tileheader':tileheader,
            'tileid':tileid,
            'tileclass':tileclass,
            'rowclass':rowclass,
            'colclass':colclass,
            };

        #formparameters
        htmlid='htmlqueryselectform01';
        htmltype='formquery_01';
        formpostbuttonidtext={'id':'posthtmlqueryselectform01','text':'execute'};
        formurl='SQLQuery';
        formparameters = {
                'htmlid':htmlid,
                'htmltype':htmltype,
                "formpostbuttonidtext":formpostbuttonidtext,
                'formurl':formurl,
                'htmlalert':htmlalert,
                };
        #add the form to the container
        self.make_container_queryForm(
            data_1,
            data1_keys,
            data1_nestkeys,
            data1_keymap,
            tileparameters_I=tileparameters,
            formparameters_I=formparameters, 
            rowcnt=rowcnt,
            colcnt=colcnt,
            datacnt=datacnt,
            );

    def make_container_queryRawForm(self,
            data_1=[{'Raw_SQL':''}],
            htmlalert=None, 
            rowcnt=1,
            colcnt=1,
            datacnt=0,
            ):
        '''default tile and form parameters for a raw sql query form'''

        #data
        data1_keys=['Raw_SQL'];
        data1_nestkeys=['Raw_SQL'];
        data1_keymap=None;

        #tileparameters
        tileheader='Raw SQL';
        tileid="htmlqueryraw01";
        tileclass="panel panel-default";
        rowclass="row";
        colclass="col-sm-12";
        tileparameters={
            'tiletype':'html',
            'tileheader':tileheader,
            'tileid':tileid,
            'tileclass':tileclass,
            'rowclass':rowclass,
            'colclass':colclass,
            };

        #formparameters
        htmlid='htmlqueryrawform01';
        htmltype='formquery_01';
        formpostbuttonidtext={'id':'posthtmlqueryrawform01','text':'execute'};
        formurl='SQLQuery';
        formparameters = {
                'htmlid':htmlid,
                'htmltype':htmltype,
                "formpostbuttonidtext":formpostbuttonidtext,
                'formurl':formurl,
                'htmlalert':htmlalert,
                };

        #add the form to the container
        self.make_container_queryForm(
            data_1,
            data1_keys,
            data1_nestkeys,
            data1_keymap,
            tileparameters_I=tileparameters,
            formparameters_I=formparameters, 
            rowcnt=rowcnt,
            colcnt=colcnt,
            datacnt=datacnt,
            );

    def make_container_queryInsertForm(self,
            data_1=[
                {'INSERT_INTO':'',
                    'VALUES':'',
                    }],
            htmlalert=None, 
            rowcnt=1,
            colcnt=1,
            datacnt=0,
            ):
        '''default tile and form parameters for a sql insert form'''
        #data
        data1_keys=['INSERT_INTO','VALUES'];
        data1_nestkeys=['INSERT_INTO'];
        data1_keymap=None;

        #tileparameters
        tileheader='SQL INSERT';
        tileid="htmlqueryinsert01";
        tileclass="panel panel-default";
        rowclass="row";
        colclass="col-sm-6";
        tileparameters={
            'tiletype':'html',
            'tileheader':tileheader,
            'tileid':tileid,
            'tileclass':tileclass,
            'rowclass':rowclass,
            'colclass':colclass,
            };

        #formparameters
        htmlid='htmlqueryinsertform01';
        htmltype='formquery_01';
        formpostbuttonidtext={'id':'posthtmlqueryinsertform01','text':'execute'};
        formurl='SQLQuery';
        formpostauthentication=True;
        formparameters = {
                'htmlid':htmlid,
                'htmltype':htmltype,
                "formpostbuttonidtext":formpostbuttonidtext,
                'formurl':formurl,
                'htmlalert':htmlalert,
                'formpostauthentication':formpostauthentication,
                };
        #add the form to the container
        self.make_container_queryForm(
            data_1,
            data1_keys,
            data1_nestkeys,
            data1_keymap,
            tileparameters_I=tileparameters,
            formparameters_I=formparameters, 
            rowcnt=rowcnt,
            colcnt=colcnt,
            datacnt=datacnt,
            );

    def make_container_queryUpdateForm(self,
            data_1=[
                {'UPDATE':'',
                    'SET':'',
                    'WHERE':'',
                    }],
            htmlalert=None, 
            rowcnt=1,
            colcnt=1,
            datacnt=0,
            ):
        '''default tile and form parameters for a sql update form'''
        #data
        data1_keys=['UPDATE','SET','WHERE'];
        data1_nestkeys=['UPDATE'];
        data1_keymap=None;

        #tileparameters
        tileheader='SQL UPDATE';
        tileid="htmlqueryupdate01";
        tileclass="panel panel-default";
        rowclass="row";
        colclass="col-sm-6";
        tileparameters={
            'tiletype':'html',
            'tileheader':tileheader,
            'tileid':tileid,
            'tileclass':tileclass,
            'rowclass':rowclass,
            'colclass':colclass,
            };

        #formparameters
        htmlid='htmlqueryupdateform01';
        htmltype='formquery_01';
        formpostbuttonidtext={'id':'posthtmlqueryupdateform01','text':'execute'};
        formurl='SQLQuery';
        formpostauthentication=True;
        formparameters = {
                'htmlid':htmlid,
                'htmltype':htmltype,
                "formpostbuttonidtext":formpostbuttonidtext,
                'formurl':formurl,
                'htmlalert':htmlalert,
                'formpostauthentication':formpostauthentication,
                };
        #add the form to the container
        self.make_container_queryForm(
            data_1,
            data1_keys,
            data1_nestkeys,
            data1_keymap,
            tileparameters_I=tileparameters,
            formparameters_I=formparameters, 
            rowcnt=rowcnt,
            colcnt=colcnt,
            datacnt=datacnt,
            );

    def make_container_queryDeleteForm(self,
            data_1=[
                {'DELETE_FROM':'',
                'WHERE':'',
                }],
            htmlalert=None, 
            rowcnt=1,
            colcnt=1,
            datacnt=0,
            ):
        '''default tile and form parameters for a sql delete form'''
        #data
        data1_keys=['DELETE_FROM','WHERE'];
        data1_nestkeys=['DELETE'];
        data1_keymap=None;

        #tileparameters
        tileheader='SQL DELETE';
        tileid="htmlquerydelete01";
        tileclass="panel panel-default";
        rowclass="row";
        colclass="col-sm-6";
        formpostauthentication=True;
        tileparameters={
            'tiletype':'html',
            'tileheader':tileheader,
            'tileid':tileid,
            'tileclass':tileclass,
            'rowclass':rowclass,
            'colclass':colclass,
            };

        #formparameters
        htmlid='htmlquerydeleteform01';
        htmltype='formquery_01';
        formpostbuttonidtext={'id':'posthtmlquerydeleteform01','text':'execute'};
        formurl='SQLQuery';
        formparameters = {
                'htmlid':htmlid,
                'htmltype':htmltype,
                "formpostbuttonidtext":formpostbuttonidtext,
                'formurl':formurl,
                'htmlalert':htmlalert,
                'formpostauthentication':formpostauthentication,
                };
        #add the form to the container
        self.make_container_queryForm(
            data_1,
            data1_keys,
            data1_nestkeys,
            data1_keymap,
            tileparameters_I=tileparameters,
            formparameters_I=formparameters, 
            rowcnt=rowcnt,
            colcnt=colcnt,
            datacnt=datacnt,
            );

    def make_container_queryInsertUpdateDeleteForm(self,
            data_1=[{'type':'ADD'},
                    {'type':'UPDATE'},
                    {'type':'DELETE'}],
            htmlalert=None, 
            rowcnt=1,
            colcnt=1,
            datacnt=0,
            ):
        '''default tile and form parameters for a sql delete form'''
        #data
        data1_keys=['type'];
        data1_nestkeys=['type'];
        data1_keymap=None;

        #tileparameters
        tileheader='SQL';
        tileid="htmlqueryinsertupdatedelete01";
        tileclass="panel panel-default";
        rowclass="row";
        colclass="col-sm-6";
        formpostauthentication=True;
        tileparameters={
            'tiletype':'html',
            'tileheader':tileheader,
            'tileid':tileid,
            'tileclass':tileclass,
            'rowclass':rowclass,
            'colclass':colclass,
            };

        #formparameters
        htmlid='htmlqueryinsertupdatedeleteform01';
        htmltype='formquery_02';
        formpostbuttonidtext={'id':'posthtmlqueryinsertupdatedeleteform01','text':'execute'};
        formurl='pipeline';
        formparameters = {
                'htmlid':htmlid,
                'htmltype':htmltype,
                "formpostbuttonidtext":formpostbuttonidtext,
                'formurl':formurl,
                'htmlalert':htmlalert,
                'formpostauthentication':formpostauthentication,
                };
        #add the form to the container
        self.make_container_queryForm(
            data_1,
            data1_keys,
            data1_nestkeys,
            data1_keymap,
            tileparameters_I=tileparameters,
            formparameters_I=formparameters, 
            rowcnt=rowcnt,
            colcnt=colcnt,
            datacnt=datacnt,
            );
