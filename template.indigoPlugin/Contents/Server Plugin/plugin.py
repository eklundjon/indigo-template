#! /usr/bin/env python

import indigo
import serial
import threading

################################################################################
class Plugin(indigo.PluginBase):
	#####################################
	# Begin Indigo plugin API functions #
	#####################################
	def __init__(self, pluginId, pluginDisplayName, pluginVersion, pluginPrefs):
	    indigo.PluginBase.__init__(self, pluginPrefs)
		self.debug = pluginPrefs.get("DebugFlag", False)
		self.stopThread = False

	def __del__(self):
	    indigo.PluginBase.__del__(self)

	########################################
	def startup(self):
		self.logger.debug(u"startup called")

	########################################
	def shutdown(self):
		self.logger.debug(u"shutdown called")
		
	########################################
	def deviceStartComm(self, dev, blockIfBusy=True):
		self.logger.debug(u"deviceStartComm called")
		#handle device upgrades
		#if 'newKey' not in dev.states:
		#	self.logger.info("Plugin Upgrade: Adding newKey state to Indigo Device")
		#	dev.stateListOrDisplayStateIdChanged()

	########################################
	def deviceStopComm(self, dev, blockIfBusy=True):
		self.logger.debug(u"deviceStopComm called")

	########################################
	#remove this function if no plugin thread is required
    def runDevConcurrentThread(self, dev):
		self.logger.debug(u"ConcurrentThread launched")
        while not self.stopThread:
            try:
                self.sleep(0.1)
            except:
                self.stopThread
                pass

	########################################
	#remove this function if no plugin thread is required
    def stopDevConcurrentThread(self):
        self.stopThread = True

	########################################
	def closedPrefsConfigUi(self, valuesDict, userCancelled):
		self.logger.debug(u"closedPrefsConfigUi enter")
		if userCancelled:
			return

	########################################
	def validateDeviceConfigUi(self, valuesDict, typeId, devId):
		self.logger.debug(u"validateDeviceConfigUi enter")

		errorsDict = indigo.Dict()

		if len(errorsDict) > 0:
			# Some UI fields are not valid, return corrected fields and error messages (client
			# will not let the dialog window close).
			return (False, valuesDict, errorsDict)

		# User choices look good, so return True (client will then close the dialog window).
		return (True, valuesDict)

	########################################
	def closedDeviceConfigUi(self, valuesDict, userCancelled, typeId, devId):
		self.logger.debug(u"closedDeviceConfigUi enter")
		if userCancelled:
			return

		#now that we're sure the device is actually being created,
		#we can finish variable initialization

    ########################################
    def didDeviceCommPropertyChange(self, origDev, newDev)
		self.logger.debug(u"didDeviceCommPropertyChange enter")
        return True
        
    ########################################
	def validateActionConfigUi(self, valuesDict, typeId, devId):
		self.logger.debug(u"validateActionConfigUi enter")
		errorsDict = indigo.Dict()

		if len(errorsDict) == 0:
			return (True, valuesDict)
		return (False, valuesDict, errorsDict)

	########################################
	def actionControlDevice(self, action, dev):
		self.logger.debug(u"actionControlDevice enter")
		
		if action.deviceAction == indigo.kDeviceAction.TurnOn: 
			self.powerOn(dev)			 
		
		if action.deviceAction == indigo.kDeviceAction.TurnOff:
			self.powerOff(dev)		
		
		if action.deviceAction == indigo.kDeviceAction.Toggle:
			if dev.onState == True:
				self.powerOff(dev)						
			elif dev.onState == False:
				self.powerOn(dev)		   
			else:			
				self.logger.error('"' + dev.name + '" in inconsistent state')		

	########################################
	#General Action callback
	def actionControlUniversal(self, action, dev):
		self.logger.debug(u"actionControlUniversal enter")
		###### STATUS REQUEST ######
		if action.deviceAction == indigo.kUniversalAction.RequestStatus:
			self.logger.debug(u"sent \"%s\" %s" % (dev.name, "status request"))

		else:
			self.logger.info(u"device cannot beep and have no energy counters")

	########################################
	def powerOff(self, dev):
	    self.logger.debug(u"Power Off")
	    return
			
	########################################
	def powerOn(self, dev):
	    self.logger.debug(u"Power On")
	    return
	
	########################################
	def doNothingMethod(self, valuesDict, typeId="", devId=None):
		# This method doesn't do anything itself, but its existence
		# forces the commandGenerator method below to get called.
		#self.logger.debug("doNothingMethod called")
		return

	########################################
	def commandGenerator(self, filter="", valuesDict=None, typeId="", devId=None):
		self.logger.debug(u"dynamicMenuGenerator called")
		self.logger.debug(valuesDict)
		group = valuesDict.get("CommandGroup", "")
		returnList = []

		if group == "":
			return returnList

		self.logger.debug("Looking up values for "+group)
		#returnList.extend([(command, self.enumCommands[command]["name"])])
        
		return returnList
