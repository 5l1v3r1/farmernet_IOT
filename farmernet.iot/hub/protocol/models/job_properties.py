# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobProperties(Model):
    """JobProperties.

    :param job_id: The unique identifier of the job.
    :type job_id: str
    :param start_time_utc: System generated. Ignored at creation. The start
     date and time of the job in UTC.
    :type start_time_utc: datetime
    :param end_time_utc: System generated. Ignored at creation. The end date
     and time of the job in UTC.
    :type end_time_utc: datetime
    :param type: The job type. Possible values include: 'unknown', 'export',
     'import', 'backup', 'readDeviceProperties', 'writeDeviceProperties',
     'updateDeviceConfiguration', 'rebootDevice', 'factoryResetDevice',
     'firmwareUpdate', 'scheduleDeviceMethod', 'scheduleUpdateTwin',
     'restoreFromBackup', 'failoverDataCopy'
    :type type: str or ~protocol.models.enum
    :param status: System generated. Ignored at creation. The status of the
     job. Possible values include: 'unknown', 'enqueued', 'running',
     'completed', 'failed', 'cancelled', 'scheduled', 'queued'
    :type status: str or ~protocol.models.enum
    :param progress: System generated. Ignored at creation. The percentage of
     job completion.
    :type progress: int
    :param input_blob_container_uri: The URI containing SAS token to a blob
     container that contains registry data to sync.
    :type input_blob_container_uri: str
    :param input_blob_name: The blob name to use when importing from the input
     blob container.
    :type input_blob_name: str
    :param output_blob_container_uri: The SAS token to access the blob
     container. This is used to output the status and results of the job.
    :type output_blob_container_uri: str
    :param output_blob_name: The blob name that will be created in the output
     blob container. This blob will contain the exported device registry
     information for the IoT Hub.
    :type output_blob_name: str
    :param exclude_keys_in_export: Optional for export jobs; ignored for other
     jobs. If not specified, the service defaults to false. If false,
     authorization keys are included in export output. Keys are exported as
     null otherwise.
    :type exclude_keys_in_export: bool
    :param storage_authentication_type: The authentication type used for
     connecting to the storage account. Possible values include: 'keyBased',
     'identityBased'
    :type storage_authentication_type: str or ~protocol.models.enum
    :param identity:
    :type identity: ~protocol.models.ManagedIdentity
    :param failure_reason: System genereated.  Ignored at creation. The reason
     for failure, if a failure occurred.
    :type failure_reason: str
    :param include_configurations: Defaults to false. If true, then
     configurations are included in the data export/import.
    :type include_configurations: bool
    :param configurations_blob_name: Defaults to configurations.txt. Specifies
     the name of the blob to use when exporting/importing configurations.
    :type configurations_blob_name: str
    """

    _attribute_map = {
        "job_id": {"key": "jobId", "type": "str"},
        "start_time_utc": {"key": "startTimeUtc", "type": "iso-8601"},
        "end_time_utc": {"key": "endTimeUtc", "type": "iso-8601"},
        "type": {"key": "type", "type": "str"},
        "status": {"key": "status", "type": "str"},
        "progress": {"key": "progress", "type": "int"},
        "input_blob_container_uri": {"key": "inputBlobContainerUri", "type": "str"},
        "input_blob_name": {"key": "inputBlobName", "type": "str"},
        "output_blob_container_uri": {"key": "outputBlobContainerUri", "type": "str"},
        "output_blob_name": {"key": "outputBlobName", "type": "str"},
        "exclude_keys_in_export": {"key": "excludeKeysInExport", "type": "bool"},
        "storage_authentication_type": {"key": "storageAuthenticationType", "type": "str"},
        "identity": {"key": "identity", "type": "ManagedIdentity"},
        "failure_reason": {"key": "failureReason", "type": "str"},
        "include_configurations": {"key": "includeConfigurations", "type": "bool"},
        "configurations_blob_name": {"key": "configurationsBlobName", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(JobProperties, self).__init__(**kwargs)
        self.job_id = kwargs.get("job_id", None)
        self.start_time_utc = kwargs.get("start_time_utc", None)
        self.end_time_utc = kwargs.get("end_time_utc", None)
        self.type = kwargs.get("type", None)
        self.status = kwargs.get("status", None)
        self.progress = kwargs.get("progress", None)
        self.input_blob_container_uri = kwargs.get("input_blob_container_uri", None)
        self.input_blob_name = kwargs.get("input_blob_name", None)
        self.output_blob_container_uri = kwargs.get("output_blob_container_uri", None)
        self.output_blob_name = kwargs.get("output_blob_name", None)
        self.exclude_keys_in_export = kwargs.get("exclude_keys_in_export", None)
        self.storage_authentication_type = kwargs.get("storage_authentication_type", None)
        self.identity = kwargs.get("identity", None)
        self.failure_reason = kwargs.get("failure_reason", None)
        self.include_configurations = kwargs.get("include_configurations", None)
        self.configurations_blob_name = kwargs.get("configurations_blob_name", None)