package io.resttestgen.implementation.responseprocessor;

import io.resttestgen.core.Environment;
import io.resttestgen.core.datatype.parameter.ParameterLeaf;
import io.resttestgen.core.datatype.parameter.StructuredParameterElement;
import io.resttestgen.core.operationdependencygraph.DependencyEdge;
import io.resttestgen.core.operationdependencygraph.OperationDependencyGraph;
import io.resttestgen.core.testing.ResponseProcessor;
import io.resttestgen.core.testing.TestInteraction;

import java.util.List;
import java.util.stream.Collectors;

public class GraphResponseProcessor extends ResponseProcessor {

    final OperationDependencyGraph operationDependencyGraph = Environment.getInstance().getOperationDependencyGraph();

    @Override
    public void process(TestInteraction testInteraction) {

        // If the obtained status code is successful, set the operation as tested in the graph
        if (testInteraction.getResponseStatusCode().isSuccessful()) {
            operationDependencyGraph.setOperationAsTested(testInteraction.getOperation());
        }

        StructuredParameterElement responseBody = testInteraction.getOperation().getResponseBody();

        // If the parsed response body is null, try to parse it
        if (responseBody == null) {
            JsonParserResponseProcessor jsonParserResponseProcessor = new JsonParserResponseProcessor();
            jsonParserResponseProcessor.process(testInteraction);
            responseBody = testInteraction.getOperation().getResponseBody();
        }

        // If the response body is still null, terminate the processing of the response
        if (responseBody == null) {
            return;
        }

        // Iterate on leaves to update the graph
        for (ParameterLeaf leaf : responseBody.getLeaves()) {
            List<DependencyEdge> satisfiedEdges = operationDependencyGraph.getGraph().edgeSet().stream()
                    .filter(edge -> edge.getNormalizedName().equals(leaf.getNormalizedName())).collect(Collectors.toList());
            for (DependencyEdge satisfiedEdge : satisfiedEdges) {
                satisfiedEdge.setAsSatisfied();
            }
        }
    }
}
