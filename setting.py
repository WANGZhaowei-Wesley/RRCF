DATA_ANALYSIS = False
OUR_FEATURE = False
FEATURE_SELECT = False
CUT_SELECT = False
CODISP_DEPTH = False
UPDATE_ANOMALY = False
UPDATE_ALL = True
TS_FRESH = False
CLUSTER = False
SELECT_POINT = "" # "TOP"/"MID"/"RANDOM"/"BUCKET"/""
FEEDBACK = "" # "WEIGHT"/ "POINT"/ "BOTH/ ""
STRING = "1.3"
def assert_parms():
    print("OUR_FEATURE", OUR_FEATURE)
    print("CLUSTER", CLUSTER)
    print("FEATURE_SELECT", FEATURE_SELECT)
    print("CUT_SELECT", CUT_SELECT)
    print("CODISP_DEPTH", CODISP_DEPTH)
    print("UPDATE_ALL", UPDATE_ALL)
    print("UPDATE_ANOMALY", UPDATE_ANOMALY)
    print("active learning", SELECT_POINT, FEEDBACK)
    assert SELECT_POINT in {"TOP", "MID", "RANDOM", "BUCKET", ""}
    assert FEEDBACK in {"WEIGHT", "POINT", "BOTH", ""}