# Copyright (c) 2014 Dark Secret Software Inc.
# Copyright (c) 2015 Rackspace
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import daemon
import logging
from logging.config import fileConfig


logger = logging.getLogger(__name__)


from winchester.config import ConfigManager
from winchester.pipeline_manager import PipelineManager
from winchester import time_sync


def main():
    parser = argparse.ArgumentParser(description="Winchester pipeline worker")
    parser.add_argument('--config', '-c', default='winchester.yaml',
                        help='The name of the winchester config file')
    parser.add_argument('--name', '-n', default='pipeline_worker',
                        help='The name of this process for logging purposes')
    parser.add_argument('--daemon', '-d', help='Run in daemon mode.')
    args = parser.parse_args()

    conf = ConfigManager.load_config_file(args.config)
    proc_name = args.name

    if 'log_level' in conf:
        level = conf['log_level']
        level = getattr(logging, level.upper())
    else:
        level = logging.INFO

    if 'log_file' in conf:
        log_file = conf['log_file'] % dict(proc_name=proc_name)
    else:
        log_file = '%(proc_name)s.log' % dict(proc_name=proc_name)

    # This is a hack, but it's needed to pass the logfile name & default
    # loglevel into log handlers configured with a config file. (mdragon)
    logging.LOCAL_LOG_FILE = log_file
    logging.LOCAL_DEFAULT_LEVEL = level

    if 'logging_config' in conf:
        fileConfig(conf['logging_config'])
    else:
        logging.basicConfig()
        logging.getLogger('winchester').setLevel(level)
    timesync = time_sync.TimeSync(conf)
    pipe = PipelineManager(conf, time_sync=timesync, proc_name=proc_name)
    if args.daemon:
        print("Backgrounding for daemon mode.")
        with daemon.DaemonContext():
            pipe.run()
    else:
        pipe.run()


if __name__ == '__main__':
    main()
