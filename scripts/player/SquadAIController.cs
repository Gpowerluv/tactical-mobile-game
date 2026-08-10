using System.Collections.Generic;
using UnityEngine;

public enum NodeState
{
    Running,
    Success,
    Failure
}

public abstract class BTNode
{
    public abstract NodeState Evaluate();
}

public class Selector : BTNode
{
    protected List<BTNode> nodes = new List<BTNode>();

    public Selector(List<BTNode> nodes) => this.nodes = nodes;

    public override NodeState Evaluate()
    {
        foreach (var node in nodes)
        {
            switch (node.Evaluate())
            {
                case NodeState.Running:
                    return NodeState.Running;
                case NodeState.Success:
                    return NodeState.Success;
                case NodeState.Failure:
                    continue;
            }
        }
        return NodeState.Failure;
    }
}

public class Sequence : BTNode
{
    protected List<BTNode> nodes = new List<BTNode>();

    public Sequence(List<BTNode> nodes) => this.nodes = nodes;

    public override NodeState Evaluate()
    {
        foreach (var node in nodes)
        {
            switch (node.Evaluate())
            {
                case NodeState.Running:
                    return NodeState.Running;
                case NodeState.Success:
                    continue;
                case NodeState.Failure:
                    return NodeState.Failure;
            }
        }
        return NodeState.Success;
    }
}

public class CheckLineOfSight : BTNode
{
    private Transform agentTransform;
    private Transform targetTransform;
    private float viewDistance;

    public CheckLineOfSight(Transform agent, Transform target, float distance)
    {
        agentTransform = agent;
        targetTransform = target;
        viewDistance = distance;
    }

    public override NodeState Evaluate()
    {
        if (targetTransform == null) return NodeState.Failure;

        float distance = Vector3.Distance(agentTransform.position, targetTransform.position);
        if (distance <= viewDistance)
        {
            Vector3 directionToTarget = (targetTransform.position - agentTransform.position).normalized;
            if (Physics.Raycast(agentTransform.position + Vector3.up, directionToTarget, out RaycastHit hit, viewDistance))
            {
                if (hit.transform == targetTransform)
                {
                    return NodeState.Success;
                }
            }
        }
        return NodeState.Failure;
    }
}
