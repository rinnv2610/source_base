from enum import Enum

from rest_framework.status import (HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED)


class AppStatus(Enum):
    SUCCESS = HTTP_200_OK, 200, "SUCCESS", "SUCCESS."
    FAILED_INTERNAL_SERVER_ERROR = HTTP_500_INTERNAL_SERVER_ERROR, 500, "FAILED_INTERNAL_SERVER_ERROR", "Server has an unknown error."
    FAILED_BAD_REQUEST = HTTP_400_BAD_REQUEST, 400, "BAD_REQUEST", "Bad request, pls recheck."
    FAILED_FORBIDDEN_REQUEST = HTTP_403_FORBIDDEN, 403, "FAILED_FORBIDDEN_REQUEST", "You do not have permission to perform this action."
    FAILED_API_NOT_FOUND = HTTP_404_NOT_FOUND, 403, "FAILED_API_NOT_FOUND", "API is not available."
    ERROR_VALIDATION = HTTP_400_BAD_REQUEST, 40001, "ERROR_VALIDATION", "There are unknown errors in validation. Pls check server log."
    FAILED_AUTHENTICATION = HTTP_401_UNAUTHORIZED, 401, "FAILED_AUTHENTICATION", "Authentication failed."

    ERROR_USER_DOES_NOT_EXISTS = HTTP_400_BAD_REQUEST, 1001, "ERROR_USER_DOES_NOT_EXISTS", "User does not exists."
    ERROR_USER_REGISTER = HTTP_400_BAD_REQUEST, 1002, "ERROR_USER_REGISTER", "Error user register new"
    ERROR_USER_GET_INFO = HTTP_400_BAD_REQUEST, 1003, "ERROR_USER_GET_INFO", "Error user get info"
    ERROR_EMAIL_OR_PASSWORD_INCORRECT = HTTP_400_BAD_REQUEST, 1003, "ERROR_EMAIL_OR_PASSWORD_INCORRECT", "Email or password isn't correct."


    @property
    def http_code(self):
        return self.value[0]

    @property
    def app_status_code(self):
        return self.value[1]

    @property
    def app_status(self):
        return self.value[2]

    @property
    def app_message(self):
        return self.value[3]

    @classmethod
    def find_by_code(cls, app_code):
        result = [app_status_enum[1] for app_status_enum in cls.__members__.items() if
                  app_status_enum[1].app_status_code == app_code]
        return result[0]
