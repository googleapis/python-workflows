# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateWorkflow
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-workflows


# [START workflows_v1beta_generated_Workflows_CreateWorkflow_sync]
from google.cloud import workflows_v1beta


def sample_create_workflow():
    # Create a client
    client = workflows_v1beta.WorkflowsClient()

    # Initialize request argument(s)
    workflow = workflows_v1beta.Workflow()
    workflow.source_contents = "source_contents_value"

    request = workflows_v1beta.CreateWorkflowRequest(
        parent="parent_value",
        workflow=workflow,
        workflow_id="workflow_id_value",
    )

    # Make the request
    operation = client.create_workflow(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END workflows_v1beta_generated_Workflows_CreateWorkflow_sync]