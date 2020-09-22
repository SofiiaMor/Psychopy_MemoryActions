#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on September 17, 2020, at 14:47
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'MemoryActions'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\psychopy\\MemoryActions\\MemoryActions_17.09_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joystick import virtualJoystick as virtualjoysticklib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joystick import virtualJoystick as virtualjoysticklib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0.239,0.239,0.239], colorSpace='rgb',
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

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
attempts = 0
sumScore = 0
missed = 0
sumRt = 0
textInstr = ''
text_instr1 = visual.TextStim(win=win, name='text_instr1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[0, 1, 0.5], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_instr2 = visual.TextStim(win=win, name='text_instr2',
    text="press button 'A' to continue",
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
button_InstrResp = type('', (), {})() # Create an object to use as a name space
button_InstrResp.device = None
button_InstrResp.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        button_InstrResp.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        button_InstrResp.device = joystickCache[0]
    else:
        button_InstrResp.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning("joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(button_InstrResp.device_number))
except Exception:
    pass
    
if not button_InstrResp.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

button_InstrResp.status = None
button_InstrResp.clock = core.Clock()
button_InstrResp.numButtons = button_InstrResp.device.getNumButtons()


# Initialize components for Routine "trial_im"
trial_imClock = core.Clock()
text_cross_im = visual.TextStim(win=win, name='text_cross_im',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_im = visual.ImageStim(
    win=win,
    name='image_im', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
x, y = [None, None]
joystick_ImmedResp = type('', (), {})() # Create an object to use as a name space
joystick_ImmedResp.device = None
joystick_ImmedResp.device_number = 0
joystick_ImmedResp.joystickClock = core.Clock()
joystick_ImmedResp.xFactor = 1
joystick_ImmedResp.yFactor = 1

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        joystick_ImmedResp.device = joystickCache[0]
        if win.units == 'height':
            joystick_ImmedResp.xFactor = 0.5 * win.size[0]/win.size[1]
            joystick_ImmedResp.yFactor = 0.5
    else:
        joystick_ImmedResp.device = virtualjoysticklib.VirtualJoystick(0)
        logging.warning("joystick_{}: Using keyboard+mouse emulation 'ctrl' + 'Alt' + digit.".format(joystick_ImmedResp.device_number))
except Exception:
    pass
    
if not joystick_ImmedResp.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

joystick_ImmedResp.status = None
joystick_ImmedResp.clock = core.Clock()
joystick_ImmedResp.numButtons = joystick_ImmedResp.device.getNumButtons()
joystick_ImmedResp.getNumButtons = joystick_ImmedResp.device.getNumButtons
joystick_ImmedResp.getAllButtons = joystick_ImmedResp.device.getAllButtons
joystick_ImmedResp.getX = lambda: joystick_ImmedResp.xFactor * joystick_ImmedResp.device.getX()
joystick_ImmedResp.getY = lambda: joystick_ImmedResp.yFactor * joystick_ImmedResp.device.getY()

joystick_ImCursor = visual.TextStim(win=win, name='joystick_ImCursor',
    text='+',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "trial_del"
trial_delClock = core.Clock()
cross_ITI = visual.TextStim(win=win, name='cross_ITI',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_del = visual.ImageStim(
    win=win,
    name='image_del', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
j_cursor_encod = visual.TextStim(win=win, name='j_cursor_encod',
    text='+',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_cross_delay = visual.TextStim(win=win, name='text_cross_delay',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')
signal = visual.TextStim(win=win, name='signal',
    text='go',
    font='Arial',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
background = visual.ImageStim(
    win=win,
    name='background', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
x, y = [None, None]
joystick_DelResp = type('', (), {})() # Create an object to use as a name space
joystick_DelResp.device = None
joystick_DelResp.device_number = 0
joystick_DelResp.joystickClock = core.Clock()
joystick_DelResp.xFactor = 1
joystick_DelResp.yFactor = 1

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        joystick_DelResp.device = joystickCache[0]
        if win.units == 'height':
            joystick_DelResp.xFactor = 0.5 * win.size[0]/win.size[1]
            joystick_DelResp.yFactor = 0.5
    else:
        joystick_DelResp.device = virtualjoysticklib.VirtualJoystick(0)
        logging.warning("joystick_{}: Using keyboard+mouse emulation 'ctrl' + 'Alt' + digit.".format(joystick_DelResp.device_number))
except Exception:
    pass
    
if not joystick_DelResp.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

joystick_DelResp.status = None
joystick_DelResp.clock = core.Clock()
joystick_DelResp.numButtons = joystick_DelResp.device.getNumButtons()
joystick_DelResp.getNumButtons = joystick_DelResp.device.getNumButtons
joystick_DelResp.getAllButtons = joystick_DelResp.device.getAllButtons
joystick_DelResp.getX = lambda: joystick_DelResp.xFactor * joystick_DelResp.device.getX()
joystick_DelResp.getY = lambda: joystick_DelResp.yFactor * joystick_DelResp.device.getY()

joystick_DelCursor = visual.TextStim(win=win, name='joystick_DelCursor',
    text='+',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#inicializace promenne
msqFeedback = ''
textFeedBack = visual.TextStim(win=win, name='textFeedBack',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "question_del"
question_delClock = core.Clock()
# initialize asnwer for the final question
corr_answer = -1
question = visual.TextStim(win=win, name='question',
    text="Which object was closer to the cross?\n\n'A'   triangle\n'B'   square",
    font='Arial',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
answer_button = type('', (), {})() # Create an object to use as a name space
answer_button.device = None
answer_button.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        answer_button.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        answer_button.device = joystickCache[0]
    else:
        answer_button.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning("joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(answer_button.device_number))
except Exception:
    pass
    
if not answer_button.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

answer_button.status = None
answer_button.clock = core.Clock()
answer_button.numButtons = answer_button.device.getNumButtons()


# Initialize components for Routine "feedback_question"
feedback_questionClock = core.Clock()
#inicialize
answFeedback = ''
fb_question = visual.TextStim(win=win, name='fb_question',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end_block"
end_blockClock = core.Clock()
text_end_block = visual.TextStim(win=win, name='text_end_block',
    text="press button 'A' to continue\n\n",
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_score = visual.TextStim(win=win, name='text_score',
    text='default text',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color=[0, 1, 0.5], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
button_resp_bk = type('', (), {})() # Create an object to use as a name space
button_resp_bk.device = None
button_resp_bk.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        button_resp_bk.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        button_resp_bk.device = joystickCache[0]
    else:
        button_resp_bk.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning("joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(button_resp_bk.device_number))
except Exception:
    pass
    
if not button_resp_bk.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

button_resp_bk.status = None
button_resp_bk.clock = core.Clock()
button_resp_bk.numButtons = button_resp_bk.device.getNumButtons()


# Initialize components for Routine "longPause"
longPauseClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_thanks = visual.TextStim(win=win, name='text_thanks',
    text='The experiment ended.\n\nThank you for your participation!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('actions.xlsx'),
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
    
    # set up handler to look after randomisation of conditions etc
    loopPause = data.TrialHandler(nReps=short_pause, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loopPause')
    thisExp.addLoop(loopPause)  # add the loop to the experiment
    thisLoopPause = loopPause.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopPause.rgb)
    if thisLoopPause != None:
        for paramName in thisLoopPause:
            exec('{} = thisLoopPause[paramName]'.format(paramName))
    
    for thisLoopPause in loopPause:
        currentLoop = loopPause
        # abbreviate parameter names if possible (e.g. rgb = thisLoopPause.rgb)
        if thisLoopPause != None:
            for paramName in thisLoopPause:
                exec('{} = thisLoopPause[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "instruction"-------
        continueRoutine = True
        # update component parameters for each repeat
        if immed==1:
            textInstr = 'move a joystick from the cross to the closest object now'
        else:
            textInstr = 'remember which object is closer to the cross; when you see a signal (word "go"), move a joystick to the supposed location of that object'
        text_instr1.setText(textInstr)
        text_3.setText(block)
        button_InstrResp.oldButtonState = button_InstrResp.device.getAllButtons()[:]
        button_InstrResp.keys = []
        button_InstrResp.rt = []
        # keep track of which components have finished
        instructionComponents = [text_instr1, text_instr2, text_3, button_InstrResp]
        for thisComponent in instructionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "instruction"-------
        while continueRoutine:
            # get current time
            t = instructionClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=instructionClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_instr1* updates
            if text_instr1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_instr1.frameNStart = frameN  # exact frame index
                text_instr1.tStart = t  # local t and not account for scr refresh
                text_instr1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_instr1, 'tStartRefresh')  # time at next scr refresh
                text_instr1.setAutoDraw(True)
            
            # *text_instr2* updates
            if text_instr2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_instr2.frameNStart = frameN  # exact frame index
                text_instr2.tStart = t  # local t and not account for scr refresh
                text_instr2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_instr2, 'tStartRefresh')  # time at next scr refresh
                text_instr2.setAutoDraw(True)
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            
            # *button_InstrResp* updates
            if button_InstrResp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                button_InstrResp.frameNStart = frameN  # exact frame index
                button_InstrResp.tStart = t  # local t and not account for scr refresh
                button_InstrResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_InstrResp, 'tStartRefresh')  # time at next scr refresh
                button_InstrResp.status = STARTED
                # joyButtons checking is just starting
                win.callOnFlip(button_InstrResp.clock.reset)  # t=0 on next screen flip
            if button_InstrResp.status == STARTED:
                button_InstrResp.newButtonState = button_InstrResp.device.getAllButtons()[:]
                button_InstrResp.pressedButtons = []
                button_InstrResp.releasedButtons = []
                button_InstrResp.newPressedButtons = []
                if button_InstrResp.newButtonState != button_InstrResp.oldButtonState:
                    button_InstrResp.pressedButtons = [i for i in range(button_InstrResp.numButtons) if button_InstrResp.newButtonState[i] and not button_InstrResp.oldButtonState[i]]
                    button_InstrResp.releasedButtons = [i for i in range(button_InstrResp.numButtons) if not button_InstrResp.newButtonState[i] and button_InstrResp.oldButtonState[i]]
                    button_InstrResp.oldButtonState = button_InstrResp.newButtonState
                    button_InstrResp.newPressedButtons = [i for i in [0] if i in button_InstrResp.pressedButtons]
                    [logging.data("joystick_{}_button: {}".format(button_InstrResp.device_number,i)) for i in button_InstrResp.pressedButtons]
                theseKeys = button_InstrResp.newPressedButtons
                if len(theseKeys) > 0:  # at least one key was pressed
                    button_InstrResp.keys = theseKeys[-1]  # just the last key pressed
                    button_InstrResp.rt = button_InstrResp.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instructionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "instruction"-------
        for thisComponent in instructionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loopPause.addData('text_instr1.started', text_instr1.tStartRefresh)
        loopPause.addData('text_instr1.stopped', text_instr1.tStopRefresh)
        loopPause.addData('text_instr2.started', text_instr2.tStartRefresh)
        loopPause.addData('text_instr2.stopped', text_instr2.tStopRefresh)
        loopPause.addData('text_3.started', text_3.tStartRefresh)
        loopPause.addData('text_3.stopped', text_3.tStopRefresh)
        # check responses
        if button_InstrResp.keys in ['', [], None]:  # No response was made
            button_InstrResp.keys=None
        loopPause.addData('button_InstrResp.keys',button_InstrResp.keys)
        if button_InstrResp.keys != None:  # we had a response
            loopPause.addData('button_InstrResp.rt', button_InstrResp.rt)
        # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed short_pause repeats of 'loopPause'
    
    
    # set up handler to look after randomisation of conditions etc
    loop_im = data.TrialHandler(nReps=immed, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_im')
    thisExp.addLoop(loop_im)  # add the loop to the experiment
    thisLoop_im = loop_im.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_im.rgb)
    if thisLoop_im != None:
        for paramName in thisLoop_im:
            exec('{} = thisLoop_im[paramName]'.format(paramName))
    
    for thisLoop_im in loop_im:
        currentLoop = loop_im
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_im.rgb)
        if thisLoop_im != None:
            for paramName in thisLoop_im:
                exec('{} = thisLoop_im[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_im"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        x1, y1 = [None, None]  
        #x1, y1 = joystick_ImmedResp.getX(), -1*joystick_ImmedResp.getY() #delta between the middle of the screen and the position of joystick before the trial
        
        joystick_resp_corr = -1
        joystick_RT_corr = 0.0
        
        # Sofiia 17.09.2020 -----<
        joystick_RT_start = [None]
        move = 0
        NoMove_x = False
        NoMove_y = False
        missed_j = 0
        #------>
        
        image_im.setImage('Images/'+picture)
        joystick_ImmedResp.oldButtonState = joystick_ImmedResp.device.getAllButtons()[:]
        joystick_ImmedResp.activeButtons=[i for i in range(joystick_ImmedResp.numButtons)]
        # setup some python lists for storing info about the joystick_ImmedResp
        joystick_ImmedResp.x = []
        joystick_ImmedResp.y = []
        joystick_ImmedResp.buttonLogs = [[] for i in range(joystick_ImmedResp.numButtons)]
        joystick_ImmedResp.time = []
        gotValidClick = False  # until a click is received
        joystick_ImmedResp.joystickClock.reset()
        # keep track of which components have finished
        trial_imComponents = [text_cross_im, image_im, joystick_ImmedResp, joystick_ImCursor, ISI]
        for thisComponent in trial_imComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_imClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_im"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_imClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_imClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_cross_im* updates
            if text_cross_im.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_cross_im.frameNStart = frameN  # exact frame index
                text_cross_im.tStart = t  # local t and not account for scr refresh
                text_cross_im.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_cross_im, 'tStartRefresh')  # time at next scr refresh
                text_cross_im.setAutoDraw(True)
            if text_cross_im.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_cross_im.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_cross_im.tStop = t  # not accounting for scr refresh
                    text_cross_im.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_cross_im, 'tStopRefresh')  # time at next scr refresh
                    text_cross_im.setAutoDraw(False)
                x1, y1 = joystick_ImmedResp.getX(), -1*joystick_ImmedResp.getY() #delta between the middle of the screen and the position of joystick before the trial
            # *image_im* updates
            if image_im.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                image_im.frameNStart = frameN  # exact frame index
                image_im.tStart = t  # local t and not account for scr refresh
                image_im.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_im, 'tStartRefresh')  # time at next scr refresh
                image_im.setAutoDraw(True)
            if image_im.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_im.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_im.tStop = t  # not accounting for scr refresh
                    image_im.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_im, 'tStopRefresh')  # time at next scr refresh
                    image_im.setAutoDraw(False)
            # *joystick_ImmedResp* updates
            if joystick_ImmedResp.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                joystick_ImmedResp.frameNStart = frameN  # exact frame index
                joystick_ImmedResp.tStart = t  # local t and not account for scr refresh
                joystick_ImmedResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(joystick_ImmedResp, 'tStartRefresh')  # time at next scr refresh
                joystick_ImmedResp.status = STARTED
            if joystick_ImmedResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > joystick_ImmedResp.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    joystick_ImmedResp.tStop = t  # not accounting for scr refresh
                    joystick_ImmedResp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(joystick_ImmedResp, 'tStopRefresh')  # time at next scr refresh
                    joystick_ImmedResp.status = FINISHED
            if joystick_ImmedResp.status == STARTED:  # only update if started and not finished!
                joystick_ImmedResp.newButtonState = joystick_ImmedResp.getAllButtons()[:]
                joystick_ImmedResp.pressedButtons = [i for i in range(joystick_ImmedResp.numButtons) if joystick_ImmedResp.newButtonState[i] and not joystick_ImmedResp.oldButtonState[i]]
                joystick_ImmedResp.releasedButtons = [i for i in range(joystick_ImmedResp.numButtons) if not joystick_ImmedResp.newButtonState[i] and joystick_ImmedResp.oldButtonState[i]]
                joystick_ImmedResp.newPressedButtons = [i for i in joystick_ImmedResp.activeButtons if i in joystick_ImmedResp.pressedButtons]
                joystick_ImmedResp.buttons = joystick_ImmedResp.newPressedButtons
                #[logging.data("joystick_{}_button: {}, pos=({:1.4f},{:1.4f})".format(joystick_ImmedResp.device_number, i, joystick_ImmedResp.getX(), joystick_ImmedResp.getY()) for i in joystick_ImmedResp.pressedButtons] Sofiia 17.09.2020 , with this line the experiment doesn't work
                #x, y = joystick_DelResp.getX(), joystick_DelResp.getY()
                x, y = joystick_ImmedResp.getX(), -1*joystick_ImmedResp.getY() # Sofiia 17.09.2020 invert y direction
                
                # Sofia 17.09.2020 ---<
                 # update/draw components on each frame
                # get time when subject just starts to move joystick
                if len(joystick_ImmedResp.x)!=0 and (x!= joystick_ImmedResp.x[-1] or y!= joystick_ImmedResp.y[-1]) and move==0:
                    joystick_RT_start = joystick_ImmedResp.joystickClock.getTime() - 2.0
                    move = 1
                    
                # compare the position of joystick with x,y coordinates of correct object each frame
                #if joystick_resp_corr<0 and (correct_object== 'square' and (float(x_square)-0.12)<x-x1<(float(x_square)+0.12) and (float(y_square)-0.12)<y-y1<(float(y_square)+0.12)) or (correct_object== 'triangle' and (float(x_triangle)-0.12)<x-x1<(float(x_triangle)+0.12) and (float(y_triangle)-0.12)<y-y1<(float(y_triangle)+0.12)):
                if joystick_resp_corr<0 and (correct_object== 'square' and (x_square-0.12)<x-x1<(x_square+0.12) and (y_square-0.12)<y-y1<(y_square+0.12)) or (correct_object== 'triangle' and (x_triangle-0.12)<x-x1<(x_triangle+0.12) and (y_triangle-0.12)<y-y1<(y_triangle+0.12)):
                    joystick_resp_corr = 1
                    joystick_RT_corr = joystick_ImmedResp.joystickClock.getTime()
                # -------->
                
                joystick_ImmedResp.x.append(x)
                joystick_ImmedResp.y.append(y)
                [joystick_ImmedResp.buttonLogs[i].append(int(joystick_ImmedResp.newButtonState[i])) for i in joystick_ImmedResp.activeButtons]
                joystick_ImmedResp.time.append(joystick_ImmedResp.joystickClock.getTime())
            
            # *joystick_ImCursor* updates
            if joystick_ImCursor.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                joystick_ImCursor.frameNStart = frameN  # exact frame index
                joystick_ImCursor.tStart = t  # local t and not account for scr refresh
                joystick_ImCursor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(joystick_ImCursor, 'tStartRefresh')  # time at next scr refresh
                joystick_ImCursor.setAutoDraw(True)
            if joystick_ImCursor.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > joystick_ImCursor.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    joystick_ImCursor.tStop = t  # not accounting for scr refresh
                    joystick_ImCursor.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(joystick_ImCursor, 'tStopRefresh')  # time at next scr refresh
                    joystick_ImCursor.setAutoDraw(False)
            if joystick_ImCursor.status == STARTED:  # only update if drawing
                joystick_ImCursor.setPos([x-x1,y-y1], log=False) # Sofiia 17.09.2020 invert y direction
            # *ISI* period
            if ISI.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                ISI.frameNStart = frameN  # exact frame index
                ISI.tStart = t  # local t and not account for scr refresh
                ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                ISI.start(0.3)
            elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                ISI.complete()  # finish the static period
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_imComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_im"-------
        for thisComponent in trial_imComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # Sofiia 17.09.2020 -----<
        # check if joystick was moved at all in this trial, checking if all elements in a List joystick_ImmedResp.x and joystick_ImmedResp.y are the same
        NoMove_x = len(joystick_ImmedResp.x) > 0 and all(elem == joystick_ImmedResp.x[0] for elem in joystick_ImmedResp.x)
        NoMove_y = len(joystick_ImmedResp.y) > 0 and all(elem == joystick_ImmedResp.y[0] for elem in joystick_ImmedResp.y)
        if NoMove_x and NoMove_y:
            missed_j = 1
        #else:
            #i = 0
            #while joystick_ImmedResp.x[i] == joystick_ImmedResp.x[i+1] and joystick_ImmedResp.y[i] == joystick_ImmedResp.y[i+1]:
            #    i +=1
            #nFrame_RT = i+1
            
            
        
        joystick_RT_corr = joystick_RT_corr-2.0  # calculate RT relative to the start of action phase
        
        attempts += 1
        if joystick_resp_corr==1:
             sumScore += joystick_resp_corr;
             sumRt += joystick_RT_corr;
        elif missed_j == 1:
            missed += 1
        # ----------->
            
        
        loop_im.addData('text_cross_im.started', text_cross_im.tStartRefresh)
        loop_im.addData('text_cross_im.stopped', text_cross_im.tStopRefresh)
        loop_im.addData('image_im.started', image_im.tStartRefresh)
        loop_im.addData('image_im.stopped', image_im.tStopRefresh)
        # store data for loop_im (TrialHandler)
        
           # Sofia 17.09.2020 --------<
        loop_im.addData('x1_immed', x1)
        loop_im.addData('y1_immed', y1)
        loop_im.addData('joystick_resp_corr_immed', joystick_resp_corr)
        loop_im.addData('joystick_RT_corr_immed', joystick_RT_corr)
        loop_im.addData('joystick_RT_start_immed', joystick_RT_start)
        loop_im.addData('missed_immed', missed_j) 
        #--- -->
        loop_im.addData('joystick_ImmedResp.x', joystick_ImmedResp.x)
        loop_im.addData('joystick_ImmedResp.y', joystick_ImmedResp.y)
        loop_im.addData('joystick_ImmedResp.time', joystick_ImmedResp.time)
        [loop_im.addData('joystick_ImmedResp.button_{0}'.format(i), joystick_ImmedResp.buttonLogs[i]) for i in joystick_ImmedResp.activeButtons if len(joystick_ImmedResp.buttonLogs[i])]
        loop_im.addData('joystick_ImmedResp.started', joystick_ImmedResp.tStartRefresh)
        loop_im.addData('joystick_ImmedResp.stopped', joystick_ImmedResp.tStopRefresh)
        loop_im.addData('joystick_ImCursor.started', joystick_ImCursor.tStartRefresh)
        loop_im.addData('joystick_ImCursor.stopped', joystick_ImCursor.tStopRefresh)
        loop_im.addData('ISI.started', ISI.tStartRefresh)
        loop_im.addData('ISI.stopped', ISI.tStopRefresh)
        thisExp.nextEntry()
        
    # completed immed repeats of 'loop_im'
    
    
    # set up handler to look after randomisation of conditions etc
    loop_del = data.TrialHandler(nReps=delayed, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_del')
    thisExp.addLoop(loop_del)  # add the loop to the experiment
    thisLoop_del = loop_del.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_del.rgb)
    if thisLoop_del != None:
        for paramName in thisLoop_del:
            exec('{} = thisLoop_del[paramName]'.format(paramName))
    
    for thisLoop_del in loop_del:
        currentLoop = loop_del
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_del.rgb)
        if thisLoop_del != None:
            for paramName in thisLoop_del:
                exec('{} = thisLoop_del[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_del"-------
        continueRoutine = True
        routineTimer.add(14.000000)
        # update component parameters for each repeat
        x1, y1 = [None, None]  
        #x1, y1 = joystick_DelResp.getX(), -1*joystick_DelResp.getY() #delta between the middle of the screen and the position of joystick before the trial
        
        joystick_resp_corr = -1
        joystick_RT_corr = 0.0
        
        # Sofiia 17.09.2020 -----<
        joystick_RT_start = [None]
        move = 0
        NoMove_x = False
        NoMove_y = False
        missed_j = 0
        #------>
        
        image_del.setImage('Images/'+picture)
        background.setImage('background.png')
        joystick_DelResp.oldButtonState = joystick_DelResp.device.getAllButtons()[:]
        joystick_DelResp.activeButtons=[i for i in range(joystick_DelResp.numButtons)]
        # setup some python lists for storing info about the joystick_DelResp
        joystick_DelResp.x = []
        joystick_DelResp.y = []
        joystick_DelResp.buttonLogs = [[] for i in range(joystick_DelResp.numButtons)]
        joystick_DelResp.time = []
        gotValidClick = False  # until a click is received
        joystick_DelResp.joystickClock.reset()
        # keep track of which components have finished
        trial_delComponents = [cross_ITI, image_del, j_cursor_encod, text_cross_delay, ISI_2, signal, background, joystick_DelResp, joystick_DelCursor]
        for thisComponent in trial_delComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_delClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_del"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_delClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_delClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross_ITI* updates
            if cross_ITI.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                cross_ITI.frameNStart = frameN  # exact frame index
                cross_ITI.tStart = t  # local t and not account for scr refresh
                cross_ITI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_ITI, 'tStartRefresh')  # time at next scr refresh
                cross_ITI.setAutoDraw(True)
            if cross_ITI.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_ITI.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_ITI.tStop = t  # not accounting for scr refresh
                    cross_ITI.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross_ITI, 'tStopRefresh')  # time at next scr refresh
                    cross_ITI.setAutoDraw(False)
            
            # *image_del* updates
            if image_del.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
                # keep track of start time/frame for later
                image_del.frameNStart = frameN  # exact frame index
                image_del.tStart = t  # local t and not account for scr refresh
                image_del.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_del, 'tStartRefresh')  # time at next scr refresh
                image_del.setAutoDraw(True)
            if image_del.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_del.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    image_del.tStop = t  # not accounting for scr refresh
                    image_del.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_del, 'tStopRefresh')  # time at next scr refresh
                    image_del.setAutoDraw(False)
            
            # *j_cursor_encod* updates
            if j_cursor_encod.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
                # keep track of start time/frame for later
                j_cursor_encod.frameNStart = frameN  # exact frame index
                j_cursor_encod.tStart = t  # local t and not account for scr refresh
                j_cursor_encod.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(j_cursor_encod, 'tStartRefresh')  # time at next scr refresh
                j_cursor_encod.setAutoDraw(True)
            if j_cursor_encod.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > j_cursor_encod.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    j_cursor_encod.tStop = t  # not accounting for scr refresh
                    j_cursor_encod.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(j_cursor_encod, 'tStopRefresh')  # time at next scr refresh
                    j_cursor_encod.setAutoDraw(False)
            if j_cursor_encod.status == STARTED:  # only update if drawing
                j_cursor_encod.setPos([0,0], log=False)
            
            # *text_cross_delay* updates
            if text_cross_delay.status == NOT_STARTED and tThisFlip >= 7.0-frameTolerance:
                # keep track of start time/frame for later
                text_cross_delay.frameNStart = frameN  # exact frame index
                text_cross_delay.tStart = t  # local t and not account for scr refresh
                text_cross_delay.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_cross_delay, 'tStartRefresh')  # time at next scr refresh
                text_cross_delay.setAutoDraw(True)
            if text_cross_delay.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_cross_delay.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_cross_delay.tStop = t  # not accounting for scr refresh
                    text_cross_delay.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_cross_delay, 'tStopRefresh')  # time at next scr refresh
                    text_cross_delay.setAutoDraw(False)
                x1, y1 = joystick_DelResp.getX(), -1*joystick_DelResp.getY() #delta between the middle of the screen and the position of joystick before the trial
            # *signal* updates
            if signal.status == NOT_STARTED and tThisFlip >= 11.5-frameTolerance:
                # keep track of start time/frame for later
                signal.frameNStart = frameN  # exact frame index
                signal.tStart = t  # local t and not account for scr refresh
                signal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(signal, 'tStartRefresh')  # time at next scr refresh
                signal.setAutoDraw(True)
            if signal.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > signal.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    signal.tStop = t  # not accounting for scr refresh
                    signal.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(signal, 'tStopRefresh')  # time at next scr refresh
                    signal.setAutoDraw(False)
            
            # *background* updates
            if background.status == NOT_STARTED and tThisFlip >= 12.0-frameTolerance:
                # keep track of start time/frame for later
                background.frameNStart = frameN  # exact frame index
                background.tStart = t  # local t and not account for scr refresh
                background.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(background, 'tStartRefresh')  # time at next scr refresh
                background.setAutoDraw(True)
            if background.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > background.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    background.tStop = t  # not accounting for scr refresh
                    background.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(background, 'tStopRefresh')  # time at next scr refresh
                    background.setAutoDraw(False)
            # *joystick_DelResp* updates
            if joystick_DelResp.status == NOT_STARTED and t >= 12.0-frameTolerance:
                # keep track of start time/frame for later
                joystick_DelResp.frameNStart = frameN  # exact frame index
                joystick_DelResp.tStart = t  # local t and not account for scr refresh
                joystick_DelResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(joystick_DelResp, 'tStartRefresh')  # time at next scr refresh
                joystick_DelResp.status = STARTED
            if joystick_DelResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > joystick_DelResp.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    joystick_DelResp.tStop = t  # not accounting for scr refresh
                    joystick_DelResp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(joystick_DelResp, 'tStopRefresh')  # time at next scr refresh
                    joystick_DelResp.status = FINISHED
            if joystick_DelResp.status == STARTED:  # only update if started and not finished!
                joystick_DelResp.newButtonState = joystick_DelResp.getAllButtons()[:]
                joystick_DelResp.pressedButtons = [i for i in range(joystick_DelResp.numButtons) if joystick_DelResp.newButtonState[i] and not joystick_DelResp.oldButtonState[i]]
                joystick_DelResp.releasedButtons = [i for i in range(joystick_DelResp.numButtons) if not joystick_DelResp.newButtonState[i] and joystick_DelResp.oldButtonState[i]]
                joystick_DelResp.newPressedButtons = [i for i in joystick_DelResp.activeButtons if i in joystick_DelResp.pressedButtons]
                joystick_DelResp.buttons = joystick_DelResp.newPressedButtons
                #[logging.data("joystick_{}_button: {}, pos=({:1.4f},{:1.4f})".format(joystick_DelResp.device_number, i, joystick_DelResp.getX(), joystick_DelResp.getY()) for i in joystick_DelResp.pressedButtons] Sofiia 17.09.2020 , with this line the experiment doesn't work
                #x, y = joystick_DelResp.getX(), joystick_DelResp.getY()
                x, y = joystick_DelResp.getX(), -1*joystick_DelResp.getY() # Sofiia 17.09.2020 invert y direction
                
                # Sofia 17.09.2020 ---<
                 # update/draw components on each frame
                  # get time when subject just starts to move joystick
                if len(joystick_DelResp.x) != 0 and (x!= joystick_DelResp.x[-1] or y!= joystick_DelResp.y[-1]) and move==0:
                    joystick_RT_start = joystick_DelResp.joystickClock.getTime() - 12.0
                    move = 1 
                # compare the position of joystick with x,y coordinates of correct object each frame
                if joystick_resp_corr<0 and (correct_object== 'square' and (x_square-0.12)<x-x1<(x_square+0.12) and (y_square-0.12)<y-y1<(y_square+0.12)) or (correct_object== 'triangle' and (x_triangle-0.12)<x-x1<(x_triangle+0.12) and (y_triangle-0.12)<y-y1<(y_triangle+0.12)):
                    joystick_resp_corr = 1
                    joystick_RT_corr = joystick_DelResp.joystickClock.getTime()
                # -------->
                joystick_DelResp.x.append(x)
                joystick_DelResp.y.append(y)
                [joystick_DelResp.buttonLogs[i].append(int(joystick_DelResp.newButtonState[i])) for i in joystick_DelResp.activeButtons]
                joystick_DelResp.time.append(joystick_DelResp.joystickClock.getTime())
            
            # *joystick_DelCursor* updates
            if joystick_DelCursor.status == NOT_STARTED and tThisFlip >= 12.0-frameTolerance:
                # keep track of start time/frame for later
                joystick_DelCursor.frameNStart = frameN  # exact frame index
                joystick_DelCursor.tStart = t  # local t and not account for scr refresh
                joystick_DelCursor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(joystick_DelCursor, 'tStartRefresh')  # time at next scr refresh
                joystick_DelCursor.setAutoDraw(True)
            if joystick_DelCursor.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > joystick_DelCursor.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    joystick_DelCursor.tStop = t  # not accounting for scr refresh
                    joystick_DelCursor.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(joystick_DelCursor, 'tStopRefresh')  # time at next scr refresh
                    joystick_DelCursor.setAutoDraw(False)
            if joystick_DelCursor.status == STARTED:  # only update if drawing
                joystick_DelCursor.setPos([x-x1,y-y1], log=False) # Sofiia 17.09.2020 invert y direction
            # *ISI_2* period
            if ISI_2.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
                # keep track of start time/frame for later
                ISI_2.frameNStart = frameN  # exact frame index
                ISI_2.tStart = t  # local t and not account for scr refresh
                ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
                ISI_2.start(0.3)
            elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
                ISI_2.complete()  # finish the static period
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_delComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_del"-------
        for thisComponent in trial_delComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                
        # Sofiia 17.09.2020 -----<
        # check if joystick was moved at all in this trial, checking if all elements in a List joystick_ImmedResp.x and joystick_ImmedResp.y are the same
        NoMove_x = len(joystick_DelResp.x) > 0 and all(elem == joystick_DelResp.x[0] for elem in joystick_DelResp.x)
        NoMove_y = len(joystick_DelResp.y) > 0 and all(elem == joystick_DelResp.y[0] for elem in joystick_DelResp.y)
        if NoMove_x and NoMove_y:
            missed_j = 1
            
        joystick_RT_corr = joystick_RT_corr-12.0  # calculate RT relative to the start of action phase
        
        attempts += 1
        if joystick_resp_corr==1:
             sumScore += joystick_resp_corr;
             sumRt += joystick_RT_corr;
        elif missed_j == 1:
            missed += 1
        # ----------->
                      
        loop_del.addData('cross_ITI.started', cross_ITI.tStartRefresh)
        loop_del.addData('cross_ITI.stopped', cross_ITI.tStopRefresh)
        loop_del.addData('image_del.started', image_del.tStartRefresh)
        loop_del.addData('image_del.stopped', image_del.tStopRefresh)
        loop_del.addData('j_cursor_encod.started', j_cursor_encod.tStartRefresh)
        loop_del.addData('j_cursor_encod.stopped', j_cursor_encod.tStopRefresh)
        loop_del.addData('text_cross_delay.started', text_cross_delay.tStartRefresh)
        loop_del.addData('text_cross_delay.stopped', text_cross_delay.tStopRefresh)
        loop_del.addData('ISI_2.started', ISI_2.tStartRefresh)
        loop_del.addData('ISI_2.stopped', ISI_2.tStopRefresh)
        loop_del.addData('signal.started', signal.tStartRefresh)
        loop_del.addData('signal.stopped', signal.tStopRefresh)
        loop_del.addData('background.started', background.tStartRefresh)
        loop_del.addData('background.stopped', background.tStopRefresh)
        # store data for loop_del (TrialHandler)
                # Sofia 17.09.2020 --------<
        loop_del.addData('x1_del', x1)
        loop_del.addData('y1_del', y1)
        loop_del.addData('joystick_resp_corr_del', joystick_resp_corr)
        loop_del.addData('joystick_RT_corr_del', joystick_RT_corr)
        loop_del.addData('joystick_RT_start_del', joystick_RT_start)
        loop_del.addData('missed_del', missed_j)
        #--- -->
        
        loop_del.addData('joystick_DelResp.x', joystick_DelResp.x)
        loop_del.addData('joystick_DelResp.y', joystick_DelResp.y)
        loop_del.addData('joystick_DelResp.time', joystick_DelResp.time)
        [loop_del.addData('joystick_DelResp.button_{0}'.format(i), joystick_DelResp.buttonLogs[i]) for i in joystick_DelResp.activeButtons if len(joystick_DelResp.buttonLogs[i])]
        loop_del.addData('joystick_DelResp.started', joystick_DelResp.tStart)
        loop_del.addData('joystick_DelResp.stopped', joystick_DelResp.tStop)
        loop_del.addData('joystick_DelCursor.started', joystick_DelCursor.tStartRefresh)
        loop_del.addData('joystick_DelCursor.stopped', joystick_DelCursor.tStopRefresh)
    # completed delayed repeats of 'loop_del'
    
    
    # set up handler to look after randomisation of conditions etc
    loopFeedback = data.TrialHandler(nReps=feedback, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loopFeedback')
    thisExp.addLoop(loopFeedback)  # add the loop to the experiment
    thisLoopFeedback = loopFeedback.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopFeedback.rgb)
    if thisLoopFeedback != None:
        for paramName in thisLoopFeedback:
            exec('{} = thisLoopFeedback[paramName]'.format(paramName))
    
    for thisLoopFeedback in loopFeedback:
        currentLoop = loopFeedback
        # abbreviate parameter names if possible (e.g. rgb = thisLoopFeedback.rgb)
        if thisLoopFeedback != None:
            for paramName in thisLoopFeedback:
                exec('{} = thisLoopFeedback[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "feedback"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        if joystick_resp_corr == 1:
            msqFeedback='correct'
        else:
            msqFeedback='wrong'
        textFeedBack.setText(msqFeedback)
        # keep track of which components have finished
        feedbackComponents = [textFeedBack]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textFeedBack* updates
            if textFeedBack.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textFeedBack.frameNStart = frameN  # exact frame index
                textFeedBack.tStart = t  # local t and not account for scr refresh
                textFeedBack.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textFeedBack, 'tStartRefresh')  # time at next scr refresh
                textFeedBack.setAutoDraw(True)
            if textFeedBack.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textFeedBack.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    textFeedBack.tStop = t  # not accounting for scr refresh
                    textFeedBack.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(textFeedBack, 'tStopRefresh')  # time at next scr refresh
                    textFeedBack.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loopFeedback.addData('textFeedBack.started', textFeedBack.tStartRefresh)
        loopFeedback.addData('textFeedBack.stopped', textFeedBack.tStopRefresh)
        thisExp.nextEntry()
        
    # completed feedback repeats of 'loopFeedback'
    
    
    # set up handler to look after randomisation of conditions etc
    loop_del_diff = data.TrialHandler(nReps=delayed_d, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_del_diff')
    thisExp.addLoop(loop_del_diff)  # add the loop to the experiment
    thisLoop_del_diff = loop_del_diff.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_del_diff.rgb)
    if thisLoop_del_diff != None:
        for paramName in thisLoop_del_diff:
            exec('{} = thisLoop_del_diff[paramName]'.format(paramName))
    
    for thisLoop_del_diff in loop_del_diff:
        currentLoop = loop_del_diff
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_del_diff.rgb)
        if thisLoop_del_diff != None:
            for paramName in thisLoop_del_diff:
                exec('{} = thisLoop_del_diff[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "question_del"-------
        continueRoutine = True
        # update component parameters for each repeat
        if correct_object == 'square':
            corr_answer = 1  # button B on joystick
        else:
            corr_answer = 0  # button A on joystick
        answer_button.oldButtonState = answer_button.device.getAllButtons()[:]
        answer_button.keys = []
        answer_button.rt = []
        # keep track of which components have finished
        question_delComponents = [question, answer_button]
        for thisComponent in question_delComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        question_delClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "question_del"-------
        while continueRoutine:
            # get current time
            t = question_delClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=question_delClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question* updates
            if question.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                question.frameNStart = frameN  # exact frame index
                question.tStart = t  # local t and not account for scr refresh
                question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question, 'tStartRefresh')  # time at next scr refresh
                question.setAutoDraw(True)
            
            # *answer_button* updates
            if answer_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                answer_button.frameNStart = frameN  # exact frame index
                answer_button.tStart = t  # local t and not account for scr refresh
                answer_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(answer_button, 'tStartRefresh')  # time at next scr refresh
                answer_button.status = STARTED
                # joyButtons checking is just starting
                win.callOnFlip(answer_button.clock.reset)  # t=0 on next screen flip
            if answer_button.status == STARTED:
                answer_button.newButtonState = answer_button.device.getAllButtons()[:]
                answer_button.pressedButtons = []
                answer_button.releasedButtons = []
                answer_button.newPressedButtons = []
                if answer_button.newButtonState != answer_button.oldButtonState:
                    answer_button.pressedButtons = [i for i in range(answer_button.numButtons) if answer_button.newButtonState[i] and not answer_button.oldButtonState[i]]
                    answer_button.releasedButtons = [i for i in range(answer_button.numButtons) if not answer_button.newButtonState[i] and answer_button.oldButtonState[i]]
                    answer_button.oldButtonState = answer_button.newButtonState
                    answer_button.newPressedButtons = [i for i in [0, 1] if i in answer_button.pressedButtons]
                    [logging.data("joystick_{}_button: {}".format(answer_button.device_number,i)) for i in answer_button.pressedButtons]
                theseKeys = answer_button.newPressedButtons
                if len(theseKeys) > 0:  # at least one key was pressed
                    answer_button.keys = theseKeys[-1]  # just the last key pressed
                    answer_button.rt = answer_button.clock.getTime()
                    # was this 'correct'?
                    if (str(answer_button.keys) == str(corr_answer)):
                        answer_button.corr = 1
                    else:
                        answer_button.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in question_delComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "question_del"-------
        for thisComponent in question_delComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_del_diff.addData('question.started', question.tStartRefresh)
        loop_del_diff.addData('question.stopped', question.tStopRefresh)
        # check responses
        if answer_button.keys in ['', [], None]:  # No response was made
            answer_button.keys=None
            # was no response the correct answer?!
            if str(corr_answer).lower() == 'none':
                answer_button.corr = 1;  # correct non-response
            else:
                answer_button.corr = 0;  # failed to respond (incorrectly)
        # store data for loop_del_diff (TrialHandler)
        loop_del_diff.addData('answer_button.keys',answer_button.keys)
        loop_del_diff.addData('answer_button.corr', answer_button.corr)
        if answer_button.keys != None:  # we had a response
            loop_del_diff.addData('answer_button.rt', answer_button.rt)
        # the Routine "question_del" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed delayed_d repeats of 'loop_del_diff'
    
    
    # set up handler to look after randomisation of conditions etc
    loop_fb_question = data.TrialHandler(nReps=feedback_q, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_fb_question')
    thisExp.addLoop(loop_fb_question)  # add the loop to the experiment
    thisLoop_fb_question = loop_fb_question.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_fb_question.rgb)
    if thisLoop_fb_question != None:
        for paramName in thisLoop_fb_question:
            exec('{} = thisLoop_fb_question[paramName]'.format(paramName))
    
    for thisLoop_fb_question in loop_fb_question:
        currentLoop = loop_fb_question
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_fb_question.rgb)
        if thisLoop_fb_question != None:
            for paramName in thisLoop_fb_question:
                exec('{} = thisLoop_fb_question[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "feedback_question"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        if answer_button.corr:
            answFeedback='correct'
        else:
            answFeedback='wrong'
        fb_question.setText(answFeedback)
        # keep track of which components have finished
        feedback_questionComponents = [fb_question]
        for thisComponent in feedback_questionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedback_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedback_question"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedback_questionClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedback_questionClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fb_question* updates
            if fb_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fb_question.frameNStart = frameN  # exact frame index
                fb_question.tStart = t  # local t and not account for scr refresh
                fb_question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fb_question, 'tStartRefresh')  # time at next scr refresh
                fb_question.setAutoDraw(True)
            if fb_question.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fb_question.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fb_question.tStop = t  # not accounting for scr refresh
                    fb_question.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fb_question, 'tStopRefresh')  # time at next scr refresh
                    fb_question.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_questionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback_question"-------
        for thisComponent in feedback_questionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_fb_question.addData('fb_question.started', fb_question.tStartRefresh)
        loop_fb_question.addData('fb_question.stopped', fb_question.tStopRefresh)
    # completed feedback_q repeats of 'loop_fb_question'
    
    
    # set up handler to look after randomisation of conditions etc
    loopEnd_block = data.TrialHandler(nReps=end_block, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loopEnd_block')
    thisExp.addLoop(loopEnd_block)  # add the loop to the experiment
    thisLoopEnd_block = loopEnd_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopEnd_block.rgb)
    if thisLoopEnd_block != None:
        for paramName in thisLoopEnd_block:
            exec('{} = thisLoopEnd_block[paramName]'.format(paramName))
    
    for thisLoopEnd_block in loopEnd_block:
        currentLoop = loopEnd_block
        # abbreviate parameter names if possible (e.g. rgb = thisLoopEnd_block.rgb)
        if thisLoopEnd_block != None:
            for paramName in thisLoopEnd_block:
                exec('{} = thisLoopEnd_block[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "end_block"-------
        continueRoutine = True
        # update component parameters for each repeat
        
        if attempts > 0:
            textScore= u'score: ' + str(sumScore) +  u' correct ' 
            textScore += ( "(%.0f" % (sumScore/attempts*100)) + ' %) from ' + str(attempts) + u' trials'
            if attempts == missed:
                textScore += '\n' + u'reaction time: --';
            else:
                textScore += '\n' + u'reaction time: ' + ( "%.0f" %  (sumRt/(attempts-missed)*1000) ) + ' ms';
            textScore += '\n'+u'missed trials: ' +  str(missed); 
        else:
            textScore = '';
        text_score.setText(textScore)
        button_resp_bk.oldButtonState = button_resp_bk.device.getAllButtons()[:]
        button_resp_bk.keys = []
        button_resp_bk.rt = []
        # keep track of which components have finished
        end_blockComponents = [text_end_block, text_score, button_resp_bk]
        for thisComponent in end_blockComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        end_blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "end_block"-------
        while continueRoutine:
            # get current time
            t = end_blockClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=end_blockClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_end_block* updates
            if text_end_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_end_block.frameNStart = frameN  # exact frame index
                text_end_block.tStart = t  # local t and not account for scr refresh
                text_end_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_end_block, 'tStartRefresh')  # time at next scr refresh
                text_end_block.setAutoDraw(True)
            
            # *text_score* updates
            if text_score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_score.frameNStart = frameN  # exact frame index
                text_score.tStart = t  # local t and not account for scr refresh
                text_score.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_score, 'tStartRefresh')  # time at next scr refresh
                text_score.setAutoDraw(True)
            
            # *button_resp_bk* updates
            if button_resp_bk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                button_resp_bk.frameNStart = frameN  # exact frame index
                button_resp_bk.tStart = t  # local t and not account for scr refresh
                button_resp_bk.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_resp_bk, 'tStartRefresh')  # time at next scr refresh
                button_resp_bk.status = STARTED
                # joyButtons checking is just starting
                win.callOnFlip(button_resp_bk.clock.reset)  # t=0 on next screen flip
            if button_resp_bk.status == STARTED:
                button_resp_bk.newButtonState = button_resp_bk.device.getAllButtons()[:]
                button_resp_bk.pressedButtons = []
                button_resp_bk.releasedButtons = []
                button_resp_bk.newPressedButtons = []
                if button_resp_bk.newButtonState != button_resp_bk.oldButtonState:
                    button_resp_bk.pressedButtons = [i for i in range(button_resp_bk.numButtons) if button_resp_bk.newButtonState[i] and not button_resp_bk.oldButtonState[i]]
                    button_resp_bk.releasedButtons = [i for i in range(button_resp_bk.numButtons) if not button_resp_bk.newButtonState[i] and button_resp_bk.oldButtonState[i]]
                    button_resp_bk.oldButtonState = button_resp_bk.newButtonState
                    button_resp_bk.newPressedButtons = [i for i in [0] if i in button_resp_bk.pressedButtons]
                    [logging.data("joystick_{}_button: {}".format(button_resp_bk.device_number,i)) for i in button_resp_bk.pressedButtons]
                theseKeys = button_resp_bk.newPressedButtons
                if len(theseKeys) > 0:  # at least one key was pressed
                    button_resp_bk.keys = theseKeys[-1]  # just the last key pressed
                    button_resp_bk.rt = button_resp_bk.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_blockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "end_block"-------
        for thisComponent in end_blockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        attempts = 0
        sumScore = 0
        missed = 0
        sumRt = 0
        loopEnd_block.addData('text_end_block.started', text_end_block.tStartRefresh)
        loopEnd_block.addData('text_end_block.stopped', text_end_block.tStopRefresh)
        loopEnd_block.addData('text_score.started', text_score.tStartRefresh)
        loopEnd_block.addData('text_score.stopped', text_score.tStopRefresh)
        # check responses
        if button_resp_bk.keys in ['', [], None]:  # No response was made
            button_resp_bk.keys=None
        loopEnd_block.addData('button_resp_bk.keys',button_resp_bk.keys)
        if button_resp_bk.keys != None:  # we had a response
            loopEnd_block.addData('button_resp_bk.rt', button_resp_bk.rt)
        # the Routine "end_block" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed end_block repeats of 'loopEnd_block'
    
    
    # set up handler to look after randomisation of conditions etc
    loopLongPause = data.TrialHandler(nReps=long_pause, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loopLongPause')
    thisExp.addLoop(loopLongPause)  # add the loop to the experiment
    thisLoopLongPause = loopLongPause.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopLongPause.rgb)
    if thisLoopLongPause != None:
        for paramName in thisLoopLongPause:
            exec('{} = thisLoopLongPause[paramName]'.format(paramName))
    
    for thisLoopLongPause in loopLongPause:
        currentLoop = loopLongPause
        # abbreviate parameter names if possible (e.g. rgb = thisLoopLongPause.rgb)
        if thisLoopLongPause != None:
            for paramName in thisLoopLongPause:
                exec('{} = thisLoopLongPause[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "longPause"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        msg_long_pause = 'Wait  ' + str(long_pause) + ' s'
        text.setText(msg_long_pause)
        # keep track of which components have finished
        longPauseComponents = [text]
        for thisComponent in longPauseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        longPauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "longPause"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = longPauseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=longPauseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in longPauseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "longPause"-------
        for thisComponent in longPauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if long_pause > 0:
            long_pause = long_pause - 1
        
        loopLongPause.addData('text.started', text.tStartRefresh)
        loopLongPause.addData('text.stopped', text.tStopRefresh)
    # completed long_pause repeats of 'loopLongPause'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [text_thanks]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_thanks* updates
    if text_thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_thanks.frameNStart = frameN  # exact frame index
        text_thanks.tStart = t  # local t and not account for scr refresh
        text_thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_thanks, 'tStartRefresh')  # time at next scr refresh
        text_thanks.setAutoDraw(True)
    if text_thanks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_thanks.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            text_thanks.tStop = t  # not accounting for scr refresh
            text_thanks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_thanks, 'tStopRefresh')  # time at next scr refresh
            text_thanks.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_thanks.started', text_thanks.tStartRefresh)
thisExp.addData('text_thanks.stopped', text_thanks.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
