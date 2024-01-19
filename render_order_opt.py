import random

class YourClass:
    PROBABILITY_TO_KEEP_A_NON_REQUIRED_LEAF = 75  # Adjust the probability as needed

    def setValueToLeaves(self):
        # Assign values to leaves and remove random non-mandatory leaves
        leaves = self.editableOperation.getLeaves()

        requiredLeaves = []
        nonRequiredLeaves = []

        # Split the leaves into required and non-required
        for leaf in leaves:
            if leaf.isRequired():
                requiredLeaves.append(leaf)
            else:
                nonRequiredLeaves.append(leaf)

        # Render the required leaves first
        for leaf in requiredLeaves:
            leaf.setValue(self.parameterValueProvider.provideValueFor(leaf))

        # Render the non-required leaves with a lower probability
        for leaf in nonRequiredLeaves:
            if random.randint(0, 99) < self.PROBABILITY_TO_KEEP_A_NON_REQUIRED_LEAF:
                leaf.setValue(self.parameterValueProvider.provideValueFor(leaf))
