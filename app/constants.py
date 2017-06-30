MSG = {
    # Success Messages
    'REGISTERATION_DONE'            : 'Registeration has been done successfully!',
    'LOGIN_DONE'                    : 'Login successful for ',
    'LOGOUT_DONE'                   : 'Logout done successfully!',
    'PATIENT_ADDED'                 : 'Patient has been added successfully!',
    'PATIENT_PROFILE_UPDATE_DONE'   : 'Patient has been updated successfully!',
    'PATIENT_PROFILE_DELET_DONE'    : 'Patient profile has been delete successfully!',
    'USER_PROFILE_CREATED'          : 'User profile has been created successfully!',
    'USER_PROFILE_EDIT_DONE'        : 'User profile has been edited successfully!',
    'USER_PASSWORD_CHANGE_DONE'     : 'Password has been changed successfully!',
    'USER_PROFILE_DELETE_DONE'      : 'User profile has been deleted successfully!',

    # CBC Analysis Success Messages
    'CBC_ANALYSIS_ADD_DONE'         : 'The CBC Analysis has been added successfully!',
    'CBC_ANALYSIS_EDIT_DONE'        : 'The CBC Analysis has been edited successfully!',
    'CBC_ANALYSIS_DELETE_DONE'      : 'The CBC Analysis has been deleted successfully!',
    'CBC_ANALYSIS_APPROVED'         : 'The CBC Analysis has been approved!',

    # User Login Error Messages
    'NO_SUCH_USER'                  : 'Sorry, but there is no such user in our system.',
    'WRONG_CREDENTIALS'             : 'You provided wrong credentials, please try again.',
    'NO_LOGIN'                      : 'Please login first',

    # User Registeration Error Messages
    'DUPLICATE_USER'                : 'This user is already registered.',
    'REGISTERATION_FAILED'          : 'Registeration has been failed.',

    # Other User Error Messages
    'USER_DELETE_DENIED'            : 'This can not be deleted.',

    # Patient Error Messages
    'DUPLICATE_PATIENT_ID'          : 'This ID (%s) is already added.',
    'INVALID_PERSONAL_ID'           : 'Please enter a valid personal id.',
    'NO_SUCH_PATIENT'               : 'There is no such patient in the system.',

    # CBC Analyssi Error Messages
    'NO_SUCH_CBC_ANALYSIS'          : 'No such CBC analysis for this patient.',

    # General Error Messages
    'UNEXPECTED_ERROR'              : 'Unexpected error.',
    'NO_DATA_SUBMITTED'             : 'No data has been submitted, please check with admin',
    'OPERATION_FAILED'              : 'Operation failed.',
    '403'                           : 'You are not authorized to access this page.',
}

PER_PAGE = {
    'USERS' : 10,
    'PATIENTS' : 10,
}

ANALYSIS_TO_ID = {
    'cbc'   : 1,
}
