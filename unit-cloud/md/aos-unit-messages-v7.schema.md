# AosUnitMessageV7

- [![Required](https://img.shields.io/badge/Required-blue) Property `AosUnitMessageV7 > header`](#header)
  - [![Required](https://img.shields.io/badge/Required-blue) Property `AosUnitMessageV7 > header > version`](#header_version)
  - [![Required](https://img.shields.io/badge/Required-blue) Property `AosUnitMessageV7 > header > systemId`](#header_systemId)
- [![Required](https://img.shields.io/badge/Required-blue) Property `AosUnitMessageV7 > data`](#data)
  - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts`](#data_oneOf_i0)
    - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > messageType`](#data_oneOf_i0_messageType)
    - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items`](#data_oneOf_i0_items)
      - [AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items](#data_oneOf_i0_items_items)
        - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertCore`](#data_oneOf_i0_items_items_oneOf_i0)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertCore > timestamp`](#data_oneOf_i0_items_items_oneOf_i0_timestamp)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertCore > tag`](#data_oneOf_i0_items_items_oneOf_i0_tag)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertCore > nodeId`](#data_oneOf_i0_items_items_oneOf_i0_nodeId)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertCore > coreComponent`](#data_oneOf_i0_items_items_oneOf_i0_coreComponent)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertCore > message`](#data_oneOf_i0_items_items_oneOf_i0_message)
        - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate`](#data_oneOf_i0_items_items_oneOf_i1)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > timestamp`](#data_oneOf_i0_items_items_oneOf_i1_timestamp)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > tag`](#data_oneOf_i0_items_items_oneOf_i1_tag)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > serviceId`](#data_oneOf_i0_items_items_oneOf_i1_serviceId)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > subjectId`](#data_oneOf_i0_items_items_oneOf_i1_subjectId)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > instance`](#data_oneOf_i0_items_items_oneOf_i1_instance)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > nodeId`](#data_oneOf_i0_items_items_oneOf_i1_nodeId)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > deviceId`](#data_oneOf_i0_items_items_oneOf_i1_deviceId)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > message`](#data_oneOf_i0_items_items_oneOf_i1_message)
        - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress`](#data_oneOf_i0_items_items_oneOf_i2)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > timestamp`](#data_oneOf_i0_items_items_oneOf_i2_timestamp)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > tag`](#data_oneOf_i0_items_items_oneOf_i2_tag)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > targetType`](#data_oneOf_i0_items_items_oneOf_i2_targetType)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > targetId`](#data_oneOf_i0_items_items_oneOf_i2_targetId)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > version`](#data_oneOf_i0_items_items_oneOf_i2_version)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > message`](#data_oneOf_i0_items_items_oneOf_i2_message)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > url`](#data_oneOf_i0_items_items_oneOf_i2_url)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > downloadedBytes`](#data_oneOf_i0_items_items_oneOf_i2_downloadedBytes)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > totalBytes`](#data_oneOf_i0_items_items_oneOf_i2_totalBytes)
        - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota`](#data_oneOf_i0_items_items_oneOf_i3)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota > timestamp`](#data_oneOf_i0_items_items_oneOf_i3_timestamp)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota > tag`](#data_oneOf_i0_items_items_oneOf_i3_tag)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota > serviceId`](#data_oneOf_i0_items_items_oneOf_i3_serviceId)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota > subjectId`](#data_oneOf_i0_items_items_oneOf_i3_subjectId)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota > instance`](#data_oneOf_i0_items_items_oneOf_i3_instance)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota > parameter`](#data_oneOf_i0_items_items_oneOf_i3_parameter)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota > value`](#data_oneOf_i0_items_items_oneOf_i3_value)
        - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance`](#data_oneOf_i0_items_items_oneOf_i4)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance > timestamp`](#data_oneOf_i0_items_items_oneOf_i4_timestamp)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance > tag`](#data_oneOf_i0_items_items_oneOf_i4_tag)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance > serviceId`](#data_oneOf_i0_items_items_oneOf_i4_serviceId)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance > subjectId`](#data_oneOf_i0_items_items_oneOf_i4_subjectId)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance > instance`](#data_oneOf_i0_items_items_oneOf_i4_instance)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance > version`](#data_oneOf_i0_items_items_oneOf_i4_version)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance > message`](#data_oneOf_i0_items_items_oneOf_i4_message)
        - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemError`](#data_oneOf_i0_items_items_oneOf_i5)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemError > timestamp`](#data_oneOf_i0_items_items_oneOf_i5_timestamp)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemError > tag`](#data_oneOf_i0_items_items_oneOf_i5_tag)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemError > nodeId`](#data_oneOf_i0_items_items_oneOf_i5_nodeId)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemError > message`](#data_oneOf_i0_items_items_oneOf_i5_message)
        - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemQuota`](#data_oneOf_i0_items_items_oneOf_i6)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemQuota > timestamp`](#data_oneOf_i0_items_items_oneOf_i6_timestamp)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemQuota > tag`](#data_oneOf_i0_items_items_oneOf_i6_tag)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemQuota > nodeId`](#data_oneOf_i0_items_items_oneOf_i6_nodeId)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemQuota > parameter`](#data_oneOf_i0_items_items_oneOf_i6_parameter)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemQuota > value`](#data_oneOf_i0_items_items_oneOf_i6_value)
        - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate`](#data_oneOf_i0_items_items_oneOf_i7)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > timestamp`](#data_oneOf_i0_items_items_oneOf_i7_timestamp)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > tag`](#data_oneOf_i0_items_items_oneOf_i7_tag)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > nodeId`](#data_oneOf_i0_items_items_oneOf_i7_nodeId)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > name`](#data_oneOf_i0_items_items_oneOf_i7_name)
          - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > errors`](#data_oneOf_i0_items_items_oneOf_i7_errors)
            - [AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > errors > AosErrorInfo](#data_oneOf_i0_items_items_oneOf_i7_errors_items)
              - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > errors > AosErrorInfo > aosCode`](#data_oneOf_i0_items_items_oneOf_i7_errors_items_aosCode)
              - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > errors > AosErrorInfo > exitCode`](#data_oneOf_i0_items_items_oneOf_i7_errors_items_exitCode)
              - [Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > errors > AosErrorInfo > message`](#data_oneOf_i0_items_items_oneOf_i7_errors_items_message)
  - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7`](#data_oneOf_i1)
    - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > messageType`](#data_oneOf_i1_messageType)
    - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > nodes`](#data_oneOf_i1_nodes)
      - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > nodes > AosNodeDesiredState](#data_oneOf_i1_nodes_items)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > nodes > AosNodeDesiredState > nodeId`](#data_oneOf_i1_nodes_items_nodeId)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > nodes > AosNodeDesiredState > status`](#data_oneOf_i1_nodes_items_status)
    - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig`](#data_oneOf_i1_unitConfig)
      - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > version`](#data_oneOf_i1_unitConfig_version)
      - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > formatVersion`](#data_oneOf_i1_unitConfig_formatVersion)
      - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes`](#data_oneOf_i1_unitConfig_nodes)
        - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig](#data_oneOf_i1_unitConfig_nodes_items)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > nodeType`](#data_oneOf_i1_unitConfig_nodes_items_nodeType)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > nodeId`](#data_oneOf_i1_unitConfig_nodes_items_nodeId)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules`](#data_oneOf_i1_unitConfig_nodes_items_alertRules)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > cpu`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > cpu > minThreshold`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_minThreshold)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > cpu > maxThreshold`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_maxThreshold)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > cpu > minTimeout`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_minTimeout)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > ram`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_ram)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > cpu > minThreshold`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_minThreshold)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > cpu > maxThreshold`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_maxThreshold)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > cpu > minTimeout`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_minTimeout)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0)
                - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items)
                  - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > minThreshold`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items_minThreshold)
                  - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > maxThreshold`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items_maxThreshold)
                  - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > minTimeout`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items_minTimeout)
                  - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > name`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items_name)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 1`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i1)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > download`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_download)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > download > minThreshold`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_download_minThreshold)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > download > maxThreshold`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_download_maxThreshold)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > download > minTimeout`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_download_minTimeout)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > upload`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_upload)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > download > minThreshold`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_download_minThreshold)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > download > maxThreshold`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_download_maxThreshold)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > download > minTimeout`](#data_oneOf_i1_unitConfig_nodes_items_alertRules_download_minTimeout)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resourceRatios`](#data_oneOf_i1_unitConfig_nodes_items_resourceRatios)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resourceRatios > cpu`](#data_oneOf_i1_unitConfig_nodes_items_resourceRatios_cpu)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resourceRatios > ram`](#data_oneOf_i1_unitConfig_nodes_items_resourceRatios_ram)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resourceRatios > storage`](#data_oneOf_i1_unitConfig_nodes_items_resourceRatios_storage)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resourceRatios > state`](#data_oneOf_i1_unitConfig_nodes_items_resourceRatios_state)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices`](#data_oneOf_i1_unitConfig_nodes_items_devices)
            - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices > AosDeviceInfo](#data_oneOf_i1_unitConfig_nodes_items_devices_items)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices > AosDeviceInfo > name`](#data_oneOf_i1_unitConfig_nodes_items_devices_items_name)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices > AosDeviceInfo > hostDevices`](#data_oneOf_i1_unitConfig_nodes_items_devices_items_hostDevices)
                - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices > AosDeviceInfo > hostDevices > hostDevices items](#data_oneOf_i1_unitConfig_nodes_items_devices_items_hostDevices_items)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices > AosDeviceInfo > sharedCount`](#data_oneOf_i1_unitConfig_nodes_items_devices_items_sharedCount)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices > AosDeviceInfo > groups`](#data_oneOf_i1_unitConfig_nodes_items_devices_items_groups)
                - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices > AosDeviceInfo > groups > groups items](#data_oneOf_i1_unitConfig_nodes_items_devices_items_groups_items)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources`](#data_oneOf_i1_unitConfig_nodes_items_resources)
            - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo](#data_oneOf_i1_unitConfig_nodes_items_resources_items)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > name`](#data_oneOf_i1_unitConfig_nodes_items_resources_items_name)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > groups`](#data_oneOf_i1_unitConfig_nodes_items_resources_items_groups)
                - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > groups > groups items](#data_oneOf_i1_unitConfig_nodes_items_resources_items_groups_items)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts`](#data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts)
                - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount](#data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items)
                  - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > destination`](#data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_destination)
                  - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > source`](#data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_source)
                  - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > type`](#data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_type)
                  - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > options`](#data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_options)
                    - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > options > options items](#data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_options_items)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > envs`](#data_oneOf_i1_unitConfig_nodes_items_resources_items_envs)
                - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > envs > envs items](#data_oneOf_i1_unitConfig_nodes_items_resources_items_envs_items)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts`](#data_oneOf_i1_unitConfig_nodes_items_resources_items_hosts)
                - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts > AosHostRecord](#data_oneOf_i1_unitConfig_nodes_items_resources_items_hosts_items)
                  - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts > AosHostRecord > ip`](#data_oneOf_i1_unitConfig_nodes_items_resources_items_hosts_items_ip)
                  - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts > AosHostRecord > hostname`](#data_oneOf_i1_unitConfig_nodes_items_resources_items_hosts_items_hostname)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > labels`](#data_oneOf_i1_unitConfig_nodes_items_labels)
            - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > labels > labels items](#data_oneOf_i1_unitConfig_nodes_items_labels_items)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > priority`](#data_oneOf_i1_unitConfig_nodes_items_priority)
    - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems`](#data_oneOf_i1_updateItems)
      - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo](#data_oneOf_i1_updateItems_items)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier`](#data_oneOf_i1_updateItems_items_identifier)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > id`](#data_oneOf_i1_updateItems_items_identifier_id)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > id > anyOf > item 0`](#data_oneOf_i1_updateItems_items_identifier_id_anyOf_i0)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > id > anyOf > item 1`](#data_oneOf_i1_updateItems_items_identifier_id_anyOf_i1)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > type`](#data_oneOf_i1_updateItems_items_identifier_type)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > type > anyOf > item 0`](#data_oneOf_i1_updateItems_items_identifier_type_anyOf_i0)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > type > anyOf > item 1`](#data_oneOf_i1_updateItems_items_identifier_type_anyOf_i1)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > codename`](#data_oneOf_i1_updateItems_items_identifier_codename)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > codename > anyOf > item 0`](#data_oneOf_i1_updateItems_items_identifier_codename_anyOf_i0)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > codename > anyOf > item 1`](#data_oneOf_i1_updateItems_items_identifier_codename_anyOf_i1)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > title`](#data_oneOf_i1_updateItems_items_identifier_title)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > title > anyOf > item 0`](#data_oneOf_i1_updateItems_items_identifier_title_anyOf_i0)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > title > anyOf > item 1`](#data_oneOf_i1_updateItems_items_identifier_title_anyOf_i1)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > description`](#data_oneOf_i1_updateItems_items_identifier_description)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > description > anyOf > item 0`](#data_oneOf_i1_updateItems_items_identifier_description_anyOf_i0)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > description > anyOf > item 1`](#data_oneOf_i1_updateItems_items_identifier_description_anyOf_i1)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > urn`](#data_oneOf_i1_updateItems_items_identifier_urn)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > urn > anyOf > item 0`](#data_oneOf_i1_updateItems_items_identifier_urn_anyOf_i0)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > urn > anyOf > item 1`](#data_oneOf_i1_updateItems_items_identifier_urn_anyOf_i1)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > version`](#data_oneOf_i1_updateItems_items_version)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > urls`](#data_oneOf_i1_updateItems_items_urls)
          - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > urls > urls items](#data_oneOf_i1_updateItems_items_urls_items)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > sha256`](#data_oneOf_i1_updateItems_items_sha256)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > size`](#data_oneOf_i1_updateItems_items_size)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo`](#data_oneOf_i1_updateItems_items_decryptionInfo)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo > blockAlg`](#data_oneOf_i1_updateItems_items_decryptionInfo_blockAlg)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo > blockIv`](#data_oneOf_i1_updateItems_items_decryptionInfo_blockIv)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo > blockKey`](#data_oneOf_i1_updateItems_items_decryptionInfo_blockKey)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo > asymAlg`](#data_oneOf_i1_updateItems_items_decryptionInfo_asymAlg)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo > receiverInfo`](#data_oneOf_i1_updateItems_items_decryptionInfo_receiverInfo)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo > receiverInfo > serial`](#data_oneOf_i1_updateItems_items_decryptionInfo_receiverInfo_serial)
            - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo > receiverInfo > issuer`](#data_oneOf_i1_updateItems_items_decryptionInfo_receiverInfo_issuer)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > signs`](#data_oneOf_i1_updateItems_items_signs)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > signs > chainName`](#data_oneOf_i1_updateItems_items_signs_chainName)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > signs > alg`](#data_oneOf_i1_updateItems_items_signs_alg)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > signs > value`](#data_oneOf_i1_updateItems_items_signs_value)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > signs > trustedTimestamp`](#data_oneOf_i1_updateItems_items_signs_trustedTimestamp)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > signs > ocspValues`](#data_oneOf_i1_updateItems_items_signs_ocspValues)
            - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > signs > ocspValues > ocspValues items](#data_oneOf_i1_updateItems_items_signs_ocspValues_items)
    - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances`](#data_oneOf_i1_instances)
      - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances > AosDesiredInstanceInfo](#data_oneOf_i1_instances_items)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances > AosDesiredInstanceInfo > update_item`](#data_oneOf_i1_instances_items_update_item)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances > AosDesiredInstanceInfo > subject`](#data_oneOf_i1_instances_items_subject)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances > AosDesiredInstanceInfo > priority`](#data_oneOf_i1_instances_items_priority)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances > AosDesiredInstanceInfo > numInstances`](#data_oneOf_i1_instances_items_numInstances)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances > AosDesiredInstanceInfo > labels`](#data_oneOf_i1_instances_items_labels)
          - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances > AosDesiredInstanceInfo > labels > labels items](#data_oneOf_i1_instances_items_labels_items)
    - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule`](#data_oneOf_i1_fotaSchedule)
      - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > ttl`](#data_oneOf_i1_fotaSchedule_ttl)
      - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > type`](#data_oneOf_i1_fotaSchedule_type)
      - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable`](#data_oneOf_i1_fotaSchedule_timetable)
        - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem](#data_oneOf_i1_fotaSchedule_timetable_items)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > dayOfWeek`](#data_oneOf_i1_fotaSchedule_timetable_items_dayOfWeek)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots`](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots)
            - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots > AosTimeSlot](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots > AosTimeSlot > start`](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items_start)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots > AosTimeSlot > end`](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items_end)
    - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > sotaSchedule`](#data_oneOf_i1_sotaSchedule)
      - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > ttl`](#data_oneOf_i1_fotaSchedule_ttl)
      - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > type`](#data_oneOf_i1_fotaSchedule_type)
      - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable`](#data_oneOf_i1_fotaSchedule_timetable)
        - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem](#data_oneOf_i1_fotaSchedule_timetable_items)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > dayOfWeek`](#data_oneOf_i1_fotaSchedule_timetable_items_dayOfWeek)
          - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots`](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots)
            - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots > AosTimeSlot](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots > AosTimeSlot > start`](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items_start)
              - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots > AosTimeSlot > end`](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items_end)
    - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificates`](#data_oneOf_i1_certificates)
      - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificates > AosCertificateInfo](#data_oneOf_i1_certificates_items)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificates > AosCertificateInfo > certificate`](#data_oneOf_i1_certificates_items_certificate)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificates > AosCertificateInfo > fingerprint`](#data_oneOf_i1_certificates_items_fingerprint)
    - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificateChains`](#data_oneOf_i1_certificateChains)
      - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificateChains > AosCertificateChainInfo](#data_oneOf_i1_certificateChains_items)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificateChains > AosCertificateChainInfo > name`](#data_oneOf_i1_certificateChains_items_name)
        - [Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificateChains > AosCertificateChainInfo > fingerprints`](#data_oneOf_i1_certificateChains_items_fingerprints)
          - [AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificateChains > AosCertificateChainInfo > fingerprints > fingerprints items](#data_oneOf_i1_certificateChains_items_fingerprints_items)

**Title:** AosUnitMessageV7

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** Unit message model.

| Property             | Pattern | Type        | Deprecated | Definition                 | Title/Description |
| -------------------- | ------- | ----------- | ---------- | -------------------------- | ----------------- |
| + [header](#header ) | No      | object      | No         | In #/$defs/AosUnitHeaderV7 | AosUnitHeaderV7   |
| + [data](#data )     | No      | Combination | No         | -                          | Data              |

## <a name="header"></a>![Required](https://img.shields.io/badge/Required-blue) Property `AosUnitMessageV7 > header`

**Title:** AosUnitHeaderV7

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosUnitHeaderV7                                                     |

**Description:** Aos Unit-Cloud message header

| Property                        | Pattern | Type   | Deprecated | Definition | Title/Description                 |
| ------------------------------- | ------- | ------ | ---------- | ---------- | --------------------------------- |
| + [version](#header_version )   | No      | const  | No         | -          | Protocol version                  |
| + [systemId](#header_systemId ) | No      | string | No         | -          | The unique system ID of the unit. |

### <a name="header_version"></a>![Required](https://img.shields.io/badge/Required-blue) Property `AosUnitMessageV7 > header > version`

**Title:** Protocol version

|          |         |
| -------- | ------- |
| **Type** | `const` |

**Description:** The version of Unit-Cloud protocol.

Specific value: `7`

### <a name="header_systemId"></a>![Required](https://img.shields.io/badge/Required-blue) Property `AosUnitMessageV7 > header > systemId`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The unique system ID of the unit.

## <a name="data"></a>![Required](https://img.shields.io/badge/Required-blue) Property `AosUnitMessageV7 > data`

**Title:** Data

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** message payload

| One of(Option)                       |
| ------------------------------------ |
| [AosAlerts](#data_oneOf_i0)          |
| [AosDesiredStatusV7](#data_oneOf_i1) |

### <a name="data_oneOf_i0"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts`

**Title:** AosAlerts

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlerts                                                           |

| Property                                     | Pattern | Type  | Deprecated | Definition | Title/Description |
| -------------------------------------------- | ------- | ----- | ---------- | ---------- | ----------------- |
| + [messageType](#data_oneOf_i0_messageType ) | No      | const | No         | -          | Messagetype       |
| + [items](#data_oneOf_i0_items )             | No      | array | No         | -          | Items             |

#### <a name="data_oneOf_i0_messageType"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > messageType`

**Title:** Messagetype

|          |         |
| -------- | ------- |
| **Type** | `const` |

**Description:** message body type

Specific value: `"alerts"`

#### <a name="data_oneOf_i0_items"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items`

**Title:** Items

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** List of AosEdge alert items.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [items items](#data_oneOf_i0_items_items) | -           |

##### <a name="data_oneOf_i0_items_items"></a>AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

| One of(Option)                                                  |
| --------------------------------------------------------------- |
| [AosAlertCore](#data_oneOf_i0_items_items_oneOf_i0)             |
| [AosAlertDeviceAllocate](#data_oneOf_i0_items_items_oneOf_i1)   |
| [AosAlertDownloadProgress](#data_oneOf_i0_items_items_oneOf_i2) |
| [AosAlertInstanceQuota](#data_oneOf_i0_items_items_oneOf_i3)    |
| [AosAlertServiceInstance](#data_oneOf_i0_items_items_oneOf_i4)  |
| [AosAlertSystemError](#data_oneOf_i0_items_items_oneOf_i5)      |
| [AosAlertSystemQuota](#data_oneOf_i0_items_items_oneOf_i6)      |
| [AosAlertResourceValidate](#data_oneOf_i0_items_items_oneOf_i7) |

###### <a name="data_oneOf_i0_items_items_oneOf_i0"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertCore`

**Title:** AosAlertCore

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlertCore                                                        |

**Description:** Aos Unit core alert information.

| Property                                                              | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [timestamp](#data_oneOf_i0_items_items_oneOf_i0_timestamp )         | No      | string | No         | -          | Timestamp         |
| + [tag](#data_oneOf_i0_items_items_oneOf_i0_tag )                     | No      | const  | No         | -          | Tag               |
| + [nodeId](#data_oneOf_i0_items_items_oneOf_i0_nodeId )               | No      | string | No         | -          | Node ID           |
| + [coreComponent](#data_oneOf_i0_items_items_oneOf_i0_coreComponent ) | No      | string | No         | -          | Corecomponent     |
| + [message](#data_oneOf_i0_items_items_oneOf_i0_message )             | No      | string | No         | -          | Message           |

###### <a name="data_oneOf_i0_items_items_oneOf_i0_timestamp"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertCore > timestamp`

**Title:** Timestamp

|            |             |
| ---------- | ----------- |
| **Type**   | `string`    |
| **Format** | `date-time` |

**Description:** Timestamp when alert was triggered in ISO8601 format.

###### <a name="data_oneOf_i0_items_items_oneOf_i0_tag"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertCore > tag`

**Title:** Tag

|          |         |
| -------- | ------- |
| **Type** | `const` |

**Description:** Type of the alert.

Specific value: `"coreAlert"`

###### <a name="data_oneOf_i0_items_items_oneOf_i0_nodeId"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertCore > nodeId`

**Title:** Node ID

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Unique ID of the node.

###### <a name="data_oneOf_i0_items_items_oneOf_i0_coreComponent"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertCore > coreComponent`

**Title:** Corecomponent

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Error information retrieved for the alert.

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |
| **Max length** | 100 |

###### <a name="data_oneOf_i0_items_items_oneOf_i0_message"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertCore > message`

**Title:** Message

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Error information retrieved for the alert.

| Restrictions   |       |
| -------------- | ----- |
| **Min length** | 1     |
| **Max length** | 32768 |

###### <a name="data_oneOf_i0_items_items_oneOf_i1"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate`

**Title:** AosAlertDeviceAllocate

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlertDeviceAllocate                                              |

**Description:** Aos Unit device allocation alert information.

| Property                                                      | Pattern | Type    | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| + [timestamp](#data_oneOf_i0_items_items_oneOf_i1_timestamp ) | No      | string  | No         | -          | Timestamp         |
| + [tag](#data_oneOf_i0_items_items_oneOf_i1_tag )             | No      | const   | No         | -          | Tag               |
| + [serviceId](#data_oneOf_i0_items_items_oneOf_i1_serviceId ) | No      | string  | No         | -          | Serviceid         |
| + [subjectId](#data_oneOf_i0_items_items_oneOf_i1_subjectId ) | No      | string  | No         | -          | Subjectid         |
| + [instance](#data_oneOf_i0_items_items_oneOf_i1_instance )   | No      | integer | No         | -          | Instance          |
| + [nodeId](#data_oneOf_i0_items_items_oneOf_i1_nodeId )       | No      | string  | No         | -          | Node ID           |
| + [deviceId](#data_oneOf_i0_items_items_oneOf_i1_deviceId )   | No      | string  | No         | -          | Deviceid          |
| + [message](#data_oneOf_i0_items_items_oneOf_i1_message )     | No      | string  | No         | -          | Message           |

###### <a name="data_oneOf_i0_items_items_oneOf_i1_timestamp"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > timestamp`

**Title:** Timestamp

|            |             |
| ---------- | ----------- |
| **Type**   | `string`    |
| **Format** | `date-time` |

**Description:** Timestamp when alert was triggered in ISO8601 format.

###### <a name="data_oneOf_i0_items_items_oneOf_i1_tag"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > tag`

**Title:** Tag

|          |         |
| -------- | ------- |
| **Type** | `const` |

**Description:** Type of the alert.

Specific value: `"deviceAllocateAlert"`

###### <a name="data_oneOf_i0_items_items_oneOf_i1_serviceId"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > serviceId`

**Title:** Serviceid

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Service unique identifier in form: UUID4.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

###### <a name="data_oneOf_i0_items_items_oneOf_i1_subjectId"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > subjectId`

**Title:** Subjectid

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Subject unique identifier.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

###### <a name="data_oneOf_i0_items_items_oneOf_i1_instance"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > instance`

**Title:** Instance

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** Service instance number (starting from 0).

###### <a name="data_oneOf_i0_items_items_oneOf_i1_nodeId"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > nodeId`

**Title:** Node ID

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Unique ID of the node.

###### <a name="data_oneOf_i0_items_items_oneOf_i1_deviceId"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > deviceId`

**Title:** Deviceid

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Device name on a Unit

###### <a name="data_oneOf_i0_items_items_oneOf_i1_message"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDeviceAllocate > message`

**Title:** Message

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Error information retrieved for the alert.

| Restrictions   |       |
| -------------- | ----- |
| **Min length** | 1     |
| **Max length** | 32768 |

###### <a name="data_oneOf_i0_items_items_oneOf_i2"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress`

**Title:** AosAlertDownloadProgress

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlertDownloadProgress                                            |

**Description:** Aos Unit download alert information.

| Property                                                                  | Pattern | Type             | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [timestamp](#data_oneOf_i0_items_items_oneOf_i2_timestamp )             | No      | string           | No         | -          | Timestamp         |
| + [tag](#data_oneOf_i0_items_items_oneOf_i2_tag )                         | No      | const            | No         | -          | Tag               |
| + [targetType](#data_oneOf_i0_items_items_oneOf_i2_targetType )           | No      | enum (of string) | No         | -          | Targettype        |
| + [targetId](#data_oneOf_i0_items_items_oneOf_i2_targetId )               | No      | string           | No         | -          | Targetid          |
| + [version](#data_oneOf_i0_items_items_oneOf_i2_version )                 | No      | string           | No         | -          | Version           |
| + [message](#data_oneOf_i0_items_items_oneOf_i2_message )                 | No      | string           | No         | -          | Message           |
| + [url](#data_oneOf_i0_items_items_oneOf_i2_url )                         | No      | string           | No         | -          | Url               |
| + [downloadedBytes](#data_oneOf_i0_items_items_oneOf_i2_downloadedBytes ) | No      | integer          | No         | -          | Downloadedbytes   |
| + [totalBytes](#data_oneOf_i0_items_items_oneOf_i2_totalBytes )           | No      | integer          | No         | -          | Totalbytes        |

###### <a name="data_oneOf_i0_items_items_oneOf_i2_timestamp"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > timestamp`

**Title:** Timestamp

|            |             |
| ---------- | ----------- |
| **Type**   | `string`    |
| **Format** | `date-time` |

**Description:** Timestamp when alert was triggered in ISO8601 format.

###### <a name="data_oneOf_i0_items_items_oneOf_i2_tag"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > tag`

**Title:** Tag

|          |         |
| -------- | ------- |
| **Type** | `const` |

**Description:** Type of the alert.

Specific value: `"downloadProgressAlert"`

###### <a name="data_oneOf_i0_items_items_oneOf_i2_targetType"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > targetType`

**Title:** Targettype

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

Must be one of:
* "component"
* "layer"
* "service"

###### <a name="data_oneOf_i0_items_items_oneOf_i2_targetId"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > targetId`

**Title:** Targetid

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="data_oneOf_i0_items_items_oneOf_i2_version"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > version`

**Title:** Version

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Version in format of the SemVer.

###### <a name="data_oneOf_i0_items_items_oneOf_i2_message"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > message`

**Title:** Message

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Error information retrieved for the alert.

| Restrictions   |       |
| -------------- | ----- |
| **Min length** | 1     |
| **Max length** | 32768 |

###### <a name="data_oneOf_i0_items_items_oneOf_i2_url"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > url`

**Title:** Url

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** URL of the downloading file.

###### <a name="data_oneOf_i0_items_items_oneOf_i2_downloadedBytes"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > downloadedBytes`

**Title:** Downloadedbytes

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** Downloaded bytes at the specified moment.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="data_oneOf_i0_items_items_oneOf_i2_totalBytes"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertDownloadProgress > totalBytes`

**Title:** Totalbytes

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** Total size in bytes of the file.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="data_oneOf_i0_items_items_oneOf_i3"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota`

**Title:** AosAlertInstanceQuota

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlertInstanceQuota                                               |

**Description:** Aos Unit instance quota alert information.

| Property                                                      | Pattern | Type    | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| + [timestamp](#data_oneOf_i0_items_items_oneOf_i3_timestamp ) | No      | string  | No         | -          | Timestamp         |
| + [tag](#data_oneOf_i0_items_items_oneOf_i3_tag )             | No      | const   | No         | -          | Tag               |
| + [serviceId](#data_oneOf_i0_items_items_oneOf_i3_serviceId ) | No      | string  | No         | -          | Serviceid         |
| + [subjectId](#data_oneOf_i0_items_items_oneOf_i3_subjectId ) | No      | string  | No         | -          | Subjectid         |
| + [instance](#data_oneOf_i0_items_items_oneOf_i3_instance )   | No      | integer | No         | -          | Instance          |
| + [parameter](#data_oneOf_i0_items_items_oneOf_i3_parameter ) | No      | string  | No         | -          | Parameter         |
| + [value](#data_oneOf_i0_items_items_oneOf_i3_value )         | No      | integer | No         | -          | Value             |

###### <a name="data_oneOf_i0_items_items_oneOf_i3_timestamp"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota > timestamp`

**Title:** Timestamp

|            |             |
| ---------- | ----------- |
| **Type**   | `string`    |
| **Format** | `date-time` |

**Description:** Timestamp when alert was triggered in ISO8601 format.

###### <a name="data_oneOf_i0_items_items_oneOf_i3_tag"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota > tag`

**Title:** Tag

|          |         |
| -------- | ------- |
| **Type** | `const` |

**Description:** Type of the alert.

Specific value: `"instanceQuotaAlert"`

###### <a name="data_oneOf_i0_items_items_oneOf_i3_serviceId"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota > serviceId`

**Title:** Serviceid

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Service unique identifier.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

###### <a name="data_oneOf_i0_items_items_oneOf_i3_subjectId"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota > subjectId`

**Title:** Subjectid

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Subject unique identifier.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

###### <a name="data_oneOf_i0_items_items_oneOf_i3_instance"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota > instance`

**Title:** Instance

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** Instance number (starting from 0).

###### <a name="data_oneOf_i0_items_items_oneOf_i3_parameter"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota > parameter`

**Title:** Parameter

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Parameter name of the system quota.

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |
| **Max length** | 100 |

###### <a name="data_oneOf_i0_items_items_oneOf_i3_value"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertInstanceQuota > value`

**Title:** Value

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** Triggered value of the parameter.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="data_oneOf_i0_items_items_oneOf_i4"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance`

**Title:** AosAlertServiceInstance

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlertServiceInstance                                             |

**Description:** Aos Unit service instance alert information.

| Property                                                      | Pattern | Type    | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| + [timestamp](#data_oneOf_i0_items_items_oneOf_i4_timestamp ) | No      | string  | No         | -          | Timestamp         |
| - [tag](#data_oneOf_i0_items_items_oneOf_i4_tag )             | No      | const   | No         | -          | Tag               |
| + [serviceId](#data_oneOf_i0_items_items_oneOf_i4_serviceId ) | No      | string  | No         | -          | Serviceid         |
| + [subjectId](#data_oneOf_i0_items_items_oneOf_i4_subjectId ) | No      | string  | No         | -          | Subjectid         |
| + [instance](#data_oneOf_i0_items_items_oneOf_i4_instance )   | No      | integer | No         | -          | Instance          |
| + [version](#data_oneOf_i0_items_items_oneOf_i4_version )     | No      | string  | No         | -          | Version           |
| + [message](#data_oneOf_i0_items_items_oneOf_i4_message )     | No      | string  | No         | -          | Message           |

###### <a name="data_oneOf_i0_items_items_oneOf_i4_timestamp"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance > timestamp`

**Title:** Timestamp

|            |             |
| ---------- | ----------- |
| **Type**   | `string`    |
| **Format** | `date-time` |

**Description:** Timestamp when alert was triggered in ISO8601 format.

###### <a name="data_oneOf_i0_items_items_oneOf_i4_tag"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance > tag`

**Title:** Tag

|          |         |
| -------- | ------- |
| **Type** | `const` |

Specific value: `"serviceInstanceAlert"`

###### <a name="data_oneOf_i0_items_items_oneOf_i4_serviceId"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance > serviceId`

**Title:** Serviceid

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Service unique identifier.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

###### <a name="data_oneOf_i0_items_items_oneOf_i4_subjectId"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance > subjectId`

**Title:** Subjectid

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Subject unique identifier.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

###### <a name="data_oneOf_i0_items_items_oneOf_i4_instance"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance > instance`

**Title:** Instance

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** Instance number (starting from 0).

###### <a name="data_oneOf_i0_items_items_oneOf_i4_version"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance > version`

**Title:** Version

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Version in format of the SemVer.

###### <a name="data_oneOf_i0_items_items_oneOf_i4_message"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertServiceInstance > message`

**Title:** Message

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Error information retrieved for the alert.

| Restrictions   |       |
| -------------- | ----- |
| **Min length** | 1     |
| **Max length** | 32768 |

###### <a name="data_oneOf_i0_items_items_oneOf_i5"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemError`

**Title:** AosAlertSystemError

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlertSystemError                                                 |

**Description:** Aos Unit system error alert information.

| Property                                                      | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [timestamp](#data_oneOf_i0_items_items_oneOf_i5_timestamp ) | No      | string | No         | -          | Timestamp         |
| + [tag](#data_oneOf_i0_items_items_oneOf_i5_tag )             | No      | const  | No         | -          | Tag               |
| + [nodeId](#data_oneOf_i0_items_items_oneOf_i5_nodeId )       | No      | string | No         | -          | Node ID           |
| + [message](#data_oneOf_i0_items_items_oneOf_i5_message )     | No      | string | No         | -          | Message           |

###### <a name="data_oneOf_i0_items_items_oneOf_i5_timestamp"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemError > timestamp`

**Title:** Timestamp

|            |             |
| ---------- | ----------- |
| **Type**   | `string`    |
| **Format** | `date-time` |

**Description:** Timestamp when alert was triggered in ISO8601 format.

###### <a name="data_oneOf_i0_items_items_oneOf_i5_tag"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemError > tag`

**Title:** Tag

|          |         |
| -------- | ------- |
| **Type** | `const` |

**Description:** Type of the alert.

Specific value: `"systemAlert"`

###### <a name="data_oneOf_i0_items_items_oneOf_i5_nodeId"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemError > nodeId`

**Title:** Node ID

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Unique ID of the node.

###### <a name="data_oneOf_i0_items_items_oneOf_i5_message"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemError > message`

**Title:** Message

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Error information retrieved for the alert.

| Restrictions   |       |
| -------------- | ----- |
| **Min length** | 1     |
| **Max length** | 32768 |

###### <a name="data_oneOf_i0_items_items_oneOf_i6"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemQuota`

**Title:** AosAlertSystemQuota

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlertSystemQuota                                                 |

**Description:** Aos Unit system quota alert information.

| Property                                                      | Pattern | Type    | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| + [timestamp](#data_oneOf_i0_items_items_oneOf_i6_timestamp ) | No      | string  | No         | -          | Timestamp         |
| + [tag](#data_oneOf_i0_items_items_oneOf_i6_tag )             | No      | const   | No         | -          | Tag               |
| + [nodeId](#data_oneOf_i0_items_items_oneOf_i6_nodeId )       | No      | string  | No         | -          | Node ID           |
| + [parameter](#data_oneOf_i0_items_items_oneOf_i6_parameter ) | No      | string  | No         | -          | Parameter         |
| + [value](#data_oneOf_i0_items_items_oneOf_i6_value )         | No      | integer | No         | -          | Value             |

###### <a name="data_oneOf_i0_items_items_oneOf_i6_timestamp"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemQuota > timestamp`

**Title:** Timestamp

|            |             |
| ---------- | ----------- |
| **Type**   | `string`    |
| **Format** | `date-time` |

**Description:** Timestamp when alert was triggered in ISO8601 format.

###### <a name="data_oneOf_i0_items_items_oneOf_i6_tag"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemQuota > tag`

**Title:** Tag

|          |         |
| -------- | ------- |
| **Type** | `const` |

**Description:** Type of the alert.

Specific value: `"systemQuotaAlert"`

###### <a name="data_oneOf_i0_items_items_oneOf_i6_nodeId"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemQuota > nodeId`

**Title:** Node ID

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Unique ID of the node.

###### <a name="data_oneOf_i0_items_items_oneOf_i6_parameter"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemQuota > parameter`

**Title:** Parameter

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Parameter name of the system quota.

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |
| **Max length** | 100 |

###### <a name="data_oneOf_i0_items_items_oneOf_i6_value"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertSystemQuota > value`

**Title:** Value

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** Triggered value of the parameter.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="data_oneOf_i0_items_items_oneOf_i7"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate`

**Title:** AosAlertResourceValidate

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlertResourceValidate                                            |

**Description:** Aos Unit resource validation alert information.

| Property                                                      | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [timestamp](#data_oneOf_i0_items_items_oneOf_i7_timestamp ) | No      | string | No         | -          | Timestamp         |
| + [tag](#data_oneOf_i0_items_items_oneOf_i7_tag )             | No      | const  | No         | -          | Tag               |
| + [nodeId](#data_oneOf_i0_items_items_oneOf_i7_nodeId )       | No      | string | No         | -          | Node ID           |
| + [name](#data_oneOf_i0_items_items_oneOf_i7_name )           | No      | string | No         | -          | Name              |
| + [errors](#data_oneOf_i0_items_items_oneOf_i7_errors )       | No      | array  | No         | -          | Errors            |

###### <a name="data_oneOf_i0_items_items_oneOf_i7_timestamp"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > timestamp`

**Title:** Timestamp

|            |             |
| ---------- | ----------- |
| **Type**   | `string`    |
| **Format** | `date-time` |

**Description:** Timestamp when alert was triggered in ISO8601 format.

###### <a name="data_oneOf_i0_items_items_oneOf_i7_tag"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > tag`

**Title:** Tag

|          |         |
| -------- | ------- |
| **Type** | `const` |

**Description:** Type of the alert.

Specific value: `"resourceValidateAlert"`

###### <a name="data_oneOf_i0_items_items_oneOf_i7_nodeId"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > nodeId`

**Title:** Node ID

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Unique ID of the node.

###### <a name="data_oneOf_i0_items_items_oneOf_i7_name"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > name`

**Title:** Name

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Name of the resource.

###### <a name="data_oneOf_i0_items_items_oneOf_i7_errors"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > errors`

**Title:** Errors

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** The list of caught errors

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                  | Description                       |
| ---------------------------------------------------------------- | --------------------------------- |
| [AosErrorInfo](#data_oneOf_i0_items_items_oneOf_i7_errors_items) | AosUnit error info structure. ... |

###### <a name="data_oneOf_i0_items_items_oneOf_i7_errors_items"></a>AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > errors > AosErrorInfo

**Title:** AosErrorInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosErrorInfo                                                        |

**Description:** AosUnit error info structure.

Encapsulates a structure for AosUnit error info.
All fields are optional. In this case treated as no error.

| Property                                                                 | Pattern | Type    | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------ | ------- | ------- | ---------- | ---------- | ----------------- |
| - [aosCode](#data_oneOf_i0_items_items_oneOf_i7_errors_items_aosCode )   | No      | integer | No         | -          | Aos error code    |
| - [exitCode](#data_oneOf_i0_items_items_oneOf_i7_errors_items_exitCode ) | No      | integer | No         | -          | Exit code         |
| - [message](#data_oneOf_i0_items_items_oneOf_i7_errors_items_message )   | No      | string  | No         | -          | Error message     |

###### <a name="data_oneOf_i0_items_items_oneOf_i7_errors_items_aosCode"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > errors > AosErrorInfo > aosCode`

**Title:** Aos error code

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `null`    |

**Description:** AosCore error code.

###### <a name="data_oneOf_i0_items_items_oneOf_i7_errors_items_exitCode"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > errors > AosErrorInfo > exitCode`

**Title:** Exit code

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `null`    |

**Description:** Module error code.

###### <a name="data_oneOf_i0_items_items_oneOf_i7_errors_items_message"></a>Property `AosUnitMessageV7 > data > oneOf > AosAlerts > items > items items > oneOf > AosAlertResourceValidate > errors > AosErrorInfo > message`

**Title:** Error message

|             |          |
| ----------- | -------- |
| **Type**    | `string` |
| **Default** | `null`   |

**Description:** Text of the error description.

### <a name="data_oneOf_i1"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7`

**Title:** AosDesiredStatusV7

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosDesiredStatusV7                                                  |

**Description:** AosUnit protocol: 'desiredStatus' message.

Unit reports all current status information using this message

| Property                                                 | Pattern | Type   | Deprecated | Definition                 | Title/Description |
| -------------------------------------------------------- | ------- | ------ | ---------- | -------------------------- | ----------------- |
| + [messageType](#data_oneOf_i1_messageType )             | No      | const  | No         | -                          | Messagetype       |
| - [nodes](#data_oneOf_i1_nodes )                         | No      | array  | No         | -                          | Nodes             |
| - [unitConfig](#data_oneOf_i1_unitConfig )               | No      | object | No         | In #/$defs/UnitConfig      | UnitConfig        |
| - [updateItems](#data_oneOf_i1_updateItems )             | No      | array  | No         | -                          | Updateitems       |
| - [instances](#data_oneOf_i1_instances )                 | No      | array  | No         | -                          | Instances         |
| - [fotaSchedule](#data_oneOf_i1_fotaSchedule )           | No      | object | No         | In #/$defs/AosScheduleRule | AosScheduleRule   |
| - [sotaSchedule](#data_oneOf_i1_sotaSchedule )           | No      | object | No         | In #/$defs/AosScheduleRule | AosScheduleRule   |
| - [certificates](#data_oneOf_i1_certificates )           | No      | array  | No         | -                          | Certificates      |
| - [certificateChains](#data_oneOf_i1_certificateChains ) | No      | array  | No         | -                          | Certificatechains |

#### <a name="data_oneOf_i1_messageType"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > messageType`

**Title:** Messagetype

|          |         |
| -------- | ------- |
| **Type** | `const` |

**Description:** Type of the message body.

Specific value: `"desiredStatus"`

#### <a name="data_oneOf_i1_nodes"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > nodes`

**Title:** Nodes

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** The list of desired node's status.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                   | Description          |
| ------------------------------------------------- | -------------------- |
| [AosNodeDesiredState](#data_oneOf_i1_nodes_items) | Desired node status. |

##### <a name="data_oneOf_i1_nodes_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > nodes > AosNodeDesiredState

**Title:** AosNodeDesiredState

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosNodeDesiredState                                                 |

**Description:** Desired node status.

| Property                                       | Pattern | Type             | Deprecated | Definition | Title/Description |
| ---------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [nodeId](#data_oneOf_i1_nodes_items_nodeId ) | No      | string           | No         | -          | Node ID           |
| + [status](#data_oneOf_i1_nodes_items_status ) | No      | enum (of string) | No         | -          | Status            |

###### <a name="data_oneOf_i1_nodes_items_nodeId"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > nodes > AosNodeDesiredState > nodeId`

**Title:** Node ID

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Unique ID of the node.

###### <a name="data_oneOf_i1_nodes_items_status"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > nodes > AosNodeDesiredState > status`

**Title:** Status

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

**Description:** The desired status of the node.

Must be one of:
* "provisioned"
* "paused"

#### <a name="data_oneOf_i1_unitConfig"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig`

**Title:** UnitConfig

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/UnitConfig                                                          |

**Description:** Desired unit config dictionary.

| Property                                                    | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [version](#data_oneOf_i1_unitConfig_version )             | No      | string | No         | -          | Version           |
| + [formatVersion](#data_oneOf_i1_unitConfig_formatVersion ) | No      | string | No         | -          | Format Version    |
| + [nodes](#data_oneOf_i1_unitConfig_nodes )                 | No      | array  | No         | -          | Nodes             |

##### <a name="data_oneOf_i1_unitConfig_version"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > version`

**Title:** Version

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Version identifies the configuration itself. It is automatically incremented with every configuration update.

##### <a name="data_oneOf_i1_unitConfig_formatVersion"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > formatVersion`

**Title:** Format Version

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** JSON format of the unit configuration may change over time. This field identifies current format of unit configuration. Cloud sets it automatically.

##### <a name="data_oneOf_i1_unitConfig_nodes"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes`

**Title:** Nodes

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** The list of node configurations.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                     | Description                    |
| --------------------------------------------------- | ------------------------------ |
| [NodeConfig](#data_oneOf_i1_unitConfig_nodes_items) | Node configuration parameters. |

###### <a name="data_oneOf_i1_unitConfig_nodes_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig

**Title:** NodeConfig

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/NodeConfig                                                          |

**Description:** Node configuration parameters.

| Property                                                                  | Pattern | Type            | Deprecated | Definition                    | Title/Description  |
| ------------------------------------------------------------------------- | ------- | --------------- | ---------- | ----------------------------- | ------------------ |
| + [nodeType](#data_oneOf_i1_unitConfig_nodes_items_nodeType )             | No      | string          | No         | -                             | Node Type          |
| - [nodeId](#data_oneOf_i1_unitConfig_nodes_items_nodeId )                 | No      | string          | No         | -                             | Node ID            |
| - [alertRules](#data_oneOf_i1_unitConfig_nodes_items_alertRules )         | No      | object          | No         | In #/$defs/AlertRules         | Alert Rules        |
| - [resourceRatios](#data_oneOf_i1_unitConfig_nodes_items_resourceRatios ) | No      | object          | No         | In #/$defs/ResourceRatiosInfo | ResourceRatiosInfo |
| - [devices](#data_oneOf_i1_unitConfig_nodes_items_devices )               | No      | array           | No         | -                             | Devices            |
| - [resources](#data_oneOf_i1_unitConfig_nodes_items_resources )           | No      | array           | No         | -                             | Resources          |
| - [labels](#data_oneOf_i1_unitConfig_nodes_items_labels )                 | No      | array of string | No         | -                             | Labels             |
| + [priority](#data_oneOf_i1_unitConfig_nodes_items_priority )             | No      | integer         | No         | -                             | Priority           |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_nodeType"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > nodeType`

**Title:** Node Type

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Group of nodes with identical configuration.

###### <a name="data_oneOf_i1_unitConfig_nodes_items_nodeId"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > nodeId`

**Title:** Node ID

|             |          |
| ----------- | -------- |
| **Type**    | `string` |
| **Default** | `null`   |

**Description:** Unique ID of the node

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules`

**Title:** Alert Rules

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/AlertRules                                                          |

**Description:** The default thresholds for services running on the node.

| Property                                                                     | Pattern | Type        | Deprecated | Definition                   | Title/Description |
| ---------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------------------------- | ----------------- |
| - [cpu](#data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu )               | No      | object      | No         | In #/$defs/AlertRulePercents | AlertRulePercents |
| - [ram](#data_oneOf_i1_unitConfig_nodes_items_alertRules_ram )               | No      | object      | No         | In #/$defs/AlertRulePercents | AlertRulePercents |
| - [partitions](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions ) | No      | Combination | No         | -                            | Partitions        |
| - [download](#data_oneOf_i1_unitConfig_nodes_items_alertRules_download )     | No      | object      | No         | In #/$defs/AlertRulePoints   | AlertRulePoints   |
| - [upload](#data_oneOf_i1_unitConfig_nodes_items_alertRules_upload )         | No      | object      | No         | In #/$defs/AlertRulePoints   | AlertRulePoints   |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > cpu`

**Title:** AlertRulePercents

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/AlertRulePercents                                                   |

**Description:** The CPU thresholds.

| Property                                                                             | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| + [minThreshold](#data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_minThreshold ) | No      | number | No         | -          | Minthreshold      |
| + [maxThreshold](#data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_maxThreshold ) | No      | number | No         | -          | Maxthreshold      |
| + [minTimeout](#data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_minTimeout )     | No      | number | No         | -          | Mintimeout        |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_minThreshold"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > cpu > minThreshold`

**Title:** Minthreshold

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The lowest percents of a value after which resource can be rebalanced back.

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_maxThreshold"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > cpu > maxThreshold`

**Title:** Maxthreshold

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The highest percents of a value after which resource have be rebalanced.

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_minTimeout"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > cpu > minTimeout`

**Title:** Mintimeout

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The timeout in seconds. Fraction of value specifies milliseconds

**Examples:**

```json
0.5
```

```json
100
```

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_ram"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > ram`

**Title:** AlertRulePercents

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/AlertRulePercents                                                   |

**Description:** The RAM thresholds.

| Property                                                                             | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| + [minThreshold](#data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_minThreshold ) | No      | number | No         | -          | Minthreshold      |
| + [maxThreshold](#data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_maxThreshold ) | No      | number | No         | -          | Maxthreshold      |
| + [minTimeout](#data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_minTimeout )     | No      | number | No         | -          | Mintimeout        |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_minThreshold"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > cpu > minThreshold`

**Title:** Minthreshold

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The lowest percents of a value after which resource can be rebalanced back.

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_maxThreshold"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > cpu > maxThreshold`

**Title:** Maxthreshold

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The highest percents of a value after which resource have be rebalanced.

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_cpu_minTimeout"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > cpu > minTimeout`

**Title:** Mintimeout

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The timeout in seconds. Fraction of value specifies milliseconds

**Examples:**

```json
0.5
```

```json
100
```

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions`

**Title:** Partitions

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** The list of thresholds partitions.

| Any of(Option)                                                                 |
| ------------------------------------------------------------------------------ |
| [item 0](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0) |
| [item 1](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i1) |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0`

|          |         |
| -------- | ------- |
| **Type** | `array` |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                                       | Description                                          |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| [AlertRulePercentsOfDisk](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items) | Information about the threshold for disk with names. |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk

**Title:** AlertRulePercentsOfDisk

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AlertRulePercentsOfDisk                                             |

**Description:** Information about the threshold for disk with names.

| Property                                                                                                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [minThreshold](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items_minThreshold ) | No      | number | No         | -          | Minthreshold      |
| + [maxThreshold](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items_maxThreshold ) | No      | number | No         | -          | Maxthreshold      |
| + [minTimeout](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items_minTimeout )     | No      | number | No         | -          | Mintimeout        |
| + [name](#data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items_name )                 | No      | string | No         | -          | Name of partition |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items_minThreshold"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > minThreshold`

**Title:** Minthreshold

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The lowest percents of a value after which resource can be rebalanced back.

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items_maxThreshold"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > maxThreshold`

**Title:** Maxthreshold

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The highest percents of a value after which resource have be rebalanced.

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items_minTimeout"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > minTimeout`

**Title:** Mintimeout

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The timeout in seconds. Fraction of value specifies milliseconds

**Examples:**

```json
0.5
```

```json
100
```

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i0_items_name"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > name`

**Title:** Name of partition

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_partitions_anyOf_i1"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_download"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > download`

**Title:** AlertRulePoints

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/AlertRulePoints                                                     |

**Description:** Alert rules for incoming network traffic(in bytes).

| Property                                                                                  | Pattern | Type    | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| + [minThreshold](#data_oneOf_i1_unitConfig_nodes_items_alertRules_download_minThreshold ) | No      | integer | No         | -          | Minthreshold      |
| + [maxThreshold](#data_oneOf_i1_unitConfig_nodes_items_alertRules_download_maxThreshold ) | No      | integer | No         | -          | Maxthreshold      |
| + [minTimeout](#data_oneOf_i1_unitConfig_nodes_items_alertRules_download_minTimeout )     | No      | number  | No         | -          | Mintimeout        |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_download_minThreshold"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > download > minThreshold`

**Title:** Minthreshold

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** The lowest points (DMIPs, Bytes, etc) of a value after which resource can be rebalanced back.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_download_maxThreshold"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > download > maxThreshold`

**Title:** Maxthreshold

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** The highest points of a value after which resource have be rebalanced.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_download_minTimeout"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > download > minTimeout`

**Title:** Mintimeout

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The timeout in seconds. Fraction of value specifies milliseconds

**Examples:**

```json
0.5
```

```json
100
```

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_upload"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > upload`

**Title:** AlertRulePoints

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/AlertRulePoints                                                     |

**Description:** Alert rules for outgoing network traffic(in bytes).

| Property                                                                                  | Pattern | Type    | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| + [minThreshold](#data_oneOf_i1_unitConfig_nodes_items_alertRules_download_minThreshold ) | No      | integer | No         | -          | Minthreshold      |
| + [maxThreshold](#data_oneOf_i1_unitConfig_nodes_items_alertRules_download_maxThreshold ) | No      | integer | No         | -          | Maxthreshold      |
| + [minTimeout](#data_oneOf_i1_unitConfig_nodes_items_alertRules_download_minTimeout )     | No      | number  | No         | -          | Mintimeout        |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_download_minThreshold"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > download > minThreshold`

**Title:** Minthreshold

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** The lowest points (DMIPs, Bytes, etc) of a value after which resource can be rebalanced back.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_download_maxThreshold"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > download > maxThreshold`

**Title:** Maxthreshold

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** The highest points of a value after which resource have be rebalanced.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_alertRules_download_minTimeout"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > alertRules > download > minTimeout`

**Title:** Mintimeout

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The timeout in seconds. Fraction of value specifies milliseconds

**Examples:**

```json
0.5
```

```json
100
```

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resourceRatios"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resourceRatios`

**Title:** ResourceRatiosInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/ResourceRatiosInfo                                                  |

**Description:** The default resource ratio allocated for a service.

| Property                                                                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [cpu](#data_oneOf_i1_unitConfig_nodes_items_resourceRatios_cpu )         | No      | number | No         | -          | Cpu               |
| - [ram](#data_oneOf_i1_unitConfig_nodes_items_resourceRatios_ram )         | No      | number | No         | -          | Ram               |
| - [storage](#data_oneOf_i1_unitConfig_nodes_items_resourceRatios_storage ) | No      | number | No         | -          | Storage           |
| - [state](#data_oneOf_i1_unitConfig_nodes_items_resourceRatios_state )     | No      | number | No         | -          | State             |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resourceRatios_cpu"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resourceRatios > cpu`

**Title:** Cpu

|             |          |
| ----------- | -------- |
| **Type**    | `number` |
| **Default** | `null`   |

**Description:** The CPU ratio in percent.

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resourceRatios_ram"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resourceRatios > ram`

**Title:** Ram

|             |          |
| ----------- | -------- |
| **Type**    | `number` |
| **Default** | `null`   |

**Description:** The memory (RAM) ratio in percent.

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resourceRatios_storage"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resourceRatios > storage`

**Title:** Storage

|             |          |
| ----------- | -------- |
| **Type**    | `number` |
| **Default** | `null`   |

**Description:** The storage ratio in percent.

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resourceRatios_state"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resourceRatios > state`

**Title:** State

|             |          |
| ----------- | -------- |
| **Type**    | `number` |
| **Default** | `null`   |

**Description:** Requested size of the "state" partition (in percents of its capacity).

###### <a name="data_oneOf_i1_unitConfig_nodes_items_devices"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices`

**Title:** Devices

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** The device list available for running services.

**Examples:**

```json
"Name=\"camera\", host_devices=[\"/dev/camera\"]"
```

```json
"Name=\"pulseaudio\", host_devices=[\"/dev/pulseaudio\"]"
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                      | Description |
| -------------------------------------------------------------------- | ----------- |
| [AosDeviceInfo](#data_oneOf_i1_unitConfig_nodes_items_devices_items) | -           |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_devices_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices > AosDeviceInfo

**Title:** AosDeviceInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosDeviceInfo                                                       |

| Property                                                                          | Pattern | Type            | Deprecated | Definition | Title/Description |
| --------------------------------------------------------------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| + [name](#data_oneOf_i1_unitConfig_nodes_items_devices_items_name )               | No      | string          | No         | -          | Name              |
| + [hostDevices](#data_oneOf_i1_unitConfig_nodes_items_devices_items_hostDevices ) | No      | array of string | No         | -          | Hostdevices       |
| - [sharedCount](#data_oneOf_i1_unitConfig_nodes_items_devices_items_sharedCount ) | No      | integer         | No         | -          | Sharedcount       |
| - [groups](#data_oneOf_i1_unitConfig_nodes_items_devices_items_groups )           | No      | array of string | No         | -          | Groups            |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_devices_items_name"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices > AosDeviceInfo > name`

**Title:** Name

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Name of the device.

###### <a name="data_oneOf_i1_unitConfig_nodes_items_devices_items_hostDevices"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices > AosDeviceInfo > hostDevices`

**Title:** Hostdevices

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

**Description:** List of files in /dev dir, associated with the device name.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                            | Description |
| ------------------------------------------------------------------------------------------ | ----------- |
| [hostDevices items](#data_oneOf_i1_unitConfig_nodes_items_devices_items_hostDevices_items) | -           |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_devices_items_hostDevices_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices > AosDeviceInfo > hostDevices > hostDevices items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_devices_items_sharedCount"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices > AosDeviceInfo > sharedCount`

**Title:** Sharedcount

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `0`       |

**Description:** The maximum allowed number of service instances that can use this device simultaneously. 0 means no restrictions.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_devices_items_groups"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices > AosDeviceInfo > groups`

**Title:** Groups

|             |                   |
| ----------- | ----------------- |
| **Type**    | `array of string` |
| **Default** | `null`            |

**Description:** List of associated user groups.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                  | Description |
| -------------------------------------------------------------------------------- | ----------- |
| [groups items](#data_oneOf_i1_unitConfig_nodes_items_devices_items_groups_items) | -           |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_devices_items_groups_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > devices > AosDeviceInfo > groups > groups items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources`

**Title:** Resources

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** Available resources for services.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                       | Description |
| --------------------------------------------------------------------- | ----------- |
| [ResourceInfo](#data_oneOf_i1_unitConfig_nodes_items_resources_items) | -           |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo

**Title:** ResourceInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/ResourceInfo                                                        |

| Property                                                                  | Pattern | Type            | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| + [name](#data_oneOf_i1_unitConfig_nodes_items_resources_items_name )     | No      | string          | No         | -          | Name              |
| - [groups](#data_oneOf_i1_unitConfig_nodes_items_resources_items_groups ) | No      | array of string | No         | -          | Groups            |
| - [mounts](#data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts ) | No      | array           | No         | -          | Mounts            |
| - [envs](#data_oneOf_i1_unitConfig_nodes_items_resources_items_envs )     | No      | array of string | No         | -          | Envs              |
| - [hosts](#data_oneOf_i1_unitConfig_nodes_items_resources_items_hosts )   | No      | array           | No         | -          | Hosts             |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_name"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > name`

**Title:** Name

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The name of the resource.

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_groups"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > groups`

**Title:** Groups

|             |                   |
| ----------- | ----------------- |
| **Type**    | `array of string` |
| **Default** | `null`            |

**Description:** The group names for the resource.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                    | Description |
| ---------------------------------------------------------------------------------- | ----------- |
| [groups items](#data_oneOf_i1_unitConfig_nodes_items_resources_items_groups_items) | -           |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_groups_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > groups > groups items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts`

**Title:** Mounts

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** The mounts list available for running services.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                          | Description |
| ---------------------------------------------------------------------------------------- | ----------- |
| [AosFileSystemMount](#data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items) | -           |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount

**Title:** AosFileSystemMount

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosFileSystemMount                                                  |

| Property                                                                                         | Pattern | Type            | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------------------ | ------- | --------------- | ---------- | ---------- | ----------------- |
| + [destination](#data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_destination ) | No      | string          | No         | -          | Destination       |
| - [source](#data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_source )           | No      | string          | No         | -          | Source            |
| - [type](#data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_type )               | No      | string          | No         | -          | Type              |
| - [options](#data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_options )         | No      | array of string | No         | -          | Options           |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_destination"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > destination`

**Title:** Destination

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The mount's destination.

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_source"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > source`

**Title:** Source

|             |          |
| ----------- | -------- |
| **Type**    | `string` |
| **Default** | `null`   |

**Description:** The mount's source.

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_type"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > type`

**Title:** Type

|             |          |
| ----------- | -------- |
| **Type**    | `string` |
| **Default** | `null`   |

**Description:** The mount's type.

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_options"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > options`

**Title:** Options

|             |                   |
| ----------- | ----------------- |
| **Type**    | `array of string` |
| **Default** | `null`            |

**Description:** The mount's options.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                                   | Description |
| ------------------------------------------------------------------------------------------------- | ----------- |
| [options items](#data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_options_items) | -           |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_mounts_items_options_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > options > options items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_envs"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > envs`

**Title:** Envs

|             |                   |
| ----------- | ----------------- |
| **Type**    | `array of string` |
| **Default** | `null`            |

**Description:** The list of environment variables.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                | Description |
| ------------------------------------------------------------------------------ | ----------- |
| [envs items](#data_oneOf_i1_unitConfig_nodes_items_resources_items_envs_items) | -           |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_envs_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > envs > envs items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_hosts"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts`

**Title:** Hosts

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** The list of hostnames.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                    | Description |
| ---------------------------------------------------------------------------------- | ----------- |
| [AosHostRecord](#data_oneOf_i1_unitConfig_nodes_items_resources_items_hosts_items) | -           |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_hosts_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts > AosHostRecord

**Title:** AosHostRecord

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosHostRecord                                                       |

| Property                                                                                  | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [ip](#data_oneOf_i1_unitConfig_nodes_items_resources_items_hosts_items_ip )             | No      | string | No         | -          | IP address        |
| + [hostname](#data_oneOf_i1_unitConfig_nodes_items_resources_items_hosts_items_hostname ) | No      | string | No         | -          | Hostname          |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_hosts_items_ip"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts > AosHostRecord > ip`

**Title:** IP address

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** IP address.

###### <a name="data_oneOf_i1_unitConfig_nodes_items_resources_items_hosts_items_hostname"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts > AosHostRecord > hostname`

**Title:** Hostname

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The hostname for the IP address.

###### <a name="data_oneOf_i1_unitConfig_nodes_items_labels"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > labels`

**Title:** Labels

|             |                   |
| ----------- | ----------------- |
| **Type**    | `array of string` |
| **Default** | `null`            |

**Description:** The list of labels for this node.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [labels items](#data_oneOf_i1_unitConfig_nodes_items_labels_items) | -           |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_labels_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > labels > labels items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="data_oneOf_i1_unitConfig_nodes_items_priority"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > unitConfig > nodes > NodeConfig > priority`

**Title:** Priority

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** The priority of the node for deploying services.

| Restrictions |                 |
| ------------ | --------------- |
| **Minimum**  | &ge; 0          |
| **Maximum**  | &lt; 4294967295 |

#### <a name="data_oneOf_i1_updateItems"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems`

**Title:** Updateitems

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** List of the desired services. If absent or null - do nothing.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                               | Description                               |
| ------------------------------------------------------------- | ----------------------------------------- |
| [AosUpdateItemDownloadInfo](#data_oneOf_i1_updateItems_items) | Service info sent from the AosEdge Cloud. |

##### <a name="data_oneOf_i1_updateItems_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo

**Title:** AosUpdateItemDownloadInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosUpdateItemDownloadInfo                                           |

**Description:** Service info sent from the AosEdge Cloud.

| Property                                                             | Pattern | Type            | Deprecated | Definition                   | Title/Description |
| -------------------------------------------------------------------- | ------- | --------------- | ---------- | ---------------------------- | ----------------- |
| + [identifier](#data_oneOf_i1_updateItems_items_identifier )         | No      | object          | No         | In #/$defs/AosIdentifier     | AosIdentifier     |
| + [version](#data_oneOf_i1_updateItems_items_version )               | No      | string          | No         | -                            | Version           |
| + [urls](#data_oneOf_i1_updateItems_items_urls )                     | No      | array of string | No         | -                            | Urls              |
| + [sha256](#data_oneOf_i1_updateItems_items_sha256 )                 | No      | string          | No         | -                            | Sha256            |
| + [size](#data_oneOf_i1_updateItems_items_size )                     | No      | integer         | No         | -                            | Size              |
| + [decryptionInfo](#data_oneOf_i1_updateItems_items_decryptionInfo ) | No      | object          | No         | In #/$defs/AosDecryptionInfo | AosDecryptionInfo |
| + [signs](#data_oneOf_i1_updateItems_items_signs )                   | No      | object          | No         | In #/$defs/AosSignInfo       | AosSignInfo       |

###### <a name="data_oneOf_i1_updateItems_items_identifier"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier`

**Title:** AosIdentifier

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosIdentifier                                                       |

**Description:** Aos objects identifier.

| Property                                                                  | Pattern | Type        | Deprecated | Definition | Title/Description                                    |
| ------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ---------------------------------------------------- |
| - [id](#data_oneOf_i1_updateItems_items_identifier_id )                   | No      | Combination | No         | -          | Aos object UUID identifier. Unique per Aos instance. |
| - [type](#data_oneOf_i1_updateItems_items_identifier_type )               | No      | Combination | No         | -          | Aos object type.                                     |
| - [codename](#data_oneOf_i1_updateItems_items_identifier_codename )       | No      | Combination | No         | -          | Aos object codename.                                 |
| - [title](#data_oneOf_i1_updateItems_items_identifier_title )             | No      | Combination | No         | -          | Aos object title.                                    |
| - [description](#data_oneOf_i1_updateItems_items_identifier_description ) | No      | Combination | No         | -          | Aos object description.                              |
| - [urn](#data_oneOf_i1_updateItems_items_identifier_urn )                 | No      | Combination | No         | -          | Aos object URN.                                      |

###### <a name="data_oneOf_i1_updateItems_items_identifier_id"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > id`

**Title:** Aos object UUID identifier. Unique per Aos instance.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object unique per Aos instance UUID.

| Any of(Option)                                                    |
| ----------------------------------------------------------------- |
| [item 0](#data_oneOf_i1_updateItems_items_identifier_id_anyOf_i0) |
| [item 1](#data_oneOf_i1_updateItems_items_identifier_id_anyOf_i1) |

###### <a name="data_oneOf_i1_updateItems_items_identifier_id_anyOf_i0"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > id > anyOf > item 0`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `uuid4`  |

###### <a name="data_oneOf_i1_updateItems_items_identifier_id_anyOf_i1"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > id > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="data_oneOf_i1_updateItems_items_identifier_type"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > type`

**Title:** Aos object type.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object type. E.g.: AosService, AosComponent

| Any of(Option)                                                      |
| ------------------------------------------------------------------- |
| [item 0](#data_oneOf_i1_updateItems_items_identifier_type_anyOf_i0) |
| [item 1](#data_oneOf_i1_updateItems_items_identifier_type_anyOf_i1) |

###### <a name="data_oneOf_i1_updateItems_items_identifier_type_anyOf_i0"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > type > anyOf > item 0`

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

Must be one of:
* "aosComponent"
* "aosService"
* "aosLayer"
* "aosSubject"
* "aosOEM"

###### <a name="data_oneOf_i1_updateItems_items_identifier_type_anyOf_i1"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > type > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="data_oneOf_i1_updateItems_items_identifier_codename"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > codename`

**Title:** Aos object codename.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object codename. Uniqueness depends on object type.

| Any of(Option)                                                          |
| ----------------------------------------------------------------------- |
| [item 0](#data_oneOf_i1_updateItems_items_identifier_codename_anyOf_i0) |
| [item 1](#data_oneOf_i1_updateItems_items_identifier_codename_anyOf_i1) |

###### <a name="data_oneOf_i1_updateItems_items_identifier_codename_anyOf_i0"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > codename > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="data_oneOf_i1_updateItems_items_identifier_codename_anyOf_i1"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > codename > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="data_oneOf_i1_updateItems_items_identifier_title"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > title`

**Title:** Aos object title.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object title.

| Any of(Option)                                                       |
| -------------------------------------------------------------------- |
| [item 0](#data_oneOf_i1_updateItems_items_identifier_title_anyOf_i0) |
| [item 1](#data_oneOf_i1_updateItems_items_identifier_title_anyOf_i1) |

###### <a name="data_oneOf_i1_updateItems_items_identifier_title_anyOf_i0"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > title > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="data_oneOf_i1_updateItems_items_identifier_title_anyOf_i1"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > title > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="data_oneOf_i1_updateItems_items_identifier_description"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > description`

**Title:** Aos object description.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object description.

| Any of(Option)                                                             |
| -------------------------------------------------------------------------- |
| [item 0](#data_oneOf_i1_updateItems_items_identifier_description_anyOf_i0) |
| [item 1](#data_oneOf_i1_updateItems_items_identifier_description_anyOf_i1) |

###### <a name="data_oneOf_i1_updateItems_items_identifier_description_anyOf_i0"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > description > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="data_oneOf_i1_updateItems_items_identifier_description_anyOf_i1"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > description > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="data_oneOf_i1_updateItems_items_identifier_urn"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > urn`

**Title:** Aos object URN.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object URN. Globally unique.

| Any of(Option)                                                     |
| ------------------------------------------------------------------ |
| [item 0](#data_oneOf_i1_updateItems_items_identifier_urn_anyOf_i0) |
| [item 1](#data_oneOf_i1_updateItems_items_identifier_urn_anyOf_i1) |

###### <a name="data_oneOf_i1_updateItems_items_identifier_urn_anyOf_i0"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > urn > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="data_oneOf_i1_updateItems_items_identifier_urn_anyOf_i1"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > identifier > urn > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="data_oneOf_i1_updateItems_items_version"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > version`

**Title:** Version

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Version in format of the SemVer.

###### <a name="data_oneOf_i1_updateItems_items_urls"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > urls`

**Title:** Urls

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

**Description:** the list of urls pointer to the same target

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [urls items](#data_oneOf_i1_updateItems_items_urls_items) | -           |

###### <a name="data_oneOf_i1_updateItems_items_urls_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > urls > urls items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="data_oneOf_i1_updateItems_items_sha256"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > sha256`

**Title:** Sha256

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `base64` |

**Description:** SHA3-256 digest of the target

###### <a name="data_oneOf_i1_updateItems_items_size"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > size`

**Title:** Size

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** size of the file in bytes

###### <a name="data_oneOf_i1_updateItems_items_decryptionInfo"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo`

**Title:** AosDecryptionInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosDecryptionInfo                                                   |

**Description:** Object with information to decrypt the component.

| Property                                                                        | Pattern | Type             | Deprecated | Definition                 | Title/Description |
| ------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------- | ----------------- |
| - [blockAlg](#data_oneOf_i1_updateItems_items_decryptionInfo_blockAlg )         | No      | const            | No         | -                          | Blockalg          |
| + [blockIv](#data_oneOf_i1_updateItems_items_decryptionInfo_blockIv )           | No      | string           | No         | -                          | Blockiv           |
| + [blockKey](#data_oneOf_i1_updateItems_items_decryptionInfo_blockKey )         | No      | string           | No         | -                          | Blockkey          |
| - [asymAlg](#data_oneOf_i1_updateItems_items_decryptionInfo_asymAlg )           | No      | enum (of string) | No         | -                          | Asymalg           |
| + [receiverInfo](#data_oneOf_i1_updateItems_items_decryptionInfo_receiverInfo ) | No      | object           | No         | In #/$defs/AosReceiverInfo | AosReceiverInfo   |

###### <a name="data_oneOf_i1_updateItems_items_decryptionInfo_blockAlg"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo > blockAlg`

**Title:** Blockalg

|             |                      |
| ----------- | -------------------- |
| **Type**    | `const`              |
| **Default** | `"AES256/CBC/pkcs7"` |

**Description:** Used block cipher in form: `cipher/mode/padding`.

Specific value: `"AES256/CBC/pkcs7"`

###### <a name="data_oneOf_i1_updateItems_items_decryptionInfo_blockIv"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo > blockIv`

**Title:** Blockiv

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `base64` |

**Description:** Initialization vector for encryption/decryption.

###### <a name="data_oneOf_i1_updateItems_items_decryptionInfo_blockKey"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo > blockKey`

**Title:** Blockkey

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `base64` |

**Description:** Symmetric block key value.

###### <a name="data_oneOf_i1_updateItems_items_decryptionInfo_asymAlg"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo > asymAlg`

**Title:** Asymalg

|             |                    |
| ----------- | ------------------ |
| **Type**    | `enum (of string)` |
| **Default** | `"RSA/PKCS1v1_5"`  |

**Description:** Used asymmetric cipher in form: `cipher/padding`.

Must be one of:
* "RSA/PKCS1v1_5"
* "RSA/PSS"

###### <a name="data_oneOf_i1_updateItems_items_decryptionInfo_receiverInfo"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo > receiverInfo`

**Title:** AosReceiverInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosReceiverInfo                                                     |

**Description:** Receiver info to detect used key.

| Property                                                                         | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [serial](#data_oneOf_i1_updateItems_items_decryptionInfo_receiverInfo_serial ) | No      | string | No         | -          | Serial            |
| + [issuer](#data_oneOf_i1_updateItems_items_decryptionInfo_receiverInfo_issuer ) | No      | string | No         | -          | Issuer            |

###### <a name="data_oneOf_i1_updateItems_items_decryptionInfo_receiverInfo_serial"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo > receiverInfo > serial`

**Title:** Serial

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Certificate serial number.

###### <a name="data_oneOf_i1_updateItems_items_decryptionInfo_receiverInfo_issuer"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > decryptionInfo > receiverInfo > issuer`

**Title:** Issuer

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `base64` |

**Description:** Certificate `Issuer DN` field bytes.

###### <a name="data_oneOf_i1_updateItems_items_signs"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > signs`

**Title:** AosSignInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosSignInfo                                                         |

**Description:** Sign values of the file.

| Property                                                                       | Pattern | Type             | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------ | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [chainName](#data_oneOf_i1_updateItems_items_signs_chainName )               | No      | string           | No         | -          | Chainname         |
| + [alg](#data_oneOf_i1_updateItems_items_signs_alg )                           | No      | enum (of string) | No         | -          | Alg               |
| + [value](#data_oneOf_i1_updateItems_items_signs_value )                       | No      | string           | No         | -          | Value             |
| + [trustedTimestamp](#data_oneOf_i1_updateItems_items_signs_trustedTimestamp ) | No      | string           | No         | -          | Trustedtimestamp  |
| - [ocspValues](#data_oneOf_i1_updateItems_items_signs_ocspValues )             | No      | array of string  | No         | -          | Ocspvalues        |

###### <a name="data_oneOf_i1_updateItems_items_signs_chainName"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > signs > chainName`

**Title:** Chainname

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** chain name from the list of `certificateChains`.

###### <a name="data_oneOf_i1_updateItems_items_signs_alg"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > signs > alg`

**Title:** Alg

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

**Description:** Used algorithm for signing in the form `alg/hash`.

Must be one of:
* "RSA/SHA256"
* "EC/SHA256"

###### <a name="data_oneOf_i1_updateItems_items_signs_value"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > signs > value`

**Title:** Value

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Base64 encoded value of the signature.

###### <a name="data_oneOf_i1_updateItems_items_signs_trustedTimestamp"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > signs > trustedTimestamp`

**Title:** Trustedtimestamp

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Timestamp of the signature in ISO8601 format.

###### <a name="data_oneOf_i1_updateItems_items_signs_ocspValues"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > signs > ocspValues`

**Title:** Ocspvalues

|             |                   |
| ----------- | ----------------- |
| **Type**    | `array of string` |
| **Default** | `null`            |

**Description:** OCSP value of the signature.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                             | Description |
| --------------------------------------------------------------------------- | ----------- |
| [ocspValues items](#data_oneOf_i1_updateItems_items_signs_ocspValues_items) | -           |

###### <a name="data_oneOf_i1_updateItems_items_signs_ocspValues_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > updateItems > AosUpdateItemDownloadInfo > signs > ocspValues > ocspValues items

|          |          |
| -------- | -------- |
| **Type** | `string` |

#### <a name="data_oneOf_i1_instances"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances`

**Title:** Instances

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** List of the desired services instances. If absent or null - do nothing.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                          | Description                               |
| -------------------------------------------------------- | ----------------------------------------- |
| [AosDesiredInstanceInfo](#data_oneOf_i1_instances_items) | Service info sent from the AosEdge Cloud. |

##### <a name="data_oneOf_i1_instances_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances > AosDesiredInstanceInfo

**Title:** AosDesiredInstanceInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosDesiredInstanceInfo                                              |

**Description:** Service info sent from the AosEdge Cloud.

| Property                                                       | Pattern | Type            | Deprecated | Definition                                                         | Title/Description |
| -------------------------------------------------------------- | ------- | --------------- | ---------- | ------------------------------------------------------------------ | ----------------- |
| + [update_item](#data_oneOf_i1_instances_items_update_item )   | No      | object          | No         | Same as [identifier](#data_oneOf_i1_updateItems_items_identifier ) | AosIdentifier     |
| + [subject](#data_oneOf_i1_instances_items_subject )           | No      | object          | No         | Same as [identifier](#data_oneOf_i1_updateItems_items_identifier ) | AosIdentifier     |
| - [priority](#data_oneOf_i1_instances_items_priority )         | No      | integer         | No         | -                                                                  | Priority          |
| - [numInstances](#data_oneOf_i1_instances_items_numInstances ) | No      | integer         | No         | -                                                                  | Numinstances      |
| - [labels](#data_oneOf_i1_instances_items_labels )             | No      | array of string | No         | -                                                                  | Labels            |

###### <a name="data_oneOf_i1_instances_items_update_item"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances > AosDesiredInstanceInfo > update_item`

**Title:** AosIdentifier

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Same definition as**    | [identifier](#data_oneOf_i1_updateItems_items_identifier)                   |

**Description:** Aos objects identifier.

###### <a name="data_oneOf_i1_instances_items_subject"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances > AosDesiredInstanceInfo > subject`

**Title:** AosIdentifier

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Same definition as**    | [identifier](#data_oneOf_i1_updateItems_items_identifier)                   |

**Description:** Aos objects identifier.

###### <a name="data_oneOf_i1_instances_items_priority"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances > AosDesiredInstanceInfo > priority`

**Title:** Priority

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `0`       |

**Description:** Priority of the service instance.

| Restrictions |              |
| ------------ | ------------ |
| **Minimum**  | &ge; 0       |
| **Maximum**  | &lt; 1000000 |

###### <a name="data_oneOf_i1_instances_items_numInstances"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances > AosDesiredInstanceInfo > numInstances`

**Title:** Numinstances

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `1`       |

**Description:** Number of service instances to run.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &gt; 0 |

###### <a name="data_oneOf_i1_instances_items_labels"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances > AosDesiredInstanceInfo > labels`

**Title:** Labels

|             |                   |
| ----------- | ----------------- |
| **Type**    | `array of string` |
| **Default** | `null`            |

**Description:** Label list associated with the service.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                             | Description |
| ----------------------------------------------------------- | ----------- |
| [labels items](#data_oneOf_i1_instances_items_labels_items) | -           |

###### <a name="data_oneOf_i1_instances_items_labels_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > instances > AosDesiredInstanceInfo > labels > labels items

|          |          |
| -------- | -------- |
| **Type** | `string` |

#### <a name="data_oneOf_i1_fotaSchedule"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule`

**Title:** AosScheduleRule

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/AosScheduleRule                                                     |

**Description:** Points to rules when FOTA can be applied.

| Property                                              | Pattern | Type             | Deprecated | Definition | Title/Description |
| ----------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| - [ttl](#data_oneOf_i1_fotaSchedule_ttl )             | No      | integer          | No         | -          | Ttl               |
| + [type](#data_oneOf_i1_fotaSchedule_type )           | No      | enum (of string) | No         | -          | Type              |
| - [timetable](#data_oneOf_i1_fotaSchedule_timetable ) | No      | array            | No         | -          | Timetable         |

##### <a name="data_oneOf_i1_fotaSchedule_ttl"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > ttl`

**Title:** Ttl

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `null`    |

**Description:** TTL of the rule in seconds.

##### <a name="data_oneOf_i1_fotaSchedule_type"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > type`

**Title:** Type

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

**Description:** Type of the Schedule rule.

Must be one of:
* "force"
* "trigger"
* "timetable"

##### <a name="data_oneOf_i1_fotaSchedule_timetable"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable`

**Title:** Timetable

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** Timetable when rule must work (only when the type is `timetable`).

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                 | Description                 |
| --------------------------------------------------------------- | --------------------------- |
| [AosTimetableItem](#data_oneOf_i1_fotaSchedule_timetable_items) | Timetable signe record. ... |

###### <a name="data_oneOf_i1_fotaSchedule_timetable_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem

**Title:** AosTimetableItem

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosTimetableItem                                                    |

**Description:** Timetable signe record.

Represent one entry of the timetable in form
`day of week`: [start time:end time]

| Property                                                              | Pattern | Type    | Deprecated | Definition | Title/Description |
| --------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| + [dayOfWeek](#data_oneOf_i1_fotaSchedule_timetable_items_dayOfWeek ) | No      | integer | No         | -          | Dayofweek         |
| + [timeSlots](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots ) | No      | array   | No         | -          | Timeslots         |

###### <a name="data_oneOf_i1_fotaSchedule_timetable_items_dayOfWeek"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > dayOfWeek`

**Title:** Dayofweek

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** Day of the week: Monday [1] ... Sunday [7].

###### <a name="data_oneOf_i1_fotaSchedule_timetable_items_timeSlots"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots`

**Title:** Timeslots

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** List of the time slots for the timetable.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                            | Description          |
| -------------------------------------------------------------------------- | -------------------- |
| [AosTimeSlot](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items) | Timetable time slot. |

###### <a name="data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots > AosTimeSlot

**Title:** AosTimeSlot

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosTimeSlot                                                         |

**Description:** Timetable time slot.

| Property                                                                      | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [start](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items_start ) | No      | string | No         | -          | Start             |
| + [end](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items_end )     | No      | string | No         | -          | End               |

###### <a name="data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items_start"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots > AosTimeSlot > start`

**Title:** Start

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `time`   |

**Description:** Start time in form `HH:MM[:SS]`.

###### <a name="data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items_end"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots > AosTimeSlot > end`

**Title:** End

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `time`   |

**Description:** End time in form `HH:MM[:SS]`.

#### <a name="data_oneOf_i1_sotaSchedule"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > sotaSchedule`

**Title:** AosScheduleRule

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/AosScheduleRule                                                     |

**Description:** Points to rules when SOTA can be applied.

| Property                                              | Pattern | Type             | Deprecated | Definition | Title/Description |
| ----------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| - [ttl](#data_oneOf_i1_fotaSchedule_ttl )             | No      | integer          | No         | -          | Ttl               |
| + [type](#data_oneOf_i1_fotaSchedule_type )           | No      | enum (of string) | No         | -          | Type              |
| - [timetable](#data_oneOf_i1_fotaSchedule_timetable ) | No      | array            | No         | -          | Timetable         |

##### <a name="data_oneOf_i1_fotaSchedule_ttl"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > ttl`

**Title:** Ttl

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `null`    |

**Description:** TTL of the rule in seconds.

##### <a name="data_oneOf_i1_fotaSchedule_type"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > type`

**Title:** Type

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

**Description:** Type of the Schedule rule.

Must be one of:
* "force"
* "trigger"
* "timetable"

##### <a name="data_oneOf_i1_fotaSchedule_timetable"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable`

**Title:** Timetable

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** Timetable when rule must work (only when the type is `timetable`).

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                 | Description                 |
| --------------------------------------------------------------- | --------------------------- |
| [AosTimetableItem](#data_oneOf_i1_fotaSchedule_timetable_items) | Timetable signe record. ... |

###### <a name="data_oneOf_i1_fotaSchedule_timetable_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem

**Title:** AosTimetableItem

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosTimetableItem                                                    |

**Description:** Timetable signe record.

Represent one entry of the timetable in form
`day of week`: [start time:end time]

| Property                                                              | Pattern | Type    | Deprecated | Definition | Title/Description |
| --------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| + [dayOfWeek](#data_oneOf_i1_fotaSchedule_timetable_items_dayOfWeek ) | No      | integer | No         | -          | Dayofweek         |
| + [timeSlots](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots ) | No      | array   | No         | -          | Timeslots         |

###### <a name="data_oneOf_i1_fotaSchedule_timetable_items_dayOfWeek"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > dayOfWeek`

**Title:** Dayofweek

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** Day of the week: Monday [1] ... Sunday [7].

###### <a name="data_oneOf_i1_fotaSchedule_timetable_items_timeSlots"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots`

**Title:** Timeslots

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** List of the time slots for the timetable.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                            | Description          |
| -------------------------------------------------------------------------- | -------------------- |
| [AosTimeSlot](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items) | Timetable time slot. |

###### <a name="data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots > AosTimeSlot

**Title:** AosTimeSlot

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosTimeSlot                                                         |

**Description:** Timetable time slot.

| Property                                                                      | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [start](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items_start ) | No      | string | No         | -          | Start             |
| + [end](#data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items_end )     | No      | string | No         | -          | End               |

###### <a name="data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items_start"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots > AosTimeSlot > start`

**Title:** Start

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `time`   |

**Description:** Start time in form `HH:MM[:SS]`.

###### <a name="data_oneOf_i1_fotaSchedule_timetable_items_timeSlots_items_end"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > fotaSchedule > timetable > AosTimetableItem > timeSlots > AosTimeSlot > end`

**Title:** End

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `time`   |

**Description:** End time in form `HH:MM[:SS]`.

#### <a name="data_oneOf_i1_certificates"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificates`

**Title:** Certificates

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** The list of the used certificates

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                         | Description                          |
| ------------------------------------------------------- | ------------------------------------ |
| [AosCertificateInfo](#data_oneOf_i1_certificates_items) | Certificate content and fingerprint. |

##### <a name="data_oneOf_i1_certificates_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificates > AosCertificateInfo

**Title:** AosCertificateInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosCertificateInfo                                                  |

**Description:** Certificate content and fingerprint.

| Property                                                        | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [certificate](#data_oneOf_i1_certificates_items_certificate ) | No      | string | No         | -          | Certificate       |
| + [fingerprint](#data_oneOf_i1_certificates_items_fingerprint ) | No      | string | No         | -          | Fingerprint       |

###### <a name="data_oneOf_i1_certificates_items_certificate"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificates > AosCertificateInfo > certificate`

**Title:** Certificate

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `base64` |

**Description:** Base64 encoded certificate in the `der` form.

###### <a name="data_oneOf_i1_certificates_items_fingerprint"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificates > AosCertificateInfo > fingerprint`

**Title:** Fingerprint

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Fingerprint of the certificate (unique ID)

#### <a name="data_oneOf_i1_certificateChains"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificateChains`

**Title:** Certificatechains

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** Certificate chains info for checking signs.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                   | Description                          |
| ----------------------------------------------------------------- | ------------------------------------ |
| [AosCertificateChainInfo](#data_oneOf_i1_certificateChains_items) | Certificate content and fingerprint. |

##### <a name="data_oneOf_i1_certificateChains_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificateChains > AosCertificateChainInfo

**Title:** AosCertificateChainInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosCertificateChainInfo                                             |

**Description:** Certificate content and fingerprint.

| Property                                                               | Pattern | Type            | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| + [name](#data_oneOf_i1_certificateChains_items_name )                 | No      | string          | No         | -          | Name              |
| + [fingerprints](#data_oneOf_i1_certificateChains_items_fingerprints ) | No      | array of string | No         | -          | Fingerprints      |

###### <a name="data_oneOf_i1_certificateChains_items_name"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificateChains > AosCertificateChainInfo > name`

**Title:** Name

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Unique name of the certificate chain.

###### <a name="data_oneOf_i1_certificateChains_items_fingerprints"></a>Property `AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificateChains > AosCertificateChainInfo > fingerprints`

**Title:** Fingerprints

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

**Description:** Fingerprint list of the certificates included in the chain.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                 | Description |
| ------------------------------------------------------------------------------- | ----------- |
| [fingerprints items](#data_oneOf_i1_certificateChains_items_fingerprints_items) | -           |

###### <a name="data_oneOf_i1_certificateChains_items_fingerprints_items"></a>AosUnitMessageV7 > data > oneOf > AosDesiredStatusV7 > certificateChains > AosCertificateChainInfo > fingerprints > fingerprints items

|          |          |
| -------- | -------- |
| **Type** | `string` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-07-23 at 12:19:56 +0300
