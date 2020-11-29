# coding: utf-8

"""
    Lab 2 API made with love by Roman Kovalchuk

    variant №12  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class MarksList(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'discipline_id': 'int',
        'mark': 'Real',
        'passed': 'bool'
    }

    attribute_map = {
        'discipline_id': 'DisciplineID',
        'mark': 'Mark',
        'passed': 'Passed'
    }

    def __init__(self, discipline_id=None, mark=None, passed=None, local_vars_configuration=None):  # noqa: E501
        """MarksList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._discipline_id = None
        self._mark = None
        self._passed = None
        self.discriminator = None

        if discipline_id is not None:
            self.discipline_id = discipline_id
        if mark is not None:
            self.mark = mark
        if passed is not None:
            self.passed = passed

    @property
    def discipline_id(self):
        """Gets the discipline_id of this MarksList.  # noqa: E501


        :return: The discipline_id of this MarksList.  # noqa: E501
        :rtype: int
        """
        return self._discipline_id

    @discipline_id.setter
    def discipline_id(self, discipline_id):
        """Sets the discipline_id of this MarksList.


        :param discipline_id: The discipline_id of this MarksList.  # noqa: E501
        :type: int
        """

        self._discipline_id = discipline_id

    @property
    def mark(self):
        """Gets the mark of this MarksList.  # noqa: E501


        :return: The mark of this MarksList.  # noqa: E501
        :rtype: Real
        """
        return self._mark

    @mark.setter
    def mark(self, mark):
        """Sets the mark of this MarksList.


        :param mark: The mark of this MarksList.  # noqa: E501
        :type: Real
        """

        self._mark = mark

    @property
    def passed(self):
        """Gets the passed of this MarksList.  # noqa: E501


        :return: The passed of this MarksList.  # noqa: E501
        :rtype: bool
        """
        return self._passed

    @passed.setter
    def passed(self, passed):
        """Sets the passed of this MarksList.


        :param passed: The passed of this MarksList.  # noqa: E501
        :type: bool
        """

        self._passed = passed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MarksList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarksList):
            return True

        return self.to_dict() != other.to_dict()