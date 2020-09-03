#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on September 03, 2020, at 17:24
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
expName = '2D_scenes'  # from the Builder filename that created this script
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
    originPath='D:\\psychopy\\2D_scenes\\2D_scenes_eng_drawing_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

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
#inicializace na zacatku
textNapoveda=u' '
#initialize first
textRespInstr = ''
text_instr1 = visual.TextStim(win=win, name='text_instr1',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_instr2 = visual.TextStim(win=win, name='text_instr2',
    text='default text',
    font='Arial',
    pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='press space to continue',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
resp_instruct = keyboard.Keyboard()

# Initialize components for Routine "precross"
precrossClock = core.Clock()
text_precross = visual.TextStim(win=win, name='text_precross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
#initialize a variable for response
typeResp = ''
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=0.7,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
mouse_resp = event.Mouse(win=win)
x, y = [None, None]
mouse_resp.mouseClock = core.Clock()
text_cross = visual.TextStim(win=win, name='text_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
brush = visual.Brush(win=win, name='brush',
   lineWidth=2.5,
   lineColor=[1.000,-1.000,-1.000],
   lineColorSpace='rgb',
   opacity='1')

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#initialize
FeedbackMouse = '';
#inicializace promenne
msqFeedback = ''
textFeedBack = visual.TextStim(win=win, name='textFeedBack',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "end_block"
end_blockClock = core.Clock()
#inicializace promenne
corrans_bk = ''
text_end_block = visual.TextStim(win=win, name='text_end_block',
    text='Which block was it?\n\n◄   closer to the border\n►   closer to the cross\n',
    font='Arial',
    pos=(0, 0.1), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_score = visual.TextStim(win=win, name='text_score',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp_bk = keyboard.Keyboard()

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
    trialList=data.importConditions('scenes.csv'),
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
        if condition=='C1' or condition=='C2':
            textNapoveda = u'closer to the border'
        else:
            textNapoveda = u'closer to the cross'
        if response=='by_mouse':
            textRespInstr='Response by mouse: move the mouse from the cross to the closest object (to the cross or to the border - according to the current condition) and click the left button'
        else:
            textRespInstr='Response by keys: t - for triangle, g - for square'
        text_instr1.setText(textNapoveda)
        text_instr2.setText(textRespInstr)
        text_3.setText(block)
        resp_instruct.keys = []
        resp_instruct.rt = []
        _resp_instruct_allKeys = []
        # keep track of which components have finished
        instructionComponents = [text_instr1, text_instr2, text_2, text_3, resp_instruct]
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
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            
            # *resp_instruct* updates
            waitOnFlip = False
            if resp_instruct.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                resp_instruct.frameNStart = frameN  # exact frame index
                resp_instruct.tStart = t  # local t and not account for scr refresh
                resp_instruct.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_instruct, 'tStartRefresh')  # time at next scr refresh
                resp_instruct.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_instruct.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp_instruct.status == STARTED and not waitOnFlip:
                theseKeys = resp_instruct.getKeys(keyList=['space'], waitRelease=False)
                _resp_instruct_allKeys.extend(theseKeys)
                if len(_resp_instruct_allKeys):
                    resp_instruct.keys = _resp_instruct_allKeys[-1].name  # just the last key pressed
                    resp_instruct.rt = _resp_instruct_allKeys[-1].rt
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
        loopPause.addData('text_2.started', text_2.tStartRefresh)
        loopPause.addData('text_2.stopped', text_2.tStopRefresh)
        loopPause.addData('text_3.started', text_3.tStartRefresh)
        loopPause.addData('text_3.stopped', text_3.tStopRefresh)
        # check responses
        if resp_instruct.keys in ['', [], None]:  # No response was made
            resp_instruct.keys = None
        loopPause.addData('resp_instruct.keys',resp_instruct.keys)
        if resp_instruct.keys != None:  # we had a response
            loopPause.addData('resp_instruct.rt', resp_instruct.rt)
        loopPause.addData('resp_instruct.started', resp_instruct.tStartRefresh)
        loopPause.addData('resp_instruct.stopped', resp_instruct.tStopRefresh)
        # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "precross"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        precrossComponents = [text_precross]
        for thisComponent in precrossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        precrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "precross"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = precrossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=precrossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_precross* updates
            if text_precross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_precross.frameNStart = frameN  # exact frame index
                text_precross.tStart = t  # local t and not account for scr refresh
                text_precross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_precross, 'tStartRefresh')  # time at next scr refresh
                text_precross.setAutoDraw(True)
            if text_precross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_precross.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_precross.tStop = t  # not accounting for scr refresh
                    text_precross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_precross, 'tStopRefresh')  # time at next scr refresh
                    text_precross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in precrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "precross"-------
        for thisComponent in precrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loopPause.addData('text_precross.started', text_precross.tStartRefresh)
        loopPause.addData('text_precross.stopped', text_precross.tStopRefresh)
        thisExp.nextEntry()
        
    # completed short_pause repeats of 'loopPause'
    
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    if response=='by_mouse':
        typeResp = mouse_resp
    else:
        typeResp = key_resp
        
        
    x_coord = []
    y_coord = []
    
    
    image.setImage('images_last/'+picture)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # setup some python lists for storing info about the mouse_resp
    mouse_resp.x = []
    mouse_resp.y = []
    mouse_resp.leftButton = []
    mouse_resp.midButton = []
    mouse_resp.rightButton = []
    mouse_resp.time = []
    gotValidClick = False  # until a click is received
    mouse_resp.mouseClock.reset()
    brush.reset()
    # keep track of which components have finished
    trialComponents = [image, key_resp, mouse_resp, text_cross, ISI, brush]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        x_coord.append(mouse_resp.getPos()[0])
        y_coord.append(mouse_resp.getPos()[1])
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['t', 'g'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(corrans)) or (key_resp.keys == corrans):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
        # *mouse_resp* updates
        if mouse_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_resp.frameNStart = frameN  # exact frame index
            mouse_resp.tStart = t  # local t and not account for scr refresh
            mouse_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_resp, 'tStartRefresh')  # time at next scr refresh
            mouse_resp.status = STARTED
            prevButtonState = mouse_resp.getPressed()  # if button is down already this ISN'T a new click
        if mouse_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                mouse_resp.tStop = t  # not accounting for scr refresh
                mouse_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_resp, 'tStopRefresh')  # time at next scr refresh
                mouse_resp.status = FINISHED
        if mouse_resp.status == STARTED:  # only update if started and not finished!
            x, y = mouse_resp.getPos()
            mouse_resp.x.append(x)
            mouse_resp.y.append(y)
            buttons = mouse_resp.getPressed()
            mouse_resp.leftButton.append(buttons[0])
            mouse_resp.midButton.append(buttons[1])
            mouse_resp.rightButton.append(buttons[2])
            mouse_resp.time.append(mouse_resp.mouseClock.getTime())
        
        # *text_cross* updates
        if text_cross.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            text_cross.frameNStart = frameN  # exact frame index
            text_cross.tStart = t  # local t and not account for scr refresh
            text_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_cross, 'tStartRefresh')  # time at next scr refresh
            text_cross.setAutoDraw(True)
        if text_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_cross.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_cross.tStop = t  # not accounting for scr refresh
                text_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_cross, 'tStopRefresh')  # time at next scr refresh
                text_cross.setAutoDraw(False)
        
        # *brush* updates
        if brush.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            brush.frameNStart = frameN  # exact frame index
            brush.tStart = t  # local t and not account for scr refresh
            brush.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(brush, 'tStartRefresh')  # time at next scr refresh
            brush.setAutoDraw(True)
        if brush.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > brush.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                brush.tStop = t  # not accounting for scr refresh
                brush.frameNStop = frameN  # exact frame index
                win.timeOnFlip(brush, 'tStopRefresh')  # time at next scr refresh
                brush.setAutoDraw(False)
        # *ISI* period
        if ISI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if response=='by_key' and key_resp.keys:
        pressed=1;
    else:
        pressed=0;
        
    #if response=='by_mouse' and mouse_resp.leftButton:    
    if response=='by_mouse':
        clicked=1;
    else:
        clicked=0; 
    
    
    x, y = mouse_resp.getPos()
    
    attempts += 1
    if pressed:
        sumScore += key_resp.corr;
        sumRt += key_resp.rt;
    elif clicked: 
        if (correct_object== 'square' and x>(x_square-0.05) and x<(x_square+0.05) and y>(y_square-0.05) and y<(y_square+0.05)) or (correct_object== 'triangle' and x>(x_triangle-0.05) and x<(x_triangle+0.05) and y>(y_triangle-0.05) and y<(y_triangle+0.05)):
        #if (correct_object== 'square' and mouse_resp.x>(x_square-0.05) and mouse_resp.x<(x_square+0.05) and mouse_resp.y>(y_square-0.05) and mouse_resp.y<(y_square+0.05)) or (correct_object== 'triangle' and mouse_resp.x>(x_triangle-0.05) and mouse_resp.x<(x_triangle+0.05) and mouse_resp.y>(y_triangle-0.05) and mouse_resp.y<(y_triangle+0.05)):
         mouse_resp.corr = 1;
        else:
         mouse_resp.corr = 0;
         
        sumScore += mouse_resp.corr;
        sumRt += sum(mouse_resp.time);
    else:
        missed = missed + 1
        
    
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('mouse_resp.x', mouse_resp.x)
    trials.addData('mouse_resp.y', mouse_resp.y)
    trials.addData('mouse_resp.leftButton', mouse_resp.leftButton)
    trials.addData('mouse_resp.midButton', mouse_resp.midButton)
    trials.addData('mouse_resp.rightButton', mouse_resp.rightButton)
    trials.addData('mouse_resp.time', mouse_resp.time)
    trials.addData('mouse_resp.started', mouse_resp.tStartRefresh)
    trials.addData('mouse_resp.stopped', mouse_resp.tStopRefresh)
    trials.addData('text_cross.started', text_cross.tStartRefresh)
    trials.addData('text_cross.stopped', text_cross.tStopRefresh)
    trials.addData('ISI.started', ISI.tStartRefresh)
    trials.addData('ISI.stopped', ISI.tStopRefresh)
    trials.addData('brush.started', brush.tStartRefresh)
    trials.addData('brush.stopped', brush.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    loopFeedback = data.TrialHandler(nReps=feedback, method='random', 
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
        #if correct_object== 'square' and mouse_resp.x>(x_square-0.05) and mouse_resp.x<(x_square+0.05) and mouse_resp.y>(y_square-0.05) and mouse_resp.y<(y_square+0.05):
          #FeedbackMouse = 'correct'
        #elif correct_object== 'triangle' and mouse_resp.x>(x_triangle-0.05) and mouse_resp.x<(x_triangle+0.05) and mouse_resp.y>(y_triangle-0.05) and mouse_resp.y<(y_triangle+0.05):
          #FeedbackMouse = 'correct'
        #else:
          #FeedbackMouse = 'wrong'
          
        
        
        if correct_object== 'square' and x>(x_square-0.05) and x<(x_square+0.05) and y>(y_square-0.05) and y<(y_square+0.05):
          FeedbackMouse = 'correct'
        elif correct_object== 'triangle' and x>(x_triangle-0.05) and x<(x_triangle+0.05) and y>(y_triangle-0.05) and y<(y_triangle+0.05):
          FeedbackMouse = 'correct'
        else:
          FeedbackMouse = 'wrong'
        if response=='by_key' and key_resp.corr:#stored on last run routine
          msqFeedback='correct'
        elif response=='by_key' and key_resp.corr==0:
          msqFeedback='wrong'
        else: 
            msqFeedback=FeedbackMouse
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
    loopEnd_block = data.TrialHandler(nReps=end_block, method='random', 
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
        if condition=='C1' or condition=='C2':
            corrans_bk = 'left'
        else:
            corrans_bk = 'right'
        
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
        resp_bk.keys = []
        resp_bk.rt = []
        _resp_bk_allKeys = []
        # keep track of which components have finished
        end_blockComponents = [text_end_block, text_score, resp_bk]
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
            
            # *resp_bk* updates
            waitOnFlip = False
            if resp_bk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_bk.frameNStart = frameN  # exact frame index
                resp_bk.tStart = t  # local t and not account for scr refresh
                resp_bk.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_bk, 'tStartRefresh')  # time at next scr refresh
                resp_bk.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_bk.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp_bk.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp_bk.status == STARTED and not waitOnFlip:
                theseKeys = resp_bk.getKeys(keyList=['left', 'right'], waitRelease=False)
                _resp_bk_allKeys.extend(theseKeys)
                if len(_resp_bk_allKeys):
                    resp_bk.keys = _resp_bk_allKeys[-1].name  # just the last key pressed
                    resp_bk.rt = _resp_bk_allKeys[-1].rt
                    # was this correct?
                    if (resp_bk.keys == str(corrans_bk)) or (resp_bk.keys == corrans_bk):
                        resp_bk.corr = 1
                    else:
                        resp_bk.corr = 0
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
        if resp_bk.keys in ['', [], None]:  # No response was made
            resp_bk.keys = None
            # was no response the correct answer?!
            if str(corrans_bk).lower() == 'none':
               resp_bk.corr = 1;  # correct non-response
            else:
               resp_bk.corr = 0;  # failed to respond (incorrectly)
        # store data for loopEnd_block (TrialHandler)
        loopEnd_block.addData('resp_bk.keys',resp_bk.keys)
        loopEnd_block.addData('resp_bk.corr', resp_bk.corr)
        if resp_bk.keys != None:  # we had a response
            loopEnd_block.addData('resp_bk.rt', resp_bk.rt)
        loopEnd_block.addData('resp_bk.started', resp_bk.tStartRefresh)
        loopEnd_block.addData('resp_bk.stopped', resp_bk.tStopRefresh)
        # the Routine "end_block" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
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
        thisExp.nextEntry()
        
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
