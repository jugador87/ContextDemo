
# This class defines the context object for a particular entity based on XCML
class ContextObject:

    def __init__(self):
        # This must consist of properties found in
        # ContextSpace.contextPropertyNames
        # Corresponds to S
        self.contextSpace = []

        # This is the current context for this entity: a mapping of each context
        # in self.contextSpace to its value. Querying this at any given time
        # should give you the current context. Not all elements may be filled.
        self.context = {}

        # This is the list of context names that are currently deemed relevant
        # to this entity/application
        self.dimension = []
        
