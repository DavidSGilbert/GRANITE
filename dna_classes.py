class ME(object):
    def __init__(self, _type,
                 _node_id,
                 _node_name,
                 _aid,
                 _sentryid,
                 _label,
                 _admin_state,
                 _operational_state,
                 _conditions,
                 _service_state,
                 _alarm_reporting,
                 _alarm_inhibit,
                 _auxip,
                 _auxipnetmask,
                 _auxipinterfaceadminstate,
                 _backplaneipprefix,
                 _clli,
                 _craftip,
                 _craftipnetmask,
                 _craftipinterfaceadminstate,
                 _dbver,
                 _dcndestination,
                 _dcngateway,
                 _dcnglobalroute,
                 _dcnip,
                 _dcnipnetmask,
                 _dcnprefixlen,
                 _ftpproxyport,
                 _gatewayproxyenabled,
                 _httpproxyport,
                 _latitude,
                 _location1,
                 _location2,
                 _longitude,
                 _netype,
                 _primarygneip,
                 _routerid,
                 _secondarygneip,
                 _swbuildinfo,
                 _swgenver,
                 _systemactivetime,
                 _systemtime,
                 _systemtimezoneoffset,
                 _telnetproxyport,
                 _tl1portid,
                 _xmlportid,
                 _xmlproxyport,
                 _arcbehaviour,
                 _tosbytealtered,
                 _trafficratelimit,
                 _licenseinfo,
                 _lastupgradetime,
                 _termloopbackbehavior,
                 _oscoobenable,
                 _restholdofftimer0,
                 _restholdofftimer1,
                 _restholdofftimer2,
                 _restholdofftimer3,
                 _restholdofftimer4,
                 _restholdofftimer5,
                 _restholdofftimer6,
                 _restholdofftimer7,
                 _enhprotsw,
                 _alsadministrationpolicy,
                 _dcninterfaceadminstate,
                 _nodecontrollerchassistype,
                 _migratednodeidlist,
                 _opticalgmplsmscid,
                 _neprepareupgradestatus,
                 _lastupgradepreptime,
                 _upgradeprepsuccesstime,
                 _loopbackaddress,
                 _loopbackaddressipv6,
                 _allow3rdpartytom,
                 _dcnip6,
                 _dcnip6netmask,
                 _dcndestination6,
                 _dcngateway6,
                 _dcnprefixlen6,
                 _craftip6,
                 _craftip6netmask,
                 _dcnip6linklocal,
                 _tmsubnetid,
                 _productname,
                 _communicationstate,
                 _mdname,
                 _owner,
                 _location,
                 _iptablestatus,
                 _polltime,
                 _timeout,
                 _isinsyncstate,
                 _tmmeaddress,
                 _domain,
                 _resourcestate,
                 _thirdpartytomenable,
                 _nwk3rdpartytomlicenseenabled):

        #        self.license = {}
        self.license = []
        self.ntpd = []
        self.bandctp_spanloss = []
        self.association = []
        self.xcon = []
        self.xfr = []
        self.community = []
        self.snmpconfig = []
        self.snmpaccesslist = []
        self.trapcfg = []
        self.snmpv3adminusertable = []
        self.te_interface = []
        self.securityprofile = []
        self.neighbor_links = []
        self.dbcontrol = []
        self.igcc = []
        self.staticroute = []
        self.gmpls_control_channel = []
        self.slot = []
        self.fiberlink = []
        self.toponode = []
        self.ctrllink = []
        self.pemshelf = []
        self.ioshelf = []
        self.olx = []
        self.otm = []
        self.tim = []
        self.xcm = []
        self.tsm = []
        self.xm = []
        self.xtim = []
        self.xmm = []
        self.chassis = []
        self.bmm = []
        self.dlm = []
        self.xlm = []
        self.tam = []
        self.tem = []
        self.tom = []
        self.mcm = []
        self.oam = []
        self.omm = []
        self.pem = []
        self.fan = []
        self.gam = []
        self.internallink = []
        self.bandctp = []
        self.bmmocgptp = []
        self.otsptp = []
        self.dcfptp = []
        self.clrchclientctp = []
        self.bandptp = []
        self.dtpctp_dtf_path_tam = []
        self.dtpctp_dtf_path_dlm = []
        self.channelctp = []
        self.dlmocgptp = []
        self.sonetclientctp = []
        self.gbe_client = []
        self.tribptp = []
        self.nctgige = []
        self.gamocgptp = []
        self.feedptp = []
        self.odukictp = []
        self.otukictp = []
        self.lmocgptp = []
        self.xtocgptp = []
        self.ochctp = []
        self.local_snc = []
        self.remote_snc = []
        self.local_sub_snc = []
        self.remote_sub_snc = []
        self.digitalsncp_1_port = []
        self.telink = []
        self.alarm = []
        self.service_object = []
        self.orm = []
        self.ram = []
        self.dse = []
        self.scm = []

        self._type = _type
        self._node_id = _node_id
        self._node_name = _node_name
        self._aid = _aid
        self._sentryid = _sentryid
        self._label = _label
        self._admin_state = _admin_state
        self._operational_state = _operational_state
        self._conditions = _conditions
        self._service_state = _service_state
        self._alarm_reporting = _alarm_reporting
        self._alarm_inhibit = _alarm_inhibit
        self._auxip = _auxip
        self._auxipnetmask = _auxipnetmask
        self._auxipinterfaceadminstate = _auxipinterfaceadminstate
        self._backplaneipprefix = _backplaneipprefix
        self._clli = _clli
        self._craftip = _craftip
        self._craftipnetmask = _craftipnetmask
        self._craftipinterfaceadminstate = _craftipinterfaceadminstate
        self._dbver = _dbver
        self._dcndestination = _dcndestination
        self._dcngateway = _dcngateway
        self._dcnglobalroute = _dcnglobalroute
        self._dcnip = _dcnip
        self._dcnipnetmask = _dcnipnetmask
        self._dcnprefixlen = _dcnprefixlen
        self._ftpproxyport = _ftpproxyport
        self._gatewayproxyenabled = _gatewayproxyenabled
        self._httpproxyport = _httpproxyport
        try:
            self._latitude = float(_latitude)
        except:
            self._latitude = 0.0

        try:
            self._longitude = float(_longitude)
        except:
            self._longitude = 0.0
        self._location1 = _location1
        self._location2 = _location2
        self._netype = _netype
        self._primarygneip = _primarygneip
        self._routerid = _routerid
        self._secondarygneip = _secondarygneip
        self._swbuildinfo = _swbuildinfo
        self._swgenver = _swgenver
        self._systemactivetime = _systemactivetime
        self._systemtime = _systemtime
        self._systemtimezoneoffset = _systemtimezoneoffset
        self._telnetproxyport = _telnetproxyport
        self._tl1portid = _tl1portid
        self._xmlportid = _xmlportid
        self._xmlproxyport = _xmlproxyport
        self._arcbehaviour = _arcbehaviour
        self._tosbytealtered = _tosbytealtered
        self._trafficratelimit = _trafficratelimit
        self._licenseinfo = _licenseinfo
        self._lastupgradetime = _lastupgradetime
        self._termloopbackbehavior = _termloopbackbehavior
        self._oscoobenable = _oscoobenable
        self._restholdofftimer0 = _restholdofftimer0
        self._restholdofftimer1 = _restholdofftimer1
        self._restholdofftimer2 = _restholdofftimer2
        self._restholdofftimer3 = _restholdofftimer3
        self._restholdofftimer4 = _restholdofftimer4
        self._restholdofftimer5 = _restholdofftimer5
        self._restholdofftimer6 = _restholdofftimer6
        self._restholdofftimer7 = _restholdofftimer7
        self._enhprotsw = _enhprotsw
        self._alsadministrationpolicy = _alsadministrationpolicy
        self._dcninterfaceadminstate = _dcninterfaceadminstate
        self._nodecontrollerchassistype = _nodecontrollerchassistype
        self._migratednodeidlist = _migratednodeidlist
        self._opticalgmplsmscid = _opticalgmplsmscid
        self._neprepareupgradestatus = _neprepareupgradestatus
        self._lastupgradepreptime = _lastupgradepreptime
        self._upgradeprepsuccesstime = _upgradeprepsuccesstime
        self._loopbackaddress = _loopbackaddress
        self._loopbackaddressipv6 = _loopbackaddressipv6
        self._allow3rdpartytom = _allow3rdpartytom
        self._dcnip6 = _dcnip6
        self._dcnip6netmask = _dcnip6netmask
        self._dcndestination6 = _dcndestination6
        self._dcngateway6 = _dcngateway6
        self._dcnprefixlen6 = _dcnprefixlen6
        self._craftip6 = _craftip6
        self._craftip6netmask = _craftip6netmask
        self._dcnip6linklocal = _dcnip6linklocal
        self._tmsubnetid = _tmsubnetid
        self._productname = _productname
        self._communicationstate = _communicationstate
        self._mdname = _mdname
        self._owner = _owner
        self._location = _location
        self._iptablestatus = _iptablestatus
        self._polltime = _polltime
        self._timeout = _timeout
        self._isinsyncstate = _isinsyncstate
        self._tmmeaddress = _tmmeaddress
        self._domain = _domain
        self._resourcestate = _resourcestate
        self._thirdpartytomenable = _thirdpartytomenable
        self._nwk3rdpartytomlicenseenabled = _nwk3rdpartytomlicenseenabled
        self._netfusionsite = ''


    def set_nf_site(self, name):
        try:
            self._netfusionsite = name
            print(u'\u2713', end='')
            print(f' set {self._node_id} NetFusion site ({self._netfusionsite})')
        except:
            pass


    def set_geo(self, lat: float, lon: float):
        try:
            self._latitude = float(lat)
            self._longitude = float(lon)
            print(u'\u2713', end='')
            print(f' set {self._node_id} geo-coordinates ({lat},{lon})')
        except:
            pass

    def get_geo(self):
        try:
            print(self._node_id, self._latitude, self._longitude)
        except:
            pass

    def set_location1(self, location):
        try:
            self._location1 = location
            print(u'\u2713', end='')
            print(f' set {self._node_id} location1 ({location})')
        except:
            pass

    def sort_slots(self, _key):
        try:
            self.slot = sorted(self.slot, key=lambda x: (x[_key]))
        except:
            pass

    def sort_gams(self, _key):
        try:
            self.gam = sorted(self.gam, key=lambda x: (x[_key]))
        except:
            pass

    def sort_tams(self, _key):
        try:
            self.tam = sorted(self.tam, key=lambda x: (x[_key]))
        except:
            pass

    def sort_toms(self, _key):
        try:
            self.tom = sorted(self.tom, key=lambda x: (x[_key]))
        except:
            pass