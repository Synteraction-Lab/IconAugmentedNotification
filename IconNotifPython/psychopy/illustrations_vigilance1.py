#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Tue 19 Jan 2021 12:04:14 PM +08
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import  trigger_notification_illustrations


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'illustrations_vigilance1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '01'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['participant'], expInfo['session'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/nj/Documents/Codes/Python/TriggerNotificationPython/psychopy/illustrations_vigilance1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[3840, 1200], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "start"
startClock = core.Clock()
txt_start = visual.TextStim(win=win, name='txt_start',
    text='Starting ...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "task"
taskClock = core.Clock()
track_click = event.Mouse(win=win)
x, y = [None, None]
track_click.mouseClock = core.Clock()
i1 = visual.ImageStim(
    win=win,
    name='i1', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
i2 = visual.ImageStim(
    win=win,
    name='i2', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
i3 = visual.ImageStim(
    win=win,
    name='i3', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
i4 = visual.ImageStim(
    win=win,
    name='i4', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
i5 = visual.ImageStim(
    win=win,
    name='i5', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
i6 = visual.ImageStim(
    win=win,
    name='i6', 
    image='img/76x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
i7 = visual.ImageStim(
    win=win,
    name='i7', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
i8 = visual.ImageStim(
    win=win,
    name='i8', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
i9 = visual.ImageStim(
    win=win,
    name='i9', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
i10 = visual.ImageStim(
    win=win,
    name='i10', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
i11 = visual.ImageStim(
    win=win,
    name='i11', 
    image='img/100x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
i12 = visual.ImageStim(
    win=win,
    name='i12', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
i13 = visual.ImageStim(
    win=win,
    name='i13', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
i14 = visual.ImageStim(
    win=win,
    name='i14', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
i15 = visual.ImageStim(
    win=win,
    name='i15', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
i16 = visual.ImageStim(
    win=win,
    name='i16', 
    image='img/100x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
i17 = visual.ImageStim(
    win=win,
    name='i17', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
i18 = visual.ImageStim(
    win=win,
    name='i18', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
i19 = visual.ImageStim(
    win=win,
    name='i19', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
i20 = visual.ImageStim(
    win=win,
    name='i20', 
    image='img/100x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
i21 = visual.ImageStim(
    win=win,
    name='i21', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
i22 = visual.ImageStim(
    win=win,
    name='i22', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
i23 = visual.ImageStim(
    win=win,
    name='i23', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
i24 = visual.ImageStim(
    win=win,
    name='i24', 
    image='img/76x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
i25 = visual.ImageStim(
    win=win,
    name='i25', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)
i26 = visual.ImageStim(
    win=win,
    name='i26', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-26.0)
i27 = visual.ImageStim(
    win=win,
    name='i27', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-27.0)
i28 = visual.ImageStim(
    win=win,
    name='i28', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-28.0)
i29 = visual.ImageStim(
    win=win,
    name='i29', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-29.0)
i30 = visual.ImageStim(
    win=win,
    name='i30', 
    image='img/76x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-30.0)
i31 = visual.ImageStim(
    win=win,
    name='i31', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-31.0)
i32 = visual.ImageStim(
    win=win,
    name='i32', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-32.0)
i33 = visual.ImageStim(
    win=win,
    name='i33', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-33.0)
i34 = visual.ImageStim(
    win=win,
    name='i34', 
    image='img/100x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-34.0)
i35 = visual.ImageStim(
    win=win,
    name='i35', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-35.0)
i36 = visual.ImageStim(
    win=win,
    name='i36', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-36.0)
i37 = visual.ImageStim(
    win=win,
    name='i37', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-37.0)
i38 = visual.ImageStim(
    win=win,
    name='i38', 
    image='img/100x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-38.0)
i39 = visual.ImageStim(
    win=win,
    name='i39', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-39.0)
i40 = visual.ImageStim(
    win=win,
    name='i40', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-40.0)
i41 = visual.ImageStim(
    win=win,
    name='i41', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-41.0)
i42 = visual.ImageStim(
    win=win,
    name='i42', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-42.0)
i43 = visual.ImageStim(
    win=win,
    name='i43', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-43.0)
i44 = visual.ImageStim(
    win=win,
    name='i44', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-44.0)
i45 = visual.ImageStim(
    win=win,
    name='i45', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-45.0)
i46 = visual.ImageStim(
    win=win,
    name='i46', 
    image='img/100x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-46.0)
i47 = visual.ImageStim(
    win=win,
    name='i47', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-47.0)
i48 = visual.ImageStim(
    win=win,
    name='i48', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-48.0)
i49 = visual.ImageStim(
    win=win,
    name='i49', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-49.0)
i50 = visual.ImageStim(
    win=win,
    name='i50', 
    image='img/76x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-50.0)
i51 = visual.ImageStim(
    win=win,
    name='i51', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-51.0)
i52 = visual.ImageStim(
    win=win,
    name='i52', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-52.0)
i53 = visual.ImageStim(
    win=win,
    name='i53', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-53.0)
i54 = visual.ImageStim(
    win=win,
    name='i54', 
    image='img/100x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-54.0)
i55 = visual.ImageStim(
    win=win,
    name='i55', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-55.0)
i56 = visual.ImageStim(
    win=win,
    name='i56', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-56.0)
i57 = visual.ImageStim(
    win=win,
    name='i57', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-57.0)
i58 = visual.ImageStim(
    win=win,
    name='i58', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-58.0)
i59 = visual.ImageStim(
    win=win,
    name='i59', 
    image='img/100x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-59.0)
i60 = visual.ImageStim(
    win=win,
    name='i60', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-60.0)
i61 = visual.ImageStim(
    win=win,
    name='i61', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-61.0)
i62 = visual.ImageStim(
    win=win,
    name='i62', 
    image='img/76x76.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-62.0)
i63 = visual.ImageStim(
    win=win,
    name='i63', 
    image='img/76x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-63.0)
i64 = visual.ImageStim(
    win=win,
    name='i64', 
    image='img/100x100.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-64.0)

# Initialize components for Routine "end"
endClock = core.Clock()
txt_end = visual.TextStim(win=win, name='txt_end',
    text='Stop',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "start"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
trigger_notification_illustrations.trigger_notification_randomly_threaded(expInfo['participant'], expInfo['session'], globalClock)
# keep track of which components have finished
startComponents = [txt_start]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt_start* updates
    if txt_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt_start.frameNStart = frameN  # exact frame index
        txt_start.tStart = t  # local t and not account for scr refresh
        txt_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt_start, 'tStartRefresh')  # time at next scr refresh
        txt_start.setAutoDraw(True)
    if txt_start.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > txt_start.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            txt_start.tStop = t  # not accounting for scr refresh
            txt_start.frameNStop = frameN  # exact frame index
            win.timeOnFlip(txt_start, 'tStopRefresh')  # time at next scr refresh
            txt_start.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt_start.started', txt_start.tStartRefresh)
thisExp.addData('txt_start.stopped', txt_start.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=6, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "task"-------
    continueRoutine = True
    routineTimer.add(40.000000)
    # update component parameters for each repeat
    # setup some python lists for storing info about the track_click
    track_click.x = []
    track_click.y = []
    track_click.leftButton = []
    track_click.midButton = []
    track_click.rightButton = []
    track_click.time = []
    gotValidClick = False  # until a click is received
    trigger_notification_illustrations.log_timing_threaded(expInfo['participant'], expInfo['session'], trials.thisRepN, globalClock.getTime(), win.getFutureFlipTime(clock=None))
    # keep track of which components have finished
    taskComponents = [track_click, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22, i23, i24, i25, i26, i27, i28, i29, i30, i31, i32, i33, i34, i35, i36, i37, i38, i39, i40, i41, i42, i43, i44, i45, i46, i47, i48, i49, i50, i51, i52, i53, i54, i55, i56, i57, i58, i59, i60, i61, i62, i63, i64]
    for thisComponent in taskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "task"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = taskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=taskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *track_click* updates
        if track_click.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            track_click.frameNStart = frameN  # exact frame index
            track_click.tStart = t  # local t and not account for scr refresh
            track_click.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(track_click, 'tStartRefresh')  # time at next scr refresh
            track_click.status = STARTED
            prevButtonState = track_click.getPressed()  # if button is down already this ISN'T a new click
        if track_click.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > track_click.tStartRefresh + 40-frameTolerance:
                # keep track of stop time/frame for later
                track_click.tStop = t  # not accounting for scr refresh
                track_click.frameNStop = frameN  # exact frame index
                win.timeOnFlip(track_click, 'tStopRefresh')  # time at next scr refresh
                track_click.status = FINISHED
        if track_click.status == STARTED:  # only update if started and not finished!
            buttons = track_click.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = track_click.getPos()
                    track_click.x.append(x)
                    track_click.y.append(y)
                    buttons = track_click.getPressed()
                    track_click.leftButton.append(buttons[0])
                    track_click.midButton.append(buttons[1])
                    track_click.rightButton.append(buttons[2])
                    track_click.time.append(globalClock.getTime())
        
        # *i1* updates
        if i1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            i1.frameNStart = frameN  # exact frame index
            i1.tStart = t  # local t and not account for scr refresh
            i1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i1, 'tStartRefresh')  # time at next scr refresh
            i1.setAutoDraw(True)
        if i1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i1.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i1.tStop = t  # not accounting for scr refresh
                i1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i1, 'tStopRefresh')  # time at next scr refresh
                i1.setAutoDraw(False)
        
        # *i2* updates
        if i2.status == NOT_STARTED and tThisFlip >= 0.625-frameTolerance:
            # keep track of start time/frame for later
            i2.frameNStart = frameN  # exact frame index
            i2.tStart = t  # local t and not account for scr refresh
            i2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i2, 'tStartRefresh')  # time at next scr refresh
            i2.setAutoDraw(True)
        if i2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i2.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i2.tStop = t  # not accounting for scr refresh
                i2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i2, 'tStopRefresh')  # time at next scr refresh
                i2.setAutoDraw(False)
        
        # *i3* updates
        if i3.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            i3.frameNStart = frameN  # exact frame index
            i3.tStart = t  # local t and not account for scr refresh
            i3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i3, 'tStartRefresh')  # time at next scr refresh
            i3.setAutoDraw(True)
        if i3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i3.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i3.tStop = t  # not accounting for scr refresh
                i3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i3, 'tStopRefresh')  # time at next scr refresh
                i3.setAutoDraw(False)
        
        # *i4* updates
        if i4.status == NOT_STARTED and tThisFlip >= 1.875-frameTolerance:
            # keep track of start time/frame for later
            i4.frameNStart = frameN  # exact frame index
            i4.tStart = t  # local t and not account for scr refresh
            i4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i4, 'tStartRefresh')  # time at next scr refresh
            i4.setAutoDraw(True)
        if i4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i4.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i4.tStop = t  # not accounting for scr refresh
                i4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i4, 'tStopRefresh')  # time at next scr refresh
                i4.setAutoDraw(False)
        
        # *i5* updates
        if i5.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            i5.frameNStart = frameN  # exact frame index
            i5.tStart = t  # local t and not account for scr refresh
            i5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i5, 'tStartRefresh')  # time at next scr refresh
            i5.setAutoDraw(True)
        if i5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i5.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i5.tStop = t  # not accounting for scr refresh
                i5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i5, 'tStopRefresh')  # time at next scr refresh
                i5.setAutoDraw(False)
        
        # *i6* updates
        if i6.status == NOT_STARTED and tThisFlip >= 3.125-frameTolerance:
            # keep track of start time/frame for later
            i6.frameNStart = frameN  # exact frame index
            i6.tStart = t  # local t and not account for scr refresh
            i6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i6, 'tStartRefresh')  # time at next scr refresh
            i6.setAutoDraw(True)
        if i6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i6.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i6.tStop = t  # not accounting for scr refresh
                i6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i6, 'tStopRefresh')  # time at next scr refresh
                i6.setAutoDraw(False)
        
        # *i7* updates
        if i7.status == NOT_STARTED and tThisFlip >= 3.75-frameTolerance:
            # keep track of start time/frame for later
            i7.frameNStart = frameN  # exact frame index
            i7.tStart = t  # local t and not account for scr refresh
            i7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i7, 'tStartRefresh')  # time at next scr refresh
            i7.setAutoDraw(True)
        if i7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i7.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i7.tStop = t  # not accounting for scr refresh
                i7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i7, 'tStopRefresh')  # time at next scr refresh
                i7.setAutoDraw(False)
        
        # *i8* updates
        if i8.status == NOT_STARTED and tThisFlip >= 4.375-frameTolerance:
            # keep track of start time/frame for later
            i8.frameNStart = frameN  # exact frame index
            i8.tStart = t  # local t and not account for scr refresh
            i8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i8, 'tStartRefresh')  # time at next scr refresh
            i8.setAutoDraw(True)
        if i8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i8.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i8.tStop = t  # not accounting for scr refresh
                i8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i8, 'tStopRefresh')  # time at next scr refresh
                i8.setAutoDraw(False)
        
        # *i9* updates
        if i9.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            i9.frameNStart = frameN  # exact frame index
            i9.tStart = t  # local t and not account for scr refresh
            i9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i9, 'tStartRefresh')  # time at next scr refresh
            i9.setAutoDraw(True)
        if i9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i9.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i9.tStop = t  # not accounting for scr refresh
                i9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i9, 'tStopRefresh')  # time at next scr refresh
                i9.setAutoDraw(False)
        
        # *i10* updates
        if i10.status == NOT_STARTED and tThisFlip >= 5.625-frameTolerance:
            # keep track of start time/frame for later
            i10.frameNStart = frameN  # exact frame index
            i10.tStart = t  # local t and not account for scr refresh
            i10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i10, 'tStartRefresh')  # time at next scr refresh
            i10.setAutoDraw(True)
        if i10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i10.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i10.tStop = t  # not accounting for scr refresh
                i10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i10, 'tStopRefresh')  # time at next scr refresh
                i10.setAutoDraw(False)
        
        # *i11* updates
        if i11.status == NOT_STARTED and tThisFlip >= 6.25-frameTolerance:
            # keep track of start time/frame for later
            i11.frameNStart = frameN  # exact frame index
            i11.tStart = t  # local t and not account for scr refresh
            i11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i11, 'tStartRefresh')  # time at next scr refresh
            i11.setAutoDraw(True)
        if i11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i11.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i11.tStop = t  # not accounting for scr refresh
                i11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i11, 'tStopRefresh')  # time at next scr refresh
                i11.setAutoDraw(False)
        
        # *i12* updates
        if i12.status == NOT_STARTED and tThisFlip >= 6.875-frameTolerance:
            # keep track of start time/frame for later
            i12.frameNStart = frameN  # exact frame index
            i12.tStart = t  # local t and not account for scr refresh
            i12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i12, 'tStartRefresh')  # time at next scr refresh
            i12.setAutoDraw(True)
        if i12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i12.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i12.tStop = t  # not accounting for scr refresh
                i12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i12, 'tStopRefresh')  # time at next scr refresh
                i12.setAutoDraw(False)
        
        # *i13* updates
        if i13.status == NOT_STARTED and tThisFlip >= 7.5-frameTolerance:
            # keep track of start time/frame for later
            i13.frameNStart = frameN  # exact frame index
            i13.tStart = t  # local t and not account for scr refresh
            i13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i13, 'tStartRefresh')  # time at next scr refresh
            i13.setAutoDraw(True)
        if i13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i13.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i13.tStop = t  # not accounting for scr refresh
                i13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i13, 'tStopRefresh')  # time at next scr refresh
                i13.setAutoDraw(False)
        
        # *i14* updates
        if i14.status == NOT_STARTED and tThisFlip >= 8.125-frameTolerance:
            # keep track of start time/frame for later
            i14.frameNStart = frameN  # exact frame index
            i14.tStart = t  # local t and not account for scr refresh
            i14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i14, 'tStartRefresh')  # time at next scr refresh
            i14.setAutoDraw(True)
        if i14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i14.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i14.tStop = t  # not accounting for scr refresh
                i14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i14, 'tStopRefresh')  # time at next scr refresh
                i14.setAutoDraw(False)
        
        # *i15* updates
        if i15.status == NOT_STARTED and tThisFlip >= 8.75-frameTolerance:
            # keep track of start time/frame for later
            i15.frameNStart = frameN  # exact frame index
            i15.tStart = t  # local t and not account for scr refresh
            i15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i15, 'tStartRefresh')  # time at next scr refresh
            i15.setAutoDraw(True)
        if i15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i15.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i15.tStop = t  # not accounting for scr refresh
                i15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i15, 'tStopRefresh')  # time at next scr refresh
                i15.setAutoDraw(False)
        
        # *i16* updates
        if i16.status == NOT_STARTED and tThisFlip >= 9.375-frameTolerance:
            # keep track of start time/frame for later
            i16.frameNStart = frameN  # exact frame index
            i16.tStart = t  # local t and not account for scr refresh
            i16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i16, 'tStartRefresh')  # time at next scr refresh
            i16.setAutoDraw(True)
        if i16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i16.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i16.tStop = t  # not accounting for scr refresh
                i16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i16, 'tStopRefresh')  # time at next scr refresh
                i16.setAutoDraw(False)
        
        # *i17* updates
        if i17.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            i17.frameNStart = frameN  # exact frame index
            i17.tStart = t  # local t and not account for scr refresh
            i17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i17, 'tStartRefresh')  # time at next scr refresh
            i17.setAutoDraw(True)
        if i17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i17.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i17.tStop = t  # not accounting for scr refresh
                i17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i17, 'tStopRefresh')  # time at next scr refresh
                i17.setAutoDraw(False)
        
        # *i18* updates
        if i18.status == NOT_STARTED and tThisFlip >= 10.625-frameTolerance:
            # keep track of start time/frame for later
            i18.frameNStart = frameN  # exact frame index
            i18.tStart = t  # local t and not account for scr refresh
            i18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i18, 'tStartRefresh')  # time at next scr refresh
            i18.setAutoDraw(True)
        if i18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i18.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i18.tStop = t  # not accounting for scr refresh
                i18.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i18, 'tStopRefresh')  # time at next scr refresh
                i18.setAutoDraw(False)
        
        # *i19* updates
        if i19.status == NOT_STARTED and tThisFlip >= 11.25-frameTolerance:
            # keep track of start time/frame for later
            i19.frameNStart = frameN  # exact frame index
            i19.tStart = t  # local t and not account for scr refresh
            i19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i19, 'tStartRefresh')  # time at next scr refresh
            i19.setAutoDraw(True)
        if i19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i19.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i19.tStop = t  # not accounting for scr refresh
                i19.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i19, 'tStopRefresh')  # time at next scr refresh
                i19.setAutoDraw(False)
        
        # *i20* updates
        if i20.status == NOT_STARTED and tThisFlip >= 11.875-frameTolerance:
            # keep track of start time/frame for later
            i20.frameNStart = frameN  # exact frame index
            i20.tStart = t  # local t and not account for scr refresh
            i20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i20, 'tStartRefresh')  # time at next scr refresh
            i20.setAutoDraw(True)
        if i20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i20.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i20.tStop = t  # not accounting for scr refresh
                i20.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i20, 'tStopRefresh')  # time at next scr refresh
                i20.setAutoDraw(False)
        
        # *i21* updates
        if i21.status == NOT_STARTED and tThisFlip >= 12.5-frameTolerance:
            # keep track of start time/frame for later
            i21.frameNStart = frameN  # exact frame index
            i21.tStart = t  # local t and not account for scr refresh
            i21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i21, 'tStartRefresh')  # time at next scr refresh
            i21.setAutoDraw(True)
        if i21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i21.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i21.tStop = t  # not accounting for scr refresh
                i21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i21, 'tStopRefresh')  # time at next scr refresh
                i21.setAutoDraw(False)
        
        # *i22* updates
        if i22.status == NOT_STARTED and tThisFlip >= 13.125-frameTolerance:
            # keep track of start time/frame for later
            i22.frameNStart = frameN  # exact frame index
            i22.tStart = t  # local t and not account for scr refresh
            i22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i22, 'tStartRefresh')  # time at next scr refresh
            i22.setAutoDraw(True)
        if i22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i22.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i22.tStop = t  # not accounting for scr refresh
                i22.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i22, 'tStopRefresh')  # time at next scr refresh
                i22.setAutoDraw(False)
        
        # *i23* updates
        if i23.status == NOT_STARTED and tThisFlip >= 13.75-frameTolerance:
            # keep track of start time/frame for later
            i23.frameNStart = frameN  # exact frame index
            i23.tStart = t  # local t and not account for scr refresh
            i23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i23, 'tStartRefresh')  # time at next scr refresh
            i23.setAutoDraw(True)
        if i23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i23.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i23.tStop = t  # not accounting for scr refresh
                i23.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i23, 'tStopRefresh')  # time at next scr refresh
                i23.setAutoDraw(False)
        
        # *i24* updates
        if i24.status == NOT_STARTED and tThisFlip >= 14.375-frameTolerance:
            # keep track of start time/frame for later
            i24.frameNStart = frameN  # exact frame index
            i24.tStart = t  # local t and not account for scr refresh
            i24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i24, 'tStartRefresh')  # time at next scr refresh
            i24.setAutoDraw(True)
        if i24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i24.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i24.tStop = t  # not accounting for scr refresh
                i24.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i24, 'tStopRefresh')  # time at next scr refresh
                i24.setAutoDraw(False)
        
        # *i25* updates
        if i25.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            i25.frameNStart = frameN  # exact frame index
            i25.tStart = t  # local t and not account for scr refresh
            i25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i25, 'tStartRefresh')  # time at next scr refresh
            i25.setAutoDraw(True)
        if i25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i25.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i25.tStop = t  # not accounting for scr refresh
                i25.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i25, 'tStopRefresh')  # time at next scr refresh
                i25.setAutoDraw(False)
        
        # *i26* updates
        if i26.status == NOT_STARTED and tThisFlip >= 15.625-frameTolerance:
            # keep track of start time/frame for later
            i26.frameNStart = frameN  # exact frame index
            i26.tStart = t  # local t and not account for scr refresh
            i26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i26, 'tStartRefresh')  # time at next scr refresh
            i26.setAutoDraw(True)
        if i26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i26.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i26.tStop = t  # not accounting for scr refresh
                i26.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i26, 'tStopRefresh')  # time at next scr refresh
                i26.setAutoDraw(False)
        
        # *i27* updates
        if i27.status == NOT_STARTED and tThisFlip >= 16.25-frameTolerance:
            # keep track of start time/frame for later
            i27.frameNStart = frameN  # exact frame index
            i27.tStart = t  # local t and not account for scr refresh
            i27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i27, 'tStartRefresh')  # time at next scr refresh
            i27.setAutoDraw(True)
        if i27.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i27.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i27.tStop = t  # not accounting for scr refresh
                i27.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i27, 'tStopRefresh')  # time at next scr refresh
                i27.setAutoDraw(False)
        
        # *i28* updates
        if i28.status == NOT_STARTED and tThisFlip >= 16.875-frameTolerance:
            # keep track of start time/frame for later
            i28.frameNStart = frameN  # exact frame index
            i28.tStart = t  # local t and not account for scr refresh
            i28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i28, 'tStartRefresh')  # time at next scr refresh
            i28.setAutoDraw(True)
        if i28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i28.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i28.tStop = t  # not accounting for scr refresh
                i28.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i28, 'tStopRefresh')  # time at next scr refresh
                i28.setAutoDraw(False)
        
        # *i29* updates
        if i29.status == NOT_STARTED and tThisFlip >= 17.5-frameTolerance:
            # keep track of start time/frame for later
            i29.frameNStart = frameN  # exact frame index
            i29.tStart = t  # local t and not account for scr refresh
            i29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i29, 'tStartRefresh')  # time at next scr refresh
            i29.setAutoDraw(True)
        if i29.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i29.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i29.tStop = t  # not accounting for scr refresh
                i29.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i29, 'tStopRefresh')  # time at next scr refresh
                i29.setAutoDraw(False)
        
        # *i30* updates
        if i30.status == NOT_STARTED and tThisFlip >= 18.125-frameTolerance:
            # keep track of start time/frame for later
            i30.frameNStart = frameN  # exact frame index
            i30.tStart = t  # local t and not account for scr refresh
            i30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i30, 'tStartRefresh')  # time at next scr refresh
            i30.setAutoDraw(True)
        if i30.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i30.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i30.tStop = t  # not accounting for scr refresh
                i30.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i30, 'tStopRefresh')  # time at next scr refresh
                i30.setAutoDraw(False)
        
        # *i31* updates
        if i31.status == NOT_STARTED and tThisFlip >= 18.75-frameTolerance:
            # keep track of start time/frame for later
            i31.frameNStart = frameN  # exact frame index
            i31.tStart = t  # local t and not account for scr refresh
            i31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i31, 'tStartRefresh')  # time at next scr refresh
            i31.setAutoDraw(True)
        if i31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i31.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i31.tStop = t  # not accounting for scr refresh
                i31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i31, 'tStopRefresh')  # time at next scr refresh
                i31.setAutoDraw(False)
        
        # *i32* updates
        if i32.status == NOT_STARTED and tThisFlip >= 19.375-frameTolerance:
            # keep track of start time/frame for later
            i32.frameNStart = frameN  # exact frame index
            i32.tStart = t  # local t and not account for scr refresh
            i32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i32, 'tStartRefresh')  # time at next scr refresh
            i32.setAutoDraw(True)
        if i32.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i32.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i32.tStop = t  # not accounting for scr refresh
                i32.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i32, 'tStopRefresh')  # time at next scr refresh
                i32.setAutoDraw(False)
        
        # *i33* updates
        if i33.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            i33.frameNStart = frameN  # exact frame index
            i33.tStart = t  # local t and not account for scr refresh
            i33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i33, 'tStartRefresh')  # time at next scr refresh
            i33.setAutoDraw(True)
        if i33.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i33.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i33.tStop = t  # not accounting for scr refresh
                i33.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i33, 'tStopRefresh')  # time at next scr refresh
                i33.setAutoDraw(False)
        
        # *i34* updates
        if i34.status == NOT_STARTED and tThisFlip >= 20.625-frameTolerance:
            # keep track of start time/frame for later
            i34.frameNStart = frameN  # exact frame index
            i34.tStart = t  # local t and not account for scr refresh
            i34.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i34, 'tStartRefresh')  # time at next scr refresh
            i34.setAutoDraw(True)
        if i34.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i34.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i34.tStop = t  # not accounting for scr refresh
                i34.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i34, 'tStopRefresh')  # time at next scr refresh
                i34.setAutoDraw(False)
        
        # *i35* updates
        if i35.status == NOT_STARTED and tThisFlip >= 21.25-frameTolerance:
            # keep track of start time/frame for later
            i35.frameNStart = frameN  # exact frame index
            i35.tStart = t  # local t and not account for scr refresh
            i35.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i35, 'tStartRefresh')  # time at next scr refresh
            i35.setAutoDraw(True)
        if i35.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i35.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i35.tStop = t  # not accounting for scr refresh
                i35.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i35, 'tStopRefresh')  # time at next scr refresh
                i35.setAutoDraw(False)
        
        # *i36* updates
        if i36.status == NOT_STARTED and tThisFlip >= 21.875-frameTolerance:
            # keep track of start time/frame for later
            i36.frameNStart = frameN  # exact frame index
            i36.tStart = t  # local t and not account for scr refresh
            i36.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i36, 'tStartRefresh')  # time at next scr refresh
            i36.setAutoDraw(True)
        if i36.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i36.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i36.tStop = t  # not accounting for scr refresh
                i36.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i36, 'tStopRefresh')  # time at next scr refresh
                i36.setAutoDraw(False)
        
        # *i37* updates
        if i37.status == NOT_STARTED and tThisFlip >= 22.5-frameTolerance:
            # keep track of start time/frame for later
            i37.frameNStart = frameN  # exact frame index
            i37.tStart = t  # local t and not account for scr refresh
            i37.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i37, 'tStartRefresh')  # time at next scr refresh
            i37.setAutoDraw(True)
        if i37.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i37.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i37.tStop = t  # not accounting for scr refresh
                i37.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i37, 'tStopRefresh')  # time at next scr refresh
                i37.setAutoDraw(False)
        
        # *i38* updates
        if i38.status == NOT_STARTED and tThisFlip >= 23.125-frameTolerance:
            # keep track of start time/frame for later
            i38.frameNStart = frameN  # exact frame index
            i38.tStart = t  # local t and not account for scr refresh
            i38.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i38, 'tStartRefresh')  # time at next scr refresh
            i38.setAutoDraw(True)
        if i38.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i38.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i38.tStop = t  # not accounting for scr refresh
                i38.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i38, 'tStopRefresh')  # time at next scr refresh
                i38.setAutoDraw(False)
        
        # *i39* updates
        if i39.status == NOT_STARTED and tThisFlip >= 23.75-frameTolerance:
            # keep track of start time/frame for later
            i39.frameNStart = frameN  # exact frame index
            i39.tStart = t  # local t and not account for scr refresh
            i39.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i39, 'tStartRefresh')  # time at next scr refresh
            i39.setAutoDraw(True)
        if i39.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i39.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i39.tStop = t  # not accounting for scr refresh
                i39.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i39, 'tStopRefresh')  # time at next scr refresh
                i39.setAutoDraw(False)
        
        # *i40* updates
        if i40.status == NOT_STARTED and tThisFlip >= 24.375-frameTolerance:
            # keep track of start time/frame for later
            i40.frameNStart = frameN  # exact frame index
            i40.tStart = t  # local t and not account for scr refresh
            i40.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i40, 'tStartRefresh')  # time at next scr refresh
            i40.setAutoDraw(True)
        if i40.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i40.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i40.tStop = t  # not accounting for scr refresh
                i40.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i40, 'tStopRefresh')  # time at next scr refresh
                i40.setAutoDraw(False)
        
        # *i41* updates
        if i41.status == NOT_STARTED and tThisFlip >= 25-frameTolerance:
            # keep track of start time/frame for later
            i41.frameNStart = frameN  # exact frame index
            i41.tStart = t  # local t and not account for scr refresh
            i41.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i41, 'tStartRefresh')  # time at next scr refresh
            i41.setAutoDraw(True)
        if i41.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i41.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i41.tStop = t  # not accounting for scr refresh
                i41.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i41, 'tStopRefresh')  # time at next scr refresh
                i41.setAutoDraw(False)
        
        # *i42* updates
        if i42.status == NOT_STARTED and tThisFlip >= 25.625-frameTolerance:
            # keep track of start time/frame for later
            i42.frameNStart = frameN  # exact frame index
            i42.tStart = t  # local t and not account for scr refresh
            i42.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i42, 'tStartRefresh')  # time at next scr refresh
            i42.setAutoDraw(True)
        if i42.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i42.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i42.tStop = t  # not accounting for scr refresh
                i42.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i42, 'tStopRefresh')  # time at next scr refresh
                i42.setAutoDraw(False)
        
        # *i43* updates
        if i43.status == NOT_STARTED and tThisFlip >= 26.25-frameTolerance:
            # keep track of start time/frame for later
            i43.frameNStart = frameN  # exact frame index
            i43.tStart = t  # local t and not account for scr refresh
            i43.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i43, 'tStartRefresh')  # time at next scr refresh
            i43.setAutoDraw(True)
        if i43.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i43.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i43.tStop = t  # not accounting for scr refresh
                i43.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i43, 'tStopRefresh')  # time at next scr refresh
                i43.setAutoDraw(False)
        
        # *i44* updates
        if i44.status == NOT_STARTED and tThisFlip >= 26.875-frameTolerance:
            # keep track of start time/frame for later
            i44.frameNStart = frameN  # exact frame index
            i44.tStart = t  # local t and not account for scr refresh
            i44.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i44, 'tStartRefresh')  # time at next scr refresh
            i44.setAutoDraw(True)
        if i44.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i44.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i44.tStop = t  # not accounting for scr refresh
                i44.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i44, 'tStopRefresh')  # time at next scr refresh
                i44.setAutoDraw(False)
        
        # *i45* updates
        if i45.status == NOT_STARTED and tThisFlip >= 27.5-frameTolerance:
            # keep track of start time/frame for later
            i45.frameNStart = frameN  # exact frame index
            i45.tStart = t  # local t and not account for scr refresh
            i45.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i45, 'tStartRefresh')  # time at next scr refresh
            i45.setAutoDraw(True)
        if i45.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i45.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i45.tStop = t  # not accounting for scr refresh
                i45.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i45, 'tStopRefresh')  # time at next scr refresh
                i45.setAutoDraw(False)
        
        # *i46* updates
        if i46.status == NOT_STARTED and tThisFlip >= 28.125-frameTolerance:
            # keep track of start time/frame for later
            i46.frameNStart = frameN  # exact frame index
            i46.tStart = t  # local t and not account for scr refresh
            i46.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i46, 'tStartRefresh')  # time at next scr refresh
            i46.setAutoDraw(True)
        if i46.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i46.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i46.tStop = t  # not accounting for scr refresh
                i46.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i46, 'tStopRefresh')  # time at next scr refresh
                i46.setAutoDraw(False)
        
        # *i47* updates
        if i47.status == NOT_STARTED and tThisFlip >= 28.75-frameTolerance:
            # keep track of start time/frame for later
            i47.frameNStart = frameN  # exact frame index
            i47.tStart = t  # local t and not account for scr refresh
            i47.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i47, 'tStartRefresh')  # time at next scr refresh
            i47.setAutoDraw(True)
        if i47.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i47.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i47.tStop = t  # not accounting for scr refresh
                i47.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i47, 'tStopRefresh')  # time at next scr refresh
                i47.setAutoDraw(False)
        
        # *i48* updates
        if i48.status == NOT_STARTED and tThisFlip >= 29.375-frameTolerance:
            # keep track of start time/frame for later
            i48.frameNStart = frameN  # exact frame index
            i48.tStart = t  # local t and not account for scr refresh
            i48.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i48, 'tStartRefresh')  # time at next scr refresh
            i48.setAutoDraw(True)
        if i48.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i48.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i48.tStop = t  # not accounting for scr refresh
                i48.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i48, 'tStopRefresh')  # time at next scr refresh
                i48.setAutoDraw(False)
        
        # *i49* updates
        if i49.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
            # keep track of start time/frame for later
            i49.frameNStart = frameN  # exact frame index
            i49.tStart = t  # local t and not account for scr refresh
            i49.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i49, 'tStartRefresh')  # time at next scr refresh
            i49.setAutoDraw(True)
        if i49.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i49.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i49.tStop = t  # not accounting for scr refresh
                i49.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i49, 'tStopRefresh')  # time at next scr refresh
                i49.setAutoDraw(False)
        
        # *i50* updates
        if i50.status == NOT_STARTED and tThisFlip >= 30.625-frameTolerance:
            # keep track of start time/frame for later
            i50.frameNStart = frameN  # exact frame index
            i50.tStart = t  # local t and not account for scr refresh
            i50.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i50, 'tStartRefresh')  # time at next scr refresh
            i50.setAutoDraw(True)
        if i50.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i50.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i50.tStop = t  # not accounting for scr refresh
                i50.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i50, 'tStopRefresh')  # time at next scr refresh
                i50.setAutoDraw(False)
        
        # *i51* updates
        if i51.status == NOT_STARTED and tThisFlip >= 31.25-frameTolerance:
            # keep track of start time/frame for later
            i51.frameNStart = frameN  # exact frame index
            i51.tStart = t  # local t and not account for scr refresh
            i51.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i51, 'tStartRefresh')  # time at next scr refresh
            i51.setAutoDraw(True)
        if i51.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i51.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i51.tStop = t  # not accounting for scr refresh
                i51.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i51, 'tStopRefresh')  # time at next scr refresh
                i51.setAutoDraw(False)
        
        # *i52* updates
        if i52.status == NOT_STARTED and tThisFlip >= 31.875-frameTolerance:
            # keep track of start time/frame for later
            i52.frameNStart = frameN  # exact frame index
            i52.tStart = t  # local t and not account for scr refresh
            i52.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i52, 'tStartRefresh')  # time at next scr refresh
            i52.setAutoDraw(True)
        if i52.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i52.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i52.tStop = t  # not accounting for scr refresh
                i52.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i52, 'tStopRefresh')  # time at next scr refresh
                i52.setAutoDraw(False)
        
        # *i53* updates
        if i53.status == NOT_STARTED and tThisFlip >= 32.5-frameTolerance:
            # keep track of start time/frame for later
            i53.frameNStart = frameN  # exact frame index
            i53.tStart = t  # local t and not account for scr refresh
            i53.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i53, 'tStartRefresh')  # time at next scr refresh
            i53.setAutoDraw(True)
        if i53.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i53.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i53.tStop = t  # not accounting for scr refresh
                i53.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i53, 'tStopRefresh')  # time at next scr refresh
                i53.setAutoDraw(False)
        
        # *i54* updates
        if i54.status == NOT_STARTED and tThisFlip >= 33.125-frameTolerance:
            # keep track of start time/frame for later
            i54.frameNStart = frameN  # exact frame index
            i54.tStart = t  # local t and not account for scr refresh
            i54.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i54, 'tStartRefresh')  # time at next scr refresh
            i54.setAutoDraw(True)
        if i54.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i54.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i54.tStop = t  # not accounting for scr refresh
                i54.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i54, 'tStopRefresh')  # time at next scr refresh
                i54.setAutoDraw(False)
        
        # *i55* updates
        if i55.status == NOT_STARTED and tThisFlip >= 33.75-frameTolerance:
            # keep track of start time/frame for later
            i55.frameNStart = frameN  # exact frame index
            i55.tStart = t  # local t and not account for scr refresh
            i55.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i55, 'tStartRefresh')  # time at next scr refresh
            i55.setAutoDraw(True)
        if i55.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i55.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i55.tStop = t  # not accounting for scr refresh
                i55.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i55, 'tStopRefresh')  # time at next scr refresh
                i55.setAutoDraw(False)
        
        # *i56* updates
        if i56.status == NOT_STARTED and tThisFlip >= 34.375-frameTolerance:
            # keep track of start time/frame for later
            i56.frameNStart = frameN  # exact frame index
            i56.tStart = t  # local t and not account for scr refresh
            i56.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i56, 'tStartRefresh')  # time at next scr refresh
            i56.setAutoDraw(True)
        if i56.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i56.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i56.tStop = t  # not accounting for scr refresh
                i56.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i56, 'tStopRefresh')  # time at next scr refresh
                i56.setAutoDraw(False)
        
        # *i57* updates
        if i57.status == NOT_STARTED and tThisFlip >= 35-frameTolerance:
            # keep track of start time/frame for later
            i57.frameNStart = frameN  # exact frame index
            i57.tStart = t  # local t and not account for scr refresh
            i57.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i57, 'tStartRefresh')  # time at next scr refresh
            i57.setAutoDraw(True)
        if i57.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i57.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i57.tStop = t  # not accounting for scr refresh
                i57.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i57, 'tStopRefresh')  # time at next scr refresh
                i57.setAutoDraw(False)
        
        # *i58* updates
        if i58.status == NOT_STARTED and tThisFlip >= 35.625-frameTolerance:
            # keep track of start time/frame for later
            i58.frameNStart = frameN  # exact frame index
            i58.tStart = t  # local t and not account for scr refresh
            i58.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i58, 'tStartRefresh')  # time at next scr refresh
            i58.setAutoDraw(True)
        if i58.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i58.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i58.tStop = t  # not accounting for scr refresh
                i58.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i58, 'tStopRefresh')  # time at next scr refresh
                i58.setAutoDraw(False)
        
        # *i59* updates
        if i59.status == NOT_STARTED and tThisFlip >= 36.25-frameTolerance:
            # keep track of start time/frame for later
            i59.frameNStart = frameN  # exact frame index
            i59.tStart = t  # local t and not account for scr refresh
            i59.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i59, 'tStartRefresh')  # time at next scr refresh
            i59.setAutoDraw(True)
        if i59.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i59.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i59.tStop = t  # not accounting for scr refresh
                i59.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i59, 'tStopRefresh')  # time at next scr refresh
                i59.setAutoDraw(False)
        
        # *i60* updates
        if i60.status == NOT_STARTED and tThisFlip >= 36.875-frameTolerance:
            # keep track of start time/frame for later
            i60.frameNStart = frameN  # exact frame index
            i60.tStart = t  # local t and not account for scr refresh
            i60.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i60, 'tStartRefresh')  # time at next scr refresh
            i60.setAutoDraw(True)
        if i60.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i60.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i60.tStop = t  # not accounting for scr refresh
                i60.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i60, 'tStopRefresh')  # time at next scr refresh
                i60.setAutoDraw(False)
        
        # *i61* updates
        if i61.status == NOT_STARTED and tThisFlip >= 37.5-frameTolerance:
            # keep track of start time/frame for later
            i61.frameNStart = frameN  # exact frame index
            i61.tStart = t  # local t and not account for scr refresh
            i61.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i61, 'tStartRefresh')  # time at next scr refresh
            i61.setAutoDraw(True)
        if i61.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i61.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i61.tStop = t  # not accounting for scr refresh
                i61.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i61, 'tStopRefresh')  # time at next scr refresh
                i61.setAutoDraw(False)
        
        # *i62* updates
        if i62.status == NOT_STARTED and tThisFlip >= 38.125-frameTolerance:
            # keep track of start time/frame for later
            i62.frameNStart = frameN  # exact frame index
            i62.tStart = t  # local t and not account for scr refresh
            i62.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i62, 'tStartRefresh')  # time at next scr refresh
            i62.setAutoDraw(True)
        if i62.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i62.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i62.tStop = t  # not accounting for scr refresh
                i62.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i62, 'tStopRefresh')  # time at next scr refresh
                i62.setAutoDraw(False)
        
        # *i63* updates
        if i63.status == NOT_STARTED and tThisFlip >= 38.75-frameTolerance:
            # keep track of start time/frame for later
            i63.frameNStart = frameN  # exact frame index
            i63.tStart = t  # local t and not account for scr refresh
            i63.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i63, 'tStartRefresh')  # time at next scr refresh
            i63.setAutoDraw(True)
        if i63.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i63.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i63.tStop = t  # not accounting for scr refresh
                i63.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i63, 'tStopRefresh')  # time at next scr refresh
                i63.setAutoDraw(False)
        
        # *i64* updates
        if i64.status == NOT_STARTED and tThisFlip >= 39.375-frameTolerance:
            # keep track of start time/frame for later
            i64.frameNStart = frameN  # exact frame index
            i64.tStart = t  # local t and not account for scr refresh
            i64.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i64, 'tStartRefresh')  # time at next scr refresh
            i64.setAutoDraw(True)
        if i64.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i64.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                i64.tStop = t  # not accounting for scr refresh
                i64.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i64, 'tStopRefresh')  # time at next scr refresh
                i64.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task"-------
    for thisComponent in taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('track_click.x', track_click.x)
    trials.addData('track_click.y', track_click.y)
    trials.addData('track_click.leftButton', track_click.leftButton)
    trials.addData('track_click.midButton', track_click.midButton)
    trials.addData('track_click.rightButton', track_click.rightButton)
    trials.addData('track_click.time', track_click.time)
    trials.addData('track_click.started', track_click.tStart)
    trials.addData('track_click.stopped', track_click.tStop)
    trials.addData('i1.started', i1.tStartRefresh)
    trials.addData('i1.stopped', i1.tStopRefresh)
    trials.addData('i2.started', i2.tStartRefresh)
    trials.addData('i2.stopped', i2.tStopRefresh)
    trials.addData('i3.started', i3.tStartRefresh)
    trials.addData('i3.stopped', i3.tStopRefresh)
    trials.addData('i4.started', i4.tStartRefresh)
    trials.addData('i4.stopped', i4.tStopRefresh)
    trials.addData('i5.started', i5.tStartRefresh)
    trials.addData('i5.stopped', i5.tStopRefresh)
    trials.addData('i6.started', i6.tStartRefresh)
    trials.addData('i6.stopped', i6.tStopRefresh)
    trials.addData('i7.started', i7.tStartRefresh)
    trials.addData('i7.stopped', i7.tStopRefresh)
    trials.addData('i8.started', i8.tStartRefresh)
    trials.addData('i8.stopped', i8.tStopRefresh)
    trials.addData('i9.started', i9.tStartRefresh)
    trials.addData('i9.stopped', i9.tStopRefresh)
    trials.addData('i10.started', i10.tStartRefresh)
    trials.addData('i10.stopped', i10.tStopRefresh)
    trials.addData('i11.started', i11.tStartRefresh)
    trials.addData('i11.stopped', i11.tStopRefresh)
    trials.addData('i12.started', i12.tStartRefresh)
    trials.addData('i12.stopped', i12.tStopRefresh)
    trials.addData('i13.started', i13.tStartRefresh)
    trials.addData('i13.stopped', i13.tStopRefresh)
    trials.addData('i14.started', i14.tStartRefresh)
    trials.addData('i14.stopped', i14.tStopRefresh)
    trials.addData('i15.started', i15.tStartRefresh)
    trials.addData('i15.stopped', i15.tStopRefresh)
    trials.addData('i16.started', i16.tStartRefresh)
    trials.addData('i16.stopped', i16.tStopRefresh)
    trials.addData('i17.started', i17.tStartRefresh)
    trials.addData('i17.stopped', i17.tStopRefresh)
    trials.addData('i18.started', i18.tStartRefresh)
    trials.addData('i18.stopped', i18.tStopRefresh)
    trials.addData('i19.started', i19.tStartRefresh)
    trials.addData('i19.stopped', i19.tStopRefresh)
    trials.addData('i20.started', i20.tStartRefresh)
    trials.addData('i20.stopped', i20.tStopRefresh)
    trials.addData('i21.started', i21.tStartRefresh)
    trials.addData('i21.stopped', i21.tStopRefresh)
    trials.addData('i22.started', i22.tStartRefresh)
    trials.addData('i22.stopped', i22.tStopRefresh)
    trials.addData('i23.started', i23.tStartRefresh)
    trials.addData('i23.stopped', i23.tStopRefresh)
    trials.addData('i24.started', i24.tStartRefresh)
    trials.addData('i24.stopped', i24.tStopRefresh)
    trials.addData('i25.started', i25.tStartRefresh)
    trials.addData('i25.stopped', i25.tStopRefresh)
    trials.addData('i26.started', i26.tStartRefresh)
    trials.addData('i26.stopped', i26.tStopRefresh)
    trials.addData('i27.started', i27.tStartRefresh)
    trials.addData('i27.stopped', i27.tStopRefresh)
    trials.addData('i28.started', i28.tStartRefresh)
    trials.addData('i28.stopped', i28.tStopRefresh)
    trials.addData('i29.started', i29.tStartRefresh)
    trials.addData('i29.stopped', i29.tStopRefresh)
    trials.addData('i30.started', i30.tStartRefresh)
    trials.addData('i30.stopped', i30.tStopRefresh)
    trials.addData('i31.started', i31.tStartRefresh)
    trials.addData('i31.stopped', i31.tStopRefresh)
    trials.addData('i32.started', i32.tStartRefresh)
    trials.addData('i32.stopped', i32.tStopRefresh)
    trials.addData('i33.started', i33.tStartRefresh)
    trials.addData('i33.stopped', i33.tStopRefresh)
    trials.addData('i34.started', i34.tStartRefresh)
    trials.addData('i34.stopped', i34.tStopRefresh)
    trials.addData('i35.started', i35.tStartRefresh)
    trials.addData('i35.stopped', i35.tStopRefresh)
    trials.addData('i36.started', i36.tStartRefresh)
    trials.addData('i36.stopped', i36.tStopRefresh)
    trials.addData('i37.started', i37.tStartRefresh)
    trials.addData('i37.stopped', i37.tStopRefresh)
    trials.addData('i38.started', i38.tStartRefresh)
    trials.addData('i38.stopped', i38.tStopRefresh)
    trials.addData('i39.started', i39.tStartRefresh)
    trials.addData('i39.stopped', i39.tStopRefresh)
    trials.addData('i40.started', i40.tStartRefresh)
    trials.addData('i40.stopped', i40.tStopRefresh)
    trials.addData('i41.started', i41.tStartRefresh)
    trials.addData('i41.stopped', i41.tStopRefresh)
    trials.addData('i42.started', i42.tStartRefresh)
    trials.addData('i42.stopped', i42.tStopRefresh)
    trials.addData('i43.started', i43.tStartRefresh)
    trials.addData('i43.stopped', i43.tStopRefresh)
    trials.addData('i44.started', i44.tStartRefresh)
    trials.addData('i44.stopped', i44.tStopRefresh)
    trials.addData('i45.started', i45.tStartRefresh)
    trials.addData('i45.stopped', i45.tStopRefresh)
    trials.addData('i46.started', i46.tStartRefresh)
    trials.addData('i46.stopped', i46.tStopRefresh)
    trials.addData('i47.started', i47.tStartRefresh)
    trials.addData('i47.stopped', i47.tStopRefresh)
    trials.addData('i48.started', i48.tStartRefresh)
    trials.addData('i48.stopped', i48.tStopRefresh)
    trials.addData('i49.started', i49.tStartRefresh)
    trials.addData('i49.stopped', i49.tStopRefresh)
    trials.addData('i50.started', i50.tStartRefresh)
    trials.addData('i50.stopped', i50.tStopRefresh)
    trials.addData('i51.started', i51.tStartRefresh)
    trials.addData('i51.stopped', i51.tStopRefresh)
    trials.addData('i52.started', i52.tStartRefresh)
    trials.addData('i52.stopped', i52.tStopRefresh)
    trials.addData('i53.started', i53.tStartRefresh)
    trials.addData('i53.stopped', i53.tStopRefresh)
    trials.addData('i54.started', i54.tStartRefresh)
    trials.addData('i54.stopped', i54.tStopRefresh)
    trials.addData('i55.started', i55.tStartRefresh)
    trials.addData('i55.stopped', i55.tStopRefresh)
    trials.addData('i56.started', i56.tStartRefresh)
    trials.addData('i56.stopped', i56.tStopRefresh)
    trials.addData('i57.started', i57.tStartRefresh)
    trials.addData('i57.stopped', i57.tStopRefresh)
    trials.addData('i58.started', i58.tStartRefresh)
    trials.addData('i58.stopped', i58.tStopRefresh)
    trials.addData('i59.started', i59.tStartRefresh)
    trials.addData('i59.stopped', i59.tStopRefresh)
    trials.addData('i60.started', i60.tStartRefresh)
    trials.addData('i60.stopped', i60.tStopRefresh)
    trials.addData('i61.started', i61.tStartRefresh)
    trials.addData('i61.stopped', i61.tStopRefresh)
    trials.addData('i62.started', i62.tStartRefresh)
    trials.addData('i62.stopped', i62.tStopRefresh)
    trials.addData('i63.started', i63.tStartRefresh)
    trials.addData('i63.stopped', i63.tStopRefresh)
    trials.addData('i64.started', i64.tStartRefresh)
    trials.addData('i64.stopped', i64.tStopRefresh)
    thisExp.nextEntry()
    
# completed 6 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [txt_end]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt_end* updates
    if txt_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt_end.frameNStart = frameN  # exact frame index
        txt_end.tStart = t  # local t and not account for scr refresh
        txt_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt_end, 'tStartRefresh')  # time at next scr refresh
        txt_end.setAutoDraw(True)
    if txt_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > txt_end.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            txt_end.tStop = t  # not accounting for scr refresh
            txt_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(txt_end, 'tStopRefresh')  # time at next scr refresh
            txt_end.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt_end.started', txt_end.tStartRefresh)
thisExp.addData('txt_end.stopped', txt_end.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
