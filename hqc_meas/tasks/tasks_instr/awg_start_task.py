# -*- coding: utf-8 -*-
# =============================================================================
# module : hqc_meas/tasks/task_instr/AWG_start_task.py
# author : Nathanael Cottet
# license : MIT license
# =============================================================================
"""
"""
from hqc_meas.tasks.api import (InstrumentTask)


class AWGStartTask(InstrumentTask):
    """Start the AWG pulse sequence loop after setting the trigger as required. 
    Need to be called after Phase Alazar task. 
    """

    driver_list = ['AWG5014B']

    def check(self, *args, **kwargs):
        """
        """
        return True, {}

    def perform(self):
        """
        Simply turning on the AWG
        """
        if not self.driver:
            self.start_driver()
        running_state = self.driver.running
        if running_state != '0 : Instrument has stopped':
            print 'WARNING: AWG already running'
            
        self.driver.running = 'RUN'
        
       
KNOWN_PY_TASKS = [AWGStartTask]