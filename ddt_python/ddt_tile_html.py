from .ddt_tile import ddt_tile

class ddt_tile_html(ddt_tile):
    def make_parameters_form_01(self,
            formparameters={},
            ):
        '''Make htmlparameters
        INPUT:
        OUTPUT:
        '''
        #defaults:
        htmlid='filtermenuform1';
        htmltype='form_01';
        formsubmitbuttonidtext={'id':'submit1','text':'submit'};
        formresetbuttonidtext={'id':'reset1','text':'reset'};
        formupdatebuttonidtext={'id':'update1','text':'update'};

        if formparameters:
            formparameters_O = formparameters;
        else: 
            formparameters_O = {
                'htmlid':htmlid,
                'htmltype':htmltype,
                "formsubmitbuttonidtext":formsubmitbuttonidtext,
                "formresetbuttonidtext":formresetbuttonidtext,
                "formupdatebuttonidtext":formupdatebuttonidtext
                };
        self.make_htmlparameters(htmlparameters=formparameters_O);
    def make_parameters_datalist_01(self,
            datalistparameters={},
            ):
        '''Make htmlparameters
        INPUT:
        OUTPUT:
        '''
        #defaults
        htmlid='datalist1';
        htmltype='datalist_01';
        datalist=[
            {'value':'hclust','text':'by cluster'},
            {'value':'probecontrast','text':'by row and column'},
            {'value':'probe','text':'by row'},
            {'value':'contrast','text':'by column'},
            {'value':'custom','text':'by value'}];

        if datalistparameters:
            datalistparameters_O = datalistparameters;
        else:
            datalistparameters_O = {
                'htmlid':htmlid,
                'htmltype':htmltype,
                'datalist':datalist
                };
        self.make_htmlparameters(htmlparameters=datalistparameters_O);