# Copyright 2019 The Kubeflow Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import kfp
import kfp.dsl as dsl


@dsl.pipeline(name='Test adding pod env', description='Test adding pod env')
def test_add_pod_env():
    op = dsl.ContainerOp(
        name='echo',
        image='library/bash',
        command=['sh', '-c'],
        arguments=['echo $KFP_POD_NAME']).add_pod_label('add-pod-env', 'true')


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(test_add_pod_env, __file__ + '.yaml')
