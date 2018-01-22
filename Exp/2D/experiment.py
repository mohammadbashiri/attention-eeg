from psychopy import visual #import some libraries from PsychoPy
import numpy as np

class Experiment(object):

    def __init__(self, win=None, trials_no=None, mode='motion-color'):

        # Welcoming/intro
        self.welcome_msg1 = visual.TextStim(win=win,
                                            text='Welcome to',
                                            pos=[0, 10], alignHoriz='center',
                                            color=(0, 0, 0))
        self.welcome_msg2 = visual.TextStim(win=win,
                                            text='AttentionEEG experiment',
                                            pos=[0, 8], alignHoriz='center',
                                            color=(0, 0, 0), bold=True)
        self.welcome_msg3 = visual.TextStim(win=win,
                                            text='Please press',
                                            pos=[0, 1], alignHoriz='center',
                                            color=(0, 0, 0))
        self.welcome_msg4 = visual.TextStim(win=win,
                                            text='RIGHT ARROW KEY',
                                            pos=[0, -1], alignHoriz='center',
                                            color=(0, 0, 0))
        self.welcome_msg5 = visual.TextStim(win=win,
                                            text='to proceed',
                                            pos=[0, -3], alignHoriz='center',
                                            color=(0, 0, 0))
        # Instructions
        if mode == 'motion-shape':
            self.instruct1_msg = visual.TextStim(win=win,
                                                 text='Attend to Shape',
                                                 pos=[0, 0], alignHoriz='center',
                                                 color=(0, 0, 0))
        elif mode == 'motion-color':
            self.instruct1_msg = visual.TextStim(win=win,
                                                 text='Attend to Color',
                                                 pos=[0, 0], alignHoriz='center',
                                                 color=(0, 0, 0))

        self.attended_feature = visual.TextStim(win=win,
                                                text='',
                                                pos=[0, 0], alignHoriz='center',
                                                color=(0, 0, 0))

        # Closing remark
        self.closing_msg = visual.TextStim(win=win,
                                           text='This is the end of experiment!',
                                           pos=[0, 0], alignHoriz='center',
                                           color=(0,0,0))

        # Task stimuli
        self.stim1 = visual.GratingStim(win=win, mask='gauss',
                                        size=3, pos=[-4, 0], sf=0)

        self.fixat = visual.TextStim(win=win,
                                     text='+',
                                     pos=[0, 0], alignHoriz='center',
                                     color=(0, 0, 0))

        self.imag_rec = visual.ShapeStim(win=win,
                                         vertices=((-5, 2), (-5, 5), (5, 5), (5, 2)),
                                         lineWidth=.5, pos=(0, 0),
                                         lineColor='black')

        self.triangle = visual.Polygon(win=win,
                                       radius=1.5, pos=(0, 2.35),
                                       fillColor='red', lineColor=None)

        self.square = visual.Rect(win=win,
                                  width=2.5, height=1.1*2, pos=(0, 2.35),
                                  fillColor='red', lineColor=None)

        self.circle = visual.Circle(win=win,
                                    radius=1.55, pos=(0, 2.35),
                                    fillColor='red', lineColor=None)

        self.trials_no = trials_no
        self.mode = mode

        # markers
        self.block_start = 1
        self.flash1_start_Non = 2
        self.flash2_start = 5

        # if mode == 'motion-color':
        #     self.block_start = 1
        #     self.flash1_start_Non = 2
        #     # self.flash1_start_standard = 3
        #     # self.flash1_start_target = 4
        #     self.flash2_start = 5
        #
        # if mode == 'motion-shape':
        #     self.block_start = 6
        #     self.flash1_start_Non = 7
        #     # self.flash1_start_standard = 8
        #     # self.flash1_start_target = 9
        #     self.flash2_start = 10

        self.response_marker = 11

    def isTarget(self, feature1, feature2, color, shape, direction, stim_type):

        # print(feature1, feature2, color, shape, direction, stim_type)
        if self.mode == 'motion-color':
            if feature1 == color and feature2 == direction and stim_type == 9:
                return True

            else:
                return False

        if self.mode == 'motion-shape':
            if feature1 == shape and feature2 == direction and stim_type == 9:
                return True

            else:
                return False

    def isStandard(self, feature1, feature2, color, shape, direction, stim_type):

        # print(feature1, feature2, color, shape, direction, stim_type)
        if self.mode == 'motion-color':
            if feature1 == color and feature2 == direction and stim_type == 3:
                return True

            else:
                return False

        if self.mode == 'motion-shape':
            if feature1 == shape and feature2 == direction and stim_type == 3:
                return True

            else:
                return False

    def getRandAttendedFeature(self, color, shape, direction):
        selected_shape = np.random.choice(np.array(shape))
        selected_color = np.random.choice(np.array(color))
        selected_direction = np.random.choice(np.array(direction))

        if self.mode == 'motion-color':
            return selected_color, selected_direction

        if self.mode == 'motion-shape':
            return selected_shape, selected_direction


    def randomize2val(self, val1, val2):
        rnd = np.concatenate((np.ones(self.trials_no//2)*val1, np.ones(self.trials_no//2)*val2), axis=0)
        np.random.shuffle(rnd)
        np.random.shuffle(rnd)
        return rnd

    def randomize2str(self, str1, str2):
        rnd = np.concatenate((np.array([str1]).repeat(self.trials_no//2), np.array([str2]).repeat(self.trials_no//2)),
                             axis=0)
        np.random.shuffle(rnd)
        np.random.shuffle(rnd)
        return rnd

    def randomize2type(self, std_delay, std_prob, target_delay, target_prob):
        rnd = np.concatenate((np.ones(int(self.trials_no * std_prob + .5)) * std_delay,
                              np.ones(int(self.trials_no * target_prob + .5)) * target_delay),
                             axis=0)
        np.random.shuffle(rnd)
        np.random.shuffle(rnd)
        return rnd.astype(int)


    def getrand_obj(self, val):
        if val:
            return self.circle
        else:
            return self.square

    def getrand_pos(self):
        return np.random.rand()*7.3-3.65,  2.35  # (x, y) this depends on the boundaries (x-axis) of the imaginary rectangle

class DataLogger:

    def __init__(self, subject_name='unknown', session_no='00', no_of_blocks=0, no_of_trials=0):

        # subject information
        self.subject_name = subject_name
        self.session_no = str(session_no)
        self._block_no = no_of_blocks
        self._trial_no = no_of_trials

        # logging information
        self._block_no_ls = []
        self._trial_mode_ls = []
        self._flash1_shape_ls = []
        self._flash2_shape_ls = []
        self._flash1_color_ls = []
        self._flash2_color_ls = []
        self._shift_ls = []
        self._stim_type_ls = []
        self._attended_feature1_ls = []
        self._attended_feature2_ls = []


    def update(self, block_counter, exp_mode, flash1_shape, flash2_shape, flash1_color, flash2_color, lr, stim_type, feature1, feature2):
        self._block_no_ls += [str(block_counter + 1)] * self._trial_no
        self._trial_mode_ls += [exp_mode] * self._trial_no
        self._flash1_shape_ls += map(str, flash1_shape)
        self._flash2_shape_ls += map(str, flash2_shape)
        self._flash1_color_ls += list(flash1_color)
        self._flash2_color_ls += list(flash2_color)
        self._shift_ls += map(str, lr)
        self._stim_type_ls += map(str, stim_type)
        self._attended_feature1_ls += [str(feature1)] * self._trial_no
        self._attended_feature2_ls += [str(feature2)] * self._trial_no


    def _get_trialtype(self, i):

        '''
        1 - TrtMposCpos(standard M+/C+) -> attended motion + attended color
        2 - TrtMposCneg
        3 - TrtMnegCpos
        4 - TrtMnegCneg
        5 - TrtMposSpos
        6 - TrtMposSneg
        7 - TrtMnegSpos
        8 - TrtMnegSneg

        11 - StdMposCpos(standard M+/C+) -> attended motion + attended color
        12 - StdMposCneg
        13 - StdMnegCpos
        14 - StdMnegCneg
        15 - StdMposSpos
        16 - StdMposSneg
        17 - StdMnegSpos
        18 - StdMnegSneg

        :param i: index of the trial (starts from 0)
        :return: type of trial (1-8 or 11-18)
        '''

        trialtype = None

        if self._stim_type_ls[i] == '3':  # standard stimulus
            if self._trial_mode_ls[i] == 'motion-color':

                if self._shift_ls[i] == self._attended_feature2_ls[i] and self._flash1_color_ls[i] == self._attended_feature1_ls[i]:
                    trialtype = 11
                elif self._shift_ls[i] == self._attended_feature2_ls[i] and self._flash1_color_ls[i] != self._attended_feature1_ls[i]:
                    trialtype = 12
                elif self._shift_ls[i] != self._attended_feature2_ls[i] and self._flash1_color_ls[i] == self._attended_feature1_ls[i]:
                    trialtype = 13
                elif self._shift_ls[i] != self._attended_feature2_ls[i] and self._flash1_color_ls[i] !=  self._attended_feature1_ls[i]:
                    trialtype = 14

            elif self._trial_mode_ls[i] == 'motion-shape':

                if self._shift_ls[i] == self._attended_feature2_ls[i] and self._flash1_shape_ls[i] == self._attended_feature1_ls[i]:
                    trialtype = 15
                elif self._shift_ls[i] == self._attended_feature2_ls[i] and self._flash1_shape_ls[i] != self._attended_feature1_ls[i]:
                    trialtype = 16
                elif self._shift_ls[i] != self._attended_feature2_ls[i] and self._flash1_shape_ls[i] == self._attended_feature1_ls[i]:
                    trialtype = 17
                elif self._shift_ls[i] != self._attended_feature2_ls[i] and self._flash1_shape_ls[i] !=  self._attended_feature1_ls[i]:
                    trialtype = 18

        elif self._stim_type_ls[i] == '9':  # target stimulus
            if self._trial_mode_ls[i] == 'motion-color':

                if self._shift_ls[i] == self._attended_feature2_ls[i] and self._flash1_color_ls[i] == self._attended_feature1_ls[i]:
                    trialtype = 1
                elif self._shift_ls[i] == self._attended_feature2_ls[i] and self._flash1_color_ls[i] != self._attended_feature1_ls[i]:
                    trialtype = 2
                elif self._shift_ls[i] != self._attended_feature2_ls[i] and self._flash1_color_ls[i] == self._attended_feature1_ls[i]:
                    trialtype = 3
                elif self._shift_ls[i] != self._attended_feature2_ls[i] and self._flash1_color_ls[i] !=  self._attended_feature1_ls[i]:
                    trialtype = 4

            elif self._trial_mode_ls[i] == 'motion-shape':

                if self._shift_ls[i] == self._attended_feature2_ls[i] and self._flash1_shape_ls[i] == self._attended_feature1_ls[i]:
                    trialtype = 5
                elif self._shift_ls[i] == self._attended_feature2_ls[i] and self._flash1_shape_ls[i] != self._attended_feature1_ls[i]:
                    trialtype = 6
                elif self._shift_ls[i] != self._attended_feature2_ls[i] and self._flash1_shape_ls[i] == self._attended_feature1_ls[i]:
                    trialtype = 7
                elif self._shift_ls[i] != self._attended_feature2_ls[i] and self._flash1_shape_ls[i] !=  self._attended_feature1_ls[i]:
                    trialtype = 8

        return trialtype


    def save(self, filepath):

        filename = filepath + self.subject_name + '_s' + self.session_no + '_' + str(self._block_no) + 'blocks_each' + str(
            self._trial_no) + 'trials' + '.txt'

        with open(filename, 'w') as f:
            f.write('trial\t' + 'block\t' + 'mode\t' + 'shape1\t' + 'shape2\t' + 'color1\t' + 'color2\t' + 'shift\t' + 'stim_type\t' + 'feat1\t' + 'feat2\n')
            for trial, (block, mode, shape1, shape2, color1, color2, shift, stim_t, feat1, feat2) in \
                    enumerate(zip(self._block_no_ls, self._trial_mode_ls, self._flash1_shape_ls, self._flash2_shape_ls, self._flash1_color_ls,
                                  self._flash2_color_ls, self._shift_ls, self._stim_type_ls, self._attended_feature1_ls, self._attended_feature2_ls)):
                f.write(str(trial + 1) + '\t' + block + '\t' + mode + '\t' + shape1 + '\t' + shape2 + '\t' + color1 + '\t' +
                        color2 + '\t' + shift + '\t' + stim_t + '\t' + feat1 + '\t' + feat2 + '\n')

        filename = filepath + self.subject_name + '_s' + self.session_no + '_' + str(self._block_no) + 'blocks_each' + str(
            self._trial_no) + 'trials_trialtype' + '.txt'

        with open(filename, 'w') as f:
            f.write('trialtype\n')
            for trial in range(len(self._block_no_ls)):
                trialtype = self._get_trialtype(trial)
                f.write(str(trialtype) + '\n')
