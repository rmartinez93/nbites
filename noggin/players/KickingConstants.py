from .. import NogginConstants
SUPER_SAFE_KICKS = False # Only kick straight when we see the goal
MAX_FORWARD_KICK_ANGLE = 55
MIN_SIDEWASE_KICK_ANGLE = 15
DEBUG_KICKS = False
ALIGN_FOR_KICK = True

KICK_STRAIGHT_BEARING_THRESH = 20
ALIGN_FOR_KICK_BEARING_THRESH = 60
ALIGN_FOR_KICK_GAIN = 2.0

(LEFT_FOOT,
 RIGHT_FOOT,
 MID_LEFT,
 MID_RIGHT,
 INCORRECT_POS ) = range(5)

LEFT_FOOT_L_Y = 10
LEFT_FOOT_R_Y = 3
RIGHT_FOOT_L_Y = -LEFT_FOOT_R_Y
RIGHT_FOOT_R_Y = -LEFT_FOOT_L_Y

MAX_KICK_X = 15
MIN_KICK_X = 0

ACROSS_GOAL_BEARING_THRESH = 60
OUT_OF_GOAL_BEARING_THRESH = -10

# Kick objectives
NUM_OBJECTIVES = 5
(OBJECTIVE_CLEAR,
 OBJECTIVE_CENTER,
 OBJECTIVE_SHOOT,
 OBJECTIVE_SHOOT_FAR,
 OBJECTIVE_UNCLEAR) = range(NUM_OBJECTIVES)

# inOppCorner constants
TOP_OPP_CORNER_SLOPE = -1
BOTTOM_OPP_CORNER_SLOPE = 1

OPP_CORNER_LEFT_X = NogginConstants.FIELD_WIDTH - 100.
TOP_OPP_CORNER_Y = NogginConstants.FIELD_HEIGHT

# Penalty Kick
ALIGN_FOR_KICK_MIN_ANGLE = 10

LOOK_POST_KICK_FRAMES_OFF = 10

# clearBall constants
CLEAR_CENTER_FIELD_STRAIGHT_ANGLE = 60
FACING_SIDELINE_ANGLE = 30

SHOT_FROM_LEFT_AIM_POINT = (NogginConstants.LANDMARK_OPP_GOAL_RIGHT_POST_X,
                            NogginConstants.LANDMARK_OPP_GOAL_RIGHT_POST_Y +
                            NogginConstants.GOAL_WIDTH *3.0/4.0)


SHOT_FROM_RIGHT_AIM_POINT = ( NogginConstants.LANDMARK_OPP_GOAL_RIGHT_POST_X,
                              NogginConstants.LANDMARK_OPP_GOAL_RIGHT_POST_Y +
                              NogginConstants.GOAL_WIDTH/4.0)


SHOOT_BALL_LOC_ALIGN_ANGLE = 10
SHOOT_BALL_SIDE_KICK_ANGLE = 45
