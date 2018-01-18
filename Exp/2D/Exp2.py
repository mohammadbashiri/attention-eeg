from psychopy import visual, core, event #import some libraries from PsychoPy

#create a window
mywin = visual.Window([800, 600], monitor="testMonitor", units="deg")


# Text stimuli
# Welcoming/intro
welcome_msg = visual.TextStim(win=mywin,
                              text='Welcome to the experiment\nPlease press SCAPE to proceed',
                              pos=[0, 0], alignHoriz='center')

# Instructions
instruct1_msg = visual.TextStim(win=mywin,
                                text='instruction',
                                pos=[0, 0], alignHoriz='center')

# Closing remark
closing_msg = visual.TextStim(win=mywin,
                              text='This is the end of experiment!',
                              pos=[4, 0], alignHoriz='center')


# Task stimuli
stim1 = visual.GratingStim(win=mywin, mask='gauss',
                           size=3, pos=[-4, 0], sf=0)

fixat = visual.GratingStim(win=mywin, size=1,
                           pos=[0, 0], sf=0, rgb=-1)


# variables initializations
trials_no = 2
rounds_no = 3

# and some handy clocks to keep track of time
roundClock = core.Clock()
trialClock = core.Clock()

# clock.reset() There is also a reset! this is helpful in getting the reaction time!

# welcoming message and introduction
welcome_msg.draw()
mywin.flip()

event.waitKeys(keyList='space')  # wait for subject to press space
event.clearEvents()

# start of the round
roundClock.reset()
for rnd in range(rounds_no):

    # display the instructions
    instruct1_msg.draw()
    mywin.flip()

    # press space to continue
    event.waitKeys(keyList='space')
    event.clearEvents()

    # start of the trial
    trialClock.reset()
    for trial in range(trials_no):

        # this is where the actual experiment lies
        for frame in range(18):
            fixat.draw()
            mywin.flip()

        # Blank screen for 300 ms = 18 frames on 60Hz monitor
        for frame in range(18):
            stim1.draw()
            mywin.flip()

closing_msg.draw()
mywin.flip()

event.waitKeys(keyList='space')
event.clearEvents()

# cleanup
mywin.close()
core.quit()
