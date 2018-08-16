#!/usr/bin/env python3

import pickle
import json
from collections import Counter
from typing import Dict, Union


do_me = dict()
headers = dict()
report = '/Users/david/PycharmProjects/GRANITE/granite_data/'
source = '/Users/david/PycharmProjects/GRANITE/'

def pickle_me() -> Dict:
    """Load the dictionary of ME objects"""
    with open(source + 'do_me.pickle', 'rb') as pickler:
        return pickle.load(pickler)


def get_headers() -> Dict:
    """Load the dictionary of type headers"""
    global headers
    with open(source + 'headers.pickle', 'rb') as pickler:
        return pickle.load(pickler)


def dna_stats():
    '''Print some counters for slots and sub-types'''
    bmmc = Counter()
    dlmc = Counter()
    gamc = Counter()
    mcmc = Counter()
    oamc = Counter()
    olxc = Counter()
    ommc = Counter()
    ormc = Counter()
    otmc = Counter()
    oxmc = Counter()
    pemc = Counter()
    ramc = Counter()
    slotc = Counter()
    tamc = Counter()
    temc = Counter()
    timc = Counter()
    tomc = Counter()
    tsmc = Counter()
    xcmc = Counter()
    xlmc = Counter()
    xmmc = Counter()
    xtimc = Counter()

    for me in do_me:
        for x in do_me[me].bmm:
            bmmc[x[13]] += 1
        for x in do_me[me].dlm:
            dlmc[x[13]] += 1
        for x in do_me[me].gam:
            gamc[x[13]] += 1
        for x in do_me[me].mcm:
            mcmc[x[13]] += 1
        for x in do_me[me].oam:
            oamc[x[13]] += 1
        for x in do_me[me].olx:
            olxc[x[13]] += 1
        for x in do_me[me].omm:
            ommc[x[13]] += 1
        for x in do_me[me].orm:
            ormc[x[13]] += 1
        for x in do_me[me].otm:
            otmc[x[13]] += 1
        for x in do_me[me].xm:
            oxmc[x[13]] += 1
        for x in do_me[me].pem:
            pemc[x[13]] += 1
        for x in do_me[me].ram:
            ramc[x[13]] += 1
        for x in do_me[me].slot:
            slotc[x[7]] += 1
        for x in do_me[me].tam:
            tamc[x[13]] += 1
        for x in do_me[me].tem:
            temc[x[13]] += 1
        for x in do_me[me].tim:
            timc[x[13]] += 1
        for x in do_me[me].tom:
            tomc[x[13]] += 1
        for x in do_me[me].tsm:
            tsmc[x[13]] += 1
        for x in do_me[me].xcm:
            xcmc[x[13]] += 1
        for x in do_me[me].xlm:
            xlmc[x[13]] += 1
        for x in do_me[me].xmm:
            xmmc[x[13]] += 1
        for x in do_me[me].xtim:
            xtimc[x[13]] += 1

    stats = [bmmc, dlmc, gamc, mcmc, oamc, olxc, ommc, ormc, otmc, oxmc, pemc, ramc,
             tamc, temc, timc, tomc, tsmc, xcmc, xlmc, xmmc, xtimc]

    print(f'\n{"Component":25} {"Count"}')
    print(f'{"-" * 25} {"-" * 5}')
    for slot in slotc:
        print(f'{slot:25} {slotc[slot]:5}')

    for stat in stats:
        print(f'\n{"Component":20} {"Count"}')
        print(f'{"-" * 20} {"-" * 5}')
        for item in stat:
            print(f'{item:20} {stat[item]:5}')


def get_me_bmms(me: str) -> Dict:
    bmms = {}
    for bmm in do_me[me].bmm:
        bmms[bmm[3]] = bmm
    return bmms


def get_me_dlms(me: str) -> Dict:
    dlms = {}
    for dlm in do_me[me].dlm:
        dlms[dlm[3]] = dlm
    return dlms


def get_me_dses(me: str) -> Dict:
    dses = {}
    for dse in do_me[me].dse:
        dses[dse[3]] = dse
    return dses


def get_me_gams(me: str) -> Dict:
    gams = {}
    for gam in do_me[me].gam:
        gams[gam[3]] = gam
    return gams


def get_me_mcms(me: str) -> Dict:
    mcms = {}
    for mcm in do_me[me].mcm:
        mcms[mcm[3]] = mcm
    return mcms


def get_me_oams(me: str) -> Dict:
    oams = {}
    for oam in do_me[me].oam:
        oams[oam[3]] = oam
    return oams


def get_me_olxs(me: str) -> Dict:
    olxs = {}
    for olx in do_me[me].olx:
        olxs[olx[3]] = olx
    return olxs


def get_me_omms(me: str) -> Dict:
    omms = {}
    for omm in do_me[me].omm:
        omms[omm[3]] = omm
    return omms


def get_me_orms(me: str) -> Dict:
    orms = {}
    for orm in do_me[me].orm:
        orms[orm[3]] = orm
    return orms


def get_me_otms(me: str) -> Dict:
    otms = {}
    for otm in do_me[me].otm:
        otms[otm[3]] = otm
    return otms


def get_me_oxms(me: str) -> Dict:
    oxms = {}
    for oxm in do_me[me].xm:
        oxms[oxm[3]] = oxm
    return oxms


def get_me_pems(me: str) -> Dict:
    pems = {}
    for pem in do_me[me].pem:
        pems[pem[3]] = pem
    return pems


def get_me_rams(me: str) -> Dict:
    rams = {}
    for ram in do_me[me].ram:
        rams[ram[3]] = ram
    return rams


def get_me_slots(me: str) -> Dict:
    slots = {}
    do_me[me].sort_slots(3)
    for slot in do_me[me].slot:
        slots[slot[3]] = slot
    return slots


def get_me_tams(me: str) -> Dict:
    """Replace the ContainedObjects with a list of ports associated with the TAM module"""
    tams = {}
    for tam in do_me[me].tam:
        ports = tam[-1].split(',')
        if ports:
            tam[-1] = [port[5:] for port in ports]
        tams[tam[3]] = tam
    return tams


def get_me_tems(me: str) -> Dict:
    tems = {}
    for tem in do_me[me].tem:
        tems[tem[3]] = tem
    return tems


def get_me_tims(me: str) -> Dict:
    tims = {}
    for tim in do_me[me].tim:
        tims[tim[3]] = tim
    return tims


def get_me_toms(me: str) -> Dict:
    toms = {}
    for tom in do_me[me].tom:
        toms[tom[3]] = tom
    return toms


def get_me_tsms(me: str) -> Dict:
    tsms = {}
    for tsm in do_me[me].tsm:
        tsms[tsm[3]] = tsm
    return tsms


def get_me_xcms(me: str) -> Dict:
    xcms = {}
    for xcm in do_me[me].xcm:
        xcms[xcm[3]] = xcm
    return xcms


def get_me_xlms(me: str) -> Dict:
    xlms = {}
    for xlm in do_me[me].xlm:
        xlms[xlm[3]] = xlm
    return xlms


def get_me_xmms(me: str) -> Dict:
    xmms = {}
    for xmm in do_me[me].xmm:
        xmms[xmm[3]] = xmm
    return xmms


def get_me_xtims(me: str) -> Dict:
    xtims = {}
    for xtim in do_me[me].xtim:
        xtims[xtim[3]] = xtim
    return xtims


def me_details(me: str) -> Dict:
    """Build and return the ME json object"""
    temp = {do_me[me]._node_id: [{headers["ME"][34]: do_me[me]._netype,
                                  'Vendor': 'Infinera',
                                  headers["ME"][2]: do_me[me]._node_name,
                                  headers["ME"][65]: do_me[me]._nodecontrollerchassistype,
                                  headers["ME"][39]: do_me[me]._swgenver,
                                  headers["ME"][9]: do_me[me]._service_state,
                                  headers["ME"][16]: do_me[me]._clli,
                                  headers["ME"][31]: do_me[me]._location1,
                                  headers["ME"][30]: do_me[me]._latitude,
                                  headers["ME"][33]: do_me[me]._longitude,
                                  # headers["ME"][17]: do_me[me]._craftip,
                                  headers["ME"][36]: do_me[me]._routerid,
                                  'NetFusionSite': do_me[me]._netfusionsite}]}
    return temp


def build_json(slot_type: str, slot, ids)-> Union[str, Dict]:
    """Build and return json object"""
    do_temp = {}
    if slot_type == 'EMPTY' and ids[0] == 100:  # return the slot name from the slot index
        # do_temp[slot[3]] = slot_type  # per JL - no AID in the object body
        return {slot[3]: [do_temp]}
    if slot_type == 'EMPTY' and ids[0] == 99:  # return the slot name from the slot
        # do_temp[slot] = slot_type  # per JL - no AID in the object body
        return {slot: [do_temp]}
    elif slot_type == 'EMPTY' and ids[0] == 98:  # This appears to be identical the above...
        # do_temp[slot] = slot_type  # per JL - no AID in the object body
        return {slot: [do_temp]}
    else:
        # do_temp[slot[3]] = slot[13]  # per JL - no AID in the object body
        for idx in ids:  # don't forget the id indexes can vary based on slot type
            do_temp[headers[slot_type][idx]] = slot[idx].strip()
    return {slot[3]: [do_temp]}


def main():
    global do_me
    global headers
    do_me = pickle_me()
    headers = get_headers()
    dna_stats()
    do_json = {}
    for me in do_me:
        me_json_obj = me_details(me)
        bmms = get_me_bmms(me)  # Band Multiplexing Module
        dlms = get_me_dlms(me)  # Digital Line Module
        gams = get_me_gams(me)  # Gain Adapter Module
        mcms = get_me_mcms(me)  # Management Control Module
        oams = get_me_oams(me)  # Optical Amplification Module
        olxs = get_me_olxs(me)  # Advanced OTN Switching Line Module
        omms = get_me_omms(me)  # Optical Management Module
        orms = get_me_orms(me)  # Optical Raman Module
        otms = get_me_otms(me)  # OTN Tributary Module
        oxms = get_me_oxms(me)  # OTN Switch Module
        pems = get_me_pems(me)  # Power Entry Module
        rams = get_me_rams(me)  # Raman Amplifier Module; random access memory
        slots = get_me_slots(me)  #
        tams = get_me_tams(me)  # Tributary Adapter Module
        tems = get_me_tems(me)  # TAM Extender Module
        tims = get_me_tims(me)  # Tributary Interface Module; trace identifier mismatch
        toms = get_me_toms(me)  # Tributary Optical Module
        tsms = get_me_tsms(me)  # Timing Synchronization Module
        xcms = get_me_xcms(me)  # DTN-X Control Module
        xlms = get_me_xlms(me)  # Switching Line Module
        xmms = get_me_xmms(me)  # CloudXpress Management Module
        xtims = get_me_xtims(me)
        for slot in slots:  # For each ME, cycle through all it's slots and add to the ME json key object
            try:
                if slots[slot][6] == 'EMPTY' and slots[slot][7] != 'TOM':
                    me_json_obj[me].append(build_json('EMPTY', slots[slot], [100]))  # not returned as a list???
                elif slots[slot][7] == 'BMM':
                    me_json_obj[me].append([build_json('BMM', bmms[slots[slot][3]], [15, 14, 23])])
                elif slots[slot][7] == 'MCM':
                    me_json_obj[me].append([build_json('MCM', mcms[slots[slot][3]], [15, 14, 21])])
                elif slots[slot][7] == 'OMM':
                    me_json_obj[me].append([build_json('OMM', omms[slots[slot][3]], [15, 14, 21])])
                elif slots[slot][7] == 'OXM':  # OXM use the xms list
                    me_json_obj[me].append([build_json('XM', oxms[slots[slot][3]], [15, 14, 23])])
                elif slots[slot][7] == 'PEM':
                    me_json_obj[me].append([build_json('PEM', pems[slots[slot][3]], [15, 14, 21])])
                elif slots[slot][7] == 'TIM':
                    me_json_obj[me].append([build_json('TIM', tims[slots[slot][3]], [15, 14, 23])])
                elif slots[slot][7] == 'TSM':
                    me_json_obj[me].append([build_json('TSM', tsms[slots[slot][3]], [15, 14, 23])])
                elif slots[slot][7] == 'XCM':
                    me_json_obj[me].append([build_json('XCM', xcms[slots[slot][3]], [15, 14, 23])])
                elif slots[slot][7] == 'XLM':
                    me_json_obj[me].append([build_json('XLM', xlms[slots[slot][3]], [15, 14, 23])])
                elif slots[slot][7] == 'XMM':
                    me_json_obj[me].append([build_json('XMM', xmms[slots[slot][3]], [15, 14, 23])])
                elif slots[slot][7] == 'XTIM':
                    me_json_obj[me].append([build_json('XTIM', xtims[slots[slot][3]], [15, 14, 23])])
                elif slots[slot][7] == 'OLM/OTM':
                    if 'OLX' in slots[slot][8]:
                        me_json_obj[me].append([build_json('OLX', olxs[slots[slot][3]], [15, 14, 23])])
                    if 'OTM' in slots[slot][8]:
                        me_json_obj[me].append([build_json('OTM', otms[slots[slot][3]], [15, 14, 23])])
                elif slots[slot][7] == 'DLM/TEM/XLM':
                    if 'DLM' in slots[slot][8]:
                        me_json_obj[me].append([build_json('DLM', dlms[slots[slot][3]], [15, 14, 23])])
                    elif 'TEM' in slots[slot][8]:
                        me_json_obj[me].append([build_json('TEM', tems[slots[slot][3]], [15, 14, 23])])
                    elif 'XLM' in slots[slot][8]:
                        me_json_obj[me].append([build_json('XLM', xlms[slots[slot][3]], [15, 14, 23])])
                elif slots[slot][7] == 'OAM/ORM/RAM/DSE/SCM/BMM':
                    if 'OAM' in slots[slot][8]:
                        me_json_obj[me].append([build_json('OAM', oams[slots[slot][3]], [15, 14, 23])])
                    elif 'ORM' in slots[slot][8]:
                        me_json_obj[me].append([build_json('ORM', orms[slots[slot][3]], [15, 14, 23])])
                    elif 'RAM' in slots[slot][8]:
                        me_json_obj[me].append([build_json('RAM', rams[slots[slot][3]], [15, 14, 23])])
                    elif 'DSE' in slots[slot][8]:
                        print("THERE ARE NO DSE TYPES")
                    elif 'SCM' in slots[slot][8]:
                        print("THERE ARE NO SCM TYPES")
                    elif 'BMM' in slots[slot][8]:
                        me_json_obj[me].append([build_json('BMM', bmms[slots[slot][3]], [15, 14, 23])])
                elif slots[slot][7] == 'TAM' and 'TAM' in slots[slot][8]:  # other possibilities are GAM, EMPTY
                    me_json_obj[me].append([build_json('TAM', tams[slots[slot][3]], [15, 14, 23])])
                    for tom in tams[slots[slot][3]][-1]:
                        if tom in toms:
                            me_json_obj[me][-1].append([build_json('TOM', toms[tom], [13, 15, 7, 14, 21])])
                        else:
                            me_json_obj[me][-1].append([build_json('EMPTY', tom, [99])])
                elif slots[slot][7] == 'TAM' and 'GAM' in slots[slot][8]:
                    me_json_obj[me].append(build_json('GAM', gams[slots[slot][3]], [15, 14, 23]))
                else:
                    if slots[slot][7] != 'TOM':
                        print(slots[slot])
            except Exception as ex:
                print(type(ex).__name__, ex.args)
                print(slots[slot])
        do_json.update(me_json_obj)
        # break  # Un-comment for a single pass
    with open(report + 'charter_dna.json', 'w') as f:
        json.dump(do_json, f, indent=4)

    dna_stats()


if __name__ == "__main__":
    main()





