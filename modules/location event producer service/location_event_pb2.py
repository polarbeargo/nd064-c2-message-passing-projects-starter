# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: location_event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
  name='location_event.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17\x6Cocation_event.proto\"N\n\x17\x4CocationEventMessage\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x10\n\x08latitude\x18\x02 \x01(\x05\x12\x11\n\tlongitude\x18\x03 \x01(\x05\x32K\n\x0bItemService\x12<\n\x06\x43reate\x12\x18.LocationEventMessage\x1a\x18.LocationEventMessage\x06proto3'
)

_location_eventMESSAGE = _descriptor.Descriptor(
  name='LocationEventMessage',
  full_name='LocationEventMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='LocationEventMessage.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='LocationEventMessage.latitude', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='LocationEventMessage.longitude', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),

  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=292,
)

DESCRIPTOR.message_types_by_name['LocationEventMessage'] = _location_eventMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

location_eventMessage = _reflection.GeneratedProtocolMessageType('LocationEventMessage', (_message.Message,), {
  'DESCRIPTOR' : _location_eventMESSAGE,
  '__module__' : 'location_event_pb2'
  # @@protoc_insertion_point(class_scope:location_eventMessage)
  })
_sym_db.RegisterMessage(location_eventMessage)

__ITEMSERVICE = _descriptor.ServiceDescriptor(
  name='ItemService',
  full_name='ItemService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=107,
  serialized_end=182,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='ItemService.Create',
    index=0,
    containing_service=None,
    input_type=_location_eventMESSAGE,
    output_type=_location_eventMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(__ITEMSERVICE)

DESCRIPTOR.services_by_name['ItemService'] = __ITEMSERVICE

# @@protoc_insertion_point(module_scope)
