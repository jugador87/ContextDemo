# This static class defines all the variables that constitute the context space
class ContextSpace:
    # This variable provides a mapping of all available context NAMES
    # to their associated range of VALUES (currently discrete)
    contextPropertyNames = {}


contextPropertyNames['rawLoudness'] = [-36, 0]
# TODO: find a reference that gives a range.
contextPropertyNames['processedLoudness'] = ['silence', 'quiet', 'medium', 'loud']
# These are non-mutually-exclusive
# TODO: some (relatively) simple algorithm for processing this - to be integrated into processAudio.py
contextPropertyNames['perceivedAudio'] = ['silence',
                                          'talking',
                                          'intermittent',
                                          'constant',
                                          'foreground',
                                          'background']

