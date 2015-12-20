#system
import json
import re

class ddt_container():
    def __init__(self,parameters_I = None,data_I = None,tile2datamap_I = None,filtermenu_I = None):
        if parameters_I:self.parameters = parameters_I;
        else: self.parameters = [];
        if data_I:self.data = data_I;
        else: self.data = [];
        if tile2datamap_I:self.tile2datamap = tile2datamap_I;
        else: self.tile2datamap = {};
        if filtermenu_I:self.filtermenu = filtermenu_I;
        else: self.filtermenu = [];

    def clear_objects(self):
        '''remove data'''
        self.parameters = None;
        self.data = None;
        self.tile2datamap = None;
        self.filtermenu = None;
    def add_objects(self,parameters_I = None,data_I = None,tile2datamap_I = None,filtermenu_I = None):
        '''add new data'''
        if parameters_I:self.parameters = parameters_I;
        else: parameters = [];
        if data_I:self.data = data_I;
        else: data = [];
        if tile2datamap_I:self.tile2datamap = tile2datamap_I;
        else: tile2datamap = {};
        if filtermenu_I:self.filtermenu = filtermenu_I;
        else: filtermenu = [];
    def get_parameters(self):
        '''Return the parameters object'''
        parameters_O = None;
        if self.parameters:
            parameters_O = self.parameters;
        return parameters_O;
    def get_data(self):
        '''Return the data object'''
        data_O = None;
        if self.data:
            data_O = self.data;
        return data_O;
    def get_tile2datamap(self):
        '''Return the tile2datamap object'''
        tile2datamap_O = None;
        if self.tile2datamap:
            tile2datamap_O = self.tile2datamap;
        return tile2datamap_O;
    def get_filtermenu(self):
        '''Return the filtermenu object'''
        filtermenu_O = None;
        if self.filtermenu:
            filtermenu_O = self.filtermenu;
        return filtermenu_O;

    def get_allObjects(self):
        '''return all container data in string format'''
        parameters_json = self.get_parameters();
        data_json = self.get_data();
        tile2datamap_json = self.get_tile2datamap();
        filtermenu_json = self.get_filtermenu();
        alldata_O = {};
        if parameters_json: alldata_O['parameters'] = parameters_json;
        if data_json: alldata_O['data'] = data_json;
        if tile2datamap_json: alldata_O['tile2datamap'] = tile2datamap_json;
        if filtermenu_json: alldata_O['filtermenu'] = filtermenu_json;
        return json.dumps(alldata_O);

    def get_allObjects_js(self):
        '''return all container data in string format'''
        parameters_json = self.get_parameters();
        data_json = self.get_data();
        tile2datamap_json = self.get_tile2datamap();
        filtermenu_json = self.get_filtermenu();
        alldata_O = '';
        if parameters_json: alldata_O+= 'var ' + 'parameters' + ' = ' + json.dumps(parameters_json) + ';' + '\n';
        if data_json: alldata_O+= 'var ' + 'data' + ' = ' + json.dumps(data_json) + ';' + '\n';
        if tile2datamap_json: alldata_O+= 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_json) + ';' + '\n';
        if filtermenu_json: alldata_O+= 'var ' + 'filtermenu' + ' = ' + json.dumps(filtermenu_json) + ';' + '\n';
        return alldata_O;

    def add_data(self,data_1,data1_keys,data1_nestkeys):
        '''add to container data
        INPUT:
        OUTPUT:
        '''
        self.data.append({"data":data_1,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});

    def add_parameters(self,parameters):
        '''add to container parameters
        INPUT:
        OUTPUT:
        '''
        self.parameters.append(parameters);

    def update_tile2datamap(self,tileid,dataindices):
        '''update container tile2datamap
        INPUT:
        tileid = string, id of the tile
        dataindices = [] of integers where each integer coresponds to an associated data object
        OUTPUT:
        '''
        self.tile2datamap.update({tileid:dataindices});

    def add_filtermenu(self,filtermenu):
        '''add container filtermenu
        INPUT:
        OUTPUT
        '''
        self.filtermenu.append(filtermenu);