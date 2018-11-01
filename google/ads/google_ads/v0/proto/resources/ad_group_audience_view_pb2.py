# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/resources/ad_group_audience_view.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/resources/ad_group_audience_view.proto',
  package='google.ads.googleads.v0.resources',
  syntax='proto3',
  serialized_pb=_b('\nDgoogle/ads/googleads_v0/proto/resources/ad_group_audience_view.proto\x12!google.ads.googleads.v0.resources\",\n\x13\x41\x64GroupAudienceView\x12\x15\n\rresource_name\x18\x01 \x01(\tB\xdd\x01\n%com.google.ads.googleads.v0.resourcesB\x18\x41\x64GroupAudienceViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V0.Resources\xca\x02!Google\\Ads\\GoogleAds\\V0\\Resourcesb\x06proto3')
)




_ADGROUPAUDIENCEVIEW = _descriptor.Descriptor(
  name='AdGroupAudienceView',
  full_name='google.ads.googleads.v0.resources.AdGroupAudienceView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.resources.AdGroupAudienceView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=151,
)

DESCRIPTOR.message_types_by_name['AdGroupAudienceView'] = _ADGROUPAUDIENCEVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupAudienceView = _reflection.GeneratedProtocolMessageType('AdGroupAudienceView', (_message.Message,), dict(
  DESCRIPTOR = _ADGROUPAUDIENCEVIEW,
  __module__ = 'google.ads.googleads_v0.proto.resources.ad_group_audience_view_pb2'
  ,
  __doc__ = """An ad group audience view. Includes performance data from interests and
  remarketing lists for Display Network and YouTube Network ads, and
  remarketing lists for search ads (RLSA), aggregated at the audience
  level.
  
  
  Attributes:
      resource_name:
          The resource name of the ad group audience view. Ad group
          audience view resource names have the form:  ``customers/{cust
          omer_id}/adGroupAudienceViews/{ad_group_id}_{criterion_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.resources.AdGroupAudienceView)
  ))
_sym_db.RegisterMessage(AdGroupAudienceView)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%com.google.ads.googleads.v0.resourcesB\030AdGroupAudienceViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V0.Resources\312\002!Google\\Ads\\GoogleAds\\V0\\Resources'))
# @@protoc_insertion_point(module_scope)
