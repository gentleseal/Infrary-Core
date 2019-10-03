IS_DEBUG = True

PROVISIONER_CONTAINER_NAME = 'eu.gcr.io/infrary-main/provisioner'
PROVISIONER_OCTO_CONF_KEY = 'octo_conf'
PROVISIONER_PROPERTIES_KEY = 'properties'
PROVISIONER_ACTION_KEY = 'action'
PROVISIONER_CREATE_ACTION = 'create'
PROVISIONER_DESTROY_ACTION = 'destroy'
PROVISIONER_ACCESS_TOKEN_KEY = 'token'
PROVISIONER_PROVIDER_KEY = 'provider'
PROVISIONER_SERVER_ID_KEY = 'server_id'
PROVISIONER_SSH_KEY_KEY = 'ssh_key'
PROVISIONER_SERVER_LOCATION_KEY = 'location'
PROVISIONER_SERVER_IMAGE_KEY = 'image'
PROVISIONER_SERVER_SIZE_KEY = 'size'
PROVISIONER_SERVER_NAME_KEY = 'name'

DIGITAL_OCEAN_PROVIDER_CODE = "DO"
BYO_PROVIDER_CODE = "BYO"

FAILED_DELETE_PROVIDER_STATUS = 'delete_fail_provider'
FAILED_DELETE_STATUS = 'delete_fail'
DELETED_STATUS = 'deleted'
DOWN_STATUS = "down"
UP_STATUS = "up"
CONFIGURING_STATUS = "configuring"
CREATED_STATUS = "created"
ALL_STATUS_LIST = [FAILED_DELETE_PROVIDER_STATUS, FAILED_DELETE_STATUS, DELETED_STATUS, DOWN_STATUS, UP_STATUS,
                   CONFIGURING_STATUS, CREATED_STATUS]
CANNOT_DELETE_STATUS_LIST = [CREATED_STATUS, CONFIGURING_STATUS]

ACTION_KEY = "action"
STATUS_KEY = "status"

SET_STATUS_ACTION = "set_status"

ACCESS_TOKEN_KEY = 'token'
STATUS_DB_KEY = "status"
MASTERCONF_KEY = 'master_conf'
SELF_DESTRUCT_KEY = 'self_destruct'
IS_MASTER_KEY = 'is_master'
VM_CONFIGURATION_DB_KEY = "vm_configuration"
ID_KEY = 'id'
PROVIDER_KEY = 'provider'
IP_KEY = 'ip'
TEMP_SSH_KEY_KEY = 'temp_ssh_key'
LOG_KEY = 'log'
SSH_KEY_FINGERPRINT_KEY = 'ssh_fgpt'


OCTO_TOKEN_KEY = 'OCTO_TOKEN'
OCTO_SERVER_STATUS_SUBMIT_PATH_KEY = 'OCTO_SERVER_STATUS_SUBMIT_PATH'
OCTO_SERVER_SUBMIT_PATH_KEY = 'OCTO_SERVER_SUBMIT_PATH'
OCTO_MESSAGE_SUBMIT_PATH_KEY = 'OCTO_MESSAGE_SUBMIT_PATH'
OCTO_URL_KEY = 'OCTO_URL'

