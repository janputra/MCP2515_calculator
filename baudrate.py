#!/usr/bin/python3

import time
import os
import sys
import numpy as np
from enum import IntEnum

class BaudrateConf:
    def __init__(self):
        self.f_osc = 0
        self.t_q = 0
        self.brp = 0 
        self.phseg1=0
        self.phseg2=0
        self.prseg=0
        self.bitrate=0
        self.targetbitrate=0.0

    def calTq(self):
        
        if self.brp==0:
            print("Input BRP\r\n")
        elif self.f_osc==0:
            print("Input FOSC\r\n")
        self.t_q = (2*self.brp)/self.f_osc 

    def calBitrate(self):
        
        self.calTq()
        self.bitrate = 1/((1+self.phseg1+self.phseg2+self.prseg)*self.t_q)

    def calRegister(self):
        print("BITRATE : "+str(self.targetbitrate))    
        acceptable = False
        while self.brp < 64:
            self.brp= self.brp+1
            acceptable = False
            for x in range(1,9):
                self.phseg1=x
                for y in range (1,9):
                    self.phseg2=y    
                    for z in range(1,9):
                        self.prseg=z
                        self.calBitrate()
                                        
                        if int(self.bitrate)==self.targetbitrate:


                            print("BRP : " + str(self.brp) +" PHSEG1 : " + str(self.phseg1) + " PHSEG2 : " + str(self.phseg2) + " PRSEG : " + str(self.prseg))


    def print_info(self):
        print("FOSC : " + str(self.f_osc))
        print("TQ : " + str(self.t_q))
        print("BRP : " + str(self.brp))
        print("PHSEG1 : " + str(self.phseg1))
        print("PHSEG2 : " + str(self.phseg2))
        print("PRSEG : " + str(self.prseg))
        print("BITRATE : "+str(self.bitrate))

def main() ->int:
    info = BaudrateConf()
    # info.brp = 16
    # info.phseg1=8
    # info.phseg2=8
    # info.prseg=8
    info.f_osc=16000000
    info.targetbitrate=20000
    # info.calBitrate()
    # info.print_info()
    info.calRegister()
    return 0

if __name__ == '__main__':
    main()