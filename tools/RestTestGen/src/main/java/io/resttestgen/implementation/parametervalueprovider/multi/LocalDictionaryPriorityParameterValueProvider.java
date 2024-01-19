package io.resttestgen.implementation.parametervalueprovider.multi;

import io.resttestgen.core.datatype.parameter.ParameterLeaf;
import io.resttestgen.core.dictionary.Dictionary;
import io.resttestgen.core.testing.parametervalueprovider.ParameterValueProvider;
import io.resttestgen.implementation.parametervalueprovider.single.*;

/**
 * This parameter value provider prioritize the usage of values available in the local dictionary
 */
@SuppressWarnings("unused")
public class LocalDictionaryPriorityParameterValueProvider extends ParameterValueProvider {

    private Dictionary localDictionary;

    @Override
    public Object provideValueFor(ParameterLeaf parameterLeaf) {

        // If local dictionary is available
        if (localDictionary != null) {

            // Try to get value from normalized dictionary
            NormalizedDictionaryParameterValueProvider localNormalizedDictionaryProvider =
                    new NormalizedDictionaryParameterValueProvider();
            localNormalizedDictionaryProvider.setDictionary(localDictionary);
            localNormalizedDictionaryProvider.setStrict(this.strict);
            if (localNormalizedDictionaryProvider.countAvailableValuesFor(parameterLeaf) > 0) {
                return localNormalizedDictionaryProvider.provideValueFor(parameterLeaf);
            }

            // Otherwise, try to get value from non-normalized dictionary
            DictionaryParameterValueProvider localDictionaryProvider = new DictionaryParameterValueProvider();
            localDictionaryProvider.setDictionary(localDictionary);
            localDictionaryProvider.setStrict(this.strict);
            if (localDictionaryProvider.countAvailableValuesFor(parameterLeaf) > 0) {
                return localDictionaryProvider.provideValueFor(parameterLeaf);
            }
        }

        // If local dictionary is not available, try other strategies (e.g., enum, example, default)
        EnumParameterValueProvider enumProvider = new EnumParameterValueProvider();
        enumProvider.setStrict(this.strict);
        if (enumProvider.countAvailableValuesFor(parameterLeaf) > 0) {
            return enumProvider.provideValueFor(parameterLeaf);
        }
        ExamplesParameterValueProvider examplesProvider = new ExamplesParameterValueProvider();
        examplesProvider.setStrict(this.strict);
        if (examplesProvider.countAvailableValuesFor(parameterLeaf) > 0) {
            return examplesProvider.provideValueFor(parameterLeaf);
        }
        DefaultParameterValueProvider defaultProvider = new DefaultParameterValueProvider();
        defaultProvider.setStrict(this.strict);
        if (defaultProvider.countAvailableValuesFor(parameterLeaf) > 0) {
            return defaultProvider.provideValueFor(parameterLeaf);
        }

        // If no other value is available, randomly generate it
        RandomParameterValueProvider randomProvider = new RandomParameterValueProvider();
        randomProvider.setStrict(this.strict);
        return randomProvider.provideValueFor(parameterLeaf);
    }

    /**
     * Set the local dictionary to use.
     * @param localDictionary the local dictionary to use.
     */
    public void setLocalDictionary(Dictionary localDictionary) {
        this.localDictionary = localDictionary;
    }
}
