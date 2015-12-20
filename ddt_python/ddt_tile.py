class ddt_tile():
    def __init__(self,tileparameters_I = [],specificparameters_I = []):
        if tileparameters_I:self.tileparameters = tileparameters_I;
        else: self.tileparameters = [];
        if specificparameters_I:self.specificparameters = specificparameters_I;
        else: self.specificparameters = [];
        
    def clear_objects(self):
        '''remove data'''
        self.tileparameters = [];
        self.specificparameters = [];

    def add_objects(self,tileparameters_I,specificparameters_I):
        '''add data'''
        if tileparameters_I:self.tileparameters = tileparameters_I;
        else: self.tileparameters = [];
        if specificparameters_I:self.specificparameters = specificparameters_I;
        else: self.specificparameters = [];
        
    def get_parameters(self):
        '''Return the parameters object'''
        tileparameters_O = {};
        specificparameters_O = {};
        parameters_O = {};
        if self.tileparameters:
            tileparameters_O = self.tileparameters;
        if self.specificparameters:
            specificparameters_O = self.specificparameters;
        parameters_O.update(tileparameters_O);
        parameters_O.update(specificparameters_O);
        return parameters_O;

    def make_tileparameters(self,
            tileparameters = {},
            tileheader='Filter menu',
            tiletype='html',
            tileid="filtermenu1",
            rowid="row1",
            colid="col1",
            tileclass="panel panel-default",
            rowclass="row",
            colclass="col-sm-6",
            ):
        '''Make tile parameters
        INPUT:
        OUTPUT:
        '''
        if tileparameters:
            tileparameters_O=tileparameters;
        else:
            tileparameters_O = {
                'tileheader':tileheader,
                'tiletype':tiletype,
                'tileid':tileid,
                'rowid':rowid,
                'colid':colid,
                'tileclass':tileclass,
                'rowclass':rowclass,
                'colclass':colclass
                };
        self.tileparameters=tileparameters_O;

    def make_htmlparameters(self,
            htmlparameters={},
            htmlid='filtermenuform1',
            htmltype='form_01',
            htmlspecific={},
            ):
        '''Make html parameters
        INPUT:
        OUTPUT:
        '''
        if htmlparameters:
            htmlparameters_O=htmlparameters;
        else:
            htmlparameters_O = {
                'htmlid':htmlid,
                "htmltype":htmltype,
                };
        if htmlspecific:
            htmlparameters_O.update(htmlspecific);
        self.specificparameters=htmlparameters_O;

    def make_svgparameters(self,
        svgparameters={},
        svgtype='volcanoplot2d_01',
        svgkeymap=[],
        svgid='svg1',
        svgmargin={},
        svgfilters=None,
        svgspecific={},
        ):
        '''make svg parameters
        INPUT:
        OUTPUT:
        '''
        if svgparameters:
            svgparameters_O=svgparameters;
        else:
            svgparameters_O = {
                "svgtype":svgtype,
                "svgkeymap":svgkeymap,
                'svgid':svgid,
                "svgmargin":svgmargin,
                'svgfilters':svgfilters,
                };
        if svgspecific:
            svgparameters_O.update(svgspecific);
        self.specificparameters=svgparameters_O;

    def make_tableparameters(self,
            tableparameters={},
            tabletype='responsivetable_01',
            tableid='table1',
            tableclass="table  table-condensed table-hover",
            tablefilters=None,
            tablespecific={},
            ):
        '''make table parameters
        INPUT:
        tableparameters = {} of table parameters
        tablespecific = {} of table specific parameters
        OUTPUT:
        '''
        if tableparameters:
            tableparameters_O=tableparameters;
        else:
            tableparameters_O = {
                "tabletype":tabletype,
                'tableid':tableid,
                "tableclass":tableclass,
                "tablefilters":tablefilters,
                    }
        if tablespecific: 
            tableparameters_O.update(tablespecific);
        self.specificparameters=tableparameters_O;