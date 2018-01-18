from psychopy import visual, core, event #import some libraries from PsychoPy
import numpy as np

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
                              pos=[0, 0], alignHoriz='center')


# Task stimuli
stim1 = visual.GratingStim(win=mywin, mask='gauss',
                           size=3, pos=[-4, 0], sf=0)

fixat = visual.TextStim(win=mywin,
                        text='+',
                        pos=[0, 0], alignHoriz='center')

imag_rec = visual.ShapeStim(win=mywin,
                            vertices=((-5, 2), (-5, 5), (5, 5), (5, 2)),
                            lineWidth=.5, pos=(.05, 0),
                            lineColor='white')

triangle = visual.ShapeStim(win=mywin,
                            vertices=((-2.5, 2), (0, 5), (2.5, 2)),
                            lineWidth=.5, pos=(0, 0),
                            fillColor='red', lineColor=None)

square = visual.ShapeStim(win=mywin,
                          vertices=((-2.5, 2), (-2.5, 5), (2.5, 5), (2.5, 2)),
                          lineWidth=.5, pos=(0, 0),
                          fillColor='red', lineColor=None)

# variables initializations
trials_no = 2
rounds_no = 3
total_no = trials_no * rounds_no

# and some handy clocks to keep track of time
roundClock = core.Clock()
trialClock = core.Clock()

# clock.reset() There is also a reset! this is helpful in getting the reaction time!

# randomize shapes and left and right movements with having a fixed number of left and rights
# shape
st = np.concatenate((np.zeros(total_no//2), np.ones(total_no//2)), axis=0).astype(int)
np.random.shuffle(st)

# left/right
shift_val = 1.5
lr = np.concatenate((np.ones(total_no//2)*shift_val, -np.ones(total_no//2)*shift_val), axis=0)
np.random.shuffle(lr)
np.random.shuffle(lr)

# color
flash1 = np.concatenate((np.array(['red']).repeat(total_no//2), np.array(['green']).repeat(total_no//2)), axis=0)
np.random.shuffle(flash1)
flash2 = np.concatenate((np.array(['red']).repeat(total_no//2), np.array(['green']).repeat(total_no//2)), axis=0)
np.random.shuffle(flash2)
np.random.shuffle(flash2)
print(flash1, flash2)

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

        # randomization takes effect here
        if st[rnd*trials_no + trial]:
            obj_disp = triangle
        else:
            obj_disp = square

        mv_shift = (lr[rnd*trials_no + trial], 0)

        # Set the initial condition (we can have a reset function/method here)
        obj_disp.pos = (0, 0)
        obj_disp.fillColor = flash1[rnd*trials_no + trial]

        # this is where the actual experiment lies
        for frame in range(18):
            # these are present in every frame of trial
            fixat.draw()
            imag_rec.draw()
            # add new stuff
            obj_disp.draw()
            # display whatever u wanted to draw
            mywin.flip()

        # implement the changes as compared to the first flash
        obj_disp.pos += mv_shift
        obj_disp.fillColor = flash2[rnd*trials_no + trial]

        # Blank screen for 300 ms = 18 frames on 60Hz monitor
        for frame in range(18):
            # these are present in every frame of trial
            fixat.draw()
            imag_rec.draw()
            # add new stuff
            obj_disp.draw()
            # display whatever u wanted to draw
            mywin.flip()

        for frame in range(30):  # ITI
            fixat.draw()
            mywin.flip()

closing_msg.draw()
mywin.flip()

event.waitKeys(keyList='space')
event.clearEvents()

# cleanup
mywin.close()
core.quit()
