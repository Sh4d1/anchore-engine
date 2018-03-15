# coding: utf-8

"""
    anchore_engine.services.policy_engine

    This is a policy evaluation service. It receives push-events from external systems for data updates and provides an api for requesting image policy checks

    OpenAPI spec version: 1.0.0
    Contact: zach@anchore.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TriggerSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'is_deprecated': 'bool',
        'superceded_by': 'str',
        'parameters': 'list[TriggerParamSpec]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'is_deprecated': 'is_deprecated',
        'superceded_by': 'superceded_by',
        'parameters': 'parameters'
    }

    def __init__(self, name=None, description=None, is_deprecated=None, superceded_by=None, parameters=None):
        """
        TriggerSpec - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._is_deprecated = None
        self._superceded_by = None
        self._parameters = None

        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if is_deprecated is not None:
          self.is_deprecated = is_deprecated
        if superceded_by is not None:
          self.superceded_by = superceded_by
        if parameters is not None:
          self.parameters = parameters

    @property
    def name(self):
        """
        Gets the name of this TriggerSpec.
        Name of the trigger as it would appear in a policy document

        :return: The name of this TriggerSpec.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TriggerSpec.
        Name of the trigger as it would appear in a policy document

        :param name: The name of this TriggerSpec.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TriggerSpec.
        Trigger description for what it tests and when it will fire during evaluation

        :return: The description of this TriggerSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TriggerSpec.
        Trigger description for what it tests and when it will fire during evaluation

        :param description: The description of this TriggerSpec.
        :type: str
        """

        self._description = description

    @property
    def is_deprecated(self):
        """
        Gets the is_deprecated of this TriggerSpec.
        True if this trigger is deprecated

        :return: The is_deprecated of this TriggerSpec.
        :rtype: bool
        """
        return self._is_deprecated

    @is_deprecated.setter
    def is_deprecated(self, is_deprecated):
        """
        Sets the is_deprecated of this TriggerSpec.
        True if this trigger is deprecated

        :param is_deprecated: The is_deprecated of this TriggerSpec.
        :type: bool
        """

        self._is_deprecated = is_deprecated

    @property
    def superceded_by(self):
        """
        Gets the superceded_by of this TriggerSpec.
        The name of another trigger that supercedes this on functionally if this is deprecated

        :return: The superceded_by of this TriggerSpec.
        :rtype: str
        """
        return self._superceded_by

    @superceded_by.setter
    def superceded_by(self, superceded_by):
        """
        Sets the superceded_by of this TriggerSpec.
        The name of another trigger that supercedes this on functionally if this is deprecated

        :param superceded_by: The superceded_by of this TriggerSpec.
        :type: str
        """

        self._superceded_by = superceded_by

    @property
    def parameters(self):
        """
        Gets the parameters of this TriggerSpec.
        The list of parameters that are valid for this trigger

        :return: The parameters of this TriggerSpec.
        :rtype: list[TriggerParamSpec]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this TriggerSpec.
        The list of parameters that are valid for this trigger

        :param parameters: The parameters of this TriggerSpec.
        :type: list[TriggerParamSpec]
        """

        self._parameters = parameters

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TriggerSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
