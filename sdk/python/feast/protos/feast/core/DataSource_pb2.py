# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/DataSource.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feast.protos.feast.core import DataFormat_pb2 as feast_dot_core_dot_DataFormat__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/core/DataSource.proto',
  package='feast.core',
  syntax='proto3',
  serialized_options=b'\n\020feast.proto.coreB\017DataSourceProtoZ3github.com/feast-dev/feast/sdk/go/protos/feast/core',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x66\x65\x61st/core/DataSource.proto\x12\nfeast.core\x1a\x1b\x66\x65\x61st/core/DataFormat.proto\"\xdb\x07\n\nDataSource\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.feast.core.DataSource.SourceType\x12?\n\rfield_mapping\x18\x02 \x03(\x0b\x32(.feast.core.DataSource.FieldMappingEntry\x12\x1e\n\x16\x65vent_timestamp_column\x18\x03 \x01(\t\x12\x1d\n\x15\x64\x61te_partition_column\x18\x04 \x01(\t\x12 \n\x18\x63reated_timestamp_column\x18\x05 \x01(\t\x12:\n\x0c\x66ile_options\x18\x0b \x01(\x0b\x32\".feast.core.DataSource.FileOptionsH\x00\x12\x42\n\x10\x62igquery_options\x18\x0c \x01(\x0b\x32&.feast.core.DataSource.BigQueryOptionsH\x00\x12<\n\rkafka_options\x18\r \x01(\x0b\x32#.feast.core.DataSource.KafkaOptionsH\x00\x12@\n\x0fkinesis_options\x18\x0e \x01(\x0b\x32%.feast.core.DataSource.KinesisOptionsH\x00\x1a\x33\n\x11\x46ieldMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aL\n\x0b\x46ileOptions\x12+\n\x0b\x66ile_format\x18\x01 \x01(\x0b\x32\x16.feast.core.FileFormat\x12\x10\n\x08\x66ile_url\x18\x02 \x01(\t\x1a\x33\n\x0f\x42igQueryOptions\x12\x11\n\ttable_ref\x18\x01 \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t\x1aj\n\x0cKafkaOptions\x12\x19\n\x11\x62ootstrap_servers\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x30\n\x0emessage_format\x18\x03 \x01(\x0b\x32\x18.feast.core.StreamFormat\x1a\x66\n\x0eKinesisOptions\x12\x0e\n\x06region\x18\x01 \x01(\t\x12\x13\n\x0bstream_name\x18\x02 \x01(\t\x12/\n\rrecord_format\x18\x03 \x01(\x0b\x32\x18.feast.core.StreamFormat\"c\n\nSourceType\x12\x0b\n\x07INVALID\x10\x00\x12\x0e\n\nBATCH_FILE\x10\x01\x12\x12\n\x0e\x42\x41TCH_BIGQUERY\x10\x02\x12\x10\n\x0cSTREAM_KAFKA\x10\x03\x12\x12\n\x0eSTREAM_KINESIS\x10\x04\x42\t\n\x07optionsBX\n\x10\x66\x65\x61st.proto.coreB\x0f\x44\x61taSourceProtoZ3github.com/feast-dev/feast/sdk/go/protos/feast/coreb\x06proto3'
  ,
  dependencies=[feast_dot_core_dot_DataFormat__pb2.DESCRIPTOR,])



_DATASOURCE_SOURCETYPE = _descriptor.EnumDescriptor(
  name='SourceType',
  full_name='feast.core.DataSource.SourceType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BATCH_FILE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BATCH_BIGQUERY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STREAM_KAFKA', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STREAM_KINESIS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=950,
  serialized_end=1049,
)
_sym_db.RegisterEnumDescriptor(_DATASOURCE_SOURCETYPE)


_DATASOURCE_FIELDMAPPINGENTRY = _descriptor.Descriptor(
  name='FieldMappingEntry',
  full_name='feast.core.DataSource.FieldMappingEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.core.DataSource.FieldMappingEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.core.DataSource.FieldMappingEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=605,
)

_DATASOURCE_FILEOPTIONS = _descriptor.Descriptor(
  name='FileOptions',
  full_name='feast.core.DataSource.FileOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_format', full_name='feast.core.DataSource.FileOptions.file_format', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_url', full_name='feast.core.DataSource.FileOptions.file_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=607,
  serialized_end=683,
)

_DATASOURCE_BIGQUERYOPTIONS = _descriptor.Descriptor(
  name='BigQueryOptions',
  full_name='feast.core.DataSource.BigQueryOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_ref', full_name='feast.core.DataSource.BigQueryOptions.table_ref', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query', full_name='feast.core.DataSource.BigQueryOptions.query', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=685,
  serialized_end=736,
)

_DATASOURCE_KAFKAOPTIONS = _descriptor.Descriptor(
  name='KafkaOptions',
  full_name='feast.core.DataSource.KafkaOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bootstrap_servers', full_name='feast.core.DataSource.KafkaOptions.bootstrap_servers', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topic', full_name='feast.core.DataSource.KafkaOptions.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_format', full_name='feast.core.DataSource.KafkaOptions.message_format', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=738,
  serialized_end=844,
)

_DATASOURCE_KINESISOPTIONS = _descriptor.Descriptor(
  name='KinesisOptions',
  full_name='feast.core.DataSource.KinesisOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='region', full_name='feast.core.DataSource.KinesisOptions.region', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stream_name', full_name='feast.core.DataSource.KinesisOptions.stream_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='record_format', full_name='feast.core.DataSource.KinesisOptions.record_format', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=846,
  serialized_end=948,
)

_DATASOURCE = _descriptor.Descriptor(
  name='DataSource',
  full_name='feast.core.DataSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='feast.core.DataSource.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field_mapping', full_name='feast.core.DataSource.field_mapping', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_timestamp_column', full_name='feast.core.DataSource.event_timestamp_column', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_partition_column', full_name='feast.core.DataSource.date_partition_column', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_timestamp_column', full_name='feast.core.DataSource.created_timestamp_column', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_options', full_name='feast.core.DataSource.file_options', index=5,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bigquery_options', full_name='feast.core.DataSource.bigquery_options', index=6,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kafka_options', full_name='feast.core.DataSource.kafka_options', index=7,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kinesis_options', full_name='feast.core.DataSource.kinesis_options', index=8,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATASOURCE_FIELDMAPPINGENTRY, _DATASOURCE_FILEOPTIONS, _DATASOURCE_BIGQUERYOPTIONS, _DATASOURCE_KAFKAOPTIONS, _DATASOURCE_KINESISOPTIONS, ],
  enum_types=[
    _DATASOURCE_SOURCETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='options', full_name='feast.core.DataSource.options',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=73,
  serialized_end=1060,
)

_DATASOURCE_FIELDMAPPINGENTRY.containing_type = _DATASOURCE
_DATASOURCE_FILEOPTIONS.fields_by_name['file_format'].message_type = feast_dot_core_dot_DataFormat__pb2._FILEFORMAT
_DATASOURCE_FILEOPTIONS.containing_type = _DATASOURCE
_DATASOURCE_BIGQUERYOPTIONS.containing_type = _DATASOURCE
_DATASOURCE_KAFKAOPTIONS.fields_by_name['message_format'].message_type = feast_dot_core_dot_DataFormat__pb2._STREAMFORMAT
_DATASOURCE_KAFKAOPTIONS.containing_type = _DATASOURCE
_DATASOURCE_KINESISOPTIONS.fields_by_name['record_format'].message_type = feast_dot_core_dot_DataFormat__pb2._STREAMFORMAT
_DATASOURCE_KINESISOPTIONS.containing_type = _DATASOURCE
_DATASOURCE.fields_by_name['type'].enum_type = _DATASOURCE_SOURCETYPE
_DATASOURCE.fields_by_name['field_mapping'].message_type = _DATASOURCE_FIELDMAPPINGENTRY
_DATASOURCE.fields_by_name['file_options'].message_type = _DATASOURCE_FILEOPTIONS
_DATASOURCE.fields_by_name['bigquery_options'].message_type = _DATASOURCE_BIGQUERYOPTIONS
_DATASOURCE.fields_by_name['kafka_options'].message_type = _DATASOURCE_KAFKAOPTIONS
_DATASOURCE.fields_by_name['kinesis_options'].message_type = _DATASOURCE_KINESISOPTIONS
_DATASOURCE_SOURCETYPE.containing_type = _DATASOURCE
_DATASOURCE.oneofs_by_name['options'].fields.append(
  _DATASOURCE.fields_by_name['file_options'])
_DATASOURCE.fields_by_name['file_options'].containing_oneof = _DATASOURCE.oneofs_by_name['options']
_DATASOURCE.oneofs_by_name['options'].fields.append(
  _DATASOURCE.fields_by_name['bigquery_options'])
_DATASOURCE.fields_by_name['bigquery_options'].containing_oneof = _DATASOURCE.oneofs_by_name['options']
_DATASOURCE.oneofs_by_name['options'].fields.append(
  _DATASOURCE.fields_by_name['kafka_options'])
_DATASOURCE.fields_by_name['kafka_options'].containing_oneof = _DATASOURCE.oneofs_by_name['options']
_DATASOURCE.oneofs_by_name['options'].fields.append(
  _DATASOURCE.fields_by_name['kinesis_options'])
_DATASOURCE.fields_by_name['kinesis_options'].containing_oneof = _DATASOURCE.oneofs_by_name['options']
DESCRIPTOR.message_types_by_name['DataSource'] = _DATASOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataSource = _reflection.GeneratedProtocolMessageType('DataSource', (_message.Message,), {

  'FieldMappingEntry' : _reflection.GeneratedProtocolMessageType('FieldMappingEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATASOURCE_FIELDMAPPINGENTRY,
    '__module__' : 'feast.core.DataSource_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.DataSource.FieldMappingEntry)
    })
  ,

  'FileOptions' : _reflection.GeneratedProtocolMessageType('FileOptions', (_message.Message,), {
    'DESCRIPTOR' : _DATASOURCE_FILEOPTIONS,
    '__module__' : 'feast.core.DataSource_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.DataSource.FileOptions)
    })
  ,

  'BigQueryOptions' : _reflection.GeneratedProtocolMessageType('BigQueryOptions', (_message.Message,), {
    'DESCRIPTOR' : _DATASOURCE_BIGQUERYOPTIONS,
    '__module__' : 'feast.core.DataSource_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.DataSource.BigQueryOptions)
    })
  ,

  'KafkaOptions' : _reflection.GeneratedProtocolMessageType('KafkaOptions', (_message.Message,), {
    'DESCRIPTOR' : _DATASOURCE_KAFKAOPTIONS,
    '__module__' : 'feast.core.DataSource_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.DataSource.KafkaOptions)
    })
  ,

  'KinesisOptions' : _reflection.GeneratedProtocolMessageType('KinesisOptions', (_message.Message,), {
    'DESCRIPTOR' : _DATASOURCE_KINESISOPTIONS,
    '__module__' : 'feast.core.DataSource_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.DataSource.KinesisOptions)
    })
  ,
  'DESCRIPTOR' : _DATASOURCE,
  '__module__' : 'feast.core.DataSource_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.DataSource)
  })
_sym_db.RegisterMessage(DataSource)
_sym_db.RegisterMessage(DataSource.FieldMappingEntry)
_sym_db.RegisterMessage(DataSource.FileOptions)
_sym_db.RegisterMessage(DataSource.BigQueryOptions)
_sym_db.RegisterMessage(DataSource.KafkaOptions)
_sym_db.RegisterMessage(DataSource.KinesisOptions)


DESCRIPTOR._options = None
_DATASOURCE_FIELDMAPPINGENTRY._options = None
# @@protoc_insertion_point(module_scope)