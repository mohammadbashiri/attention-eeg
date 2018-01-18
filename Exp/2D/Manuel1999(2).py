from psychopy import visual, core, event, parallel, monitors  # import some libraries from PsychoPy
from experiment import Experiment
import numpy as np


# initialize parallel port
port = parallel.ParallelPort(0xDC00)


# exp spcecifications
no_of_blocks = 2
no_of_trials = 20  # per block

block_counter = 0

# create a window
mywin = visual.Window((1920, 1200), screen=1, monitor="testMonitor", units="deg",color=(.9,.9,.9))

for blocks in range(no_of_blocks):

    if block_counter % 2 == 0:
        exp = Experiment(win=mywin, blocks_no=1, trials_no=no_of_trials, mode='motion-shape')
    else:
        exp = Experiment(win=mywin, blocks_no=1, trials_no=no_of_trials, mode='motion-color')

    # randomize shapes and left and right movements with having a fixed number  of left and rights
    # shape
    flash1_shape = exp.randomize2val(0, 1).astype(int)  # 1: circle, 0: square
    flash2_shape = exp.randomize2val(0, 1).astype(int)  # 1: circle, 0: square

    # left/right
    shift_val = 2.5
    lr = exp.randomize2val(shift_val, -shift_val)

    # color
    flash1_color = exp.randomize2str('red', 'green')
    flash2_color = exp.randomize2str('red', 'green')

    # type
    prob_target = 1
    prob_std = 0
    stim_type = exp.randomize2type(3, prob_std, 9, prob_target)  # delay (frames), probability, delay (frames), probability

    # get randomized target value, depending on the experiment mode
    feature1, feature2 = exp.getRandAttendedFeature(('red', 'green'), (0, 1), (shift_val, -shift_val))

    if feature1 == 'red' or feature1 == 'green':
        feature1Text = feature1
    elif feature1 == 0:
        feature1Text = 'square'
    elif feature1 == 1:
        feature1Text = 'circle'

    if feature2 == -2.5:
        feature2Text = 'left'
    else:
        feature2Text = 'right'
    space = " "
    attended_feature_text = (feature1Text, 'to', feature2Text)
    attended_feature_text_joined = space.join(attended_feature_text)

    print(feature1, feature1Text, feature2, feature2Text, attended_feature_text_joined)

    # welcoming message and introduction
    if block_counter == 0:
        exp.welcome_msg.draw()
        mywin.flip()
        event.waitKeys(keyList='space')  # wait for subject to press space
        event.clearEvents()

    # start of the block
    for block in range(exp.blocks_no):

        # marker - block start
        port.setData(exp.block_start)

        # display the instructions
        exp.instruct1_msg.draw()
        exp.attended_feature.setText(attended_feature_text_joined)
        exp.attended_feature.pos = (0, -1.5)
        exp.attended_feature.draw()
        mywin.flip()

        # press space to continue
        event.waitKeys(keyList='space')

        for frame in range(60):
            exp.fixat.draw()
            mywin.flip()

        # start of the trial
        for trial in range(exp.trials_no):

            # randomization takes effect here
            obj_disp = exp.getrand_obj(flash1_shape[block*exp.trials_no + trial])
            mv_shift = (lr[block*exp.trials_no + trial], 0)  # 0 because the change is only in x direction

            # Set the initial condition (we can have a res et function/method here)
            obj_disp.pos = exp.getrand_pos()
            position = obj_disp.pos
            obj_disp.fillColor = flash1_color[block*exp.trials_no + trial]

            # marker - flash1
            if exp.isTarget(feature1, feature2,
                            flash1_color[block*exp.trials_no + trial],  # color
                            flash1_shape[block*exp.trials_no + trial],  # shape
                            lr[block * exp.trials_no + trial], stim_type[block*exp.trials_no + trial]):  # shift

                port.setData(exp.flash1_start_target)

            elif exp.isStandard(feature1, feature2,
                                flash1_color[block*exp.trials_no + trial],  # color
                                flash1_shape[block*exp.trials_no + trial],  # shape
                                lr[block * exp.trials_no + trial], stim_type[block*exp.trials_no + trial]):  # shift

                port.setData(exp.flash1_start_standard)

            else:
                port.setData(exp.flash1_start_Notarget)

            # this is where the actual experiment lies
            for frame in range(2):
                # these are present in every frame of trial
                exp.fixat.draw()
                # exp.imag_rec.draw()
                # add new stuff
                obj_disp.draw()
                # display whatever u wanted to draw
                mywin.flip()

                if event.getKeys(keyList='space'):
                    print('SPACE was pressed!')
                    port.setData(exp.response_marker)

            for frame in range(stim_type[block*exp.trials_no + trial]):  # SOA
                exp.fixat.draw()
                mywin.flip()

                if event.getKeys(keyList='space'):
                    print('SPACE was pressed!')
                    port.setData(exp.response_marker)

            # Implement the changes between two flashes
            if exp.mode == 'motion-color':
                obj_disp = exp.getrand_obj(flash2_shape[block * exp.trials_no + trial])
                obj_disp.fillColor = flash1_color[block*exp.trials_no + trial]  # color must stay the same

            else:
                obj_disp = exp.getrand_obj(flash1_shape[block * exp.trials_no + trial])  # object must stay the same
                obj_disp.fillColor = flash2_color[block * exp.trials_no + trial]  # color should change

            # shift is always there
            obj_disp.pos = position
            obj_disp.pos += mv_shift

            # marker - flash 2
            port.setData(exp.flash2_start)

            # clear the event buffer
            # event.clearEvents()
            if event.getKeys(keyList='space'):
                print('SPACE was pressed!')
                port.setData(exp.response_marker)

            # Blank screen for 300 ms = 18 frames on 60Hz monitor
            for frame in range(2):
                # these are present in every frame of trial
                exp.fixat.draw()
                # exp.imag_rec.draw()
                # add new stuff
                obj_disp.draw()
                # display whatever u wanted to draw
                mywin.flip()
                if event.getKeys(keyList='space'):
                    print('SPACE was pressed!')
                    port.setData(exp.response_marker)


            for frame in range(np.random.randint(15, 45)):  # ITI
                exp.fixat.draw()
                mywin.flip()

                if event.getKeys(keyList='space'):
                    print('SPACE was pressed!')
                    port.setData(exp.response_marker)

            if event.getKeys(keyList='space'):
                print('SPACE was pressed!')
                port.setData(exp.response_marker)

    event.clearEvents()

    block_counter += 1
    if block_counter == no_of_blocks:
        exp.closing_msg.draw()
        mywin.flip()

        event.waitKeys(keyList='space')

# cleanup
mywin.close()
core.quit()

