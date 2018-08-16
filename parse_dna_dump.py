#!/usr/bin/env python3

from dna_classes import ME
from typing import Dict, List, Union, Tuple
import codecs
import csv
import googlemaps
import pickle
import re


APIKEY = 'AIzaSyCLT1VCSDSfgCIA2sFWy6yCIbcQKlgezZY'  # dna-geo GoogleMaps API key
do_me = dict()  # dictionary of ME objects
gmaps = googlemaps.Client(key = APIKEY)  # GoogleMaps client
file_name = '/Users/david/PycharmProjects/charter_granite/dna_dump.csv'
nf_sites = '/Users/david/PycharmProjects/charter_granite/netfusion_sites.csv'


def pickle_headers(heads: dict):
    '''
    Serialize dictionary of headers
    :param heads:
    :return:
    '''
    with open('headers.pickle', 'wb') as pickler:
        pickle.dump(heads, pickler)


def pickle_me():
    '''
    Serialize dict of ME objects
    :return:
    '''
    global do_me
    with open('do_me.pickle', 'wb') as pickler:
        pickle.dump(do_me, pickler)


def reverse_geocode_result(lat: float, lng: float) -> List:
    '''
    Return a list of formatted addresses from lat & lng
    :param lat: float
    :param lng: float
    :return: List of GoogleMaps addresses
    '''
    try:
        _address = gmaps.reverse_geocode((lat, lng))
        return _address
    except:
        return []


def build_type_headers() -> Dict:
    '''
    Build a dictionary of headers for each item type in the DNA dump
    :return:
    '''
    TYPES = []
    HEADERS = {}
    with open(file_name, 'r') as dna_file:
        dna = csv.reader(dna_file)
        for row in dna:
            if row[0] == '#Type':
                header = [re.sub(r'[ #]*', '', x) for x in row if x]  # remove spaces and hashes
                # header = [x for x in row if x]
                continue
            try:
                if row[0] not in TYPES:
                    TYPES.append(row[0])
                    HEADERS[row[0].replace(':', '')] = header
            except:
                pass
    return HEADERS


def create_me_objects() -> Dict:
    # create the dict of ME objects
    _node_hash = {}
    global do_me
    with open(file_name, 'r') as dna_file:
        dna = csv.reader(dna_file)
        for row in dna:
            if row[0] == 'ME':
                do_me[row[1]] = ME(*[x for x in row[:97]])
                _node_hash[row[2]] = row[1]
    return _node_hash


def populate_me_objects(_headers: dict, _node_hash: dict):
    """Populate the ME sub-type lists"""
    global do_me
    exceptions = list()
    with open(file_name, 'r') as dna_file:
        dna = csv.reader(dna_file)
        for row in dna:
            try:
                if row[0] == 'LICENSE':
                    do_me[row[1]].license.append(row[:len(_headers['LICENSE'])])
                elif row[0] == 'NTPD':
                    do_me[row[1]].ntpd.append(row[:len(_headers['NTPD'])])
                elif row[0] == 'BANDCTP_SPANLOSS':
                    do_me[row[1]].bandctp_spanloss.append(row[:len(_headers['BANDCTP_SPANLOSS'])])
                elif row[0] == 'ASSOCIATION':
                    do_me[row[1]].association.append(row[:len(_headers['ASSOCIATION'])])
                elif row[0] == 'XCON':
                    do_me[row[1]].xcon.append(row[:len(_headers['XCON'])])
                elif row[0] == 'XFR':
                    do_me[row[1]].xfr.append(row[:len(_headers['XFR'])])
                elif row[0] == 'COMMUNITY':
                    do_me[_node_hash[row[1]]].community.append(row[:len(_headers['COMMUNITY'])])
                elif row[0] == 'SNMPCONFIG':
                    do_me[_node_hash[row[1]]].community.append(row[:len(_headers['SNMPCONFIG'])])
                elif row[0] == 'SNMPACCESSLIST':
                    do_me[_node_hash[row[1]]].snmpaccesslist.append(row[:len(_headers['SNMPACCESSLIST'])])
                elif row[0] == 'TRAPCFG':
                    do_me[_node_hash[row[1]]].trapcfg.append(row[:len(_headers['TRAPCFG'])])
                elif row[0] == 'SnmpV3AdminUserTable':
                    do_me[row[1]].snmpv3adminusertable.append(row[:len(_headers['SnmpV3AdminUserTable'])])
                elif row[0] == 'TE_INTERFACE':
                    do_me[row[1]].te_interface.append(row[:len(_headers['TE_INTERFACE'])])
                elif row[0] == 'SECURITYPROFILE':
                    do_me[row[1]].securityprofile.append(row[:len(_headers['SECURITYPROFILE'])])
                elif row[0] == 'Neighbor Links':
                    do_me[_node_hash[row[1]]].neighbor_links.append(row[:len(_headers['Neighbor Links'])])
                elif row[0] == 'DBCONTROL':
                    do_me[row[1]].dbcontrol.append(row[:len(_headers['DBCONTROL'])])
                elif row[0] == 'IGCC':
                    do_me[row[1]].igcc.append(row[:len(_headers['IGCC'])])
                elif row[0] == 'STATICROUTE':
                    do_me[row[1]].staticroute.append(row[:len(_headers['STATICROUTE'])])
                elif row[0] == 'GMPLS_CONTROL_CHANNEL':
                    do_me[row[1]].gmpls_control_channel.append(row[:len(_headers['GMPLS_CONTROL_CHANNEL'])])
                elif row[0] == 'SLOT':
                    do_me[row[1]].slot.append(row[:len(_headers['SLOT'])])
                elif row[0] == 'FIBERLINK':
                    do_me[_node_hash[row[1]]].fiberlink.append(row[:len(_headers['FIBERLINK'])])
                elif row[0] == 'TopoNode':
                    do_me[row[1]].toponode.append(row[:len(_headers['TopoNode'])])
                elif row[0] == 'CtrlLink':
                    do_me[row[1]].ctrllink.append(row[:len(_headers['CtrlLink'])])
                elif row[0] == 'PEMSHELF':
                    do_me[row[1]].pemshelf.append(row[:len(_headers['PEMSHELF'])])
                elif row[0] == 'IOSHELF':
                    do_me[row[1]].ioshelf.append(row[:len(_headers['IOSHELF'])])
                elif row[0] == 'OLX':
                    do_me[row[1]].olx.append(row[:len(_headers['OLX'])])
                elif row[0] == 'OTM':
                    do_me[row[1]].otm.append(row[:len(_headers['OTM'])])
                elif row[0] == 'TIM':
                    do_me[row[1]].tim.append(row[:len(_headers['TIM'])])
                elif row[0] == 'XCM':
                    do_me[row[1]].xcm.append(row[:len(_headers['XCM'])])
                elif row[0] == 'TSM':
                    do_me[row[1]].tsm.append(row[:len(_headers['TSM'])])
                elif row[0] == 'XM':
                    do_me[row[1]].xm.append(row[:len(_headers['XM'])])
                elif row[0] == 'XTIM':
                    do_me[row[1]].xtim.append(row[:len(_headers['XTIM'])])
                elif row[0] == 'XMM':
                    do_me[row[1]].xmm.append(row[:len(_headers['XMM'])])
                elif row[0] == 'CHASSIS':
                    do_me[row[1]].chassis.append(row[:len(_headers['CHASSIS'])])
                elif row[0] == 'BMM':
                    do_me[row[1]].bmm.append(row[:len(_headers['BMM'])])
                elif row[0] == 'DLM':
                    do_me[row[1]].dlm.append(row[:len(_headers['DLM'])])
                elif row[0] == 'XLM':
                    do_me[row[1]].xlm.append(row[:len(_headers['XLM'])])
                elif row[0] == 'TAM':
                    do_me[row[1]].tam.append(row[:len(_headers['TAM'])])
                elif row[0] == 'TOM':
                    do_me[row[1]].tom.append(row[:len(_headers['TOM'])])
                elif row[0] == 'TEM':
                    do_me[row[1]].tem.append(row[:len(_headers['TEM'])])
                elif row[0] == 'MCM':
                    do_me[row[1]].mcm.append(row[:len(_headers['MCM'])])
                elif row[0] == 'OAM':
                    do_me[row[1]].oam.append(row[:len(_headers['OAM'])])
                elif row[0] == 'OMM':
                    do_me[row[1]].omm.append(row[:len(_headers['OMM'])])
                elif row[0] == 'PEM':
                    do_me[row[1]].pem.append(row[:len(_headers['PEM'])])
                elif row[0] == 'FAN':
                    do_me[row[1]].fan.append(row[:len(_headers['FAN'])])
                elif row[0] == 'GAM':
                    do_me[row[1]].gam.append(row[:len(_headers['GAM'])])
                elif row[0] == 'InternalLink':
                    do_me[row[1]].internallink.append(row[:len(_headers['InternalLink'])])
                elif row[0] == 'BANDCTP':
                    do_me[row[1]].bandctp.append(row[:len(_headers['BANDCTP'])])
                elif row[0] == 'BMMOCGPTP':
                    do_me[row[1]].bmmocgptp.append(row[:len(_headers['BMMOCGPTP'])])
                elif row[0] == 'OTSPTP':
                    do_me[row[1]].otsptp.append(row[:len(_headers['OTSPTP'])])
                elif row[0] == 'DCFPTP':
                    do_me[row[1]].dcfptp.append(row[:len(_headers['DCFPTP'])])
                elif row[0] == 'CLRCHCLIENTCTP':
                    do_me[row[1]].clrchclientctp.append(row[:len(_headers['CLRCHCLIENTCTP'])])
                elif row[0] == 'BANDPTP':
                    do_me[row[1]].bandptp.append(row[:len(_headers['BANDPTP'])])
                elif row[0] == 'DTPCTP DTF Path TAM':
                    do_me[row[1]].dtpctp_dtf_path_tam.append(row[:len(_headers['DTPCTP DTF Path TAM'])])
                elif row[0] == 'DTPCTP DTF Path DLM':
                    do_me[row[1]].dtpctp_dtf_path_dlm.append(row[:len(_headers['DTPCTP DTF Path DLM'])])
                elif row[0] == 'CHANNELCTP':
                    do_me[row[1]].channelctp.append(row[:len(_headers['CHANNELCTP'])])
                elif row[0] == 'DLMOCGPTP':
                    do_me[row[1]].dlmocgptp.append(row[:len(_headers['DLMOCGPTP'])])
                elif row[0] == 'SONETCLIENTCTP':
                    do_me[row[1]].sonetclientctp.append(row[:len(_headers['SONETCLIENTCTP'])])
                elif row[0] == 'GbE Client':
                    do_me[row[1]].gbe_client.append(row[:len(_headers['GbE Client'])])
                elif row[0] == 'TRIBPTP':
                    do_me[row[1]].tribptp.append(row[:len(_headers['TRIBPTP'])])
                elif row[0] == 'NCTGIGE':
                    do_me[row[1]].nctgige.append(row[:len(_headers['NCTGIGE'])])
                # elif row[0] == 'GAMOCGPTP':
                #     do_me[row[1]].gamocgptp.append(row[:len(_headers['GAMOCGPTP'])])
                elif row[0] == 'GAMOCGPTP':
                    do_me[row[1]].gamocgptp.append(row[:len(_headers['GAMOCGPTP'])])
                elif row[0] == 'FEEDPTP':
                    do_me[row[1]].feedptp.append(row[:len(_headers['FEEDPTP'])])
                # elif row[0] == 'ODUKICTP':
                #     do_me[row[1]].odukictp.append(row[:len(_headers['ODUKICTP'])])
                elif row[0] == 'OTUKICTP':
                    do_me[row[1]].otukictp.append(row[:len(_headers['OTUKICTP'])])
                elif row[0] == 'LMOCGPTP':
                    do_me[row[1]].lmocgptp.append(row[:len(_headers['LMOCGPTP'])])
                elif row[0] == 'XTOCGPTP':
                    do_me[row[1]].xtocgptp.append(row[:len(_headers['XTOCGPTP'])])
                elif row[0] == 'OCHCTP':
                    do_me[row[1]].ochctp.append(row[:len(_headers['OCHCTP'])])
                elif row[0] == 'LOCAL_SNC':
                    do_me[row[1]].local_snc.append(row[:len(_headers['LOCAL_SNC'])])
                elif row[0] == 'REMOTE_SNC':
                    do_me[row[1]].remote_snc.append(row[:len(_headers['REMOTE_SNC'])])
                elif row[0] == 'LOCAL_SUB_SNC':
                    do_me[row[1]].local_sub_snc.append(row[:len(_headers['LOCAL_SUB_SNC'])])
                elif row[0] == 'REMOTE_SUB_SNC':
                    do_me[row[1]].remote_sub_snc.append(row[:len(_headers['REMOTE_SUB_SNC'])])
                elif row[0] == 'DigitalSNCP-1-port':
                    do_me[row[1]].digitalsncp_1_port.append(row[:len(_headers['DigitalSNCP-1-port'])])
                elif row[0] == 'TeLink':
                    do_me[row[2]].telink.append(row[:len(_headers['TeLink'])])
                elif row[0] == 'ALARM':
                    do_me[row[6]].alarm.append(row[:len(_headers['ALARM'])])
                elif row[0] == 'SERVICE_OBJECT':
                    do_me[row[2]].service_object.append(row[:len(_headers['SERVICE_OBJECT'])])
                elif row[0] == 'ORM':
                    do_me[row[1]].orm.append(row[:len(_headers['ORM'])])
                elif row[0] == 'RAM':
                    do_me[row[1]].ram.append(row[:len(_headers['RAM'])])
                elif row[0] == 'SCM':
                    do_me[row[2]].scm.append(row[:len(_headers['SCM'])])
            except Exception as ex:
                exceptions.append(row)
                print(type(ex).__name__, ex.args)
                pass
            
        _type = ''
        filename = 'dna_exceptions.csv'
        with open(filename, 'w') as issues:
            writer = csv.writer(issues)
            for row in exceptions:
                if _type == '':
                    _type = row[0]
                    writer.writerow(_headers[_type])
                if _type != row[0]:
                    _type = row[0]
                    writer.writerow(_headers[_type])
                writer.writerow(row)
        print(f'\n\t{len(exceptions)} exceptions written to {filename}\n')


def get_nf_site_address():
    '''
    Create 'nf_site_data.pickle' from the Charter DNA NetFusion site data
    :return:
    '''
    nf_w_add = []
    with codecs.open(nf_sites, 'r', encoding='ascii', errors='ignore') as infile:
        reader = csv.reader(infile)
        for row in reader:
            try:
                lat, lng = (float(row[3]), float(row[4]))
                address = reverse_geocode_result(lat, lng)
                row.extend([address])
                nf_w_add.append(row)
            except Exception as ex:
                print(type(ex).__name__, ex.args)
                pass
    with open('nf_site_data.pickle', 'wb') as pickler:
        pickle.dump(nf_w_add, pickler)


def update_netfusion_sites(_node_hash: dict):
    '''
    Update ME objects with NetFusion site, geo-coordinates and address
    :param _node_hash: A dictionary of ME node names and node IDs {'rdm01alcyal': 'MA3207324395'}
    '''
    global do_me

    with open('nf_site_data.pickle', 'rb') as pickler:
        nf_sites = pickle.load(pickler)
        for row in nf_sites:
            try:
                do_me[_node_hash[row[0]]].set_geo(float(row[3]),float(row[4]))
                do_me[_node_hash[row[0]]].set_location1(row[5][0]['formatted_address'])
                if row[2]:
                    do_me[_node_hash[row[0]]].set_nf_site(row[2])
            except Exception as ex:
                print(type(ex).__name__, ex.args)
                pass


def main():
    headers = build_type_headers()
    node_hash = create_me_objects()
    populate_me_objects(headers, node_hash)
    update_netfusion_sites(node_hash)
    pickle_me()
    pickle_headers(headers)


if __name__ == "__main__":
    main()


