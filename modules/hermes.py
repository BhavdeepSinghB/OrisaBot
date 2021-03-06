from modules.logging_service import LoggingService
import signal
import datetime
import json
import os.path
import copy


class Hermes:
    __core = None
    __enabled = False
    __interval = 0
    __filename = None
    __backup_on_death = False
    signals = [signal.SIGINT, signal.SIGTERM]

    def __init__(self, settings, log=None):
        self.__enabled = settings.get('enabled', False)
        self.__interval = settings.get('interval', 0)
        self.__backup_on_death = settings.get('backup_on_death', False)
        self.__filename = f"backups/coredump.bak" #TODO add a backup task in the future
        if log:
            self.log = copy.copy(log)
        else:
            self.log = LoggingService(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
        self.log.sender = "HERMES"
        self.__config = {}
        self.log.info("Successfully constructed Hermes")
    
    @property
    def config(self):
        return self.__config

    @property
    def enabled(self):
        return self.__enabled
    
    @property
    def interval(self):
        return self.__interval

    @property
    def backup_on_death(self):
        return self.__backup_on_death

    def attach_core(self, Core):
        self.__core = Core
        self.log.info(f"Successfully attached Core: {Core}")


    def _format_globalMap(self, globalMap):
        self.log.info("Formatting globalMap")
        id_globalMap = {}
        for i in globalMap.keys():
            id_globalMap[i.id] = globalMap[i].isoformat()
        self.log.info("Successfully formatted globalMap")
        return id_globalMap 
    
    def _format_notify_dict(self, notifyDict):
        self.log.info("Formatting notifyDict")
        id_notifyDict = {}
        for i in notifyDict.keys():
            try:
                id_notifyDict[i.id] = [u.id for u in notifyDict[i]]
            except AttributeError:
                self.log.info("Adding 'All' to notifyDict")
                id_notifyDict["All"] = [u.id for u in notifyDict["All"]]
        return id_notifyDict

    def write_config(self):
        globalMap = self.__core.get_online_users()
        self.log.info("Writing globalMap")
        self.__config['globalMap'] = self._format_globalMap(globalMap) if globalMap else {}
        notifyDict = self.__core.notif_data
        self.log.info("Writing notifyDict")
        self.__config['notifyDict'] = self._format_notify_dict(notifyDict) if notifyDict else {}
        smurfList = self.__core.smurfs
        self.log.info("Writing smurfList")
        self.__config['smurfList'] = [x.id for x in smurfList] if smurfList else []
        with open(self.__filename, 'w') as outfile:
            json.dump(self.__config, outfile, indent=2)
        
    def read_config(self):
        if os.path.isfile(self.__filename):
            self.log.info("Backup exists")
            with open(self.__filename) as backup_file:
                self.log.info("Reading config")
                self.__config = json.load(backup_file)
                return True
        self.log.warn("Backup file not found")
        return False



