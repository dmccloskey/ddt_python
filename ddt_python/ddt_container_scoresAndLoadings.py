from .ddt_container import ddt_container
from .ddt_tile import ddt_tile
from .ddt_tile_html import ddt_tile_html

class ddt_container_scoresAndLoadings(ddt_container):
    def make_scoresAndLoadings(self,
            data_scores_123,data_loadings_123,
            PCs,
            data1_keys,data1_nestkeys,
            data2_keys,data2_nestkeys,
            data1_keymap_serieslabel,data1_keymap_featureslabel,
            data2_keymap_serieslabel,data2_keymap_featureslabel,
            data1_keymap_tooltiplabel = None,
            data2_keymap_tooltiplabel = None,

            ):
        '''make the heatmap container object
        INPUT:
        data_scores_123 = {'[1,2]':[],'[1,3]':[],'[2,3]':[],...} where each [] is a listDict of the data from PCs e.g. 1,2
        data_loadings_123 = {'[1,2]':[],'[1,3]':[],'[2,3]':[],...}
        PCs = [[],[],...] of integers, describing the 2D PC plots
            E.G. PCs = [[1,2],[1,3],[2,3]];
        '''
        
        cnt = 0;
        for PC_cnt,PC in enumerate(PCs):
            # scores
            if PC_cnt == 0:
                form = ddt_tile();
                form.make_tileparameters(
                    tileparameters={
                    'tileheader':'Scores filter menu',
                    'tiletype':'html',
                    'tileid':"filtermenu1",
                    'rowid':"row1",
                    'colid':"col0",
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
                self.update_tile2datamap("filtermenu1",[cnt]);
                self.add_filtermenu(
                    {"filtermenuid":"filtermenu1",
                    "filtermenuhtmlid":"filtermenuform1",
                    "filtermenusubmitbuttonid":"submit1",
                    "filtermenuresetbuttonid":"reset1",
                    "filtermenuupdatebuttonid":"update1"}
                    );
            data1_keymap = {
                'xdata':'score_'+str(PC[0]),
                'ydata':'score_'+str(PC[1]),
                'serieslabel':data1_keymap_serieslabel,
                'featureslabel':data1_keymap_featureslabel,
                'tooltiplabel':data1_keymap_tooltiplabel};
            self.add_data(
                data_scores_123[str(PC)],
                data1_keys,
                data1_nestkeys
                );
            # define the svg tile parameters
            svg = ddt_tile();
            svg.make_tileparameters(
                tileparameters={
                'tileheader':'Scores',
                'tiletype':'svg',
                'tileid':"scorestile"+str(PC_cnt),
                'rowid':"row1",
                'colid':"col"+str(PC_cnt+1),
                'tileclass':"panel panel-default",
                'rowclass':"row",
                'colclass':"col-sm-6"}
                    );
            svg.make_svgparameters(
                svgparameters={
                "svgtype":'pcaplot2d_scores_01',"svgkeymap":[data1_keymap],
                'svgid':'svg1',
                "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                "svgwidth":400,"svgheight":350,
                "svgx1axislabel":data_scores_123[str(PC)][0]['axislabel'+str(PC[0])],
                "svgy1axislabel":data_scores_123[str(PC)][0]['axislabel'+str(PC[1])]
                }
                );
            self.add_parameters(svg.get_parameters());
            self.update_tile2datamap("scorestile"+str(PC_cnt),[cnt]);
            cnt+=1;
        for PC_cnt,PC in enumerate(PCs):
            # loadings
            if PC_cnt == 0:
                #define the filter menu
                form = ddt_tile();
                form.make_tileparameters(
                    tileparameters={
                    'tileheader':'Loadings filter menu',
                    'tiletype':'html',
                    'tileid':"filtermenu2",
                    'rowid':"row2",
                    'colid':"col0",
                    'tileclass':"panel panel-default",
                    'rowclass':"row",
                    'colclass':"col-sm-6"}
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
            # define the data object
            data2_keymap = {'xdata':'loadings_'+str(PC[0]),
                            'ydata':'loadings_'+str(PC[1]),
                            'serieslabel':data2_keymap_serieslabel,
                            'featureslabel':data2_keymap_featureslabel,
                'tooltiplabel':data2_keymap_tooltiplabel};
            self.add_data(
                data_loadings_123[str(PC)],
                data2_keys,
                data2_nestkeys
                );
            # define the svg tile parameters
            svg = ddt_tile();
            svg.make_tileparameters(
                tileparameters={
                'tileheader':'Loadings',
                'tiletype':'svg',
                'tileid':"loadingstile"+str(PC_cnt),
                'rowid':"row2",
                'colid':"col"+str(PC_cnt+1),
                'tileclass':"panel panel-default",
                'rowclass':"row",
                'colclass':"col-sm-6"}
                    );
            svg.make_svgparameters(
                svgparameters={
                #"svgtype":'verticalbarschart2d_01',
                "svgtype":'volcanoplot2d_01', 
                "svgkeymap":[data2_keymap],
                'svgid':'svg1',
                "svgmargin":{ 'top': 50, 'right': 50, 'bottom': 50, 'left': 50 },
                "svgwidth":400,
                "svgheight":350,
                "svgx1axislabel":data_loadings_123[str(PC)][0]['axislabel'+str(PC[0])],
                "svgy1axislabel":data_loadings_123[str(PC)][0]['axislabel'+str(PC[1])]}
                );
            self.add_parameters(svg.get_parameters());
            self.update_tile2datamap("loadingstile"+str(PC_cnt),[cnt]);
            cnt+=1;