from cloudify import ctx
from cloudify.decorators import workflow
from cloudify.workflows import ctx as workflow_ctx

from cloudify.decorators import operation

@operation
def multiply(input1, input2, target, **kwargs):
    ctx.logger.info('input1={0}, input2={1}'.format(input1, input2))
    ctx.instance.runtime_properties[target] = input1 * input2

@operation
def log(input, **kwargs):
    ctx.logger.info('input={0}'.format(input))


def copy_property(prop_target, prop_source , **kwargs ):
    ctx.source.instance.runtime_properties[prop_source] = ctx.target.instance.runtime_properties[prop_target]


@workflow
def solution(parameter, **kwargs):
    ctx = workflow_ctx
    ctx.logger.info("Starting Custom Workflow, Parameter {0}" . format(parameter))
