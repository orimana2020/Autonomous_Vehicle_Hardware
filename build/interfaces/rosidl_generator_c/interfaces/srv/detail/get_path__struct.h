// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:srv/GetPath.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__GET_PATH__STRUCT_H_
#define INTERFACES__SRV__DETAIL__GET_PATH__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'start'
// Member 'goal'
#include "geometry_msgs/msg/detail/point__struct.h"
// Member 'path_name'
#include "std_msgs/msg/detail/string__struct.h"

/// Struct defined in srv/GetPath in the package interfaces.
typedef struct interfaces__srv__GetPath_Request
{
  geometry_msgs__msg__Point start;
  geometry_msgs__msg__Point goal;
  std_msgs__msg__String path_name;
} interfaces__srv__GetPath_Request;

// Struct for a sequence of interfaces__srv__GetPath_Request.
typedef struct interfaces__srv__GetPath_Request__Sequence
{
  interfaces__srv__GetPath_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__GetPath_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'path'
// already included above
// #include "geometry_msgs/msg/detail/point__struct.h"

/// Struct defined in srv/GetPath in the package interfaces.
typedef struct interfaces__srv__GetPath_Response
{
  geometry_msgs__msg__Point__Sequence path;
} interfaces__srv__GetPath_Response;

// Struct for a sequence of interfaces__srv__GetPath_Response.
typedef struct interfaces__srv__GetPath_Response__Sequence
{
  interfaces__srv__GetPath_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__GetPath_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__SRV__DETAIL__GET_PATH__STRUCT_H_
