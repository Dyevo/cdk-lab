import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_lab.cdk_lab_stack import CdkLabStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_lab/cdk_lab_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkLabStack(app, "cdk-lab")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })