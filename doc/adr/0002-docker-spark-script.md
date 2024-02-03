# 2. Docker spark scripts

Date: 2024-02-01

## Status

Accepted

## Context
Knowingly that spark is used in the project. Has been decided as the data service to build the docker on.
Now the encapsulation of the DevOps/CICD layer has been introduced, the communications between the runtime 
and base code are to be consider alongside with the local hosts. 

The consideration is to make it as shareable as possible

## Decision
To allow flexibility on the next iterations and incremental size of the base-code & modules, the decision
is to make a plug-n-play solution that shows PySpark capacities. 

## Consequences
We will have a framework of Spark cluster on docker strategy. Allowing input / run-time scripts / output to be configurable.
